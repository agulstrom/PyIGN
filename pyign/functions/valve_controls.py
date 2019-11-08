import numpy as np

# local imports
from classes import UpperClass as ucl


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


def getValveState(*args):
    """Access protected class data to evaluate and monitor all of the system actuated valve states.
       The numpy data structure representation is a numpy array. This approach is a secure method
       to access saved valve system state values. A valve state value equal to '0' represents valve
       'Safe' orientation.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance

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
    return args[0].Controls.ValveState.valve_state


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


def labview_to_python(*args):
    """Overhead function that acts as a bridge between LabVIEW and Python. This function will receive
       all data passed from LabVIEW and distribute it to sub-functions. Returns Control values to LabVIEW
       after checking states and limits.

                Arguments
                ---------
                args[0] : ucl --> UpperClass Instance
                args[1] : Data passed from Labview to Python

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
    setValveState(args[0], args[1])
    return getValveState(args[0])


if __name__ == '__main__':
    ucl = _init_upper_class()
    valve_state0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    valve_state1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(ucl.Controls.ValveState.valve_state)
    print(labview_to_python(ucl, valve_state1))
