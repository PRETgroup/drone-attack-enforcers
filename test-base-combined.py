import missions.take_off_and_land as TOAL
import missions.a2b as a2b
import missions.a2b2a as a2b2a
from multiprocessing import Process, Pipe
from time import sleep, asctime, localtime

# Toggles demonstration of MITM attacker enforcer
ATTACK_ENFORCER = False 
RI_ATTACK_ENFORCER = False 

# Toggles logging to csv under logs directory
LOG_STATUS = True

# Height the drone will fly to
TOAL_DESIRED_HEIGHT = 10
A2B_DESIRED_HEIGHT = 15
A2B2A_DESIRED_HEIGHT = 20

# Location to travel to
A2B_NORTH = -20
A2B_EAST = 0
A2B2A_NORTH = 10
A2B2A_EAST = -20

if ATTACK_ENFORCER:
    import attackers.enforcer as Attacker

if RI_ATTACK_ENFORCER:
    import attackers.ri_enforcer as Attacker

if __name__ == '__main__':
    firstRunCompleted = False
    l = "L_IDLE"
    init = True
    pipe_p = None
    pipe_c = None
    exited = False
    while not exited:

        if init:
            print("BASE: Creating comms pipe")
            
            if pipe_p is not None and pipe_c is not None:
                pipe_p, pipe_c = Pipe()
            else:
                pipe_p = None
                pipe_c = None
                pipe_p, pipe_c = Pipe()

            if RI_ATTACK_ENFORCER:
                ATTACK_ENFORCER = True
                a = Attacker.RI_AttackEnforcer_TOAL_A2B_A2B2A(pipe_p)
                pipe_p = a

            init = False
        
        print("BASE: " + str(l))
        sleep(1) # Slow things down
        if pipe_p.poll():
            update = pipe_p.recv()
            if update is not None:
                print("BASE: Update from drone: " + str(update))
            else:
                update = [None, ""]
        else:
            update = [None, ""]
            if ATTACK_ENFORCER: pipe_p.tick() # Quick hack to tick the enforcer

        curLoc = l

        if l == "L_IDLE":
            if update[1] == "":
                print("BASE: Create new TOAL mission")
                m = TOAL.Manager(pipe_c, LOG_STATUS)
                p = Process(target=m.run, args=(None,))

                print("BASE: Setup Mission")
                p.start()
                pipe_p.send([asctime(localtime()), "NEW"])
            l = "L_CONNECT"

        elif l == "L_CONNECT":
            pipe_p.send([asctime(localtime()), "NEW"])
            if update[1] == "CONNECTED":
                # pipe_p.send([asctime(localtime()), "CONFIG_ALT", TOAL_DESIRED_HEIGHT])
                l = "L_CONFIG_TOAL"

        elif l == "L_CONFIG_TOAL":
            if update[1] == "CONFIGED":
                pipe_p.send([asctime(localtime()), "RUN"])
                l = "L_RUN_TOAL"
            else:
                pipe_p.send([asctime(localtime()), "CONFIG_ALT", TOAL_DESIRED_HEIGHT])
                
        elif l == "L_RUN_TOAL":
            if update[1] == "TAKE_OFF":
                l = "L_CLIMB"
            else:
                pipe_p.send([asctime(localtime()), "RUN"])

        elif l == "L_CLIMB":
            if update[1] == "AT_ALTITUDE":
                pipe_p.send([asctime(localtime()), "LAND"])
                l = "L_AT_ALTITUDE"

        elif l == "L_AT_ALTITUDE":
            if update[1] == "LANDING":
                l = "L_DESCEND"
            else:
                pipe_p.send([asctime(localtime()), "LAND"])

        elif l == "L_DESCEND":
            if update[1] == "LANDED":
                l = "L_LANDED"

        elif l == "L_LANDED":
            pipe_p.send([asctime(localtime()), "END"])
            l = "L_END_TOAL"

        elif l == "L_ABORT":
            if update[1] == "LANDING":
                l = "L_DESCEND"
            else:
                pipe_p.send([asctime(localtime()), "ABORT"])

        elif l == "L_END_TOAL":
            # pipe_p.send([asctime(localtime()), "END"])
            if update[1] == "END":
                print("BASE: Mission Ended")
                if not firstRunCompleted:
                    # l = "L_IDLE" # Change to this if you want to repeat TOAL 
                    # print("BASE: Repeat TOAL Mission")
                    firstRunCompleted = True
                    print("BASE: Moving to start A2B2A mission")
                    l = "L_A2B2A_IDLE"
                else:
                    exited = True
                    print("BASE: Exiting")

        elif l == "L_A2B2A_IDLE":
            if update[1] == "":
                print("BASE: Create new A2B2 mission")
                m = a2b2a.Manager(pipe_c, LOG_STATUS)
                p = Process(target=m.run, args=(None,))

                print("BASE: New A2B2A Mission")
                p.start()
                pipe_p.send([asctime(localtime()), "NEW"])
            l = "L_A2B2A_CONNECT"

        elif l == "L_A2B2A_CONNECT":
            if update[1] == "CONNECTED":
                print("BASE: Configure A2B2A Mission")
                l = "L_A2B2A_CONFIG"
                # sleep(5)
                # print("BASE: Abort mission!")
                # pipe_p.send([asctime(localtime()), "ABORT"])

        elif l == "L_A2B2A_CONFIG":
            if update[1] == "CONFIGED":
                pipe_p.send([asctime(localtime()), "RUN"])
                l = "L_A2B2A_TRAVEL_TO_B"
            else:
                pipe_p.send([asctime(localtime()), "CONFIG_LOC", A2B2A_DESIRED_HEIGHT, A2B2A_NORTH, A2B2A_EAST])

        elif l == "L_A2B2A_TRAVEL_TO_B":
            if update[1] == "AT_B":
                print("BASE: Request land")
                pipe_p.send([asctime(localtime()), "LAND"])
                l = "L_A2B2A_LANDING"

        elif l == "L_A2B2A_LANDING":
            if update[1] == "LANDED": # at b
                print("BASE: Doing things at B")
                sleep(5)
                print("BASE: Now ready to return to A")
                pipe_p.send([asctime(localtime()), "RETURN_A"])
                l = "L_A2B2A_RETURNING"

        elif l == "L_A2B2A_RETURNING":
            if update[1] == "LANDED":
                print("BASE: Request End Mission")
                pipe_p.send([asctime(localtime()), "END"])
                l = "L_A2B2A_END"
            
        elif l == "L_A2B2A_END":
            if update[1] == "END":
                # pipe_p.send([asctime(localtime()), "END"])
                # exited = True
                print("BASE: Ended A2B2A Mission")
                l = "L_START_A2B"

        elif l == "L_START_A2B":
            l = "L_A2B_IDLE"

        elif l == "L_A2B_IDLE":
            print("BASE: " + str(update[1]))
            if update[1] == "":
                print("BASE: Create new A2B mission")
                m = a2b.Manager(pipe_c, LOG_STATUS)
                p = Process(target=m.run, args=(None,))

                print("BASE: New A2B Mission")
                p.start()
                pipe_p.send([asctime(localtime()), "NEW"])
            l = "L_A2B_CONNECT"

        elif l == "L_A2B_CONNECT":
            if update[1] == "CONNECTED":
                print("BASE: Configure A2B Mission")
                l = "L_A2B_CONFIG"
                # sleep(5)
                # print("BASE: Abort mission!")
                # pipe_p.send([asctime(localtime()), "ABORT"])

        elif l == "L_A2B_CONFIG":
            if update[1] == "CONFIGED":
                pipe_p.send([asctime(localtime()), "RUN"])
                l = "L_A2B_TRAVEL_TO_B"
            else:
                pipe_p.send([asctime(localtime()), "CONFIG_LOC", A2B_DESIRED_HEIGHT, A2B_NORTH, A2B_EAST])

        elif l == "L_A2B_TRAVEL_TO_B":
            if update[1] == "AT_B":
                print("BASE: Request land")
                pipe_p.send([asctime(localtime()), "LAND"])
                l = "L_A2B_LANDING"

        elif l == "L_A2B_LANDING":
            if update[1] == "LANDED":
                print("BASE: Request end mission")
                pipe_p.send([asctime(localtime()), "END"])
                l = "L_A2B_END"

        elif l == "L_A2B_END":
            if update[1] == "END":
                pipe_p.send([asctime(localtime()), "END"])
                exited = True
                print("BASE: End Mission")
        
        if curLoc != l:
            print("BASE: FSM Location Transition: " + str(curLoc) + " to " + str(l))