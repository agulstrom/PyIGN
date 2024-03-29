# third-party libraries
import numpy as np

'''
# local imports
from pyign.functions.limits import PTLimits as ptl
from pyign.functions.limits import TCLimits as tcl
from pyign.functions.limits import LCLimits as lcl
from pyign.functions.states import ValveState as vst
from pyign.functions.states import IgnitorState as ist
from pyign.functions.states import AbortState as ast
from pyign.functions.states import GoState as gst
'''

# local imports
from limits import PTLimits as ptl
from limits import TCLimits as tcl
from limits import LCLimits as lcl
from limits import PTData as ptd
from limits import TCData as tcd
from limits import LCData as lcd
from limits import LSData as lsd
from states import ValveState as vst
from states import IgnitorState as ist
from states import AbortState as ast
from states import GoState as gst
from states import SystemState as sst
from states import ClassWrapper as cw



# def _init_system():
#     valve_state_class = vst()
#     ignitor_state_class = ist()
#     abort_state_class = ast()
#     go_state_class = gst()
#     pt_limit_class = ptl()
#     tc_limit_class = tcl()
#     lc_limit_class = lcl()
#     return valve_state_class, ignitor_state_class, abort_state_class, go_state_class, pt_limit_class, tc_limit_class, lc_limit_class


def _init_system():
    valve_state_class = vst()
    ignitor_state_class = ist()
    abort_state_class = ast()
    go_state_class = gst()
    pt_limit_class = ptl()
    tc_limit_class = tcl()
    lc_limit_class = lcl()
    pt_data_class = ptd()
    tc_data_class = tcd()
    lc_data_class = lcd()
    ls_data_class = lsd()
    return valve_state_class, ignitor_state_class, abort_state_class, go_state_class, pt_limit_class, tc_limit_class, lc_limit_class, pt_data_class, tc_data_class, lc_data_class, ls_data_class


# def getPTData(filename):
#     """Import Pressure Transducer data from as a .txt file and creates a numpy array of sensed data
#
#     Parameters
#     ----------
#     filename : .txt file
#         The first parameter.
#
#     Returns
#     -------
#     pt_input_data : numpy array
#         numpy array of sensed pressure transducer data
#     """
#     try:
#         pt_input_data = np.loadtxt(filename)
#     except IOError:
#         print ('Pressure Transducer Input Data File Read Error', filename)
#     return pt_input_data


def getPTData(*args):
    """Import Pressure Transducer data from as a .txt file and creates a numpy array of sensed data

    Parameters
    ----------
    filename : .txt file
        The first parameter.

    Returns
    -------
    pt_input_data : numpy array
        numpy array of sensed pressure transducer data
    """
    return ptd.pt_data


# def getTCData(filename):
#     """Import Thermocouple data from as a .txt file and creates a numpy array of values of sensed data
#
#     Parameters
#     ----------
#     filename : .txt file
#         The first parameter.
#
#     Returns
#     -------
#     tc_input_data : numpy array
#         numpy array of sensed thermocouple data
#     """
#     try:
#         tc_input_data = np.loadtxt(filename)
#     except IOError:
#         print ('Thermocouple Input Data File Read Error', filename)
#     return tc_input_data


def getTCData(*args):
    """Import Thermocouple data from as a .txt file and creates a numpy array of values of sensed data

    Parameters
    ----------
    filename : .txt file
        The first parameter.

    Returns
    -------
    tc_input_data : numpy array
        numpy array of sensed thermocouple data
    """

    return tcd.tc_data


# def getLCData(filename):
#     """Import Load Cell data from as a .txt file and creates a numpy array of values of sensed data
#
#     Parameters
#     ----------
#     filename : .txt file
#         The first parameter.
#
#     Returns
#     -------
#     lc_input_data : numpy array
#         numpy array of sensed load cell data
#     """
#     try:
#         lc_input_data = np.loadtxt(filename)
#     except IOError:
#         print ('Load Cell Input Data File Read Error', filename)
#     return lc_input_data


def getLCData(*args):
    """Import Load Cell data from as a .txt file and creates a numpy array of values of sensed data

    Parameters
    ----------
    filename : .txt file
        The first parameter.

    Returns
    -------
    lc_input_data : numpy array
        numpy array of sensed load cell data
    """

    return lcd.lc_data


# def getLSData(filename):
#     """Import Limit Switch data from as a .txt file and creates a numpy array of values of sensed data
#
#     Parameters
#     ----------
#     filename : .txt file
#         The first parameter.
#
#     Returns
#     -------
#     ls_input_data : numpy array
#         numpy array of sensed limit switch data
#     """
#     try:
#         ls_input_data = np.loadtxt(filename)
#     except IOError:
#         print ('Limit Switch Input Data File Read Error', filename)
#     return ls_input_data


def getLSData(*args):
    """Import Limit Switch data from as a .txt file and creates a numpy array of values of sensed data

    Parameters
    ----------
    filename : .txt file
        The first parameter.

    Returns
    -------
    ls_input_data : numpy array
        numpy array of sensed limit switch data
    """

    return lsd.ls_state


def getAbortState(*args):
    """Access protected class data of the systems Abort State. This approach is a secure method to access saved system state values. If an abort is tripped, the test stand control system will automatically enter 'Safe' mode and valve configuration

    Parameters
    ----------
    abort_state : int
        Value for abort system state indicates a system abort has not been tripped if 0, and a tripped system abort if 1

    Returns
    -------
    abort_state : int
         0 = system state is nominal, 1 = system abort.
    """
    # return (args[0].abort_state)
    return abt.abort_state


def getNanny(*args):
    """Access protected class data to evaluate if the controls systems automated garduian or 'Nanny' mode is active. This approach is a secure method to access saved system state values. If Nanny mode is activated the test stand control system will automatically enter 'Safe' mode and valve configuration if sensor values exceed set bounds

    Parameters
    ----------
    abort_state : int
        Value for Nanny mode system state indicates if test stand can automatically enter 'Safe' mode if value is 0, and automated monitoring system is operating if value is 1.

    Returns
    -------
    nanny : int
         0 = automated system monitoring mode disabled, 1 = automated system monitoring mode enabled.
    """
    # return (args[0].nanny)
    return abt.nanny


def getGOState(*args):
    """Access protected class data to evaluate if the Fuel, Liquid Oxygen (LOX), and Control Panel system state are a 'GO' as a 1 by 3 numpy array. This approach is a secure method to access saved system state values. If the system sensor values are all nominal and all three controller panels operators are prepared to begin the firing sequence, the three 'GO' state values will return 1.

    Parameters
    ----------
    go_state : int numpy array
        Values for system ready or 'GO' state indicates if a tests firing sequence can commence. If any of the three control panel operators return 0 or 'NOGO', the system will automatically dissable the firing sequence.

    Returns
    -------
    go_state : int numpy array
         [1, 1, 1] = enabled firing sequence.
    """
    # return (args[0].go_states)
    return gst.go_states


def getValveState(*args):
    ##valve_state_class = vst()
    """Access protected class data to evaluate and monitor all 11 of the system actuated valve states. The numpy data structure representation is a 1 by 11 integer numpy array. This approach is a secure method to access saved valve system state values. A valve state value equal to 0 represents valve 'Safe' orientation.

    Parameters
    ----------
    valve_state : int numpy array
        Values for valve state range from 0 for 'Safe' to 1 for 'Active'.
    ignitor_state : int
        Values for ignitor state range from 0 for 'Safe' to 1 for 'Active'.
    abort_state : int
        Values for abort state range from 0 for 'System Performance Nominal' to 1 for 'Abort'.
    check_abort : int
        Nested Function checks if a system abort has been tripped.

    Returns
    -------
    valve_state : int numpy array
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] = 'Safe' system valve state.
    """
    ##return (valve_state_class.valve_state)
    check_abort()
    return (vst.valve_state)
    #check_abort(args[0], args[1], args[2])
    #return (args[0].valve_state)


def getIgnitorState(*args):
    """Access protected class data to evaluate and monitor the system ignitor states. The returned value representation is an integer ranging from 0 to 1. This approach is a secure method to access saved system ignitor state values. The method calls two nested functions.

    Parameters
    ----------
    valve_state : int numpy array
        Values for valve state range from 0 for 'Safe' to 1 for 'Active'.
    ignitor_state : int
        Values for ignitor state range from 0 for 'Safe' to 1 for 'Active'.
    abort_state : int
        Values for abort state range from 0 for 'System Performance Nominal' to 1 for 'Abort'.
    go_state : int numpy array
        Values for go state range from 0 for 'NOGO' to 1 for 'GO'.
    check_go : int
        Nested Function checks if all systems are 'GO' for startup sequence.
    check_abort : int
        Nested Function checks if a system abort has been tripped.

    Returns
    -------
    ignitor_state : int
         0 = 'Safe' system ignitor state, 1 = 'Active' system ignitor state.
    """
    # check_go(args[1], args[3])
    # check_abort(args[0], args[1], args[2])
    # return (args[1].ignitor_state)

    check_go()
    check_abort()
    return (ist.ignitor_state)


def setPTData(*args):
    """Access and changes protected pt_data class data. The returned value representation is an array of data from
       pressure transducers

    Parameters
    ----------
    pt_data: an array containing the pressure transducer data

       """
    ptd.pt_data = args[0]

    # return ptd.pt_data


def setTCData(*args):
    """Access and changes protected tc_data class data. The returned value representation is an array of data from
       thermocouples

    Parameters
    ----------
    tc_data: an array containing the thermocouple data

       """
    tcd.tc_data = args[0]

    # return tcd.tc_data


def setLCData(*args):
    """Access and changes protected lc_data class data. The returned value representation is an array of data from
       load cells

    Parameters
    ----------
    lc_data: an array containing the load cell data

       """
    lcd.lc_data = args[0]

    # return lcd.lc_data


def setLSData(*args):
    """Access and changes protected ls_states class data. The returned value representation is an array of data from
       limit switches

    Parameters
    ----------
    ls_data: an array containing the limit switch states

       """
    lsd.lc_data = args[0]

    # return lsd.lc_data


def setAbortState(*args):
    """Access and changes protected abort_state class data. The returned value representation is an integer ranging from 0 to 1. This approach is a secure method to access and change saved system abort state values.

    Parameters
    ----------
    abort_state : int
        Values for abort state range from 0 for 'System Performance Nominal' to 1 for 'Abort'.
    value : int
        Set values from 0 for 'System Performance Nominal' to 1 for 'Abort'.

    Returns
    -------
    abort_state : int
         Values for abort state range from 0 for 'System Performance Nominal' to 1 for 'Abort'.
    """
    # args[0].abort_state = args[1]
    # return args[0]

    abt.abort_state = args[0]
    # return abt.abort_state

def setNanny(*args):
    """Access and changes protected Nanny mode class data. The returned value representation is an integer ranging from 0 to 1. This approach is a secure method to access and change saved system Nanny mode values.

    Parameters
    ----------
    abort_state : int
        Values for abort state range from 0 for 'System Performance Nominal' to 1 for 'Abort'.
    value : int
        Set values from 0 for 'System Performance Nominal' to 1 for 'Abort'.

    Returns
    -------
    nanny : int
         0 = automated system monitoring mode disabled, 1 = automated system monitoring mode enabled.
    """
    # args[0].nanny = args[1]
    # return args[0]

    abt.nanny = args[0]
    # return abt.nanny

def setGOState(*args):
    """Access and changes protected 'GO' state class data. The returned value representation is a 1 by 3 integer numpy array. This approach is a secure method to access and change saved system 'GO' state values.

    Parameters
    ----------
    go_state : int numpy array
        Values for abort state range from 0 for 'System Performance Nominal' to 1 for 'Abort'.
    panel : str
        Set strings are 'a' for 'Control Panel', 'b' for 'Liquid Oxygen Panel', and 'c' for 'Fuel Panel'.
    value : int
        Set panel values from 0 for 'NOGO' to 1 for 'GO'.

    Returns
    -------
    go_state : int numpy array
         [1, 1, 1] = enabled firing sequence.
    """
    # if args[1] == 'a':
    #     args[0].go_control = args[2]
    # elif args[1] == 'b':
    #     args[0].go_lox = args[2]
    # elif args[1] == 'c':
    #     args[0].go_fuel = args[2]
    # return args[0]

    if args[0] == 'a':
        gst.go_control = args[1]
    elif args[0] == 'b':
        gst.go_lox = args[1]
    elif args[0] == 'c':
        gst.go_fuel = args[1]
    # return gst

def setValveState(*args):
    """Access and changes protected valve state class data. The returned value representation is a 1 by 11 integer numpy array. This approach is a secure method to access and change saved system valve state values.

    Parameters
    ----------
    valve_state : int numby array
        Values for valve state range from 0 for 'Safe' to 1 for 'Active'.
    valve : str
        Set strings range from 'a-k' for each test stand valve.
    value : int
        Set valve values from 0 for 'Safe' to 1 for 'Active'.

    Returns
    -------
    valve_state : int numpy array
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] = 'Safe' system valve state.
    """
    #if args[1] == 'a':
    #    args[0].valve_a = args[2]
    #elif args[1] == 'b':
    #    args[0].valve_b = args[2]
    #elif args[1] == 'c':
    #    args[0].valve_c = args[2]
    #elif args[1] == 'd':
    #    args[0].valve_d = args[2]
    #elif args[1] == 'e':
    #    args[0].valve_e = args[2]
    #elif args[1] == 'f':
    #    args[0].valve_f = args[2]
    #elif args[1] == 'g':
    #    args[0].valve_g = args[2]
    #elif args[1] == 'h':
    #    args[0].valve_h = args[2]
    #elif args[1] == 'i':
    #    args[0].valve_i = args[2]
    #elif args[1] == 'j':
    #    args[0].valve_j = args[2]
    #elif args[1] == 'k':
    #    args[0].valve_k = args[2]
    #return args[0]

    # if args[0] == 'a':
    #     vst.valve_a = args[1]
    # elif args[0] == 'b':
    #     vst.valve_b = args[1]
    # elif args[0] == 'c':
    #     vst.valve_c = args[1]
    # elif args[0] == 'd':
    #     vst.valve_d = args[1]
    # elif args[0] == 'e':
    #     vst.valve_e = args[1]
    # elif args[0] == 'f':
    #     vst.valve_f = args[1]
    # elif args[0] == 'g':
    #     vst.valve_g = args[1]
    # elif args[0] == 'h':
    #     vst.valve_h = args[1]
    # elif args[0] == 'i':
    #     vst.valve_i = args[1]
    # elif args[0] == 'j':
    #     vst.valve_j = args[1]
    # elif args[0] == 'k':
    #     vst.valve_k = args[1]
    # return vst.valve_state
    #check_abort()
    vst.valve_state = args[0]



def setIgnitorState(*args):
    """Access and changes protected ignitor state class data. The returned value representation is an integer. This approach is a secure method to access and change saved system ignitor state values.

    Parameters
    ----------
    ignitor_state : int
        Values for ignitor state range from 0 for 'Safe' to 1 for 'Active'.
    value : int
        Set ignitor value from 0 for 'Safe' to 1 for 'Active'.

    Returns
    -------
    ignitor_state : int
         0 = 'Safe' system ignitor state, 1 = 'Active' system ignitor state
    """
    #args[0].ignitor_state = args[1]
    #return args[0]

    ist.ignitor_state = args[0]
    # return ist


# def pt_index(*args):
#     """Access stored Pressure Transducer data from the sensor limits and collected data to index and build an integer numpy array for sensor values that have exceeded the set bounds.
#
#     Parameters
#     ----------
#     pt_limits : int numpy array
#         Values for pressure transducer limits.
#     pt_data : float numpy array
#         Collected sensor data used to .
#
#     Returns
#     -------
#     pt_input_data : numpy array
#         numpy array of pressure transducers sensed out of bounds
#     """
#     # index = []
#     # x = check_pt_data(args[0], args[1])
#     # i = 0
#     # for line in args[1]:
#     #     i += 1
#     #     if line != x[i-1]:
#     #         index.append(0)
#     #     elif line == x[i-1]:
#     #         index.append(i)
#     # return index
#
#     index = []
#     x = check_pt_data(args[0])
#     i = 0
#     for line in args[0]:
#         i += 1
#         if line != x[i - 1]:
#             index.append(0)
#         elif line == x[i - 1]:
#             index.append(i)
#     return index


def pt_index(*args):
    """Access stored Pressure Transducer data from the sensor limits and collected data to index and build an integer numpy array for sensor values that have exceeded the set bounds.

    Parameters
    ----------
    pt_limits : int numpy array
        Values for pressure transducer limits.
    pt_data : float numpy array
        Collected sensor data used to .

    Returns
    -------
    pt_input_data : numpy array
        numpy array of pressure transducers sensed out of bounds
    """
    # index = []
    # x = check_pt_data(args[0], args[1])
    # i = 0
    # for line in args[1]:
    #     i += 1
    #     if line != x[i-1]:
    #         index.append(0)
    #     elif line == x[i-1]:
    #         index.append(i)
    # return index

    index = []
    x = check_pt_data()
    i = 0
    for line in ptd.pt_data:
        i += 1
        if line != x[i - 1]:
            index.append(0)
        elif line == x[i - 1]:
            index.append(i)
    return index


# def tc_index(*args):
#     """Access stored Thermocouple data from the sensor limits and collected data to index and build an integer numpy array for sensor values that have exceeded the set bounds.
#
#     Parameters
#     ----------
#     tc_limits : int numpy array
#         Values for thermocouple limits.
#     tc_data : float numpy array
#         Collected sensor data used to .
#
#     Returns
#     -------
#     tc_input_data : numpy array
#         numpy array of thermocouples sensed out of bounds
#     """
#     # tc_index = []
#     # x = check_tc_data(args[0], args[1])
#     # i = 0
#     # for line in args[1]:
#     #     i += 1
#     #     if line != x[i-1]:
#     #         tc_index.append(0)
#     #     elif line == x[i-1]:
#     #         tc_index.append(i)
#     # return tc_index
#
#     tc_index = []
#     x = check_tc_data(args[0])
#     i = 0
#     for line in args[0]:
#         i += 1
#         if line != x[i - 1]:
#             tc_index.append(0)
#         elif line == x[i - 1]:
#             tc_index.append(i)
#     return tc_index


def tc_index(*args):
    """Access stored Thermocouple data from the sensor limits and collected data to index and build an integer numpy array for sensor values that have exceeded the set bounds.

    Parameters
    ----------
    tc_limits : int numpy array
        Values for thermocouple limits.
    tc_data : float numpy array
        Collected sensor data used to .

    Returns
    -------
    tc_input_data : numpy array
        numpy array of thermocouples sensed out of bounds
    """
    # tc_index = []
    # x = check_tc_data(args[0], args[1])
    # i = 0
    # for line in args[1]:
    #     i += 1
    #     if line != x[i-1]:
    #         tc_index.append(0)
    #     elif line == x[i-1]:
    #         tc_index.append(i)
    # return tc_index

    tc_index = []
    x = check_tc_data()
    i = 0
    for line in tcd.tc_data:
        i += 1
        if line != x[i - 1]:
            tc_index.append(0)
        elif line == x[i - 1]:
            tc_index.append(i)
    return tc_index


# def lc_index(*args):
#     """Access stored Load Cell data from the sensor limits and collected data to index and build an integer numpy array
#     for sensor values that have exceeded the set bounds.
#
#     Parameters
#     ----------
#     lc_limits : int numpy array
#         Values for load cell limits.
#     lc_data : float numpy array
#         Collected sensor data used to .
#
#     Returns
#     -------
#     lc_input_data : numpy array
#         numpy array of load cells sensed out of bounds.
#     """
#     # lc_index = []
#     # x = check_lc_data(args[0], args[1])
#     # i = 0
#     # for line in args[1]:
#     #     i += 1
#     #     if line != x[i-1]:
#     #         lc_index.append(0)
#     #     elif line == x[i-1]:
#     #         lc_index.append(i)
#     # return lc_index
#
#     lc_index = []
#     x = check_lc_data(args[0])
#     i = 0
#     for line in args[0]:
#         i += 1
#         if line != x[i - 1]:
#             lc_index.append(0)
#         elif line == x[i - 1]:
#             lc_index.append(i)
#     return lc_index


def lc_index(*args):
    """Access stored Load Cell data from the sensor limits and collected data to index and build an integer numpy array
    for sensor values that have exceeded the set bounds.

    Parameters
    ----------
    lc_limits : int numpy array
        Values for load cell limits.
    lc_data : float numpy array
        Collected sensor data used to .

    Returns
    -------
    lc_input_data : numpy array
        numpy array of load cells sensed out of bounds.
    """
    # lc_index = []
    # x = check_lc_data(args[0], args[1])
    # i = 0
    # for line in args[1]:
    #     i += 1
    #     if line != x[i-1]:
    #         lc_index.append(0)
    #     elif line == x[i-1]:
    #         lc_index.append(i)
    # return lc_index

    lc_index = []
    x = check_lc_data()
    i = 0
    for line in lcd.lc_data:
        i += 1
        if line != x[i - 1]:
            lc_index.append(0)
        elif line == x[i - 1]:
            lc_index.append(i)
    return lc_index


# def check_pt_data(*args):
#     """Access stored Pressure Transducer data from the sensor limits and collected data to index and build an integer numpy array for sensor values that have exceeded the set bounds.
#
#     Parameters
#     ----------
#     pt_limits : int numpy array
#         Values for pressure transducer limits.
#     pt_data : float numpy array
#         Collected sensor data used to.
#
#     Returns
#     -------
#     pt_input_data : numpy array
#         numpy array of sensed pressure transducer values data.
#     """
#     # limits = args[0].pt_limits
#     # pt = []
#     # for i in range(len(limits)):
#     #     x=(args[1][i]-limits[i])
#     #     if x >= 0:
#     #         pt.append(args[1][i])
#     #     else:
#     #         pt.append(0)
#     # return pt
#
#     limits = ptl.pt_limits
#     pt = []
#     for i in range(len(limits)):
#         x = (args[0][i] - limits[i])
#         if x >= 0:
#             pt.append(args[0][i])
#         else:
#             pt.append(0)
#     return pt


def check_pt_data(*args):
    """Access stored Pressure Transducer data from the sensor limits and collected data to index and build an integer numpy array for sensor values that have exceeded the set bounds.

    Parameters
    ----------
    pt_limits : int numpy array
        Values for pressure transducer limits.
    pt_data : float numpy array
        Collected sensor data used to.

    Returns
    -------
    pt_input_data : numpy array
        numpy array of sensed pressure transducer values data.
    """
    # limits = args[0].pt_limits
    # pt = []
    # for i in range(len(limits)):
    #     x=(args[1][i]-limits[i])
    #     if x >= 0:
    #         pt.append(args[1][i])
    #     else:
    #         pt.append(0)
    # return pt

    limits = ptl.pt_limits
    pt = []
    for i in range(len(limits)):
        x = (ptd.pt_data[i] - limits[i])
        if x >= 0:
            pt.append(ptl.pt_limits[i])
        else:
            pt.append(0)
    return pt


# def check_tc_data(*args):
#     """Access stored Thermocouple data from the sensor limits and collected data to index and build an integer numpy array for sensor values that have exceeded the set bounds.
#
#     Parameters
#     ----------
#     tc_limits : int numpy array
#         Values for thermocouple limits.
#     tc_data : float numpy array
#         Collected sensor data used to.
#
#     Returns
#     -------
#     tc_input_data : numpy array
#         numpy array of sensed thermocouple values data.
#     """
#     # limits = args[0].tc_limits
#     # tc = []
#     # for i in range(len(limits)):
#     #     x=(args[1][i]-limits[i])
#     #     if x >= 0:
#     #         tc.append(args[1][i])
#     #     else:
#     #         tc.append(0)
#     # return tc
#
#     limits = tcl.tc_limits
#     tc = []
#     for i in range(len(limits)):
#         x = (args[0][i] - limits[i])
#         if x >= 0:
#             tc.append(args[0][i])
#         else:
#             tc.append(0)
#     return tc


def check_tc_data(*args):
    """Access stored Thermocouple data from the sensor limits and collected data to index and build an integer numpy array for sensor values that have exceeded the set bounds.

    Parameters
    ----------
    tc_limits : int numpy array
        Values for thermocouple limits.
    tc_data : float numpy array
        Collected sensor data used to.

    Returns
    -------
    tc_input_data : numpy array
        numpy array of sensed thermocouple values data.
    """
    # limits = args[0].tc_limits
    # tc = []
    # for i in range(len(limits)):
    #     x=(args[1][i]-limits[i])
    #     if x >= 0:
    #         tc.append(args[1][i])
    #     else:
    #         tc.append(0)
    # return tc

    limits = tcl.tc_limits
    tc = []
    for i in range(len(limits)):
        x = (tcd.tc_data[i] - limits[i])
        if x >= 0:
            tc.append(tcd.tc_data[i])
        else:
            tc.append(0)
    return tc


# def check_lc_data(*args):
#     """Access stored Load Cell data from the sensor limits and collected data to index and build an integer numpy array for sensor values that have exceeded the set bounds.
#
#     Parameters
#     ----------
#     lc_limits : int numpy array
#         Values for load cell limits.
#     lc_data : float numpy array
#         Collected sensor data used to.
#
#     Returns
#     -------
#     lc_input_data : numpy array
#         numpy array of sensed load cell values data.
#     """
#     # limits = args[0].lc_limits
#     # lc = []
#     # for i in range(len(limits)):
#     #     x=(args[1][i]-limits[i])
#     #     if x >= 0:
#     #         lc.append(args[1][i])
#     #     else:
#     #         lc.append(0)
#     # return lc
#
#     limits = lcl.lc_limits
#     lc = []
#     for i in range(len(limits)):
#         x = (args[0][i] - limits[i])
#         if x >= 0:
#             lc.append(args[0][i])
#         else:
#             lc.append(0)
#     return lc


def check_lc_data(*args):
    """Access stored Load Cell data from the sensor limits and collected data to index and build an integer numpy array for sensor values that have exceeded the set bounds.

    Parameters
    ----------
    lc_limits : int numpy array
        Values for load cell limits.
    lc_data : float numpy array
        Collected sensor data used to.

    Returns
    -------
    lc_input_data : numpy array
        numpy array of sensed load cell values data.
    """
    # limits = args[0].lc_limits
    # lc = []
    # for i in range(len(limits)):
    #     x=(args[1][i]-limits[i])
    #     if x >= 0:
    #         lc.append(args[1][i])
    #     else:
    #         lc.append(0)
    # return lc

    limits = lcl.lc_limits
    lc = []
    for i in range(len(limits)):
        x = (lcd.lc_data[i] - limits[i])
        if x >= 0:
            lc.append(lcd.lc_data[i])
        else:
            lc.append(0)
    return lc


# def check_limits(*args):
#     """Check if any sensor is out of limit range, if out of bounds is detected, abort is tripped and system enters 'Safe' mode.
#
#     Parameters
#     ----------
#     nanny : int
#         Value for Nanny mode system state indicates if test stand can automatically enter 'Safe' mode if value is 0, and automated monitoring system is operating if value is 1.
#     pt_limits : int numpy array
#         Values for pressure transducer limits.
#     tc_limits : int numpy array
#         Values for thermocouple limits.
#     lc_limits : int numpy array
#         Values for load cell limits.
#     pt_data : float numpy array
#         Sensed pressure transducer data.
#     tc_data : float numpy array
#         Sensed thermocouple data.
#     lc_data : float numpy array
#         Sensed load cell data.
#
#     Returns
#     -------
#     abort_state : int
#          0 = system state is nominal, 1 = system abort.
#     """
#     # if getNanny(args[0]) == 1:
#     #     if np.sum(pt_index(args[1], args[4]))!= 0:
#     #         setAbortState(args[0], 1)
#     #     elif np.sum(tc_index(args[2], args[5]))!= 0:
#     #         setAbortState(args[0], 1)
#     #     elif np.sum(lc_index(args[3], args[6]))!= 0:
#     #         setAbortState(args[0], 1)
#     # return args[0]
#
#     if getNanny() == 1:
#         if np.sum(pt_index(args[0])) != 0:
#             setAbortState(1)
#         elif np.sum(tc_index(args[1])) != 0:
#             setAbortState(1)
#         elif np.sum(lc_index(args[2])) != 0:
#             setAbortState(1)
#
#     return abt.abort_state


def check_limits(*args):
    """Check if any sensor is out of limit range, if out of bounds is detected, abort is tripped and system enters 'Safe' mode.

    Parameters
    ----------
    nanny : int
        Value for Nanny mode system state indicates if test stand can automatically enter 'Safe' mode if value is 0, and automated monitoring system is operating if value is 1.
    pt_limits : int numpy array
        Values for pressure transducer limits.
    tc_limits : int numpy array
        Values for thermocouple limits.
    lc_limits : int numpy array
        Values for load cell limits.
    pt_data : float numpy array
        Sensed pressure transducer data.
    tc_data : float numpy array
        Sensed thermocouple data.
    lc_data : float numpy array
        Sensed load cell data.

    Returns
    -------
    abort_state : int
         0 = system state is nominal, 1 = system abort.
    """
    # if getNanny(args[0]) == 1:
    #     if np.sum(pt_index(args[1], args[4]))!= 0:
    #         setAbortState(args[0], 1)
    #     elif np.sum(tc_index(args[2], args[5]))!= 0:
    #         setAbortState(args[0], 1)
    #     elif np.sum(lc_index(args[3], args[6]))!= 0:
    #         setAbortState(args[0], 1)
    # return args[0]

    if getNanny() == 1:
        if np.sum(pt_index()) != 0:
            setAbortState(1)
        elif np.sum(tc_index()) != 0:
            setAbortState(1)
        elif np.sum(lc_index()) != 0:
            setAbortState(1)

    return abt.abort_state


# def check_limit_switch(*args):
#     """Check if valve is in correct state by comparing set valve state to sensed limit switch state, if values differ, abort mode is tripped.
#
#     Parameters
#     ----------
#     abort_state : int
#         Values for abort state range from 0 for 'System Performance Nominal' to 1 for 'Abort'.
#     valve_state : int numby array
#         Values for valve state range from 0 for 'Safe' to 1 for 'Active'.
#     ls_data : int numpy array
#         Sensed limit switch data.
#
#     Returns
#     -------
#     abort_state : int
#          0 = system state is nominal, 1 = system abort.
#     """
#     # if np.array_equal(args[1].valve_state, args[2]) == False:
#     #     setAbortState(args[0], 1)
#     # return args[0]
#
#     if np.array_equal(vst.valve_state, args[0]) == False:
#         setAbortState(1)
#
#     return abt.abort_state


def check_limit_switch(*args):
    ##_____________________________________________________________________________________________________________##
    """Check if valve is in correct state by comparing set valve state to sensed limit switch state, if values differ, abort mode is tripped.

    Parameters
    ----------
    abort_state : int
        Values for abort state range from 0 for 'System Performance Nominal' to 1 for 'Abort'.
    valve_state : int numby array
        Values for valve state range from 0 for 'Safe' to 1 for 'Active'.
    ls_data : int numpy array
        Sensed limit switch data.

    Returns
    -------
    abort_state : int
         0 = system state is nominal, 1 = system abort.
    """
    # if np.array_equal(args[1].valve_state, args[2]) == False:
    #     setAbortState(args[0], 1)
    # return args[0]

    ##_____________________________________________________________________________________________________________##
    ## USE TIME DELAY TO EVALUATE CHECK_LSL ##

    if np.array_equal(vst.valve_state, lsd.ls_state) == False:
        setAbortState(1)

    return abt.abort_state


def check_abort(*args):
    """Check Abort State, if abort has been tripped, all valves and the ignitor are set to 'Safe' state until system is restarted.

    Parameters
    ----------
    valve_state : int numby array
        Values for valve state range from 0 for 'Safe' to 1 for 'Active'.
    ignitor_state : int
        Values for ignitor state range from 0 for 'Safe' to 1 for 'Active'.
    abort_state : int
        Values for abort state range from 0 for 'System Performance Nominal' to 1 for 'Abort'.

    Returns
    -------
    valve_state : int numpy array
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] = 'Safe' system valve state.
    ignitor_state : int
         0 = 'Safe' system ignitor state, 1 = 'Active' system ignitor state.
    """
    # if np.sum(getAbortState(args[2])) == 1:
    #     args[0].valve_a = 0
    #     args[0].valve_b = 0
    #     args[0].valve_c = 0
    #     args[0].valve_c = 0
    #     args[0].valve_e = 0
    #     args[0].valve_f = 0
    #     args[0].valve_g = 0
    #     args[0].valve_h = 0
    #     args[0].valve_i = 0
    #     args[0].valve_j = 0
    #     args[0].valve_k = 0
    #     args[1].ignitor_state = 0
    # return args[0], args[1]

    # if getAbortState() == 1:
    #     vst.valve_a = 0
    #     vst.valve_b = 0
    #     vst.valve_c = 0
    #     vst.valve_c = 0
    #     vst.valve_e = 0
    #     vst.valve_f = 0
    #     vst.valve_g = 0
    #     vst.valve_h = 0
    #     vst.valve_i = 0
    #     vst.valve_j = 0
    #     vst.valve_k = 0
    #     ist.ignitor_state = 0

    if getAbortState() == 1:
        vst.valve_state = [0]*11
        ist.ignitor_state = 0
    return vst, ist.ignitor_state


def check_go(*args):
    """Check GO State, if all three panels are NOT a 'GO', set ignitor state 'Safe' mode.

    Parameters
    ----------
    ignitor_state : int
        Values for ignitor state range from 0 for 'Safe' to 1 for 'Active'.
    go_state : int numpy array
        Values for system ready or 'GO' state indicates if a tests firing sequence can commence. If any of the three control panel operators return 0 or 'NOGO', the system will automatically dissable the firing sequence.

    Returns
    -------
    ignitor_state : int
         0 = 'Safe' system ignitor state, 1 = 'Active' system ignitor state.
    """
    # if np.sum(getGOState(args[1]))!= 3:
    #     args[0].ignitor_state = 0
    # return args[0]

    if np.sum(getGOState())!= 3:
        ist.ignitor_state = 0

    return ist


# def access_class():
#     vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
#     return vst, ist, abt, gst, ptl, tcl, lcl

def access_class():
    vst, ist, abt, gst, ptl, tcl, lcl, ptd, tcd, lcd, lsd = _init_system()
    return vst, ist, abt, gst, ptl, tcl, lcl, ptd, tcd, lcd, lsd


def labview_access():
    """"Define wrapper for LabVIEW Python node"""
    new_class_object = cw(4882)
    return new_class_object.get_value()


def labview_to_python(*args):
    """Take information from Labview and break into classes

    Parameters
    ----------
    input_data : int numpy array
        Most recent data from Labview with the following setup:
        """


    valve_states = args[0][0:11]
    check_valve_change(valve_states)

    return getValveState()

def check_valve_change(*args):
    """Check if valve states have changed since previous data pull

    Parameters
    ----------
    valve_state_new: int numpy array
        The most recent state of the valves range from 0 for 'Safe' to 1 for 'Active'
    """

    valve_state_old = getValveState()
    if np.array_equal(valve_state_old, args[0]) == False:
        setValveState(args[0])



if __name__ == '__main__':
    '''
    vst, ist, abt, gst, ptl, tcl, lcl = access_class()
    #setGOState(gst, 'a', 1)
    #print('GO State =', getGOState(gst))

    print(getValveState())
    setValveState('a', 1)
    print(getValveState())
    setValveState('d', 1)
    print(getValveState())
    '''
    '''
    def getIgnitorState(vst, ist, abt, gst):
        check_go(ist, gst)
        return (ist.ignitor_state)
    def setIgnitorState(ist, args):
        ist.ignitor_state = args
        return ist
    def check_go(ist, gst):
        go = getGOState(gst)
        if np.sum(go)!= 3:
            ist.ignitor_state = 0
        return ist
    '''
    ####
    '''
    vst, ist, abt, gst, ptl, tcl, lcl = _init_system()
    setGOState(gst,'a',1)
    setGOState(gst,'b',1)
    setGOState(gst,'c',1)
    print('Ignitor State =', getIgnitorState(vst, ist, abt, gst))
    setIgnitorState(ist,1)
    print('Ignitor State =', getIgnitorState(vst, ist, abt, gst))
    print('')
    '''
    ####
    '''
    print(getAbortState(abt))
    setAbortState(abt,1)
    print(getAbortState(abt))
    setAbortState(abt,0)
    print(abt.abort_state)
    print(getAbortState(abt))
    print(getNanny(abt))
    setNanny(abt, 1)
    print(getNanny(abt))
    '''
    ####
    '''
    setNanny(abt, 1)
    print('Nanny =', getNanny(abt))
    pt_data = [500, 500, 530, 500, 530, 500, 750]
    tc_data = [82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572]
    lc_data = [599, 599, 2999]
    ls_data = [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]
    check_limits(abt, ptl, tcl, lcl, pt_data, tc_data, lc_data)
    setValveState(vst, 'b', 1)
    setValveState(vst, 'c', 1)
    setValveState(vst, 'g', 1)
    print('Abort State =', getAbortState(abt))
    print('Valve State =', getValveState(vst, ist, abt))
    print('')
    print('Abort State =', getAbortState(abt))
    print(ls_data)
    check_limit_switch(abt, vst, ls_data)
    print('Abort State =', getAbortState(abt))
    print('Valve State =', getValveState(vst, ist, abt))
    print('')
    '''
    ####
    '''
    pt_data = [500, 500, 530, 500, 530, 500, 750]
    tc_data = [82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572]
    lc_data = [599, 599, 3999]
    ls_data = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    check_limits(abt, ptl, tcl, lcl, pt_data, tc_data, lc_data)
    print('Abort State =', getAbortState(abt))
    print('Valve State =', getValveState(vst, ist, abt))
    print('')
    setValveState(vst, 'b', 1)
    setValveState(vst, 'c', 1)
    setValveState(vst, 'g', 1)
    check_limits(abt, ptl, tcl, lcl, pt_data, tc_data, lc_data)
    print('Abort State =', getAbortState(abt))
    print('Valve State =', getValveState(vst, ist, abt))
    print('')
    setAbortState(abt, 0)
    setValveState(vst, 'b', 1)
    setValveState(vst, 'c', 1)
    setValveState(vst, 'g', 1)
    setNanny(abt, 0)
    print('Nanny =', getNanny(abt))
    check_limits(abt, ptl, tcl, lcl, pt_data, tc_data, lc_data)
    print('Abort State =', getAbortState(abt))
    print('Valve State =', getValveState(vst, ist, abt))
    print('')
    setNanny(abt, 1)
    pt_data = [500, 500, 530, 500, 530, 500, 750]
    tc_data = [82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572]
    lc_data = [599, 599, 2999]
    ls_data = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    check_limits(abt, ptl, tcl, lcl, pt_data, tc_data, lc_data)
    print('Abort State =', getAbortState(abt))
    print('Valve State =', getValveState(vst, ist, abt))
    print('')
    setValveState(vst, 'b', 1)
    setValveState(vst, 'c', 1)
    setValveState(vst, 'g', 1)
    check_limits(abt, ptl, tcl, lcl, pt_data, tc_data, lc_data)
    print('Abort State =', getAbortState(abt))
    print('Valve State =', getValveState(vst, ist, abt))
    print('')
    pt_data = [500, 500, 530, 500, 530, 500, 750]
    tc_data = [82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572]
    lc_data = [599, 599, 3999]
    ls_data = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    check_limits(abt, ptl, tcl, lcl, pt_data, tc_data, lc_data)
    print('Abort State =', getAbortState(abt))
    print('Valve State =', getValveState(vst, ist, abt))
    print('')
    setValveState(vst, 'b', 1)
    setValveState(vst, 'c', 1)
    setValveState(vst, 'g', 1)
    check_limits(abt, ptl, tcl, lcl, pt_data, tc_data, lc_data)
    print('Abort State =', getAbortState(abt))
    print('Valve State =', getValveState(vst, ist, abt))
    print('')
    pt_data = [500, 500, 530, 500, 530, 500, 750]
    tc_data = [82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572]
    lc_data = [599, 599, 2999]
    ls_data = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    check_limits(abt, ptl, tcl, lcl, pt_data, tc_data, lc_data)
    print('Abort State =', getAbortState(abt))
    print('Valve State =', getValveState(vst, ist, abt))
    print('')
    '''
    ####
    '''
    print(getAbortState(abt))
    print(getValveState(vst, ist, abt))
    setValveState(vst, 'c', 1)
    print(getValveState(vst, ist, abt))
    setValveState(vst, 'c', 0)
    '''
    ####
    '''
    print(b)
    b = getAbortState()
    print(b)
    print(setAbortState(0))


    print('Got it!')
    '''
    ####
    '''
    print('End')
    '''

    ## REVISED TESTING



    vst, ist, abt, gst, ptl, tcl, lcl, ptd, tcd, lcd, lsd = access_class()
    labview_import = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(labview_to_python(labview_import))
    labview_import = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    print(labview_to_python(labview_import))
    setAbortState(1)
    labview_import = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    print(labview_to_python(labview_import))

    '''
    setGOState('a', 1)
    print('GO State =', getGOState())
    print(getValveState())
    print(setValveState('a', 1))
    print(getValveState())
    setValveState('d', 1)
    print(getValveState())
    '''
    ####

    '''
    setGOState('a',1)
    setGOState('b',1)
    setGOState('c',1)
    print('Ignitor State =', getIgnitorState())
    setIgnitorState(1)
    print('Ignitor State =', getIgnitorState())

    ####

    print(getAbortState())
    setAbortState(1)
    print(getAbortState())
    setAbortState(0)
    print(abt.abort_state)
    print(getAbortState())
    print(getNanny())
    setNanny(1)

    ####

    setNanny(0)
    print('Nanny =', getNanny())
    pt_data = [500, 500, 530, 500, 530, 500, 750]
    tc_data = [82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572]
    lc_data = [599, 599, 2999]
    ls_data = [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]
    check_limits(pt_data, tc_data, lc_data)
    setValveState('b', 1)
    setValveState('c', 1)
    setValveState('g', 1)
    print('Abort State =', getAbortState())
    print('Valve State =', getValveState())
    print('')
    print('Abort State =', getAbortState())
    print(ls_data)
    check_limit_switch(ls_data)
    print('Abort State =', getAbortState())
    print('Valve State =', getValveState())
    print('')
    '''
    ####
    '''
    setPTData([2000, 500, 500, 530, 500, 530, 500, 750])
    setTCData([82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572])
    setLCData([599, 599, 3999])
    setLSData([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    check_limits()
    print('Abort State =', getAbortState())
    print('Nanny State =', getNanny())
    print('Valve State =', getValveState())
    print('')
    setValveState('b', 1)
    setValveState('c', 1)
    setValveState('g', 1)
    check_limits()
    print('Abort State =', getAbortState())
    print('Nanny State =', getNanny())
    print('Valve State =', getValveState())
    print('')
    setAbortState(0)
    setValveState('b', 1)
    setValveState('c', 1)
    setValveState('g', 1)
    setNanny(0)
    check_limits()
    print('Abort State =', getAbortState())
    print('Nanny State =', getNanny())
    print('Valve State =', getValveState())
    print('')
    setNanny(1)
    setPTData([2000, 500, 500, 530, 500, 530, 500, 750])
    setTCData([82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572])
    setLCData([599, 599, 2999])
    setLSData([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    check_limits()
    print('Abort State =', getAbortState())
    print('Nanny State =', getNanny())
    print('Valve State =', getValveState())
    print('')
    setValveState('b', 1)
    setValveState('c', 1)
    setValveState('g', 1)
    check_limits()
    print('Abort State =', getAbortState())
    print('Nanny State =', getNanny())
    print('Valve State =', getValveState())
    print('')
    setPTData([2000, 500, 500, 530, 500, 530, 500, 750])
    setTCData([82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572])
    setLCData([599, 599, 3999])
    setLSData([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    check_limits()
    print('Abort State =', getAbortState())
    print('Nanny State =', getNanny())
    print('Valve State =', getValveState())
    print('')
    setValveState('b', 1)
    setValveState('c', 1)
    setValveState('g', 1)
    check_limits()
    print('Abort State =', getAbortState())
    print('Nanny State =', getNanny())
    print('Valve State =', getValveState())
    print('')
    setPTData([2000, 500, 500, 530, 500, 530, 500, 750])
    setTCData([82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572])
    setLCData([599, 599, 2999])
    setLSData([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    check_limits()
    print('Abort State =', getAbortState())
    print('Nanny State =', getNanny())
    print('Valve State =', getValveState())
    print('')
    '''
    ####
    '''
    print(getAbortState())
    print(getValveState())
    setValveState('c', 1)
    print(getValveState())
    setValveState('c', 0)
    '''
    ####
    '''
    b = getAbortState()
    print(b)
    print(setAbortState(0))


    print('Got it!')
    '''
    ####

    '''
    print('End')
    '''
    ###

    '''
    setPTData([500, 500, 530, 500, 530, 500, 750])
    print(getPTData())

    setTCData([82, 302, 72, 72, 72, 72, 302, 72, 72, 572, 572, 572])
    print(getTCData())

    setLCData([599, 599, 2999])
    print(getLCData())

    setLSData([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    print(getLSData())
    '''