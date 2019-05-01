"""Data from the pressure transducer sensors is read and formatted"""
import numpy as np
import pandas as pd


class Nominal:
    def __init__(self):
        self.x = 1
        self.y = 0

def setEngine():
    return Nominal()


def getPressure(filename):
    """Reads pressure data and creates an array"""
    try:
        data = np.loadtxt(filename)
    except IOError:
        print ('File Error', filename)
    p_data = []
    for line in data:
        p_data.append(float(line))
    return p_data


def evalPressure(p_list):
    """Evaluates pressure data from each pressure transducer"""
    length = p_list[p_list>500]
    if length > 0:
        nom = setEngine()
        nominal = nom.y
        return nominal

    elif len(p_list[p_list<0]) > 0:
        raise ValueError('Negative Sensor Value')
        nom = setEngine()
        nominal = nom.x
        return nominal






    #if __name__ == '__main__':
    #vlv_state = np.ones((1,7),int)
    #values = getPressure("test_pres_data.txt")
