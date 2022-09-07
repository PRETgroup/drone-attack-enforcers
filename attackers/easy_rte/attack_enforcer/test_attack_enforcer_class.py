import attack_enforcer_class as atk_enf_cls
# from attackers.easy_rte.attack_enforcer.attack_enforcer_class import Attack_Enforcer_Policy_Alter_Config_Location

def print_data(count, inputs, outputs):
    print("Tick: " + str(count) + " I: " + str(inputs) + " O: " + str(outputs))

if __name__ == '__main__':
    enf = atk_enf_cls.Attack_Enforcer_Policy_Alter_Config_Location()

    enf.attack_enforcer_init_all_vars()

    count = 0
    while (count <= 30):
        # enf.outputs_attack_enforcer_t["NEW"] = True
        # enf.outputs_attack_enforcer_t["RUN"] = True
        # enf.outputs_attack_enforcer_t["LAND"] = True
        # enf.outputs_attack_enforcer_t["LAND"] = True
        # enf.outputs_attack_enforcer_t["END"] = True
        enf.outputs_attack_enforcer_t["CONFIG"] = True
        enf.outputs_attack_enforcer_t["CONFIG_VALUE"] = 0
        enf.outputs_attack_enforcer_t["CONFIG_VALUE_NORTH"] = 0
        enf.outputs_attack_enforcer_t["CONFIG_VALUE_EAST"] = 0
        # if (count == 10):
            # enf.outputs_attack_enforcer_t["CONFIG"] = True
            # enf.outputs_attack_enforcer_t["CONFIG_VALUE"] = 10
        #     enf.outputs_attack_enforcer_t["run"] = False
        #     enf.outputs_attack_enforcer_t["abort"] = True

        enf.attack_enforcer_run_via_enforcer()

        print_data(count, enf.inputs_attack_enforcer_t, enf.outputs_attack_enforcer_t)

        count += 1