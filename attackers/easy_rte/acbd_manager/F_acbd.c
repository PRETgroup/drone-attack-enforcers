
//This file should be called F_acbd.c
//This is autogenerated code. Edit by hand at your peril!
#include "F_acbd.h"

void acbd_init_all_vars(enforcervars_acbd_t* me, inputs_acbd_t* inputs, outputs_acbd_t* outputs, activations_acbd_t* activations) {
	//set any input vars with default values
	
	//set any output vars with default values
	

	
	me->_policy_ab_state = POLICY_STATE_acbd_ab_s0;
	//input policy internal vars
	
	
	me->_policy_cd_state = POLICY_STATE_acbd_cd_s0;
	//input policy internal vars
	
	
}

void acbd_run_via_enforcer(enforcervars_acbd_t* me, inputs_acbd_t* inputs, outputs_acbd_t* outputs, activations_acbd_t* activations) {
	//run the policies in reverse order for the inputs (last policies have highest priority)
	
	if (activations->cd) acbd_run_input_enforcer_cd(me, inputs);
	if (activations->ab) acbd_run_input_enforcer_ab(me, inputs);

	acbd_run(inputs, outputs);

	//run policies in specified order for outputs
	if (activations->ab) acbd_run_output_enforcer_ab(me, inputs,outputs);
	if (activations->cd) acbd_run_output_enforcer_cd(me, inputs,outputs);
	
}


//input policies

//INPUT POLICY ab BEGIN
//This will run the input enforcer for acbd's policy ab
void acbd_run_input_enforcer_ab(enforcervars_acbd_t* me, inputs_acbd_t* inputs) {
	switch(me->_policy_ab_state) {
		case POLICY_STATE_acbd_ab_s0:
			
			if(inputs->A) {
				//transition s0 -> violation on A
				//select a transition to solve the problem
				
				//Selected non-violation transition "s0 -> s0 on A" which has an equivalent guard, so no action is required
				
			} 
			if( !(inputs->A)) {
				//transition s0 -> violation on not (A)
				//select a transition to solve the problem
				
				//Selected non-violation transition "s0 -> s0 on not (A)" which has an equivalent guard, so no action is required
				
			} 
			
			break;

		
	}
}

//INPUT POLICY ab END

//INPUT POLICY cd BEGIN
//This will run the input enforcer for acbd's policy cd
void acbd_run_input_enforcer_cd(enforcervars_acbd_t* me, inputs_acbd_t* inputs) {
	switch(me->_policy_cd_state) {
		case POLICY_STATE_acbd_cd_s0:
			
			if(inputs->C) {
				//transition s0 -> violation on C
				//select a transition to solve the problem
				
				//Selected non-violation transition "s0 -> s0 on C" which has an equivalent guard, so no action is required
				
			} 
			if( !(inputs->C)) {
				//transition s0 -> violation on not (C)
				//select a transition to solve the problem
				
				//Selected non-violation transition "s0 -> s0 on not (C)" which has an equivalent guard, so no action is required
				
			} 
			
			break;

		
	}
}

//INPUT POLICY cd END



//output policies

//OUTPUT POLICY ab BEGIN
//This will run the input enforcer for acbd's policy ab
void acbd_run_output_enforcer_ab(enforcervars_acbd_t* me, inputs_acbd_t* inputs, outputs_acbd_t* outputs) {
	//advance timers
	
	
	//run enforcer
	switch(me->_policy_ab_state) {
		case POLICY_STATE_acbd_ab_s0:
			
			if(inputs->A && !(outputs->B)) {
				//transition s0 -> violation on ( A and !B )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->B = 1;
				
			} 
			if( !(inputs->A) && outputs->B) {
				//transition s0 -> violation on ( !A and B )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->B = 0;
				
			} 

			break;

		
	}

	//select transition to advance state
	switch(me->_policy_ab_state) {
		case POLICY_STATE_acbd_ab_s0:
			
			if( !(inputs->A)) {
				//transition s0 -> s0 on !A
				me->_policy_ab_state = POLICY_STATE_acbd_ab_s0;
				//set expressions
				
				break;
			} 
			if(inputs->A && outputs->B) {
				//transition s0 -> s0 on ( A and B )
				me->_policy_ab_state = POLICY_STATE_acbd_ab_s0;
				//set expressions
				
				break;
			} 
			if(inputs->A && !(outputs->B)) {
				//transition s0 -> violation on ( A and !B )
				me->_policy_ab_state = POLICY_STATE_acbd_ab_violation;
				//set expressions
				
				break;
			} 
			if( !(inputs->A) && outputs->B) {
				//transition s0 -> violation on ( !A and B )
				me->_policy_ab_state = POLICY_STATE_acbd_ab_violation;
				//set expressions
				
				break;
			} 
			
			//ensure a transition was taken in this state
			assert(false && "acbd_ab_s0 must take a transition"); //if we are still here, then no transition was taken and we are no longer satisfying liveness

			break;

		
	}

	//ensure we did not violate (i.e. we did not enter violation state)
	assert(me->_policy_ab_state != POLICY_STATE_acbd_ab_violation);
}

//OUTPUT POLICY ab END

//OUTPUT POLICY cd BEGIN
//This will run the input enforcer for acbd's policy cd
void acbd_run_output_enforcer_cd(enforcervars_acbd_t* me, inputs_acbd_t* inputs, outputs_acbd_t* outputs) {
	//advance timers
	
	
	//run enforcer
	switch(me->_policy_cd_state) {
		case POLICY_STATE_acbd_cd_s0:
			
			if(inputs->C && !(outputs->D)) {
				//transition s0 -> violation on ( C and !D )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->D = 1;
				
			} 
			if( !(inputs->C) && outputs->D) {
				//transition s0 -> violation on ( !C and D )
				//select a transition to solve the problem
				
				//Recovery instructions manually provided.
				outputs->D = 0;
				
			} 

			break;

		
	}

	//select transition to advance state
	switch(me->_policy_cd_state) {
		case POLICY_STATE_acbd_cd_s0:
			
			if( !(inputs->C)) {
				//transition s0 -> s0 on !C
				me->_policy_cd_state = POLICY_STATE_acbd_cd_s0;
				//set expressions
				
				break;
			} 
			if(inputs->C && outputs->D) {
				//transition s0 -> s0 on ( C and D )
				me->_policy_cd_state = POLICY_STATE_acbd_cd_s0;
				//set expressions
				
				break;
			} 
			if(inputs->C && !(outputs->D)) {
				//transition s0 -> violation on ( C and !D )
				me->_policy_cd_state = POLICY_STATE_acbd_cd_violation;
				//set expressions
				
				break;
			} 
			if( !(inputs->C) && outputs->D) {
				//transition s0 -> violation on ( !C and D )
				me->_policy_cd_state = POLICY_STATE_acbd_cd_violation;
				//set expressions
				
				break;
			} 
			
			//ensure a transition was taken in this state
			assert(false && "acbd_cd_s0 must take a transition"); //if we are still here, then no transition was taken and we are no longer satisfying liveness

			break;

		
	}

	//ensure we did not violate (i.e. we did not enter violation state)
	assert(me->_policy_cd_state != POLICY_STATE_acbd_cd_violation);
}

//OUTPUT POLICY cd END



//This function is provided in "F_acbd.c"
//It will check the state of the enforcer monitor code
//It returns one of the following:
//0: currently true (safe)
//1: always true (safe)
//-1: currently false (unsafe)
//-2: always false (unsafe)
//It will need to do some reachability analysis to achieve this
