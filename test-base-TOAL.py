import missions.take_off_and_land as TOAL
from multiprocessing import Process, Pipe
from time import sleep, asctime, localtime

# Toggles demonstration of MITM attacker enforcer
ATTACK_ENFORCER = False 
RI_ATTACK_ENFORCER = True 

# Toggles logging to csv under logs directory
LOG_STATUS = True

# Height the drone will fly to
DESIRED_HEIGHT = 5

if ATTACK_ENFORCER:
    import attackers.enforcer as Attacker

if RI_ATTACK_ENFORCER:
    import attackers.ri_enforcer as Attacker

if __name__ == '__main__':
    print("BASE: Creating comms pipe")
    pipe_p, pipe_c = Pipe()

    if ATTACK_ENFORCER:
        # a = Attacker.AttackEnforcer_JamAbort(pipe_p) # For this to do anything you need an abort signal from your base station
        # a = Attacker.AttackEnforcer_JamAll(pipe_p)
        # a = Attacker.AttackEnforcer_JamTime(pipe_p)
        a = Attacker.Attack_Enforcer_Policy_InjectAbort(pipe_p)
        # a = Attacker.AttackEnforcer_AlterConfig(pipe_p)
        a = Attacker.Attack_Enforcer_Policy_InjectAbort(pipe_p)
        pipe_p = a # a implements send and recv to allow normal pipe api

    if RI_ATTACK_ENFORCER:
        ATTACK_ENFORCER = True
        a = Attacker.RI_AttackEnforcer_TOAL(pipe_p)
        pipe_p = a

    print("BASE: Create new TOAL mission")
    m = TOAL.Manager(pipe_c, LOG_STATUS)
    p = Process(target=m.run, args=(None,))

    l = "L_IDLE"

    exited = False
    while not exited:
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
                print("BASE: Setup Mission")
                p.start()
                pipe_p.send([asctime(localtime()), "NEW"])
            l = "L_CONNECT"

        elif l == "L_CONNECT":
            if update[1] == "CONNECTED":
                pipe_p.send([asctime(localtime()), "CONFIG_ALT"])
                l = "L_CONFIG"

        elif l == "L_CONFIG":
            if update[1] == "CONFIGED":
                pipe_p.send([asctime(localtime()), "RUN"])
                l = "L_RUN"
            else:
                pipe_p.send([asctime(localtime()), "CONFIG_ALT", DESIRED_HEIGHT])
                
        elif l == "L_RUN":
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
            l = "L_END"

        elif l == "L_ABORT":
            if update[1] == "LANDING":
                l = "L_DESCEND"
            else:
                pipe_p.send([asctime(localtime()), "ABORT"])

        elif l == "L_END":
            pipe_p.send([asctime(localtime()), "END"])
            if update[1] == "END":
                exited = True
            print("BASE: Mission Ended")

        if curLoc != l:
            print("BASE: FSM Location Transition: " + str(curLoc) + " to " + str(l))