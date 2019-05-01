import numpy as np
import sns_read as sr

def setState(vlv_state):
    """Evaluates the pressure data results and alters the valve state"""
    nominal = evalPressure()
    if nominal == 0:
        vlv_state = np.zeros((1,7),int)
        return print(valve_state)
    elif nominal == 1:
        return print(vlv_state)










if __name__ == '__main__':
#    vlv_state = np.ones((1,7),int)
#    values = sr.getPressure("test_pres_data.txt")
