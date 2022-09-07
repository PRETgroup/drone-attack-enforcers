
//This file should be called F_acbd_manager.c
//This is autogenerated code. Edit by hand at your peril!
#include "F_acbd_manager.h"

void acbd_manager_init_all_vars(enforcervars_acbd_manager_t* me, inputs_acbd_manager_t* inputs, outputs_acbd_manager_t* outputs) {
	//set any input vars with default values
	
	//set any output vars with default values
	

	
	me->_policy_am_state = POLICY_STATE_acbd_manager_am_s0;
	//input policy internal vars
	
	me->v = 0;
	
	
}

void acbd_manager_run_via_enforcer(enforcervars_acbd_manager_t* me, inputs_acbd_manager_t* inputs, outputs_acbd_manager_t* outputs) {
	//run the policies in reverse order for the inputs (last policies have highest priority)
	
	 acbd_manager_run_input_enforcer_am(me, inputs);
	

	acbd_manager_run(inputs, outputs);

	//run policies in specified order for outputs
	acbd_manager_run_output_enforcer_am(me, inputs,outputs);
	
}


//input policies

//INPUT POLICY am BEGIN
//This will run the input enforcer for acbd_manager's policy am
void acbd_manager_run_input_enforcer_am(enforcervars_acbd_manager_t* me, inputs_acbd_manager_t* inputs) {
	switch(me->_policy_am_state) {
		case POLICY_STATE_acbd_manager_am_s0:
			
			if(me->v < 3) {
				//transition s0 -> violation on v < 3
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				
			} 
			
			break;

		case POLICY_STATE_acbd_manager_am_s1:
			
			if(me->v < 3) {
				//transition s1 -> violation on v < 3
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				
			} 
			
			break;

		
	}
}

//INPUT POLICY am END



//output policies

//OUTPUT POLICY am BEGIN
//This will run the input enforcer for acbd_manager's policy am
void acbd_manager_run_output_enforcer_am(enforcervars_acbd_manager_t* me, inputs_acbd_manager_t* inputs, outputs_acbd_manager_t* outputs) {
	//advance timers
	
	me->v++;
	
	//run enforcer
	switch(me->_policy_am_state) {
		case POLICY_STATE_acbd_manager_am_s0:
			
			if( !(outputs->activate_ab) && me->v < 3) {
				//transition s0 -> violation on ( !activate_ab and v < 3 )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->activate_ab = 1;
				
			} 

			break;

		case POLICY_STATE_acbd_manager_am_s1:
			
			if( !(outputs->activate_cd) && me->v < 3) {
				//transition s1 -> violation on ( !activate_cd and v < 3 )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->activate_cd = 1;
				
			} 

			break;

		
	}

	//select transition to advance state
	switch(me->_policy_am_state) {
		case POLICY_STATE_acbd_manager_am_s0:
			
			if(outputs->activate_ab && me->v < 3) {
				//transition s0 -> s0 on ( activate_ab and v < 3 )
				me->_policy_am_state = POLICY_STATE_acbd_manager_am_s0;
				//set expressions
				
				break;
			} 
			if(me->v >= 3) {
				//transition s0 -> s1 on v >= 3
				me->_policy_am_state = POLICY_STATE_acbd_manager_am_s1;
				//set expressions
				
				me->v = 0;
				break;
			} 
			if( !(outputs->activate_ab) && me->v < 3) {
				//transition s0 -> violation on ( !activate_ab and v < 3 )
				me->_policy_am_state = POLICY_STATE_acbd_manager_am_violation;
				//set expressions
				
				break;
			} 
			
			//ensure a transition was taken in this state
			assert(false && "acbd_manager_am_s0 must take a transition"); //if we are still here, then no transition was taken and we are no longer satisfying liveness

			break;

		case POLICY_STATE_acbd_manager_am_s1:
			
			if(outputs->activate_cd && me->v < 3) {
				//transition s1 -> s1 on ( activate_cd and v < 3 )
				me->_policy_am_state = POLICY_STATE_acbd_manager_am_s1;
				//set expressions
				
				break;
			} 
			if(me->v >= 3) {
				//transition s1 -> s0 on v >= 3
				me->_policy_am_state = POLICY_STATE_acbd_manager_am_s0;
				//set expressions
				
				me->v = 0;
				break;
			} 
			if( !(outputs->activate_cd) && me->v < 3) {
				//transition s1 -> violation on ( !activate_cd and v < 3 )
				me->_policy_am_state = POLICY_STATE_acbd_manager_am_violation;
				//set expressions
				
				break;
			} 
			
			//ensure a transition was taken in this state
			assert(false && "acbd_manager_am_s1 must take a transition"); //if we are still here, then no transition was taken and we are no longer satisfying liveness

			break;

		
	}

	//ensure we did not violate (i.e. we did not enter violation state)
	assert(me->_policy_am_state != POLICY_STATE_acbd_manager_am_violation);
}

//OUTPUT POLICY am END



//This function is provided in "F_acbd_manager.c"
//It will check the state of the enforcer monitor code
//It returns one of the following:
//0: currently true (safe)
//1: always true (safe)
//-1: currently false (unsafe)
//-2: always false (unsafe)
//It will need to do some reachability analysis to achieve this

