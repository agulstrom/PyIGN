"""Data file from sensors is read and formatted"""
import numpy as np

def getData(filename):
    try:
        in_data = np.loadtxt(filename)
    except IOError:
        print ('Data Read Error', filename)
    return in_data

def ptArray(pt_array):
    pt_index = []
    #x = funcEval(pt_array)
    x = pt_array[pt_array>500]
    i = 0
    for line in pt_array:
        i += 1
        if line != x:
            pt_index.append(0)
        elif line == x:
            pt_index.append(i)
    return pt_index

def funcEval(pt_values):
    x = pt_values[pt_values>500]
    return x

def ptIndex(pt_array):
    pt_index = []
    ###x = funcEval(pt_array)
    x = pt_array[pt_array>500]
    i = 0
    for line in pt_array:
        i += 1
        if line != x:
            pt_index.append(0)
        if line == x:
            pt_index.append(i)
    return pt_index
