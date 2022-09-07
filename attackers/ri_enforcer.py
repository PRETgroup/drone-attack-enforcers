from attackers.easy_rte.attack_enforcer.attack_enforcer_class import Attack_Enforcer_Policy_Alter_Config_Location, Attack_Enforcer_Policy_Inject_Abort, Attack_Enforcer_Policy_Inject_Land, Attack_Enforcer_Policy_Jam_Abort, Attack_Enforcer_Policy_Jam_Land
# from attackers.easy_rte.attack_enforcer.attack_enforcer_class import Attack_Enforcer_Policy_Jam_Land_Time
from attackers.easy_rte.attack_enforcer.attack_enforcer_class import Attack_Enforcer_Policy_Alter_Config

class RI_AttackEnforcer_TOAL:
    def __init__(self, toDrone):
        self.pipeToDrone = toDrone

        self.enfJamLand = Attack_Enforcer_Policy_Jam_Land()
        self.enfAlter = Attack_Enforcer_Policy_Alter_Config()

        self.l = "L_IDLE"
        self.suspend_enfJamLand = True
        self.suspend_enfAlter = True

        self.t = 0

        self.enfJamLand.attack_enforcer_init_all_vars()
        self.enfAlter.attack_enforcer_init_all_vars()

    def _notify(self, message):
        print("RI ATTACKER: " + str(message))

    def send(self, message):
        self.maliciousSend(message)

    def poll(self):
        return self.pipeToDrone.poll()

    # def tick_and_update(self):
    #     self.t += 1
    #     # Run output enforcer
    #     if not self.suspend_enfJamLand: self.enfJamLand.attack_enforcer_run_via_enforcer()
    #     if not self.suspend_enfAlter: self.enfAlter.attack_enforcer_run_via_enforcer()

    def tick(self):
        self.t += 1
        # Run output enforcer
        if not self.suspend_enfJamLand: self.enfJamLand.attack_enforcer_run_via_enforcer()
        if not self.suspend_enfAlter: self.enfAlter.attack_enforcer_run_via_enforcer()

    def recv(self):
        return self.maliciousRecv()

    def _updateLocation(self, inp, outp):
        oldL = self.l
        
        if self.l == "L_IDLE":
            if inp == "CONNECTED":
                self.l = "L_ALTER_CONFIG"

        elif self.l == "L_ALTER_CONFIG":
            if inp == "CONFIGED":
                self.l = "L_CLIMBING"

        elif self.l == "L_CLIMBING":
            if inp == "AT_ALTITUDE":
                self.t = 0
                self.l = "L_BLOCK_LAND" 

        elif self.l == "L_BLOCK_LAND":
            self._notify(self.t)
            if self.t >= 5: 
                self.l = "L_DONE"

        elif self.l == "L_DONE":
            pass

        self._notify("Transition from " + str(oldL) + " to " + str(self.l))

    def _updateSuspensions(self):
        # Determine suspend signals
        if self.l == "L_IDLE":
            self.suspend_enfJamLand = True
            self.suspend_enfAlter = True

        elif self.l == "L_ALTER_CONFIG":
            self.suspend_enfJamLand = True
            self.suspend_enfAlter = False

        elif self.l == "L_CLIMBING":
            self.suspend_enfJamLand = True
            self.suspend_enfAlter = True

        elif self.l == "L_BLOCK_LAND":
            self.suspend_enfJamLand = False
            self.suspend_enfAlter = True

        elif self.l == "L_DONE":
            self.suspend_enfJamLand = True
            self.suspend_enfAlter = True
            
        self._notify("Suspend enfJamLand: " + str(self.suspend_enfJamLand) + ". Suspend enfAlter: " + str(self.suspend_enfAlter))

    def maliciousRecv(self): # this is like the input
        a = self.pipeToDrone.recv()
        self._notify("intercepted recv " + str(a))
        inp = str(a[1])

        # Update RI location
        self._updateLocation(inp,None)

        self._updateSuspensions()

        return a

    def maliciousSend(self, message): # this is like the output
        self._notify("intercepted send " + str(message))
        outp = str(message[1])

        self._updateLocation(None,outp)

        self._updateSuspensions()

        # Update enforcer output signals
        # self.enfJamLand.outputs_attack_enforcer_t[str(message[1])] = False
        if not self.suspend_enfJamLand: 
            self._notify("Running enfJamLand Attacker Pre Tick")
            self.enfJamLand.outputs_attack_enforcer_t[str(message[1])] = True

        # Update enforcer output signals
        # self.enfAlter.outputs_attack_enforcer_t[str(message[1])] = False
        if not self.suspend_enfAlter:
            self.enfAlter.outputs_attack_enforcer_t[str(message[1])] = True
            try:
                self._notify("Running enfAlter Attacker Pre Tick " + str(message[1]) + " " + str(message[2]))
                if message[1] == "CONFIG":
                    self.enfAlter.outputs_attack_enforcer_t["CONFIG_VALUE"] = int(message[2])
            except:
                pass

        # Run output enforcers
        self.tick()

        ## --------
        ## ENF JAM
        if not self.suspend_enfJamLand:
            self._notify("Running enfJamLand Attacker Post Tick")
            if not self.enfJamLand.outputs_attack_enforcer_t[str(message[1])]: # enforcer blocks transmission
                self._notify("Jammed signal")

            # If enforcer hasn't set output to false 
            if self.enfJamLand.outputs_attack_enforcer_t[str(message[1])]:
                # send the message
                self.pipeToDrone.send(message)
        ## --------

        ## --------
        ## ENF ALTER
        if not self.suspend_enfAlter:
            self._notify("Running enfAlter Attacker Post Tick " + str(self.enfAlter.outputs_attack_enforcer_t["CONFIG_VALUE"]))
            try:
                if message[2] != self.enfAlter.outputs_attack_enforcer_t["CONFIG_VALUE"]:
                    message[2] = self.enfAlter.outputs_attack_enforcer_t["CONFIG_VALUE"]
                    self._notify("Changed config value")
            except:
                pass

            # If enforcer hasn't set output to false 
            if self.enfAlter.outputs_attack_enforcer_t[str(message[1])]:
                # send the message
                self.pipeToDrone.send(message)
        ## --------

        if self.suspend_enfJamLand and self.suspend_enfAlter:
            self.pipeToDrone.send(message)

class RI_AttackEnforcer_TOAL_A2B_A2B2A:
    def __init__(self, toDrone):
        self.pipeToDrone = toDrone

        self.enfJamLand = Attack_Enforcer_Policy_Jam_Land()
        self.enfAlterAltitude = Attack_Enforcer_Policy_Alter_Config()
        self.enfAlterLocation = Attack_Enforcer_Policy_Alter_Config_Location()
        self.enfInjectLand = Attack_Enforcer_Policy_Inject_Land()
        self.enfJamAbort = Attack_Enforcer_Policy_Jam_Abort()

        self.l = "L_IDLE"
        self.suspend_enfJamLand = True
        self.suspend_enfAlterAltitude = True
        self.suspend_enfAlterLocation = True
        self.suspend_enfInjectLand = True
        self.suspend_enfJamAbort = True

        self.t = 0

        self.enfJamLand.attack_enforcer_init_all_vars()
        self.enfAlterAltitude.attack_enforcer_init_all_vars()
        self.enfAlterLocation.attack_enforcer_init_all_vars()
        self.enfInjectLand.attack_enforcer_init_all_vars()
        self.enfJamAbort.attack_enforcer_init_all_vars()

    def _notify(self, message):
        print("RI ATTACKER: " + str(message))

    def send(self, message):
        self.maliciousSend(message)

    def poll(self):
        return self.pipeToDrone.poll()

    def tick(self):
        self.t += 1
        # Run output enforcer
        if not self.suspend_enfJamLand: self.enfJamLand.attack_enforcer_run_via_enforcer()
        if not self.suspend_enfAlterAltitude: self.enfAlterAltitude.attack_enforcer_run_via_enforcer()
        if not self.suspend_enfAlterLocation: self.enfAlterLocation.attack_enforcer_run_via_enforcer()
        if not self.suspend_enfInjectLand: self.enfInjectLand.attack_enforcer_run_via_enforcer()
        if not self.suspend_enfJamAbort: self.enfJamAbort.attack_enforcer_run_via_enforcer()

    def recv(self):
        return self.maliciousRecv()

    def _updateLocation(self, inp, outp):
        oldL = self.l
        
        if self.l == "L_IDLE":
            if inp == "CONNECTED":
                self.l = "L_CONNECTED"

        elif self.l == "L_CONNECTED":
            if outp == "CONFIG_ALT":
                self.l = "L_ALTER_ALT"
            elif outp == "CONFIG_LOC":
                self.l = "L_ALTER_LOC"

        elif self.l == "L_ALTER_ALT":
            if outp == "RUN":
                self.l = "L_CLIMBING"

        elif self.l == "L_ALTER_LOC":
            if outp == "RUN":
                self.l = "L_CLIMBING" 

        elif self.l == "L_CLIMBING":
            if inp == "AT_ALTITUDE":
                self.t = 0
                self.l = "L_BLOCK_LAND" 

            if inp == "AT_B": # this means at location
                self.l = "L_AT_LOCATION" 

        elif self.l == "L_BLOCK_LAND":
            self._notify(self.t)
            if self.t >= 5: 
                self.l = "L_LAND_TOAL"

        elif self.l == "L_LAND_TOAL":
            if inp == "LANDED":
                self.l = "L_IDLE"

        elif self.l == "L_AT_LOCATION":
            if inp == "LANDED":
                self.l = "L_LAND_B"

        elif self.l == "L_LAND_B":
            if inp == "END":
                self.l = "L_STOLEN_DRONE"
            elif outp == "RETURN_A":
                self.l = "L_STOLEN_PACKAGE"

        elif self.l == "L_STOLEN_DRONE":
            # Trap location
            pass

        elif self.l == "L_STOLEN_PACKAGE":
            if outp == "END":
                self.l = "L_IDLE"

        self._notify("Transition from " + str(oldL) + " to " + str(self.l))

    def _anyActiveEnf(self):
        if not self.suspend_enfJamLand: return True
        if not self.suspend_enfAlterAltitude: return True
        if not self.suspend_enfAlterLocation: return True
        if not self.suspend_enfInjectLand: return True
        if not self.suspend_enfJamAbort: return True
        return False

    def _updateSuspensions(self):
        # Determine suspend signals
        self.suspend_enfJamLand = True
        self.suspend_enfAlterAltitude = True
        self.suspend_enfAlterLocation = True

        self.suspend_enfInjectLand = True
        self.suspend_enfJamAbort = True

        if self.l == "L_IDLE":
            pass

        elif self.l == "L_CONNECTED":
            pass

        elif self.l == "L_ALTER_ALT":
            self.suspend_enfAlterAltitude = False
            self._notify("Activate: alter altitude")
            pass

        elif self.l == "L_ALTER_LOC":
            self.suspend_enfAlterLocation = False
            self._notify("Activate: alter location")
            pass

        elif self.l == "L_CLIMBING":
            pass

        elif self.l == "L_BLOCK_LAND":
            self.suspend_enfJamLand = False
            self._notify("Activate: jam land")
            pass

        elif self.l == "L_LAND_TOAL":
            pass

        elif self.l == "L_AT_LOCATION":
            self.suspend_enfInjectLand = False
            self.suspend_enfJamAbort = False
            self._notify("Activate: inject land")
            self._notify("Activate: jam abort")
            pass

        elif self.l == "L_LAND_B":
            pass

        elif self.l == "L_STOLEN_DRONE":
            pass

        elif self.l == "L_STOLEN_PACKAGE":
            pass

        elif self.l == "L_DONE":
            pass
            
    def maliciousRecv(self): # this is like the input
        a = self.pipeToDrone.recv()
        self._notify("intercepted recv " + str(a))
        inp = str(a[1])

        # Update RI location
        self._updateLocation(inp,None)

        self._updateSuspensions()

        return a

    def maliciousSend(self, message): # this is like the output
        self._notify("intercepted send " + str(message))
        outp = str(message[1])

        self._updateLocation(None,outp)

        self._updateSuspensions()

        ## --------
        ## Update controller output signals for enforcers 
        # (that are active)

        # self.enfJamLand.outputs_attack_enforcer_t[str(message[1])] = False
        if not self.suspend_enfJamLand: 
            self._notify("Running enfJamLand Attacker Pre Tick")
            self.enfJamLand.outputs_attack_enforcer_t[str(message[1])] = True

        # Update enforcer output signals
        # self.enfAlterAltitude.outputs_attack_enforcer_t[str(message[1])] = False
        if not self.suspend_enfAlterAltitude:
            self.enfAlterAltitude.outputs_attack_enforcer_t[str(message[1])] = True
            try:
                self._notify("Running enfAlterAltitude Attacker Pre Tick " + str(message[1]) + " " + str(message[2]))
                if message[1] == "CONFIG_ALT":
                    self.enfAlterAltitude.outputs_attack_enforcer_t["CONFIG_VALUE"] = int(message[2])
            except:
                pass

        if not self.suspend_enfAlterLocation:
            self.enfAlterLocation.outputs_attack_enforcer_t[str(message[1])] = True
            try:
                if message[1] == "CONFIG_LOC":
                    self.enfAlterLocation.outputs_attack_enforcer_t["CONFIG_VALUE"] = int(message[2])
                    self.enfAlterLocation.outputs_attack_enforcer_t["CONFIG_VALUE_NORTH"] = int(message[3])
                    self.enfAlterLocation.outputs_attack_enforcer_t["CONFIG_VALUE_EAST"] = int(message[4])
            except:
                pass

        if not self.suspend_enfJamAbort:
            self.enfJamAbort.outputs_attack_enforcer_t[str(message[1])] = True
            
        if not self.suspend_enfInjectLand:
            self.enfInjectLand.outputs_attack_enforcer_t[str(message[1])] = True

        # The whole above section could be done better.. 
        ## --------

        # Run output enforcers
        self.tick()

        ## --------
        ## ENF JAM
        if not self.suspend_enfJamLand:
            self._notify("Running enfJamLand Attacker Post Tick")
            if not self.enfJamLand.outputs_attack_enforcer_t[str(message[1])]: # enforcer blocks transmission
                self._notify("Jammed signal")

            # If enforcer hasn't set output to false 
            if self.enfJamLand.outputs_attack_enforcer_t[str(message[1])]:
                # send the message
                self.pipeToDrone.send(message)
        ## --------

        ## --------
        ## ENF ALTER ALTITUDE
        if not self.suspend_enfAlterAltitude:
            self._notify("Running enfAlterAltitude Attacker Post Tick " + str(self.enfAlterAltitude.outputs_attack_enforcer_t["CONFIG_VALUE"]))
            try:
                if message[2] != self.enfAlterAltitude.outputs_attack_enforcer_t["CONFIG_VALUE"]:
                    message[2] = self.enfAlterAltitude.outputs_attack_enforcer_t["CONFIG_VALUE"]
                    self._notify("Changed config value")
            except:
                pass

            # If enforcer hasn't set output to false 
            if self.enfAlterAltitude.outputs_attack_enforcer_t[str(message[1])]:
                # send the message
                self.pipeToDrone.send(message)
        ## --------

        ## --------
        ## ENF ALTER LOCATION
        if not self.suspend_enfAlterLocation:
            try:
                if message[2] != self.enfAlterLocation.outputs_attack_enforcer_t["CONFIG_VALUE"]:
                    message[2] = self.enfAlterLocation.outputs_attack_enforcer_t["CONFIG_VALUE"]
                    self._notify("Changed config value ALTITUDE")
                    
                if message[3] != self.enfAlterLocation.outputs_attack_enforcer_t["CONFIG_VALUE_NORTH"]:
                    message[3] = self.enfAlterLocation.outputs_attack_enforcer_t["CONFIG_VALUE_NORTH"]
                    self._notify("Changed config value NORTH")

                if message[4] != self.enfAlterLocation.outputs_attack_enforcer_t["CONFIG_VALUE_EAST"]:
                    message[4] = self.enfAlterLocation.outputs_attack_enforcer_t["CONFIG_VALUE_EAST"]
                    self._notify("Changed config value EAST")
            except:
                pass

            # If enforcer hasn't set output to false 
            if self.enfAlterLocation.outputs_attack_enforcer_t[str(message[1])]:
                # send the message
                self.pipeToDrone.send(message)
        ## --------

        ## --------
        ## ENF INJECT LAND
        if not self.suspend_enfInjectLand:

            pass
        ## --------

        ## --------
        ## ENF BLOCK ABORT
        if not self.suspend_enfJamAbort:
            if self.enfJamAbort.outputs_attack_enforcer_t[str(message[1])]:
                # send the message
                self.pipeToDrone.send(message)
        ## --------

        # if enforcer are active, it is the job of the above code to send any messages (transparency incl)
        # if no enforcers are active, the below code, sends whatever came though (RI maintains transparency)
        if not self._anyActiveEnf(): 
            self.pipeToDrone.send(message)