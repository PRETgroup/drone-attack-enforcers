
//This file should be called F_attack_enforcer.c
//This is autogenerated code. Edit by hand at your peril!
#include "F_attack_enforcer.h"

void attack_enforcer_init_all_vars(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs) {
	//set any input vars with default values
	
	//set any output vars with default values
	

	
	me->_policy_attack_1_state = POLICY_STATE_attack_enforcer_attack_1_s0;
	//input policy internal vars
	
	
	me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_s0;
	//input policy internal vars
	
	me->t = 0;
	
	
}

void attack_enforcer_run_via_enforcer(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs) {
	//run the policies in reverse order for the inputs (last policies have highest priority)
	
	 attack_enforcer_run_input_enforcer_jam_time(me, inputs);
	 attack_enforcer_run_input_enforcer_attack_1(me, inputs);
	

	attack_enforcer_run(inputs, outputs);

	//run policies in specified order for outputs
	attack_enforcer_run_output_enforcer_attack_1(me, inputs,outputs);
	attack_enforcer_run_output_enforcer_jam_time(me, inputs,outputs);
	
}


//input policies

//INPUT POLICY attack_1 BEGIN
//This will run the input enforcer for attack_enforcer's policy attack_1
void attack_enforcer_run_input_enforcer_attack_1(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs) {
	switch(me->_policy_attack_1_state) {
		case POLICY_STATE_attack_enforcer_attack_1_s0:
			
			
			break;

		
	}
}

//INPUT POLICY attack_1 END

//INPUT POLICY jam_time BEGIN
//This will run the input enforcer for attack_enforcer's policy jam_time
void attack_enforcer_run_input_enforcer_jam_time(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs) {
	switch(me->_policy_jam_time_state) {
		case POLICY_STATE_attack_enforcer_jam_time_s0:
			
			if(me->t >= CONST_jam_time_start_jam && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> violation on t >= start_jam and t <= end_jam
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				
			} 
			if(me->t >= CONST_jam_time_start_jam && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> violation on t >= start_jam and t <= end_jam
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				
			} 
			if(me->t >= CONST_jam_time_start_jam && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> violation on t >= start_jam and t <= end_jam
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				
			} 
			if(me->t >= CONST_jam_time_start_jam && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> violation on t >= start_jam and t <= end_jam
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				
			} 
			
			break;

		case POLICY_STATE_attack_enforcer_jam_time_s1:
			
			
			break;

		
	}
}

//INPUT POLICY jam_time END



//output policies

//OUTPUT POLICY attack_1 BEGIN
//This will run the input enforcer for attack_enforcer's policy attack_1
void attack_enforcer_run_output_enforcer_attack_1(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs) {
	//advance timers
	
	
	//run enforcer
	switch(me->_policy_attack_1_state) {
		case POLICY_STATE_attack_enforcer_attack_1_s0:
			
			if(outputs->abort) {
				//transition s0 -> violation on ( abort )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->abort = 0;
				
			} 

			break;

		
	}

	//select transition to advance state
	switch(me->_policy_attack_1_state) {
		case POLICY_STATE_attack_enforcer_attack_1_s0:
			
			if( !(outputs->abort)) {
				//transition s0 -> s0 on ( !abort )
				me->_policy_attack_1_state = POLICY_STATE_attack_enforcer_attack_1_s0;
				//set expressions
				
				break;
			} 
			if(outputs->abort) {
				//transition s0 -> violation on ( abort )
				me->_policy_attack_1_state = POLICY_STATE_attack_enforcer_attack_1_violation;
				//set expressions
				
				break;
			} 
			
			//ensure a transition was taken in this state
			assert(false && "attack_enforcer_attack_1_s0 must take a transition"); //if we are still here, then no transition was taken and we are no longer satisfying liveness

			break;

		
	}

	//ensure we did not violate (i.e. we did not enter violation state)
	assert(me->_policy_attack_1_state != POLICY_STATE_attack_enforcer_attack_1_violation);
}

//OUTPUT POLICY attack_1 END

//OUTPUT POLICY jam_time BEGIN
//This will run the input enforcer for attack_enforcer's policy jam_time
void attack_enforcer_run_output_enforcer_jam_time(enforcervars_attack_enforcer_t* me, inputs_attack_enforcer_t* inputs, outputs_attack_enforcer_t* outputs) {
	//advance timers
	
	me->t++;
	
	//run enforcer
	switch(me->_policy_jam_time_state) {
		case POLICY_STATE_attack_enforcer_jam_time_s0:
			
			if((outputs->run && me->t >= CONST_jam_time_start_jam) && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> violation on ( run and t >= start_jam and t <= end_jam )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->run = 0;
				
			} 
			if((outputs->new && me->t >= CONST_jam_time_start_jam) && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> violation on ( new and t >= start_jam and t <= end_jam )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->new = 0;
				
			} 
			if((outputs->end && me->t >= CONST_jam_time_start_jam) && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> violation on ( end and t >= start_jam and t <= end_jam )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->end = 0;
				
			} 
			if((outputs->abort && me->t >= CONST_jam_time_start_jam) && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> violation on ( abort and t >= start_jam and t <= end_jam )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->abort = 0;
				
			} 

			break;

		case POLICY_STATE_attack_enforcer_jam_time_s1:
			
			if(outputs->run) {
				//transition s1 -> violation on ( run )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->run = 0;
				
			} 
			if(outputs->new) {
				//transition s1 -> violation on ( new )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->new = 0;
				
			} 
			if(outputs->land) {
				//transition s1 -> violation on ( new )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->land = 0;
				
			} 
			if(outputs->end) {
				//transition s1 -> violation on ( end )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->end = 0;
				
			} 
			if(outputs->abort) {
				//transition s1 -> violation on ( abort )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->abort = 0;
				
			} 

			break;

		
	}

	//select transition to advance state
	switch(me->_policy_jam_time_state) {
		case POLICY_STATE_attack_enforcer_jam_time_s0:
			
			if(me->t < CONST_jam_time_start_jam || me->t > CONST_jam_time_end_jam) {
				//transition s0 -> s0 on ( t < start_jam or t > end_jam )
				me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_s0;
				//set expressions
				
				break;
			} 
			if(me->t >= CONST_jam_time_start_jam && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> s1 on ( t >= start_jam and t <= end_jam )
				me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_s1;
				//set expressions
				
				break;
			} 
			if((outputs->run && me->t >= CONST_jam_time_start_jam) && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> violation on ( run and t >= start_jam and t <= end_jam )
				me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_violation;
				//set expressions
				
				break;
			} 
			if((outputs->new && me->t >= CONST_jam_time_start_jam) && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> violation on ( new and t >= start_jam and t <= end_jam )
				me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_violation;
				//set expressions
				
				break;
			} 
			if((outputs->end && me->t >= CONST_jam_time_start_jam) && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> violation on ( end and t >= start_jam and t <= end_jam )
				me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_violation;
				//set expressions
				
				break;
			} 
			if((outputs->abort && me->t >= CONST_jam_time_start_jam) && me->t <= CONST_jam_time_end_jam) {
				//transition s0 -> violation on ( abort and t >= start_jam and t <= end_jam )
				me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_violation;
				//set expressions
				
				break;
			} 
			
			//ensure a transition was taken in this state
			assert(false && "attack_enforcer_jam_time_s0 must take a transition"); //if we are still here, then no transition was taken and we are no longer satisfying liveness

			break;

		case POLICY_STATE_attack_enforcer_jam_time_s1:
			
			if(me->t < CONST_jam_time_start_jam || me->t > CONST_jam_time_end_jam) {
				//transition s1 -> s0 on ( t < start_jam or t > end_jam )
				me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_s0;
				//set expressions
				
				break;
			} 
			if(me->t >= CONST_jam_time_start_jam && me->t <= CONST_jam_time_end_jam) {
				//transition s1 -> s1 on ( t >= start_jam and t <= end_jam )
				me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_s1;
				//set expressions
				
				break;
			} 
			if(outputs->run) {
				//transition s1 -> violation on ( run )
				me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_violation;
				//set expressions
				
				break;
			} 
			if(outputs->new) {
				//transition s1 -> violation on ( new )
				me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_violation;
				//set expressions
				
				break;
			} 
			if(outputs->end) {
				//transition s1 -> violation on ( end )
				me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_violation;
				//set expressions
				
				break;
			} 
			if(outputs->abort) {
				//transition s1 -> violation on ( abort )
				me->_policy_jam_time_state = POLICY_STATE_attack_enforcer_jam_time_violation;
				//set expressions
				
				break;
			} 
			
			//ensure a transition was taken in this state
			assert(false && "attack_enforcer_jam_time_s1 must take a transition"); //if we are still here, then no transition was taken and we are no longer satisfying liveness

			break;

		
	}

	//ensure we did not violate (i.e. we did not enter violation state)
	assert(me->_policy_jam_time_state != POLICY_STATE_attack_enforcer_jam_time_violation);
}

//OUTPUT POLICY jam_time END



//This function is provided in "F_attack_enforcer.c"
//It will check the state of the enforcer monitor code
//It returns one of the following:
//0: currently true (safe)
//1: always true (safe)
//-1: currently false (unsafe)
//-2: always false (unsafe)
//It will need to do some reachability analysis to achieve this

