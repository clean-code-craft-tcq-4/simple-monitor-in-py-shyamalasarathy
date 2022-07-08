TEMP_MIN = 0
TEMP_MAX = 45
SOC_MIN = 20
SOC_MAX = 80
CHARGE_RATE_MIN = 0.2 #assuming min limit as 0.2
CHARGE_RATE_MAX = 0.8

def limits(param, minlimit, maxlimit):
    if param < minlimit or param > maxlimit:
        return False
    return True

def battery(temp, soc, charge):
    temp_ok = limits(temp, TEMP_MIN, TEMP_MAX)
    soc_ok = limits(soc, SOC_MIN, SOC_MAX)
    chargerate_ok = limits(charge, CHARGE_RATE_MIN, CHARGE_RATE_MAX)
    if temp_ok and soc_ok and chargerate_ok:
        return True
    if not temp_ok:
        print('Temperature is out of range')
    if not soc_ok:
        print('State of charge is out of range')
    if not chargerate_ok:
        print('Charge rate is out of range')
    return False

if __name__ == '__main__':
    assert (battery(30, 50, 0.6) is True)
    assert (battery(50, 90, 0.1) is False)
