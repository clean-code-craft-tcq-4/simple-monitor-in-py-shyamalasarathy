SOC_MIN = 20
SOC_MAX = 80

def soc_is_ok(soc):
    if soc < SOC_MIN or soc > SOC_MAX:
        print('State of Charge is out of range!')
        return False
    return True
