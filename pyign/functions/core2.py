import numpy as np

# local imports
from functions.classes import UpperClass as ucl


# Initialization Functions:


def _init_upper_class(*args):
    """Initialize an instance of the class 'UpperClass'. 'UpperClass' then creates instances of all nested
       functions, including all controls, data, limits, and time states. For more details, see structure of
       'UpperClass' within pyign.functions.classes.

       NOTE: THIS FUNCTION SHOULD ONLY BE CALLED ONCE DURING INITIALIZATION. PRODUCING MULTIPLE INSTANCES OF
             'UpperClass' COULD ENDANGER THE SYSTEM AND RESULT IN NECESSARY ABORTS FAILING TO TRIGGER!

                Arguments
                ---------
                N/A

                Nested Classes
                --------------
                ucl() : Initialize an instance of class 'UpperClass'

                Returns
                -------
                upper_class : Instance of class 'UpperClass' (referenced elsewhere as ucl)
    """
    upper_class = ucl()
    return upper_class


def _init_system(*args):
    """Initialize the element lengths of adjustable class arrays by calling a series of sub-functions which
       allow for altering of element lengths.

       NOTE: THIS FUNCTION SHOULD ONLY BE CALLED ONCE DURING INITIALIZATION. OVERWRITING ELEMENT LENGTH VALUES
             COULD ENDANGER THE SYSTEM AND RESULT IN MISSED SENSOR READINGS!

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : delay_elements --> length of time_delay
                args[2] : valve_number --> length of valve_state
                args[3] : go_elements --> length of go_state
                args[4] : pt_number --> length of pt_data and pt_limit
                args[5] : tc_number --> length of tc_data and tc_limit
                args[6] : lc_number --> length of lc_data and lc_limit
                args[7] : ls_number --> length of ls_data and ls_limit

                Nested Functions
                ----------------
                __set_time_elements : edit element lengths of TimeState subclass arrays
                __set_control_elements : edit element lengths of Controls subclass arrays
                __set_sensor_elements : edit element lengths of Data and Limit subclass arrays

                Returns
                -------
                N/A
    """
    __set_time_elements(args[0], args[1])
    __set_control_elements(args[0], args[2], args[3])
    __set_sensor_elements(args[0], args[4], args[5], args[6], args[7])


def __set_sensor_elements(*args):
    """Access protected class data and edit the element lengths of pt_data, pt_limit, tc_data, tc_limit,
       lc_data, lc_limit, ls_data, and ls_limit.

       NOTE: THIS FUNCTION SHOULD NEVER BE DIRECTLY ACCESSED. '_init_system' SHOULD BE THE ONLY CALL TO
             THIS FUNCTION, AND SHOULD ONLY BE CALLED ONCE DURING INITIALIZATION. OVERWRITING ELEMENT
             LENGTH VALUES COULD ENDANGER THE SYSTEM AND RESULT IN MISSED SENSOR READINGS!

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : pt_number --> length of pt_data and pt_limit
                args[2] : tc_number --> length of tc_data and tc_limit
                args[3] : lc_number --> length of lc_data and lc_limit
                args[4] : ls_number --> length of ls_data and ls_limit

                Returns
                -------
                N/A
    """
    args[0].Data.pt_number = args[1]
    args[0].Data.set_pt_number()
    args[0].Limit.pt_number = args[1]
    args[0].Limit.set_pt_number()
    args[0].Data.tc_number = args[2]
    args[0].Data.set_tc_number()
    args[0].Limit.tc_number = args[2]
    args[0].Limit.set_tc_number()
    args[0].Data.lc_number = args[3]
    args[0].Data.set_lc_number()
    args[0].Limit.lc_number = args[3]
    args[0].Limit.set_lc_number()
    args[0].Data.ls_number = args[4]
    args[0].Data.set_ls_number()
    args[0].Limit.ls_number = args[4]
    args[0].Limit.set_ls_number()


def __set_control_elements(*args):
    """Access protected class data and edit the element lengths of valve_state and go_state.

       NOTE: THIS FUNCTION SHOULD NEVER BE DIRECTLY ACCESSED. '_init_system' SHOULD BE THE ONLY CALL TO
             THIS FUNCTION, AND SHOULD ONLY BE CALLED ONCE DURING INITIALIZATION. OVERWRITING ELEMENT
             LENGTH VALUES COULD ENDANGER THE SYSTEM AND RESULT IN MISSED SENSOR READINGS!

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : valve_number --> length of valve_state
                args[2] : go_elements --> length of go_state

                Returns
                -------
                N/A
    """
    args[0].Controls.valve_number = args[1]
    args[0].Controls.set_valve_number()
    args[0].Controls.go_elements = args[2]
    args[0].Controls.set_go_elements()


def __set_time_elements(*args):
    """Access protected class data and edit the element lengths of time_delay.

       NOTE: THIS FUNCTION SHOULD NEVER BE DIRECTLY ACCESSED. '_init_system' SHOULD BE THE ONLY CALL TO
             THIS FUNCTION, AND SHOULD ONLY BE CALLED ONCE DURING INITIALIZATION. OVERWRITING ELEMENT
             LENGTH VALUES COULD ENDANGER THE SYSTEM AND RESULT IN MISSED SENSOR READINGS!

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : delay_elements --> length of time_delay

                Returns
                -------
                N/A
    """
    args[0].TimeState.delay_elements = args[1]
    args[0].TimeState.set_delay_elements()


# Get Functions


def getPTData(*args):
    """Access protected class data of the system Pressure Transducer data. This approach is a secure
       method to access saved system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                pt_data : Pressure Transducer Data
    """
    return args[0].Data.PTData.pt_data


def getPTLimits(*args):
    """Access protected class data of the system Pressure Transducer limits. This approach is a secure
       method to access saved system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                pt_limit : Pressure Transducer Limits
    """
    return args[0].Limit.PTLimit.pt_limit


def getTCData(*args):
    """Access protected class data of the system Thermocouple data. This approach is a secure method to
       access saved system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                tc_data : Thermocouple Data
    """
    return args[0].Data.TCData.tc_data


def getTCLimits(*args):
    """Access protected class data of the system Thermocouple limits. This approach is a secure method to
       access saved system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                tc_limit : Thermocouple Limits
    """
    return args[0].Limit.TCLimit.tc_limit


def getLCData(*args):
    """Access protected class data of the system Load Cell data. This approach is a secure method to
       access saved system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                lc_data : Load Cell Data
    """
    return args[0].Data.LCData.lc_data


def getLCLimits(*args):
    """Access protected class data of the system Load Cell limits. This approach is a secure method to
       access saved system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                lc_limit : Load Cell Limits
    """
    return args[0].Limit.LCLimit.lc_limit


def getLSData(*args):
    """Access protected class data of the system Limit Switch data. This approach is a secure method to
       access saved system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                ls_data : Limit Switch Data
    """
    return args[0].Data.LSData.ls_data


def getLSLimits(*args):
    """Access protected class data of the system Limit Switch limits. This approach is a secure method to
       access saved system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                ls_limit : Limit Switch Limits
    """
    return args[0].Limit.LSLimit.ls_limit


def getAbortState(*args):
    """Access protected class data of the system Abort State. This approach is a secure method to access
       saved system state values. If an abort is tripped, the test stand control system will automatically
       enter 'Safe' mode and valve configuration

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                abort_state : Abort State Integer
                    state[0] = system is nominal
                    state[1] = system abort
    """
    return args[0].Controls.AbortState.abort_state


def getNanny(*args):
    """Access protected class data to evaluate if the control system's automated guardian or 'Nanny' mode
       is active. This approach is a secure method to access saved system state values. If Nanny mode is
       activated the test stand control system will automatically enter 'Safe' mode and trigger an abort
       if sensor values exceed set bounds.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                nanny : Nanny State Integer
                     state[0] = automated system monitoring mode disabled
                     state[1] = automated system monitoring mode enabled
    """
    return args[0].Controls.NannyState.nanny_state


def getGOState(*args):
    """Access protected class data to evaluate if the Fuel, Liquid Oxygen (LOX), and Control Panel system
       state are a 'GO' as a 1 by 3 numpy array. This approach is a secure method to access saved system
       state values. If the system sensor values are all nominal and all three controller panels operators
       are prepared to begin the firing sequence, the three 'GO' state values will return '1'. Values for
       system ready or 'GO' state indicates if a tests firing sequence can commence. If any of the three
       control panel operators return '0' or 'NOGO', the system will automatically disable the firing sequence.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                go_state : Go State Array
                    go_state[0] = Control Panel State
                    go_state[1] = LOX Panel State
                    go_state[2] = Fuel Panel State
                        state[0] = 'NOGO'
                        state[1] = 'GO'
    """
    return args[0].Controls.GoState.go_state


def getValveState(*args):
    """Access protected class data to evaluate and monitor all of the system actuated valve states.
       The numpy data structure representation is a numpy array. This approach is a secure method
       to access saved valve system state values. A valve state value equal to '0' represents valve
       'Safe' orientation.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Nested Functions
                ----------------
                check_abort() : check if a system abort has been tripped.
                    NOTE: If an abort has been tripped, check_abort will set all valve_state
                          elements to '0' or 'Safe' mode.

                Returns
                -------
                valve_state : Valve State Array
                    valve_state[0] = valve ABV-PR-110 (pressure ox)
                    valve_state[1] = valve ABV-PR-120 (pressure fuel)
                    valve_state[2] = valve ABV-OX-210 (vent ox)
                    valve_state[3] = valve ABV-FU-310 (vent fuel)
                    valve_state[4] = valve ABV-OX-220  (iso ox)
                    valve_state[5] = valve ABV-FU-320 (iso fuel)
                    valve_state[6] = valve ABV-OX-230 (chill ox)
                    valve_state[7] = valve ABV-FU-330 (purge fuel)
                    valve_state[8] = valve ABV-OX-240 (main ox)
                    valve_state[9] = valve ABV-FU-340 (main fuel)
                    valve_state[10] = valve ABV-OX-250 (fill ox)
                        state[0] = 'Safe'
                        state[1] = 'Active'
    """
    check_abort(args[0])
    return args[0].Controls.ValveState.valve_state


def getIgnitorState(*args):
    """Access protected class data to evaluate and monitor the system ignitor states. The returned
       value representation is an integer ranging from '0' to '1'. This approach is a secure method
       to access saved system state values. The method calls two nested functions.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Nested Functions
                ----------------
                check_go() : check if all systems are 'GO' for startup sequence.
                    NOTE: if any panel returns a '0' or 'NOGO', ignitor_state will
                          automatically be set to a '0' or 'Safe'.
                check_abort : checks if a system abort has been tripped.
                    NOTE: if an abort has been tripped, ignitor_state will automatically
                          be set to a '0' or 'Safe'.

                Returns
                -------
                ignitor_state : Ignitor State Integer
                     state[0] = 'Safe'
                     state[1] = 'Active'
    """
    check_go(args[0])
    check_abort(args[0])
    return args[0].Controls.IgnitorState.ignitor_state


def getTimeRegime(*args):
    """Access protected class data to evaluate and monitor the current regime in which the system is
       operating. The returned value representation is an integer ranging from '0' to '4'. This approach
       is a secure method to access saved system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                time_regime : Time Regime Integer
                     state[0] = Initialization Regime
                     state[1] = System Evaluation Regime
                     state[2] = Combustion Regime
                     state[3] = Drain Regime
                     state[4] = Abort Regime
    """
    return args[0].TimeState.TimeRegime.time_regime


def getTimeDelay(*args):
    """Access protected class data to evaluate the delays in an automated firing sequence. The
       returned value representation is an array ranging containing real time delays. This approach
       is a secure method to access saved system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                time_delay: Time Delay Array
                    time_delay[0] = auto_time_primary
                    time_delay[1] = ignition_delay
                    time_delay[2] = ox_main_delay
                    time_delay[3] = fuel_main_delay
                    time_delay[4] = burn_duration
                    time_delay[5] = purge_delay
    """
    return args[0].TimeState.TimeDelay.time_delay


# Set Functions


def setPTData(*args):
    """Access and changes protected system class data. The returned value representation is an array of
       data from pressure transducers.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : pt_data --> an array containing the most recent pressure transducer data

                Returns
                -------
                N/A
    """
    args[0].Data.PTData.pt_data = args[1]


def setPTLimits(*args):
    """Access and changes protected system class data. The returned value representation is an array of
       limits for pressure transducers.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : pt_limit --> an array containing the pressure transducer limits

                Returns
                -------
                N/A
    """
    args[0].Limit.PTLimit.pt_limit = args[1]


def setTCData(*args):
    """Access and changes protected system class data. The returned value representation is an array of
       data from thermocouples.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : tc_data --> an array containing the most recent thermocouple data

                Returns
                -------
                N/A
    """
    args[0].Data.TCData.tc_data = args[1]


def setTCLimits(*args):
    """Access and changes protected system class data. The returned value representation is an array of
       limits for thermocouples.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : tc_limits --> an array containing the thermocouple limits

                Returns
                -------
                N/A
    """
    args[0].Limit.TCLimit.tc_limit = args[1]


def setLCData(*args):
    """Access and changes protected system class data. The returned value representation is an array of
       data from load cells.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : lc_data --> an array containing the most recent load cell data

                Returns
                -------
                N/A
    """
    args[0].Data.LCData.lc_data = args[1]


def setLCLimits(*args):
    """Access and changes protected system class data. The returned value representation is an array of
       limits for load cells.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : lc_limits --> an array containing the load cell limits

                Returns
                -------
                N/A
    """
    args[0].Limit.LCLimit.lc_limit = args[1]


def setLSData(*args):
    """Access and changes protected system class data. The returned value representation is an array of
       data from limit switches.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : ls_data --> an array containing the most recent limit switch data

                Returns
                -------
                N/A
    """
    args[0].Data.LSData.lc_data = args[1]


def setLSLimits(*args):
    """Access and changes protected system class data. The returned value representation is an array of
       limits for limit switches.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : ls_limits --> an array containing the limit switch limits

                Returns
                -------
                N/A
    """
    args[0].Limit.LSLimit.ls_limit = args[1]


def setAbortState(*args):
    """Access and changes protected abort_state class data. The returned value representation is an
       integer ranging from '0' to '1'. This approach is a secure method to access and change saved system
       state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : abort_state --> abort_state integer
                    state[0] = 'System Performance Nominal'
                    state[1] = 'Abort'

                Returns
                -------
                N/A
    """
    args[0].Controls.AbortState.abort_state = args[1]


def setNanny(*args):
    """Access and changes protected Nanny mode class data. The returned value representation is an
       integer ranging from '0' to '1'. This approach is a secure method to access and change saved
       system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : nanny_state --> nanny_state integer
                    state[0] = 'automated system monitoring disabled'
                    state[1] = 'automated system monitoring enabled'.

                Returns
                -------
                N/A
    """
    args[0].Controls.NannyState.nanny_state = args[1]


def setGOState(*args):
    """Access and changes protected 'GO' state class data. The returned value representation is a 1 by 3
       integer numpy array. This approach is a secure method to access and change saved system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : go_state --> go_state array
                    go_state[0] = Control Panel State
                    go_state[1] = LOX Panel State
                    go_state[2] = Fuel Panel State
                        state[0] = 'NOGO'
                        state[1] = 'GO'

                Returns
                -------
                N/A
    """
    args[0].Controls.GoState.go_state = args[1]


def setValveState(*args):
    """Access and changes protected valve state class data. The returned value representation is an
       integer ranging from '0' to '1'. This approach is a secure method to access and change saved
       system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : valve_state --> valve state array
                    valve_state[0] = valve ABV-PR-110 (pressure ox)
                    valve_state[1] = valve ABV-PR-120 (pressure fuel)
                    valve_state[2] = valve ABV-OX-210 (vent ox)
                    valve_state[3] = valve ABV-FU-310 (vent fuel)
                    valve_state[4] = valve ABV-OX-220  (iso ox)
                    valve_state[5] = valve ABV-FU-320 (iso fuel)
                    valve_state[6] = valve ABV-OX-230 (chill ox)
                    valve_state[7] = valve ABV-FU-330 (purge fuel)
                    valve_state[8] = valve ABV-OX-240 (main ox)
                    valve_state[9] = valve ABV-FU-340 (main fuel)
                    valve_state[10] = valve ABV-OX-250 (fill ox)
                        state[0] = 'Safe'
                        state[1] = 'Active'

                Returns
                -------
                N/A
    """
    args[0].Controls.ValveState.valve_state = args[1]


def setIgnitorState(*args):
    """Access and changes protected ignitor state class data. The returned value representation is an
       integer ranging from '0' to '1'. This approach is a secure method to access and change saved
       system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : ignitor_state -->ignitor_state integer
                    state[0] = 'Safe'
                    state[1] = 'Active'

                Returns
                -------
                N/A
    """
    args[0].Controls.IgnitorState.ignitor_state = args[1]


def setTimeRegime(*args):
    """Access and changes protected time regime class data. The returned value representation is an
       integer ranging from '0' to '4'. This approach is a secure method to access and change saved
       system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : time_regime -->time_regime integer
                    state[0] = Initialization Regime
                    state[1] = System Evaluation Regime
                    state[2] = Combustion Regime
                    state[3] = Drain Regime
                    state[4] = Abort Regime

                Returns
                -------
                N/A
    """

    args[0].TimeState.TimeRegime.time_regime = args[1]


def setTimeDelay(*args):
    """Access and changes protected time delay class data. The returned value representation is an
       array containing all ignition sequence time delays. This approach is a secure method to access
       and change saved system state values.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : time_delay -->time_delay array
                    time_delay[0] = auto_time_primary
                    time_delay[1] = ignition_delay
                    time_delay[2] = ox_main_delay
                    time_delay[3] = fuel_main_delay
                    time_delay[4] = burn_duration
                    time_delay[5] = purge_delay

                Returns
                -------
                N/A
    """
    args[0].TimeState.TimeDelay.time_delay = args[1]


# Index Functions


def pt_index(*args):
    """Access stored Pressure Transducer data from the sensor limits and collected data to
       index and build an integer numpy array for sensor values that have exceeded the set bounds.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Nested Functions
                ----------------
                check_pt_data() : Access stored Pressure Transducer data from the sensor limits
                                  and collected data to index and build an integer numpy array for
                                  sensor values that have exceeded the set bounds.

                Returns
                -------
                index : numpy array
                    numpy array of pressure transducers sensed out of bounds
    """
    index = []
    x = check_pt_data(args[0])
    i = 0
    for line in args[0].Data.PTData.pt_data:
        i += 1
        if line != x[i - 1]:
            index.append(0)
        elif line == x[i - 1]:
            index.append(i)
    return index


def tc_index(*args):
    """Access stored thermocouple data from the sensor limits and collected data to index
       and build an integer numpy array for sensor values that have exceeded the set bounds.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Nested Functions
                ----------------
                check_tc_data() : Access stored thermocouple data from the sensor limits and
                                  collected data to index and build an integer numpy array for
                                  sensor values that have exceeded the set bounds.

                Returns
                -------
                index : numpy array
                    numpy array of thermocouples sensed out of bounds
    """
    index = []
    x = check_tc_data(args[0])
    i = 0
    for line in args[0].Data.TCData.tc_data:
        i += 1
        if line != x[i - 1]:
            index.append(0)
        elif line == x[i - 1]:
            index.append(i)
    return index


def lc_index(*args):
    """Access stored load cell data from the sensor limits and collected data to index
       and build an integer numpy array for sensor values that have exceeded the set bounds.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Nested Functions
                ----------------
                check_lc_data() : Access stored load cell data from the sensor limits and
                                  collected data to index and build an integer numpy array for
                                  sensor values that have exceeded the set bounds.

                Returns
                -------
                index : numpy array
                    numpy array of load cells sensed out of bounds
    """
    index = []
    x = check_lc_data(args[0])
    i = 0
    for line in args[0].Data.LCData.lc_data:
        i += 1
        if line != x[i - 1]:
            index.append(0)
        elif line == x[i - 1]:
            index.append(i)
    return index


# Check Functions


def check_pt_data(*args):
    """Access stored pressure transducer data from the sensor limits and collected data to
       index and build an integer numpy array for sensor values that have exceeded the set bounds.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                pt_input_data : numpy array of sensed pressure transducer values data that
                                have exceeded set bounds.
    """

    limits = args[0].Limit.PTLimit.pt_limit
    pt = []
    for i in range(len(limits)):
        x = (args[0].Data.PTData.pt_data[i] - limits[i])
        if x >= 0:
            pt.append(args[0].Data.PTData.pt_data[i])
        else:
            pt.append(0)
    return pt


def check_tc_data(*args):
    """Access stored thermocouple data from the sensor limits and collected data to index and
       build an integer numpy array for sensor values that have exceeded the set bounds.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                tc_input_data : numpy array of sensed thermocouple values data that have exceeded
                                set bounds.
    """
    limits = args[0].Limit.TCLimit.tc_limit
    tc = []
    for i in range(len(limits)):
        x = (args[0].Data.TCData.tc_data[i] - limits[i])
        if x >= 0:
            tc.append(args[0].Data.TCData.tc_data[i])
        else:
            tc.append(0)
    return tc


def check_lc_data(*args):
    """Access stored load cell data from the sensor limits and collected data to index and
       build an integer numpy array for sensor values that have exceeded the set bounds.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Returns
                -------
                lc_input_data : numpy array of sensed load cell values data that have exceeded
                                set bounds.
    """
    limits = args[0].Limit.LCLimit.lc_limit
    lc = []
    for i in range(len(limits)):
        x = (args[0].Data.LCData.lc_data[i] - limits[i])
        if x >= 0:
            lc.append(args[0].Data.LCData.lc_data[i])
        else:
            lc.append(0)
    return lc


def check_limits(*args):
    """Check if any sensor is out of limit range, if out of bounds is detected, abort is tripped
       and system enters 'Safe' mode.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Nested Functions
                ----------------
                getNanny() : A '1' indicates that sensor data will be checked against limits to find
                             any sensors which have exceeded set bounds.

                setAbortState() : if any sensor has exceeded its limit, a system abort will be tripped.

                pt_index() : Access stored pressure transducer data from the sensor limits and collected
                             data to index and build an integer numpy array for sensor values that have
                             exceeded the set bounds.

                tc_index() : Access stored thermocouple data from the sensor limits and collected data
                             to index and build an integer numpy array for sensor values that have
                             exceeded the set bounds.

                lc_index() : Access stored load cell data from the sensor limits and collected data
                             to index and build an integer numpy array for sensor values that have
                             exceeded the set bounds.

                Returns
                -------
                abort_state : abort_state integer
                     state[0] = system state is nominal
                     state[1] = system abort
    """
    if getNanny(args[0]) == 1:
        if np.sum(pt_index(args[0])) != 0:
            setAbortState(args[0], 1)
        elif np.sum(tc_index(args[0])) != 0:
            setAbortState(args[0], 1)
        elif np.sum(lc_index(args[0])) != 0:
            setAbortState(args[0], 1)
    return args[0].Controls.AbortState.abort_state


def check_abort(*args):
    """Check Abort State, if abort has been tripped, all valves and the ignitor are set to 'Safe'
       state until system is restarted.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Nested Functions
                ----------------
                getAbortState() : All valve and ignitor states are set to 'Safe' if an abort has
                                  been tripped.

                Returns
                -------
                valve_state : valve_state numpy array
                    valve_state[0] = valve ABV-PR-110 (pressure ox)
                    valve_state[1] = valve ABV-PR-120 (pressure fuel)
                    valve_state[2] = valve ABV-OX-210 (vent ox)
                    valve_state[3] = valve ABV-FU-310 (vent fuel)
                    valve_state[4] = valve ABV-OX-220  (iso ox)
                    valve_state[5] = valve ABV-FU-320 (iso fuel)
                    valve_state[6] = valve ABV-OX-230 (chill ox)
                    valve_state[7] = valve ABV-FU-330 (purge fuel)
                    valve_state[8] = valve ABV-OX-240 (main ox)
                    valve_state[9] = valve ABV-FU-340 (main fuel)
                    valve_state[10] = valve ABV-OX-250 (fill ox)
                        state[0] = 'Safe'
                        state[1] = 'Active'
                ignitor_state : ignitor_state integer
                    state[0] = 'Safe'
                    state[1] = 'Active'
    """
    if getAbortState(args[0]) == 1:
        args[0].Controls.ValveState.valve_state = [0] * args[0].Controls.valve_number
        args[0].Controls.IgnitorState.ignitor_state = 0
    return args[0].Controls.ValveState.valve_state, args[0].Controls.IgnitorState.ignitor_state


def check_go(*args):
    """Check GO State. If all three panels are NOT a 'GO', ignitor state is set to 'Safe' mode.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Nested Functions
                ----------------
                getGOState() : if any panel returns a 'NOGO' ignitor_state will be set to 'Safe' mode

                Returns
                -------
                ignitor_state : ignitor_state integer
                    state[0] = 'Safe'
                    state[1] = 'Active'
    """
    if np.sum(getGOState(args[0]))!= 3:
        args[0].Controls.IgnitorState.ignitor_state = 0
    return args[0].Controls.IgnitorState.ignitor_state


def check_time_regime(*args):
    """Check time regime. """
    time_regime = getTimeRegime(args[0])
    if time_regime == 0:
        args[0].Controls.ValveState.valve_state[8] = 0
        args[0].Controls.ValveState.valve_state[9] = 0


def check_manual_circuit(*args):
    """Check if the manual switch circuit is active to determine Time Regime. If the switch panel
       is active, this sets the Time Regime to a '0' or 'Initialize Regime'.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Nested Functions
                ----------------
                setTimeRegime() : If the switch panel is 'Active', Time Regime is set to a '0' or
                                  'Initialize Regime'. If the switch panel is 'Inactive', Time Regime
                                  is set to a '1' or 'System Eval Regime'.
                Returns
                -------
                N/A
    """
    if args[0] == 0:
        setTimeRegime(1)
    elif args[0] == 1:
        setTimeRegime(0)


# Interface Functions


def labview_to_python(*args):
    """Overhead function that acts as a bridge between LabVIEW and Python. This function will receive
       all data passed from LabVIEW and distribute it to sub-functions. Returns Control values to LabVIEW
       after checking states and limits.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

                Nested Functions
                ----------------
                setValveState() : Sets valve_state to new states as passed from LabVIEW
                getValveState() : Returns valve_state to LabVIEW. If an abort has been triggered,
                                  this method will ensure that all valves are set to '0' or 'Safe'.

                Returns
                -------
                valve_state : valve_state array
                    valve_state[0] = valve ABV-PR-110 (pressure ox)
                    valve_state[1] = valve ABV-PR-120 (pressure fuel)
                    valve_state[2] = valve ABV-OX-210 (vent ox)
                    valve_state[3] = valve ABV-FU-310 (vent fuel)
                    valve_state[4] = valve ABV-OX-220  (iso ox)
                    valve_state[5] = valve ABV-FU-320 (iso fuel)
                    valve_state[6] = valve ABV-OX-230 (chill ox)
                    valve_state[7] = valve ABV-FU-330 (purge fuel)
                    valve_state[8] = valve ABV-OX-240 (main ox)
                    valve_state[9] = valve ABV-FU-340 (main fuel)
                    valve_state[10] = valve ABV-OX-250 (fill ox)
                        state[0] = 'Safe'
                        state[1] = 'Active'
    """
    setValveState(args[0][0])
    ### ADD ARGUMENT HERE FOR THE SIGNAL WIRE BETWEEN LABVIEW AND KEY CIRCUIT ###
    ### ex) check_manual_circuit(args[0][])
    return getValveState()
