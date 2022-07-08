import temperature_limits
import soc_limits
import charge_rate_limits

def battery(temp,soc,charge):
    temp_is_ok = temperature_limits.temp_is_ok(temp)
    soc_is_ok = soc_limits.soc_is_ok(soc)
    chargerate_is_ok = charge_rate_limits.charge_rate_is_ok(charge)
    if temp_is_ok and soc_is_ok and chargerate_is_ok:
        return True
    return False

if __name__ == '__main__':
    assert (battery(30,50,0.6) is True)
    assert (battery(50,90,0.1) is False)
