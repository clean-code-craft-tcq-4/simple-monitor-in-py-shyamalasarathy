TEMP_MIN = 0
TEMP_MAX = 45

def temp_is_ok(temp):
    if temp < TEMP_MIN or temp > TEMP_MAX:
        print('Temperature is out of range!')
        return False
    else:   return True
