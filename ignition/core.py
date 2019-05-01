"""Data file from sensors is read and formatted"""
import numpy as np


#class InputDataOpen(object):
    #def __init__(self, filename):
        #self.file = open(filename)

    #def __enter__(self):
        #return self.file

    #def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        #self.file.close()

#with InputDataOpen('file') as f:
    #in_data = f.read()

def getData(filename):
    try:
        in_data = np.loadtxt(filename)
    except IOError:
        print ('Data Read Error', filename)
    return in_data

#def ptArray(pt_array):
    #pt_index = []
    ###x = funcEval(pt_array)
    #x = pt_array[pt_array>500]
    ###p_data = [float(line) for line in dataname]
    #i = 0
    #for line in pt_array:
        #i += 1
        #if line != x:
            #pt_index.append(0)
        #elif line == x:
            #pt_index.append(i)
    #return pt_index


    #in_data = getData(dataname)
    #p_data = [float(line) for line in in_data]

    #p_data = [float(line) for line in dataname]
    #for line in in_data:
        #p_data.append(float(line))
    #return p_data

def funcEval(pt_values):
    x = pt_values[pt_values>500]
    return x

def ptIndex(pt_array):
    pt_index = []
    ###x = funcEval(pt_array)
    x = pt_array[pt_array>500]
    ###p_data = [float(line) for line in dataname]
    i = 0
    for line in pt_array:
        i += 1
        if line != x:
            pt_index.append(0)
        elif line == x:
            pt_index.append(i)
    return pt_index
