CHARGE_RATE_MIN = 0.2 #assuming min limit as 0.2
CHARGE_RATE_MAX = 0.8

def charge_rate_is_ok(charge_rate):
    if charge_rate < CHARGE_RATE_MIN or charge_rate > CHARGE_RATE_MAX:
        print('Charge rate is out of range!')
        return False
    return True
