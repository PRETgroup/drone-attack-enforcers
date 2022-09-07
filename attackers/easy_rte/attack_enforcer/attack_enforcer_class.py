from enum import Enum

class Attack_Enforcer_Policy_Jam_Abort:
    class attack_enforcer_policy_attack_1_states(Enum):
        POLICY_STATE_attack_enforcer_attack_1_s0 = 1
        POLICY_STATE_attack_enforcer_attack_1_violation = 2

    def __init__(self):
        self.inputs_attack_enforcer_t = {}

        self.outputs_attack_enforcer_t = {
            "NEW": False,
            "RUN": False,
            "END": False,
            "ABORT": False
        }

        self.enforcervars_attack_enforcer_t = {
            "_policy_attack_1_state": self.attack_enforcer_policy_attack_1_states
        } 


    # def attack_enforcer_init_all_vars(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_init_all_vars(self):
        #set any input vars with default values
        
        #set any output vars with default values
        
        self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] = self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_s0
        
    # def attack_enforcer_run_via_enforcer(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_run_via_enforcer(self):
        #run the policies in reverse order for the inputs (last policies have highest priority)

        self.attack_enforcer_run_input_enforcer_attack_1()

        self.attack_enforcer_run()

        #run policies in specified order for outputs
        self.attack_enforcer_run_output_enforcer_attack_1()
        

    #input policies

    #INPUT POLICY attack_1 BEGIN
    #This will run the input enforcer for attack_enforcer's policy attack_1
    # def attack_enforcer_run_input_enforcer_attack_1(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs):
    def attack_enforcer_run_input_enforcer_attack_1(self):
        if self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] == self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_s0:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] == self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_violation:
            return
    #INPUT POLICY attack_1 END

    #output policies

    #OUTPUT POLICY attack_1 BEGIN
    #This will run the input enforcer for attack_enforcer's policy attack_1
    # def attack_enforcer_run_output_enforcer_attack_1(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs):
    def attack_enforcer_run_output_enforcer_attack_1(self):
        #advance timers
        
        #run enforcer
        if self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] == self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_s0:
            if self.outputs_attack_enforcer_t["ABORT"]:
                self.outputs_attack_enforcer_t["ABORT"] = False 
                return
        elif self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] == self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_violation:
            return

        #select transition to advance state
        if self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] == self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_s0:
            if not self.outputs_attack_enforcer_t["ABORT"]:
                self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] = self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_s0
            if self.outputs_attack_enforcer_t["ABORT"]:
                self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] = self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_violation

            #ensure a transition was taken in this state
            # assert(false && "attack_enforcer_attack_1_s0 must take a transition"); #if we are still here, then no transition was taken and we are no longer satisfying liveness


        #ensure we did not violate (i.e. we did not enter violation state)
        # assert(me->_policy_attack_1_state != POLICY_STATE_attack_enforcer_attack_1_violation);

    #OUTPUT POLICY attack_1 END

    def attack_enforcer_run(self):
        return
        
class Attack_Enforcer_Policy_Jam_Land:
    class attack_enforcer_policy_attack_1_states(Enum):
        POLICY_STATE_attack_enforcer_attack_1_s0 = 1
        POLICY_STATE_attack_enforcer_attack_1_violation = 2

    def __init__(self):
        self.inputs_attack_enforcer_t = {}

        self.outputs_attack_enforcer_t = {
            "NEW": False,
            "RUN": False,
            "END": False,
            "LAND": False
        }

        self.enforcervars_attack_enforcer_t = {
            "_policy_attack_1_state": self.attack_enforcer_policy_attack_1_states
        } 


    # def attack_enforcer_init_all_vars(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_init_all_vars(self):
        #set any input vars with default values
        
        #set any output vars with default values
        
        self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] = self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_s0
        
    # def attack_enforcer_run_via_enforcer(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_run_via_enforcer(self):
        #run the policies in reverse order for the inputs (last policies have highest priority)

        self.attack_enforcer_run_input_enforcer_attack_1()

        self.attack_enforcer_run()

        #run policies in specified order for outputs
        self.attack_enforcer_run_output_enforcer_attack_1()
        

    #input policies

    #INPUT POLICY attack_1 BEGIN
    #This will run the input enforcer for attack_enforcer's policy attack_1
    # def attack_enforcer_run_input_enforcer_attack_1(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs):
    def attack_enforcer_run_input_enforcer_attack_1(self):
        if self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] == self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_s0:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] == self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_violation:
            return
    #INPUT POLICY attack_1 END

    #output policies

    #OUTPUT POLICY attack_1 BEGIN
    #This will run the input enforcer for attack_enforcer's policy attack_1
    # def attack_enforcer_run_output_enforcer_attack_1(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs):
    def attack_enforcer_run_output_enforcer_attack_1(self):
        #advance timers
        
        #run enforcer
        if self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] == self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_s0:
            if self.outputs_attack_enforcer_t["LAND"]:
                self.outputs_attack_enforcer_t["LAND"] = False 
                return
        elif self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] == self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_violation:
            return

        #select transition to advance state
        if self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] == self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_s0:
            if not self.outputs_attack_enforcer_t["LAND"]:
                self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] = self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_s0
            if self.outputs_attack_enforcer_t["LAND"]:
                self.enforcervars_attack_enforcer_t["_policy_attack_1_state"] = self.attack_enforcer_policy_attack_1_states.POLICY_STATE_attack_enforcer_attack_1_violation

            #ensure a transition was taken in this state
            # assert(false && "attack_enforcer_attack_1_s0 must take a transition"); #if we are still here, then no transition was taken and we are no longer satisfying liveness


        #ensure we did not violate (i.e. we did not enter violation state)
        # assert(me->_policy_attack_1_state != POLICY_STATE_attack_enforcer_attack_1_violation);

    #OUTPUT POLICY attack_1 END

    def attack_enforcer_run(self):
        return

class Attack_Enforcer_Policy_Jam_All:
    class attack_enforcer_policy_jam_all_states(Enum):
        POLICY_STATE_attack_enforcer_jam_all_s0 = 1
        POLICY_STATE_attack_enforcer_jam_all_violation = 2

    def __init__(self):
        self.inputs_attack_enforcer_t = {}

        self.outputs_attack_enforcer_t = {
            "NEW": False,
            "RUN": False,
            "END": False,
            "ABORT": False
        }

        self.enforcervars_attack_enforcer_t = {
            "_policy_jam_all_state": self.attack_enforcer_policy_jam_all_states
        } 


    # def attack_enforcer_init_all_vars(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_init_all_vars(self):
        #set any input vars with default values
        
        #set any output vars with default values
        
        self.enforcervars_attack_enforcer_t["_policy_jam_all_state"] = self.attack_enforcer_policy_jam_all_states.POLICY_STATE_attack_enforcer_jam_all_s0
        
    # def attack_enforcer_run_via_enforcer(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_run_via_enforcer(self):
        #run the policies in reverse order for the inputs (last policies have highest priority)

        self.attack_enforcer_run_input_enforcer_jam_all()

        self.attack_enforcer_run()

        #run policies in specified order for outputs
        self.attack_enforcer_run_output_enforcer_jam_all()
        

    #input policies

    #INPUT POLICY jam_all BEGIN
    #This will run the input enforcer for attack_enforcer's policy jam_all
    # def attack_enforcer_run_input_enforcer_jam_all(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs):
    def attack_enforcer_run_input_enforcer_jam_all(self):
        if self.enforcervars_attack_enforcer_t["_policy_jam_all_state"] == self.attack_enforcer_policy_jam_all_states.POLICY_STATE_attack_enforcer_jam_all_s0:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_jam_all_state"] == self.attack_enforcer_policy_jam_all_states.POLICY_STATE_attack_enforcer_jam_all_violation:
            return
    #INPUT POLICY jam_all END

    #output policies

    #OUTPUT POLICY jam_all BEGIN
    #This will run the input enforcer for attack_enforcer's policy jam_all
    # def attack_enforcer_run_output_enforcer_jam_all(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs):
    def attack_enforcer_run_output_enforcer_jam_all(self):
        #advance timers
        
        #run enforcer
        if self.enforcervars_attack_enforcer_t["_policy_jam_all_state"] == self.attack_enforcer_policy_jam_all_states.POLICY_STATE_attack_enforcer_jam_all_s0:
            if self.outputs_attack_enforcer_t["NEW"]:
                self.outputs_attack_enforcer_t["NEW"] = False 
            if self.outputs_attack_enforcer_t["RUN"]:
                self.outputs_attack_enforcer_t["RUN"] = False 
            if self.outputs_attack_enforcer_t["END"]:
                self.outputs_attack_enforcer_t["END"] = False 
            if self.outputs_attack_enforcer_t["ABORT"]:
                self.outputs_attack_enforcer_t["ABORT"] = False 
                return
        elif self.enforcervars_attack_enforcer_t["_policy_jam_all_state"] == self.attack_enforcer_policy_jam_all_states.POLICY_STATE_attack_enforcer_jam_all_violation:
            return

        #select transition to advance state
        if self.enforcervars_attack_enforcer_t["_policy_jam_all_state"] == self.attack_enforcer_policy_jam_all_states.POLICY_STATE_attack_enforcer_jam_all_s0:
            if not self.outputs_attack_enforcer_t["NEW"] and not self.outputs_attack_enforcer_t["RUN"] and not self.outputs_attack_enforcer_t["END"] and not self.outputs_attack_enforcer_t["ABORT"]:
                self.enforcervars_attack_enforcer_t["_policy_jam_all_state"] = self.attack_enforcer_policy_jam_all_states.POLICY_STATE_attack_enforcer_jam_all_s0
            if  self.outputs_attack_enforcer_t["NEW"] and  self.outputs_attack_enforcer_t["RUN"] and  self.outputs_attack_enforcer_t["END"] and  self.outputs_attack_enforcer_t["ABORT"]:
                self.enforcervars_attack_enforcer_t["_policy_jam_all_state"] = self.attack_enforcer_policy_jam_all_states.POLICY_STATE_attack_enforcer_jam_all_violation

            #ensure a transition was taken in this state
            # assert(false && "attack_enforcer_jam_all_s0 must take a transition"); #if we are still here, then no transition was taken and we are no longer satisfying liveness


        #ensure we did not violate (i.e. we did not enter violation state)
        # assert(me->_policy_jam_all_state != POLICY_STATE_attack_enforcer_jam_all_violation);

    #OUTPUT POLICY jam_all END

    def attack_enforcer_run(self):
        return

class Attack_Enforcer_Policy_Jam_Time:

    CONST_jam_time_start_jam = 20
    CONST_jam_time_end_jam = 40

    class attack_enforcer_policy_jam_time_states(Enum):
        POLICY_STATE_attack_enforcer_jam_time_s0 = 1
        POLICY_STATE_attack_enforcer_jam_time_s1 = 1
        POLICY_STATE_attack_enforcer_jam_time_violation = 2

    def __init__(self):
        self.inputs_attack_enforcer_t = {}

        self.outputs_attack_enforcer_t = {
            "NEW": False,
            "RUN": False,
            "LAND": False,
            "END": False,
            "ABORT": False
        }

        self.enforcervars_attack_enforcer_t = {
            "_policy_jam_time_state": self.attack_enforcer_policy_jam_time_states,
            "_policy_jam_time_t": 0
        } 


    # def attack_enforcer_init_all_vars(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_init_all_vars(self):
        #set any input vars with default values
        
        #set any output vars with default values
        
        self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_s0
        self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] = 0
        
    # def attack_enforcer_run_via_enforcer(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_run_via_enforcer(self):
        #run the policies in reverse order for the inputs (last policies have highest priority)

        self.attack_enforcer_run_input_enforcer_jam_time()

        self.attack_enforcer_run()

        #run policies in specified order for outputs
        self.attack_enforcer_run_output_enforcer_jam_time()
        

    #input policies

    #INPUT POLICY jam_time BEGIN
    #This will run the input enforcer for attack_enforcer's policy jam_time
    # def attack_enforcer_run_input_enforcer_jam_time(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs):
    def attack_enforcer_run_input_enforcer_jam_time(self):
        if self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] == self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_s0:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] == self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_s1:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] == self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_violation:
            return
    #INPUT POLICY jam_time END

    #output policies

    #OUTPUT POLICY jam_time BEGIN
    #This will run the input enforcer for attack_enforcer's policy jam_time
    # def attack_enforcer_run_output_enforcer_jam_time(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs):
    def attack_enforcer_run_output_enforcer_jam_time(self):
        #advance timers
        # print("")
        # print(self.enforcervars_attack_enforcer_t["_policy_jam_time_state"])
        self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] += 1
        # print(self.enforcervars_attack_enforcer_t["_policy_jam_time_t"])
        # print(self.outputs_attack_enforcer_t["RUN"] and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam)
        # print(self.CONST_jam_time_end_jam)
        
        #run enforcer
        if self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] == self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_s0:
            if self.outputs_attack_enforcer_t["RUN"] and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam:
                self.outputs_attack_enforcer_t["RUN"] = False 
            if self.outputs_attack_enforcer_t["NEW"] and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam:
                self.outputs_attack_enforcer_t["NEW"] = False 
            if self.outputs_attack_enforcer_t["LAND"] and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam:
                self.outputs_attack_enforcer_t["LAND"] = False 
            if self.outputs_attack_enforcer_t["END"] and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam:
                self.outputs_attack_enforcer_t["END"] = False 
            if self.outputs_attack_enforcer_t["ABORT"] and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam:
                self.outputs_attack_enforcer_t["ABORT"] = False 

        elif self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] == self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_s1:
            if self.outputs_attack_enforcer_t["RUN"]:
                self.outputs_attack_enforcer_t["RUN"] = False 
            if self.outputs_attack_enforcer_t["NEW"]:
                self.outputs_attack_enforcer_t["NEW"] = False 
            if self.outputs_attack_enforcer_t["LAND"]:
                self.outputs_attack_enforcer_t["LAND"] = False 
            if self.outputs_attack_enforcer_t["END"]:
                self.outputs_attack_enforcer_t["END"] = False 
            if self.outputs_attack_enforcer_t["ABORT"]:
                self.outputs_attack_enforcer_t["ABORT"] = False

        elif self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] == self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_violation:
            return

        #select transition to advance state
        if self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] == self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_s0:
            if self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] < self.CONST_jam_time_start_jam or self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] > self.CONST_jam_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_s0
                
            if self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_s1

            if self.outputs_attack_enforcer_t["RUN"] and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_violation
            if self.outputs_attack_enforcer_t["NEW"] and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_violation
            if self.outputs_attack_enforcer_t["LAND"] and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_violation
            if self.outputs_attack_enforcer_t["END"] and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_violation
            if self.outputs_attack_enforcer_t["ABORT"] and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_violation

        elif self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] == self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_s1:
            if self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] < self.CONST_jam_time_start_jam or self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] > self.CONST_jam_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_s0

            if self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] >= self.CONST_jam_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_time_t"] <= self.CONST_jam_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_s1

            if self.outputs_attack_enforcer_t["RUN"]:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_violation
            if self.outputs_attack_enforcer_t["NEW"]:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_violation
            if self.outputs_attack_enforcer_t["LAND"]:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_violation
            if self.outputs_attack_enforcer_t["END"]:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_violation
            if self.outputs_attack_enforcer_t["ABORT"]:
                self.enforcervars_attack_enforcer_t["_policy_jam_time_state"] = self.attack_enforcer_policy_jam_time_states.POLICY_STATE_attack_enforcer_jam_time_violation

            #ensure a transition was taken in this state
            # assert(false && "attack_enforcer_jam_time_s0 must take a transition"); #if we are still here, then no transition was taken and we are no longer satisfying liveness

        #ensure we did not violate (i.e. we did not enter violation state)
        # assert(me->_policy_jam_time_state != POLICY_STATE_attack_enforcer_jam_time_violation);

    #OUTPUT POLICY jam_time END

    def attack_enforcer_run(self):
        return

class Attack_Enforcer_Policy_Jam_Land_Time:

    CONST_jam_land_time_start_jam = 0
    CONST_jam_land_time_end_jam = 40

    class attack_enforcer_policy_jam_land_time_states(Enum):
        POLICY_STATE_attack_enforcer_jam_land_time_s0 = 1
        POLICY_STATE_attack_enforcer_jam_land_time_s1 = 2
        POLICY_STATE_attack_enforcer_jam_land_time_violation = 3

    def __init__(self):
        self.inputs_attack_enforcer_t = {}

        self.outputs_attack_enforcer_t = {
            "NEW": False,
            "RUN": False,
            "LAND": False,
            "END": False,
            "ABORT": False
        }

        self.enforcervars_attack_enforcer_t = {
            "_policy_jam_land_time_state": self.attack_enforcer_policy_jam_land_time_states,
            "_policy_jam_land_time_t": 0
        } 


    # def attack_enforcer_init_all_vars(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_init_all_vars(self):
        #set any input vars with default values
        
        #set any output vars with default values
        
        self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] = self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_s0
        self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] = 0
        
    # def attack_enforcer_run_via_enforcer(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_run_via_enforcer(self):
        #run the policies in reverse order for the inputs (last policies have highest priority)

        self.attack_enforcer_run_input_enforcer_jam_land_time()

        self.attack_enforcer_run()

        #run policies in specified order for outputs
        self.attack_enforcer_run_output_enforcer_jam_land_time()
        

    #input policies

    #INPUT POLICY jam_land_time BEGIN
    #This will run the input enforcer for attack_enforcer's policy jam_land_time
    # def attack_enforcer_run_input_enforcer_jam_land_time(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs):
    def attack_enforcer_run_input_enforcer_jam_land_time(self):
        if self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] == self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_s0:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] == self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_s1:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] == self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_violation:
            return
    #INPUT POLICY jam_land_time END

    #output policies

    #OUTPUT POLICY jam_land_time BEGIN
    #This will run the input enforcer for attack_enforcer's policy jam_land_time
    # def attack_enforcer_run_output_enforcer_jam_land_time(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs):
    def attack_enforcer_run_output_enforcer_jam_land_time(self):
        #advance timers
        # print("")
        # print(self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"])
        self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] += 1
        # print(self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"])
        # print(self.outputs_attack_enforcer_t["RUN"] and self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] >= self.CONST_jam_land_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] <= self.CONST_jam_land_time_end_jam)
        # print(self.CONST_jam_land_time_end_jam)
        
        #run enforcer
        if self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] == self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_s0:
            if self.outputs_attack_enforcer_t["LAND"] and self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] >= self.CONST_jam_land_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] <= self.CONST_jam_land_time_end_jam:
                self.outputs_attack_enforcer_t["LAND"] = False 

        elif self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] == self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_s1:
            if self.outputs_attack_enforcer_t["LAND"]:
                self.outputs_attack_enforcer_t["LAND"] = False 

        elif self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] == self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_violation:
            return

        #select transition to advance state
        if self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] == self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_s0:
            if self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] < self.CONST_jam_land_time_start_jam or self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] > self.CONST_jam_land_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] = self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_s0
                
            if self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] >= self.CONST_jam_land_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] <= self.CONST_jam_land_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] = self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_s1

            if self.outputs_attack_enforcer_t["LAND"] and self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] >= self.CONST_jam_land_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] <= self.CONST_jam_land_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] = self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_violation

        elif self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] == self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_s1:
            if self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] < self.CONST_jam_land_time_start_jam or self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] > self.CONST_jam_land_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] = self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_s0

            if self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] >= self.CONST_jam_land_time_start_jam and self.enforcervars_attack_enforcer_t["_policy_jam_land_time_t"] <= self.CONST_jam_land_time_end_jam:
                self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] = self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_s1

            if self.outputs_attack_enforcer_t["LAND"]:
                self.enforcervars_attack_enforcer_t["_policy_jam_land_time_state"] = self.attack_enforcer_policy_jam_land_time_states.POLICY_STATE_attack_enforcer_jam_land_time_violation

            #ensure a transition was taken in this state
            # assert(false && "attack_enforcer_jam_land_time_s0 must take a transition"); #if we are still here, then no transition was taken and we are no longer satisfying liveness

        #ensure we did not violate (i.e. we did not enter violation state)
        # assert(me->_policy_jam_land_time_state != POLICY_STATE_attack_enforcer_jam_land_time_violation);

    #OUTPUT POLICY jam_land_time END

    def attack_enforcer_run(self):
        return

class Attack_Enforcer_Policy_Inject_Abort:

    CONST_inject_abort_time = 18

    class attack_enforcer_policy_inject_abort_states(Enum):
        POLICY_STATE_attack_enforcer_inject_abort_s0 = 1
        POLICY_STATE_attack_enforcer_inject_abort_s1 = 2
        POLICY_STATE_attack_enforcer_inject_abort_violation = 3

    def __init__(self):
        self.inputs_attack_enforcer_t = {}

        self.outputs_attack_enforcer_t = {
            "NEW": False,
            "RUN": False,
            "LAND": False,
            "END": False,
            "ABORT": False
        }

        self.enforcervars_attack_enforcer_t = {
            "_policy_inject_abort_state": self.attack_enforcer_policy_inject_abort_states,
            "_policy_inject_abort_t": 0
        } 


    # def attack_enforcer_init_all_vars(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_init_all_vars(self):
        #set any input vars with default values
        
        #set any output vars with default values
        
        self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"] = self.attack_enforcer_policy_inject_abort_states.POLICY_STATE_attack_enforcer_inject_abort_s0
        self.enforcervars_attack_enforcer_t["_policy_inject_abort_t"] = 0
        
    # def attack_enforcer_run_via_enforcer(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_run_via_enforcer(self):
        #run the policies in reverse order for the inputs (last policies have highest priority)

        self.attack_enforcer_run_input_enforcer_inject_abort()

        self.attack_enforcer_run()

        #run policies in specified order for outputs
        self.attack_enforcer_run_output_enforcer_inject_abort()
        

    #input policies

    #INPUT POLICY inject_abort BEGIN
    #This will run the input enforcer for attack_enforcer's policy inject_abort
    # def attack_enforcer_run_input_enforcer_inject_abort(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs):
    def attack_enforcer_run_input_enforcer_inject_abort(self):
        if self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"] == self.attack_enforcer_policy_inject_abort_states.POLICY_STATE_attack_enforcer_inject_abort_s0:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"] == self.attack_enforcer_policy_inject_abort_states.POLICY_STATE_attack_enforcer_inject_abort_s1:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"] == self.attack_enforcer_policy_inject_abort_states.POLICY_STATE_attack_enforcer_inject_abort_violation:
            return
    #INPUT POLICY inject_abort END

    #output policies

    #OUTPUT POLICY inject_abort BEGIN
    #This will run the input enforcer for attack_enforcer's policy inject_abort
    # def attack_enforcer_run_output_enforcer_inject_abort(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs):
    def attack_enforcer_run_output_enforcer_inject_abort(self):
        #advance timers
        # print("")
        # print(self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"])
        self.enforcervars_attack_enforcer_t["_policy_inject_abort_t"] += 1
        # print(self.enforcervars_attack_enforcer_t["_policy_inject_abort_t"])
        # print(self.outputs_attack_enforcer_t["RUN"] and self.enforcervars_attack_enforcer_t["_policy_inject_abort_t"] >= self.CONST_inject_abort_start_jam and self.enforcervars_attack_enforcer_t["_policy_inject_abort_t"] <= self.CONST_inject_abort_end_jam)
        # print(self.CONST_inject_abort_end_jam)
        
        #run enforcer
        if self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"] == self.attack_enforcer_policy_inject_abort_states.POLICY_STATE_attack_enforcer_inject_abort_s0:
            if self.enforcervars_attack_enforcer_t["_policy_inject_abort_t"] >= self.CONST_inject_abort_time:
                self.outputs_attack_enforcer_t["ABORT"] = True 

        # elif self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"] == self.attack_enforcer_policy_inject_abort_states.POLICY_STATE_attack_enforcer_inject_abort_s1:
        #     return

        elif self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"] == self.attack_enforcer_policy_inject_abort_states.POLICY_STATE_attack_enforcer_inject_abort_violation:
            return

        #select transition to advance state
        if self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"] == self.attack_enforcer_policy_inject_abort_states.POLICY_STATE_attack_enforcer_inject_abort_s0:
            # print("Ding")
            # print(self.outputs_attack_enforcer_t["ABORT"])
            # print(self.CONST_inject_abort_time)
            if self.outputs_attack_enforcer_t["ABORT"] == True and self.enforcervars_attack_enforcer_t["_policy_inject_abort_t"] >= self.CONST_inject_abort_time:
                # print("Dong")
                self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"] = self.attack_enforcer_policy_inject_abort_states.POLICY_STATE_attack_enforcer_inject_abort_s1
                # print(self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"])

            if self.outputs_attack_enforcer_t["ABORT"] == False and self.enforcervars_attack_enforcer_t["_policy_inject_abort_t"] >= self.CONST_inject_abort_time:
                self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"] = self.attack_enforcer_policy_inject_abort_states.POLICY_STATE_attack_enforcer_inject_abort_violation

        elif self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"] == self.attack_enforcer_policy_inject_abort_states.POLICY_STATE_attack_enforcer_inject_abort_s1:
            self.enforcervars_attack_enforcer_t["_policy_inject_abort_state"] = self.attack_enforcer_policy_inject_abort_states.POLICY_STATE_attack_enforcer_inject_abort_s1

            #ensure a transition was taken in this state
            # assert(false && "attack_enforcer_inject_abort_s0 must take a transition"); #if we are still here, then no transition was taken and we are no longer satisfying liveness

        #ensure we did not violate (i.e. we did not enter violation state)
        # assert(me->_policy_inject_abort_state != POLICY_STATE_attack_enforcer_inject_abort_violation);

    #OUTPUT POLICY inject_abort END

    def attack_enforcer_run(self):
        return

class Attack_Enforcer_Policy_Inject_Land:

    CONST_inject_land_time = 0 

    class attack_enforcer_policy_inject_land_states(Enum):
        POLICY_STATE_attack_enforcer_inject_land_s0 = 1
        POLICY_STATE_attack_enforcer_inject_land_s1 = 2
        POLICY_STATE_attack_enforcer_inject_land_violation = 3

    def __init__(self):
        self.inputs_attack_enforcer_t = {}

        self.outputs_attack_enforcer_t = {
            "NEW": False,
            "RUN": False,
            "LAND": False,
            "END": False,
            "ABORT": False
        }

        self.enforcervars_attack_enforcer_t = {
            "_policy_inject_land_state": self.attack_enforcer_policy_inject_land_states,
            "_policy_inject_land_t": 0
        } 


    # def attack_enforcer_init_all_vars(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_init_all_vars(self):
        #set any input vars with default values
        
        #set any output vars with default values
        
        self.enforcervars_attack_enforcer_t["_policy_inject_land_state"] = self.attack_enforcer_policy_inject_land_states.POLICY_STATE_attack_enforcer_inject_land_s0
        self.enforcervars_attack_enforcer_t["_policy_inject_land_t"] = 0
        
    # def attack_enforcer_run_via_enforcer(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_run_via_enforcer(self):
        #run the policies in reverse order for the inputs (last policies have highest priority)

        self.attack_enforcer_run_input_enforcer_inject_land()

        self.attack_enforcer_run()

        #run policies in specified order for outputs
        self.attack_enforcer_run_output_enforcer_inject_land()
        

    #input policies

    #INPUT POLICY inject_land BEGIN
    #This will run the input enforcer for attack_enforcer's policy inject_land
    # def attack_enforcer_run_input_enforcer_inject_land(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs):
    def attack_enforcer_run_input_enforcer_inject_land(self):
        if self.enforcervars_attack_enforcer_t["_policy_inject_land_state"] == self.attack_enforcer_policy_inject_land_states.POLICY_STATE_attack_enforcer_inject_land_s0:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_inject_land_state"] == self.attack_enforcer_policy_inject_land_states.POLICY_STATE_attack_enforcer_inject_land_s1:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_inject_land_state"] == self.attack_enforcer_policy_inject_land_states.POLICY_STATE_attack_enforcer_inject_land_violation:
            return
    #INPUT POLICY inject_land END

    #output policies

    #OUTPUT POLICY inject_land BEGIN
    #This will run the input enforcer for attack_enforcer's policy inject_land
    # def attack_enforcer_run_output_enforcer_inject_land(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs):
    def attack_enforcer_run_output_enforcer_inject_land(self):
        #advance timers
        # print("")
        # print(self.enforcervars_attack_enforcer_t["_policy_inject_land_state"])
        self.enforcervars_attack_enforcer_t["_policy_inject_land_t"] += 1
        # print(self.enforcervars_attack_enforcer_t["_policy_inject_land_t"])
        # print(self.outputs_attack_enforcer_t["RUN"] and self.enforcervars_attack_enforcer_t["_policy_inject_land_t"] >= self.CONST_inject_land_start_jam and self.enforcervars_attack_enforcer_t["_policy_inject_land_t"] <= self.CONST_inject_land_end_jam)
        # print(self.CONST_inject_land_end_jam)
        
        #run enforcer
        if self.enforcervars_attack_enforcer_t["_policy_inject_land_state"] == self.attack_enforcer_policy_inject_land_states.POLICY_STATE_attack_enforcer_inject_land_s0:
            if self.enforcervars_attack_enforcer_t["_policy_inject_land_t"] >= self.CONST_inject_land_time:
                self.outputs_attack_enforcer_t["LAND"] = True 

        # elif self.enforcervars_attack_enforcer_t["_policy_inject_land_state"] == self.attack_enforcer_policy_inject_land_states.POLICY_STATE_attack_enforcer_inject_land_s1:
        #     return

        elif self.enforcervars_attack_enforcer_t["_policy_inject_land_state"] == self.attack_enforcer_policy_inject_land_states.POLICY_STATE_attack_enforcer_inject_land_violation:
            return

        #select transition to advance state
        if self.enforcervars_attack_enforcer_t["_policy_inject_land_state"] == self.attack_enforcer_policy_inject_land_states.POLICY_STATE_attack_enforcer_inject_land_s0:
            if self.outputs_attack_enforcer_t["LAND"] == True and self.enforcervars_attack_enforcer_t["_policy_inject_land_t"] >= self.CONST_inject_land_time:
                self.enforcervars_attack_enforcer_t["_policy_inject_land_state"] = self.attack_enforcer_policy_inject_land_states.POLICY_STATE_attack_enforcer_inject_land_s1

            if self.outputs_attack_enforcer_t["LAND"] == False and self.enforcervars_attack_enforcer_t["_policy_inject_land_t"] >= self.CONST_inject_land_time:
                self.enforcervars_attack_enforcer_t["_policy_inject_land_state"] = self.attack_enforcer_policy_inject_land_states.POLICY_STATE_attack_enforcer_inject_land_violation

        elif self.enforcervars_attack_enforcer_t["_policy_inject_land_state"] == self.attack_enforcer_policy_inject_land_states.POLICY_STATE_attack_enforcer_inject_land_s1:
            self.enforcervars_attack_enforcer_t["_policy_inject_land_state"] = self.attack_enforcer_policy_inject_land_states.POLICY_STATE_attack_enforcer_inject_land_s1

            #ensure a transition was taken in this state
            # assert(false && "attack_enforcer_inject_land_s0 must take a transition"); #if we are still here, then no transition was taken and we are no longer satisfying liveness

        #ensure we did not violate (i.e. we did not enter violation state)
        # assert(me->_policy_inject_land_state != POLICY_STATE_attack_enforcer_inject_land_violation);

    #OUTPUT POLICY inject_land END

    def attack_enforcer_run(self):
        return

class Attack_Enforcer_Policy_Alter_Config:
    class attack_enforcer_policy_alter_config_states(Enum):
        POLICY_STATE_attack_enforcer_alter_config_s0 = 1
        POLICY_STATE_attack_enforcer_alter_config_violation = 2

    def __init__(self):
        self.inputs_attack_enforcer_t = {}

        self.outputs_attack_enforcer_t = {
            "NEW": False,
            "RUN": False,
            "END": False,
            "ABORT": False,
            "CONFIG_ALT": False,
            "CONFIG_VALUE": 0
        }

        self.enforcervars_attack_enforcer_t = {
            "_policy_alter_config_state": self.attack_enforcer_policy_alter_config_states
        } 


    # def attack_enforcer_init_all_vars(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_init_all_vars(self):
        #set any input vars with default values
        
        #set any output vars with default values
        
        self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] = self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_s0
        
    # def attack_enforcer_run_via_enforcer(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_run_via_enforcer(self):
        #run the policies in reverse order for the inputs (last policies have highest priority)

        self.attack_enforcer_run_input_enforcer_alter_config()

        self.attack_enforcer_run()

        #run policies in specified order for outputs
        self.attack_enforcer_run_output_enforcer_alter_config()
        

    #input policies

    #INPUT POLICY alter_config BEGIN
    #This will run the input enforcer for attack_enforcer's policy alter_config
    # def attack_enforcer_run_input_enforcer_alter_config(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs):
    def attack_enforcer_run_input_enforcer_alter_config(self):
        if self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] == self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_s0:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] == self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_violation:
            return
    #INPUT POLICY alter_config END

    #output policies

    #OUTPUT POLICY alter_config BEGIN
    #This will run the input enforcer for attack_enforcer's policy alter_config
    # def attack_enforcer_run_output_enforcer_alter_config(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs):
    def attack_enforcer_run_output_enforcer_alter_config(self):
        #advance timers
        #run enforcer
        if self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] == self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_s0:
            if self.outputs_attack_enforcer_t["CONFIG_ALT"]:
                self.outputs_attack_enforcer_t["CONFIG_VALUE"] = 5 
        elif self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] == self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_violation:
            return

        #select transition to advance state
        if self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] == self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_s0:
            if self.outputs_attack_enforcer_t["CONFIG_ALT"] and self.outputs_attack_enforcer_t["CONFIG_VALUE"] == 5:
                self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] = self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_s0

            if self.outputs_attack_enforcer_t["CONFIG_ALT"] and self.outputs_attack_enforcer_t["CONFIG_VALUE"] != 5:
                self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] = self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_violation

            #ensure a transition was taken in this state
            # assert(false && "attack_enforcer_alter_config_s0 must take a transition"); #if we are still here, then no transition was taken and we are no longer satisfying liveness


        #ensure we did not violate (i.e. we did not enter violation state)
        # assert(me->_policy_alter_config_state != POLICY_STATE_attack_enforcer_alter_config_violation);

    #OUTPUT POLICY alter_config END

    def attack_enforcer_run(self):
        return

class Attack_Enforcer_Policy_Alter_Config_Location:
    class attack_enforcer_policy_alter_config_states(Enum):
        POLICY_STATE_attack_enforcer_alter_config_s0 = 1
        POLICY_STATE_attack_enforcer_alter_config_violation = 2

    def __init__(self):
        self.inputs_attack_enforcer_t = {}

        self.outputs_attack_enforcer_t = {
            "NEW": False,
            "RUN": False,
            "END": False,
            "ABORT": False,
            "CONFIG_LOC": False,
            "CONFIG_VALUE": 0,
            "CONFIG_VALUE_NORTH": 0,
            "CONFIG_VALUE_EAST": 0
        }

        self.enforcervars_attack_enforcer_t = {
            "_policy_alter_config_state": self.attack_enforcer_policy_alter_config_states
        } 

        self.CONFIG_ALTITUDE = 5
        self.CONFIG_NORTH = 20
        self.CONFIG_EAST = 20

    # def attack_enforcer_init_all_vars(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_init_all_vars(self):
        #set any input vars with default values
        
        #set any output vars with default values
        
        self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] = self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_s0
        
    # def attack_enforcer_run_via_enforcer(enforcervars_attack_enforcer_t, inputs_attack_enforcer_t, outputs_attack_enforcer_t):
    def attack_enforcer_run_via_enforcer(self):
        #run the policies in reverse order for the inputs (last policies have highest priority)

        self.attack_enforcer_run_input_enforcer_alter_config_location()

        self.attack_enforcer_run()

        #run policies in specified order for outputs
        self.attack_enforcer_run_output_enforcer_alter_config_location()
        

    #input policies

    #INPUT POLICY alter_config BEGIN
    #This will run the input enforcer for attack_enforcer's policy alter_config
    # def attack_enforcer_run_input_enforcer_alter_config(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs):
    def attack_enforcer_run_input_enforcer_alter_config_location(self):
        if self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] == self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_s0:
            return
        elif self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] == self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_violation:
            return
    #INPUT POLICY alter_config END

    #output policies

    #OUTPUT POLICY alter_config BEGIN
    #This will run the input enforcer for attack_enforcer's policy alter_config
    # def attack_enforcer_run_output_enforcer_alter_config(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs):
    def attack_enforcer_run_output_enforcer_alter_config_location(self):
        #advance timers
        #run enforcer
        if self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] == self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_s0:
            if self.outputs_attack_enforcer_t["CONFIG_LOC"]:
                self.outputs_attack_enforcer_t["CONFIG_VALUE"] = self.CONFIG_ALTITUDE
                self.outputs_attack_enforcer_t["CONFIG_VALUE_NORTH"] = self.CONFIG_NORTH
                self.outputs_attack_enforcer_t["CONFIG_VALUE_EAST"] = self.CONFIG_EAST
        elif self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] == self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_violation:
            return

        #select transition to advance state
        if self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] == self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_s0:
            if self.outputs_attack_enforcer_t["CONFIG_LOC"] and self.outputs_attack_enforcer_t["CONFIG_VALUE"] == self.CONFIG_ALTITUDE:
                self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] = self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_s0

            if self.outputs_attack_enforcer_t["CONFIG_LOC"] and (self.outputs_attack_enforcer_t["CONFIG_VALUE"] != self.CONFIG_ALTITUDE or self.outputs_attack_enforcer_t["CONFIG_VALUE_NORTH"] != self.CONFIG_NORTH or self.outputs_attack_enforcer_t["CONFIG_VALUE_EAST"] != self.CONFIG_EAST):
                self.enforcervars_attack_enforcer_t["_policy_alter_config_state"] = self.attack_enforcer_policy_alter_config_states.POLICY_STATE_attack_enforcer_alter_config_violation

            #ensure a transition was taken in this state
            # assert(false && "attack_enforcer_alter_config_s0 must take a transition"); #if we are still here, then no transition was taken and we are no longer satisfying liveness


        #ensure we did not violate (i.e. we did not enter violation state)
        # assert(me->_policy_alter_config_state != POLICY_STATE_attack_enforcer_alter_config_violation);

    #OUTPUT POLICY alter_config END

    def attack_enforcer_run(self):
        return