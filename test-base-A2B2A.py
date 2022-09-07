import missions.a2b2a as a2b2a
from multiprocessing import Process, Pipe
from time import sleep, asctime, localtime

# Toggles demonstration of MITM attacker enforcer
ATTACK_ENFORCER = True 

# Toggles logging to csv under logs directory
LOG_STATUS = True

# Height the drone will fly to
DESIRED_HEIGHT = 5
# Location to travel to (location B)
NORTH = -10
EAST = -10

if ATTACK_ENFORCER:
    import attackers.enforcer as Attacker

if __name__ == '__main__':
    print("BASE: Creating comms pipe")
    pipe_p, pipe_c = Pipe()

    if ATTACK_ENFORCER:
        a = Attacker.AttackEnforcer_AlterConfig_Location(pipe_p)
        pipe_p = a # a implements send and recv to allow normal pipe api

    print("BASE: Create new A2B2 mission")
    m = a2b2a.Manager(pipe_c, LOG_STATUS)
    p = Process(target=m.run, args=(None,))

    l = "L_IDLE"

    exited = False
    while not exited:
        if not LOG_STATUS: print("BASE: " + str(l))
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
                print("BASE: New A2B2A Mission")
                p.start()
                pipe_p.send([asctime(localtime()), "NEW"])
            l = "L_CONNECT"

        elif l == "L_CONNECT":
            if update[1] == "CONNECTED":
                print("BASE: Configure A2B2A Mission")
                l = "L_CONFIG"
                # sleep(5)
                # print("BASE: Abort mission!")
                # pipe_p.send([asctime(localtime()), "ABORT"])

        elif l == "L_CONFIG":
            if update[1] == "CONFIGED":
                pipe_p.send([asctime(localtime()), "RUN"])
                l = "L_TRAVEL_TO_B"
            else:
                pipe_p.send([asctime(localtime()), "CONFIG_LOC", DESIRED_HEIGHT, NORTH, EAST])

        elif l == "L_TRAVEL_TO_B":
            if update[1] == "AT_B":
                print("BASE: Request land")
                pipe_p.send([asctime(localtime()), "LAND"])
                l = "L_LANDING"

        elif l == "L_LANDING":
            if update[1] == "LANDED": # at b
                print("BASE: Doing things at B")
                sleep(5)
                print("BASE: Now ready to return to A")
                pipe_p.send([asctime(localtime()), "RETURN_A"])
                l = "L_RETURNING"

        elif l == "L_RETURNING":
            if update[1] == "LANDED":
                print("BASE: Request End Mission")
                pipe_p.send([asctime(localtime()), "END"])
                l = "L_END"
            
        elif l == "L_END":
            if update[1] == "END":
                pipe_p.send([asctime(localtime()), "END"])
                exited = True
                print("BASE: Ended Mission")
