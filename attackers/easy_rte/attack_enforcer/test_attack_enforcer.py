from attack_enforcer_class import Attack_Enforcer_Policy_Attack_1 

def print_data(count, inputs, outputs):
    print("Tick: " + str(count) + " I: " + str(inputs) + " O: " + str(outputs))

if __name__ == '__main__':
    enf = Attack_Enforcer_Policy_Attack_1()

    enf.attack_enforcer_init_all_vars()

    count = 0
    while (count <= 30):
        enf.outputs_attack_enforcer_t["run"] = True
        if (count >= 10):
            enf.outputs_attack_enforcer_t["run"] = False
            enf.outputs_attack_enforcer_t["abort"] = True

        enf.attack_enforcer_run_via_enforcer()

        print_data(count, enf.inputs_attack_enforcer_t, enf.outputs_attack_enforcer_t)

        count += 1