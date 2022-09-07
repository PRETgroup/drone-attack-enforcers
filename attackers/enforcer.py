from attackers.easy_rte.attack_enforcer.attack_enforcer_class import Attack_Enforcer_Policy_Jam_Abort
from attackers.easy_rte.attack_enforcer.attack_enforcer_class import Attack_Enforcer_Policy_Jam_All
from attackers.easy_rte.attack_enforcer.attack_enforcer_class import Attack_Enforcer_Policy_Jam_Time
from attackers.easy_rte.attack_enforcer.attack_enforcer_class import Attack_Enforcer_Policy_Inject_Abort
from attackers.easy_rte.attack_enforcer.attack_enforcer_class import Attack_Enforcer_Policy_Inject_Land
from attackers.easy_rte.attack_enforcer.attack_enforcer_class import Attack_Enforcer_Policy_Alter_Config
from attackers.easy_rte.attack_enforcer.attack_enforcer_class import Attack_Enforcer_Policy_Alter_Config_Location

from time import asctime, localtime

class AttackEnforcer_JamAbort:
    def __init__(self, toDrone):
        self.pipeToDrone = toDrone

        self.enf = Attack_Enforcer_Policy_Jam_Abort()
        self.enf.attack_enforcer_init_all_vars()

    def _notify(self, message):
        print("ATTACKER: " + str(message))

    def send(self, message):
        self.maliciousSend(message)

    def poll(self):
        return self.pipeToDrone.poll()

    def tick(self):
        # Run output enforcer
        self.enf.attack_enforcer_run_output_enforcer_attack_1()

    def recv(self):
        return self.maliciousRecv()

    def maliciousRecv(self):
        a = self.pipeToDrone.recv()
        self._notify("intercepted recv " + str(a))
        return a

    def maliciousSend(self, message):
        self._notify("intercepted send " + str(message))

        # Update enforcer output signals
        self.enf.outputs_attack_enforcer_t[str(message[1])] = True
        # Run output enforcer
        self.tick()
        if not self.enf.outputs_attack_enforcer_t[str(message[1])]: # enforcer blocks transmission
            self._notify("Jammed signal")

        # If enforcer hasn't set output to false 
        if self.enf.outputs_attack_enforcer_t[str(message[1])]:
            # send the message
            self.pipeToDrone.send(message)

class AttackEnforcer_JamAll:
    def __init__(self, toDrone):
        self.pipeToDrone = toDrone

        self.enf = Attack_Enforcer_Policy_Jam_All()
        self.enf.attack_enforcer_init_all_vars()

    def _notify(self, message):
        print("ATTACKER: " + str(message))

    def send(self, message):
        self.maliciousSend(message)

    def poll(self):
        return self.pipeToDrone.poll()

    def tick(self):
        # Run output enforcer
        self.enf.attack_enforcer_run_output_enforcer_jam_all()

    def recv(self):
        return self.maliciousRecv()

    def maliciousRecv(self):
        a = self.pipeToDrone.recv()
        self._notify("intercepted recv " + str(a))
        return a

    def maliciousSend(self, message):
        self._notify("intercepted send " + str(message))

        # Update enforcer output signals
        self.enf.outputs_attack_enforcer_t[str(message[1])] = True
        # Run output enforcer
        self.tick()
        if not self.enf.outputs_attack_enforcer_t[str(message[1])]: # enforcer blocks transmission
            self._notify("Jammed signal")

        # If enforcer hasn't set output to false 
        if self.enf.outputs_attack_enforcer_t[str(message[1])]:
            # send the message
            self.pipeToDrone.send(message)

class AttackEnforcer_JamTime:
    def __init__(self, toDrone):
        self.pipeToDrone = toDrone

        self.enf = Attack_Enforcer_Policy_Jam_Time()
        self.enf.attack_enforcer_init_all_vars()

    def _notify(self, message):
        print("ATTACKER: " + str(message))

    def send(self, message):
        self.maliciousSend(message)

    def poll(self):
        return self.pipeToDrone.poll()

    def recv(self):
        return self.maliciousRecv()

    def tick(self):
        # Run output enforcer
        self.enf.attack_enforcer_run_output_enforcer_jam_time()

    def maliciousRecv(self):
        a = self.pipeToDrone.recv()
        self._notify("intercepted recv " + str(a))
        return a

    def maliciousSend(self, message):
        self._notify("intercepted send " + str(message))

        # Update enforcer output signals
        self.enf.outputs_attack_enforcer_t[str(message[1])] = True

        # Run output enforcer
        self.tick()

        if not self.enf.outputs_attack_enforcer_t[str(message[1])]: # enforcer blocks transmission
            self._notify("Jammed signal")

        # If enforcer hasn't set output to false 
        if self.enf.outputs_attack_enforcer_t[str(message[1])]:
            # send the message
            self.pipeToDrone.send(message)

class Attack_Enforcer_Policy_InjectAbort:
    def __init__(self, toDrone):
        self.pipeToDrone = toDrone

        self.enf = Attack_Enforcer_Policy_Inject_Abort()
        self.enf.attack_enforcer_init_all_vars()

    def _notify(self, message):
        print("ATTACKER: " + str(message))

    def send(self, message):
        self.maliciousSend(message)

    def poll(self):
        return self.pipeToDrone.poll()

    def recv(self):
        return self.maliciousRecv()

    def tick(self):
        # Run output enforcer
        self.enf.attack_enforcer_run_output_enforcer_inject_abort()

        if self.enf.outputs_attack_enforcer_t["ABORT"] == True:
            self._notify("Sending abort signal")
            self.pipeToDrone.send([asctime(localtime()), "ABORT"])

    def maliciousRecv(self):
        a = self.pipeToDrone.recv()
        self._notify("intercepted recv " + str(a))
        return a

    def maliciousSend(self, message):
        self._notify("intercepted send " + str(message))

        # Update enforcer output signals
        self.enf.outputs_attack_enforcer_t[str(message[1])] = True

        # Run output enforcer
        self.tick()

        if not self.enf.outputs_attack_enforcer_t[str(message[1])]: # enforcer blocks transmission
            self._notify("Jammed signal")

        # If enforcer hasn't set output to false 
        if self.enf.outputs_attack_enforcer_t[str(message[1])]:
            # send the message
            self.pipeToDrone.send(message)
            
class Attack_Enforcer_Policy_InjectLand:
    def __init__(self, toDrone):
        self.pipeToDrone = toDrone

        self.enf = Attack_Enforcer_Policy_Inject_Land()
        self.enf.attack_enforcer_init_all_vars()

    def _notify(self, message):
        print("ATTACKER: " + str(message))

    def send(self, message):
        self.maliciousSend(message)

    def poll(self):
        return self.pipeToDrone.poll()

    def recv(self):
        return self.maliciousRecv()

    def tick(self):
        # Run output enforcer
        self.enf.attack_enforcer_run_output_enforcer_inject_land()

        if self.enf.outputs_attack_enforcer_t["LAND"] == True:
            self._notify("Sending land signal")
            self.pipeToDrone.send([asctime(localtime()), "LAND"])

    def maliciousRecv(self):
        a = self.pipeToDrone.recv()
        self._notify("intercepted recv " + str(a))
        return a

    def maliciousSend(self, message):
        self._notify("intercepted send " + str(message))

        # Update enforcer output signals
        self.enf.outputs_attack_enforcer_t[str(message[1])] = True

        # Run output enforcer
        self.tick()

        if not self.enf.outputs_attack_enforcer_t[str(message[1])]: # enforcer blocks transmission
            self._notify("Jammed signal")

        # If enforcer hasn't set output to false 
        if self.enf.outputs_attack_enforcer_t[str(message[1])]:
            # send the message
            self.pipeToDrone.send(message)

class AttackEnforcer_AlterConfig:
    def __init__(self, toDrone):
        self.pipeToDrone = toDrone

        self.enf = Attack_Enforcer_Policy_Alter_Config()
        self.enf.attack_enforcer_init_all_vars()

    def _notify(self, message):
        print("ATTACKER: " + str(message))

    def send(self, message):
        self.maliciousSend(message)

    def poll(self):
        return self.pipeToDrone.poll()

    def tick(self):
        # Run output enforcer
        self.enf.attack_enforcer_run_output_enforcer_alter_config()

    def recv(self):
        return self.maliciousRecv()

    def maliciousRecv(self):
        a = self.pipeToDrone.recv()
        self._notify("intercepted recv " + str(a))
        return a

    def maliciousSend(self, message):
        self._notify("intercepted send " + str(message))

        # Update enforcer output signals
        self.enf.outputs_attack_enforcer_t[str(message[1])] = True
        try:
            if message[1] == "CONFIG":
                self.enf.outputs_attack_enforcer_t["CONFIG_VALUE"] = int(message[2])
        except:
            pass

        # Run output enforcer
        self.tick()

        try:
            if message[2] != self.enf.outputs_attack_enforcer_t["CONFIG_VALUE"]:
                message[2] = self.enf.outputs_attack_enforcer_t["CONFIG_VALUE"]
                self._notify("Changed config value")
        except:
            pass

        # If enforcer hasn't set output to false 
        if self.enf.outputs_attack_enforcer_t[str(message[1])]:
            # send the message
            self.pipeToDrone.send(message)

class AttackEnforcer_AlterConfig_Location:
    def __init__(self, toDrone):
        self.pipeToDrone = toDrone

        self.enf = Attack_Enforcer_Policy_Alter_Config_Location()
        self.enf.attack_enforcer_init_all_vars()

    def _notify(self, message):
        print("ATTACKER: " + str(message))

    def send(self, message):
        self.maliciousSend(message)

    def poll(self):
        return self.pipeToDrone.poll()

    def tick(self):
        # Run output enforcer
        self.enf.attack_enforcer_run_output_enforcer_alter_config_location()

    def recv(self):
        return self.maliciousRecv()

    def maliciousRecv(self):
        a = self.pipeToDrone.recv()
        self._notify("intercepted recv " + str(a))
        return a

    def maliciousSend(self, message):
        self._notify("intercepted send " + str(message))

        # Update enforcer output signals
        self.enf.outputs_attack_enforcer_t[str(message[1])] = True
        try:
            if message[1] == "CONFIG":
                self.enf.outputs_attack_enforcer_t["CONFIG_VALUE"] = int(message[2])
                self.enf.outputs_attack_enforcer_t["CONFIG_VALUE_NORTH"] = int(message[3])
                self.enf.outputs_attack_enforcer_t["CONFIG_VALUE_EAST"] = int(message[4])
        except:
            pass

        # Run output enforcer
        self.tick()

        try:
            if message[2] != self.enf.outputs_attack_enforcer_t["CONFIG_VALUE"]:
                message[2] = self.enf.outputs_attack_enforcer_t["CONFIG_VALUE"]
                self._notify("Changed config value ALTITUDE")
                
            if message[3] != self.enf.outputs_attack_enforcer_t["CONFIG_VALUE_NORTH"]:
                message[3] = self.enf.outputs_attack_enforcer_t["CONFIG_VALUE_NORTH"]
                self._notify("Changed config value NORTH")

            if message[4] != self.enf.outputs_attack_enforcer_t["CONFIG_VALUE_EAST"]:
                message[4] = self.enf.outputs_attack_enforcer_t["CONFIG_VALUE_EAST"]
                self._notify("Changed config value EAST")
        except:
            pass

        # If enforcer hasn't set output to false 
        if self.enf.outputs_attack_enforcer_t[str(message[1])]:
            # send the message
            self.pipeToDrone.send(message)