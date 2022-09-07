#include "F_acbd_manager.h"

#include "F_acbd.h"

#include <stdio.h>
#include <stdint.h>

void print_data(uint32_t count, inputs_acbd_t inputs, outputs_acbd_t outputs, inputs_acbd_manager_t mgr_inputs, outputs_acbd_manager_t mgr_outputs) {
    printf("Tick %7d: ab:%d - A:%d, B:%d. cd:%d - C:%d, D:%d\r\n", count, mgr_outputs.activate_ab, inputs.A, outputs.B, mgr_outputs.activate_cd, inputs.C, outputs.D);
}

int main() {
    enforcervars_acbd_manager_t mgr_enf;
    inputs_acbd_manager_t mgr_inputs;
    outputs_acbd_manager_t mgr_outputs;

    enforcervars_acbd_t enf;
    inputs_acbd_t inputs;
    outputs_acbd_t outputs;
    activations_acbd_t activations;

    acbd_manager_init_all_vars(&mgr_enf, &mgr_inputs, &mgr_outputs);
    acbd_init_all_vars(&enf, &inputs, &outputs, &activations);

    inputs.A = false;
    inputs.C = false;
    outputs.B = false;
    outputs.D = false;

    mgr_outputs.activate_ab = true; // starts true
    mgr_outputs.activate_cd = false;


    uint32_t count = 0;
    while(count++ < 30) {

        // if(count % 5 == 0) {
            inputs.C = true;
        // } else { 
        //     inputs.C = false;
        // }
        // if(count % 10 == 0) {
            inputs.A = true;
        // } else {
        //     inputs.A = false;
        // }
        outputs.B = false;
        outputs.D = false;

        acbd_run_via_enforcer(&enf, &inputs, &outputs, &activations);
        print_data(count, inputs, outputs, mgr_inputs, mgr_outputs);

        mgr_outputs.activate_ab = false;
        mgr_outputs.activate_cd = false;

        acbd_manager_run_via_enforcer(&mgr_enf, &mgr_inputs, &mgr_outputs);

        activations.ab = mgr_outputs.activate_ab;
        activations.cd = mgr_outputs.activate_cd;

    }
}

void acbd_manager_run(inputs_acbd_manager_t * inputs, outputs_acbd_manager_t * outputs) {
    //do nothing
}

void acbd_run(inputs_acbd_t *inputs, outputs_acbd_t *outputs) {
    //do nothing
}

