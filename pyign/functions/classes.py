# third-party libraries
import numpy as np


class UpperClass(object):
    """UpperClass is the overarching class which contains all values created within a System.

    Structure
    ---------
    UpperClass:
        Controls:               Data:               Limit:              TimeState:
            ValveState              PTData              PTLimit             TimeDelay
            GoState                 TCData              TCLimit             TimeRegime
            IgnitorState            LCData              LCLimit
            AbortState              LSData              LSLimit
            NannyState
            """

    def __init__(self):
        self.Controls = self.Controls()
        self.Data = self.Data()
        self.Limit = self.Limit()
        self.TimeState = self.TimeState()


    class Controls(object):
        """Controls contains all control oriented classes

                    Attributes
                    ----------
                    valve_number : Integer used to determine how many actuated valves are in a System
                    go_elements : Integer used to determine how many Go/NoGo elements are in a System
        """

        def __init__(self, valve_number=11, go_elements=3):
            self.ValveState = self.ValveState()
            self.GoState = self.GoState()
            self.IgnitorState = self.IgnitorState()
            self.AbortState = self.AbortState()
            self.NannyState = self.NannyState()
            self._valve_number = valve_number
            self._go_elements = go_elements

        @property
        def valve_number(self):
            return self._valve_number

        @property
        def go_elements(self):
            return self._go_elements

        @valve_number.setter
        def valve_number(self, valve_number):
            self._valve_number = valve_number

        @go_elements.setter
        def go_elements(self, go_elements):
            self._go_elements = go_elements

        def set_valve_number(self):
            self.ValveState.valve_state = (self._valve_number * self.ValveState.valve_state)

        def set_go_elements(self):
            self.GoState.go_state = (self._go_elements * self.GoState.go_state)


        class ValveState(object):
            """The State of a Valve determines if a valve set to 'opened' or 'closed'.

                    Attributes
                    ----------
                    valve_state : Valve State [11]
                        valve_state[0] : valve ABV-PR-110 (pressure ox)
                        valve_state[1] : valve ABV-PR-120 (pressure fuel)
                        valve_state[2] : valve ABV-OX-210 (vent ox)
                        valve_state[3] : valve ABV-FU-310 (vent fuel)
                        valve_state[4] : valve ABV-OX-220  (iso ox)
                        valve_state[5] : valve ABV-FU-320 (iso fuel)
                        valve_state[6] : valve ABV-OX-230 (chill ox)
                        valve_state[7] : valve ABV-FU-330 (purge fuel)
                        valve_state[8] : valve ABV-OX-240 (main ox)
                        valve_state[9] : valve ABV-FU-340 (main fuel)
                        valve_state[10] : valve ABV-OX-250 (fill ox)

                    state[0] : 'Safe'
                    state[1] : 'Active'
            """

            def __init__(self, valve_state=[0]):
                self._valve_state = valve_state

            @property
            def valve_state(self):
                return self._valve_state

            @valve_state.setter
            def valve_state(self, valve_state):
                self._valve_state = valve_state


        class GoState(object):
            """A 'Go' signal is required from all control ends before beginning the ignition phase.

                    Attributes
                    ----------
                    go_state : 'Go' State [3]
                        go_state[0] is go_control : Control Panel State
                        go_state[1] is go_lox : LOX Panel State
                        go_state[2] is go_fuel : Fuel Panel State

                    state[0] : 'NoGo'
                    state[1] : 'Go'
                    """

            def __init__(self, go_state=[0]):
                self._go_state = go_state

            @property
            def go_state(self):
                return self._go_state

            @go_state.setter
            def go_state(self, go_state):
                self._go_state = go_state


        class IgnitorState(object):
            """The Ignitor State determines if the engine ignitor has lit.

                    Attributes
                    ----------
                    ignitor_state : Ignitor State [1]
                    state[0] : 'Safe'
                    state[1] : 'Ignition'
                    """

            def __init__(self, ignitor_state=0):
                self._ignitor_state = ignitor_state

            @property
            def ignitor_state(self):
                return self._ignitor_state

            @ignitor_state.setter
            def ignitor_state(self, ignitor_state):
                self._ignitor_state = ignitor_state


        class AbortState(object):
            """The Abort State of a System determines if an 'Abort' has been tripped and the system is in
               manditory 'Safe' mode.

                    Attributes
                    ----------
                    state : 'Abort' State [1]
                    state[0] : 'Go' State
                    state[1] : 'Abort Has Been Tripped' State
                    """
            def __init__(self, abort_state=0):
                self._abort_state = abort_state

            @property
            def abort_state(self):
                return self._abort_state

            @abort_state.setter
            def abort_state(self, abort_state):
                self._abort_state = abort_state


        class NannyState(object):
            """The Nanny State of a System is active during System operation, and oversees all System checks

                    Attributes
                    ----------
                    state : 'Nanny' State [1]
                    state[0] : 'Go' State
                    state[1] : 'Abort Has Been Tripped' State
            """

            def __init__(self, nanny_state=0):
                self._nanny_state = nanny_state

            @property
            def nanny_state(self):
                return self._nanny_state

            @nanny_state.setter
            def nanny_state(self, nanny_state):
                self._nanny_state = nanny_state


    class Data(object):
        """Data stores all data that is sent from Python for a single sampling

                        Attributes
                        ----------
                        pt_number : Integer used to designate the number of Pressure Transducers in a System
                        tc_number : Integer used to designate the number of Thermocouples in a System
                        lc_number : Integer used to designate the number of Load Cells in a System
                        ls_number : Integer used to designate the number of Limit Switches in a System
         """

        def __init__(self, pt_number=8, tc_number=16, lc_number=3, ls_number=11):
            self.PTData = self.PTData()
            self.TCData = self.TCData()
            self.LCData = self.LCData()
            self.LSData = self.LSData()
            self._pt_number = pt_number
            self._tc_number = tc_number
            self._lc_number = lc_number
            self._ls_number = ls_number

        @property
        def pt_number(self):
            return self._pt_number

        @property
        def tc_number(self):
            return self._tc_number

        @property
        def lc_number(self):
            return self._lc_number

        @property
        def ls_number(self):
            return self._ls_number

        @pt_number.setter
        def pt_number(self, pt_number):
            self._pt_number = pt_number

        @tc_number.setter
        def tc_number(self, tc_number):
            self._tc_number = tc_number

        @lc_number.setter
        def lc_number(self, lc_number):
            self._lc_number = lc_number

        @ls_number.setter
        def ls_number(self, ls_number):
            self._ls_number = ls_number

        def set_pt_number(self):
            self.PTData.pt_data = (self._pt_number * self.PTData.pt_data)

        def set_tc_number(self):
            self.TCData.tc_data = (self._tc_number * self.TCData.tc_data)

        def set_lc_number(self):
            self.LCData.lc_data = (self._lc_number * self.LCData.lc_data)

        def set_ls_number(self):
            self.LSData.ls_data = (self._ls_number * self.LSData.ls_data)


        class PTData(object):
            """The Pressure Transducer Data collected.

                        Attributes
                        ----------
                        pt_data : pressure transducer data array [8]
                            pt_data[0] : pressure transducer PT-PR-110
                            pt_data[1] : pressure transducer PT-OX-120
                            pt_data[2] : pressure transducer PT-FU-130
                            pt_data[3] : pressure transducer PT-OX-210
                            pt_data[4] : pressure transducer PT-FU-310
                            pt_data[5] : pressure transducer PT-OX-220
                            pt_data[6] : pressure transducer PT-FU-320
                            pt_data[7] : pressure transducer PT-CC-410
             """

            def __init__(self, pt_data=[0]):
                self._pt_data = pt_data

            @property
            def pt_data(self):
                return self._pt_data

            @pt_data.setter
            def pt_data(self, pt_data):
                self._pt_data = pt_data


        class TCData(object):
            """The Thermocouple Data collected.

                        Attributes
                        ----------
                        tc_data : thermocouple data array[12]
                            tc_data[0] : thermocouple T-OX-210
                            tc_data[1] : thermocouple T-FU-310
                            tc_data[2] : thermocouple T-OX-220
                            tc_data[3] : thermocouple T-OX-230
                            tc_data[4] : thermocouple T-OX-240
                            tc_data[5] : thermocouple T-OX-250
                            tc_data[6] : thermocouple T-FU-320
                            tc_data[7] : thermocouple T-OX-260
                            tc_data[8] : thermocouple T-OX-270
                            tc_data[9] : thermocouple T-CC-410
                            tc_data[10] : thermocouple T-CC-420
                            tc_data[11] : thermocouple T-CC-430
            """

            def __init__(self, tc_data=[0]):
                self._tc_data = tc_data

            @property
            def tc_data(self):
                return self._tc_data

            @tc_data.setter
            def tc_data(self, tc_data):
                self._tc_data = tc_data


        class LCData(object):
            """The Load Cell data collected.

                        Attributes
                        ----------
                        lc_data : load cell data array [3]
                            lc_data[0] : load cell LC-OX-210
                            lc_data[1] : load cell LC-FU-310
                            lc_data[2] : load cell LC-CC-410
            """

            def __init__(self, lc_data=[0]):
                self._lc_data = lc_data

            @property
            def lc_data(self):
                return self._lc_data

            @lc_data.setter
            def lc_data(self, lc_data):
                self._lc_data = lc_data


        class LSData(object):
            """The State of a Limit Switch determines if a valve is 'opened' or 'closed'.

                        Attributes
                        ----------
                        ls_state : limit switch data array [11]
                            ls_state[0] : valve ABV-PR-110
                            ls_state[1] : valve ABV-PR-120
                            ls_state[2] : valve ABV-OX-210
                            ls_state[3] : valve ABV-FU-310
                            ls_state[4] : valve ABV-OX-220
                            ls_state[5] : valve ABV-FU-320
                            ls_state[6] : valve ABV-OX-230
                            ls_state[7] : valve ABV-FU-330
                            ls_state[8] : valve ABV-OX-240
                            ls_state[9] : valve ABV-FU-340
                            ls_state[10] : valve ABV-OX-250
            """

            def __init__(self, ls_data=[0]):
                self._ls_data = ls_data

            @property
            def ls_data(self):
                return self._ls_data

            @ls_data.setter
            def ls_data(self, ls_data):
                self._ls_data = ls_data


    class Limit(object):
        """Limit stores all sensor limits to determine when 'Safe' mode is breaking

                        Attributes
                        ----------
                        pt_number : Integer used to designate the number of Pressure Transducers in a System
                        tc_number : Integer used to designate the number of Thermocouples in a System
                        lc_number : Integer used to designate the number of Load Cells in a System
                        ls_number : Integer used to designate the number of Limit Switches in a System
         """

        def __init__(self, pt_number=8, tc_number=16, lc_number=3, ls_number=11):
            self.PTLimit = self.PTLimit()
            self.TCLimit = self.TCLimit()
            self.LCLimit = self.LCLimit()
            self.LSLimit = self.LSLimit()
            self._pt_number = pt_number
            self._tc_number = tc_number
            self._lc_number = lc_number
            self._ls_number = ls_number

        @property
        def pt_number(self):
            return self._pt_number

        @property
        def tc_number(self):
            return self._tc_number

        @property
        def lc_number(self):
            return self._lc_number

        @property
        def ls_number(self):
            return self._ls_number

        @pt_number.setter
        def pt_number(self, pt_number):
            self._pt_number = pt_number

        @tc_number.setter
        def tc_number(self, tc_number):
            self._tc_number = tc_number

        @lc_number.setter
        def lc_number(self, lc_number):
            self._lc_number = lc_number

        @ls_number.setter
        def ls_number(self, ls_number):
            self._ls_number = ls_number

        def set_pt_number(self):
            self.PTLimit.pt_limit = (self._pt_number * self.PTLimit.pt_limit)

        def set_tc_number(self):
            self.TCLimit.tc_limit = (self._tc_number * self.TCLimit.tc_limit)

        def set_lc_number(self):
            self.LCLimit.lc_limit = (self._lc_number * self.LCLimit.lc_limit)

        def set_ls_number(self):
            self.LSLimit.ls_limit = (self._ls_number * self.LSLimit.ls_limit)


        class PTLimit(object):
            """The Pressure Transducer Limits determine when 'Safe' mode breaks.

                        Attributes
                        ----------
                        pt_limit : pressure transducers limit array[8]
                            pt_limits[0] : pressure transducer PT-PR-110
                            pt_limits[1] : pressure transducer PT-OX-120
                            pt_limits[2] : pressure transducer PT-FU-130
                            pt_limits[3] : pressure transducer PT-OX-210
                            pt_limits[4] : pressure transducer PT-FU-310
                            pt_limits[5] : pressure transducer PT-OX-220
                            pt_limits[6] : pressure transducer PT-FU-320
                            pt_limits[7] : pressure transducer PT-CC-410
            """

            def __init__(self, pt_limit=[0]):
                self._pt_limit = pt_limit

            @property
            def pt_limit(self):
                return self._pt_limit

            @pt_limit.setter
            def pt_limit(self, pt_limit):
                self._pt_limit = pt_limit


        class TCLimit(object):
            """The Thermocouple Limits determine when 'Safe' mode breaks.

                        Attributes
                        ----------
                        tc_limit : thermocouple limit array[12]
                            tc_data[0] : thermocouple T-OX-210
                            tc_data[1] : thermocouple T-FU-310
                            tc_data[2] : thermocouple T-OX-220
                            tc_data[3] : thermocouple T-OX-230
                            tc_data[4] : thermocouple T-OX-240
                            tc_data[5] : thermocouple T-OX-250
                            tc_data[6] : thermocouple T-FU-320
                            tc_data[7] : thermocouple T-OX-260
                            tc_data[8] : thermocouple T-OX-270
                            tc_data[9] : thermocouple T-CC-410
                            tc_data[10] : thermocouple T-CC-420
                            tc_data[11] : thermocouple T-CC-430
            """

            def __init__(self, tc_limit=[0]):
                self._tc_limit = tc_limit

            @property
            def tc_limit(self):
                return self._tc_limit

            @tc_limit.setter
            def tc_limit(self, tc_limit):
                self._tc_limit = tc_limit


        class LCLimit(object):
            """The Load Cell Limits determine when 'Safe' mode breaks.

                        Attributes
                        ----------
                        lc_data : load cell limit array [3]
                            lc_data[0] : load cell LC-OX-210
                            lc_data[1] : load cell LC-FU-310
                            lc_data[2] : load cell LC-CC-410
            """

            def __init__(self, lc_limit=[0]):
                self._lc_limit = lc_limit

            @property
            def lc_limit(self):
                return self._lc_limit

            @lc_limit.setter
            def lc_limit(self, lc_limit):
                self._lc_limit = lc_limit


        class LSLimit(object):
            """The Limit of a Limit Switch is the time delay for limit switches to return a signal.

                        Attributes
                        ----------
                        ls_state : limit switch limit array [11]
                            ls_state[0] : valve ABV-PR-110
                            ls_state[1] : valve ABV-PR-120
                            ls_state[2] : valve ABV-OX-210
                            ls_state[3] : valve ABV-FU-310
                            ls_state[4] : valve ABV-OX-220
                            ls_state[5] : valve ABV-FU-320
                            ls_state[6] : valve ABV-OX-230
                            ls_state[7] : valve ABV-FU-330
                            ls_state[8] : valve ABV-OX-240
                            ls_state[9] : valve ABV-FU-340
                            ls_state[10] : valve ABV-OX-250
            """

            def __init__(self, ls_limit=[0]):
                self._ls_limit = ls_limit

            @property
            def ls_limit(self):
                return self._ls_limit

            @ls_limit.setter
            def ls_limit(self, ls_limit):
                self._ls_limit = ls_limit


    class TimeState(object):
        """TimeState holds all time related values, including TimeDelay and TimeRegime

                        Attributes
                        ----------
                        delay_elements : Integer used to determine how many delays are present during firing sequence
        """

        def __init__(self, delay_elements=6):
            self.TimeDelay = self.TimeDelay()
            self.TimeRegime = self.TimeRegime()
            self._delay_elements = delay_elements

        @property
        def delay_elements(self):
            return self._delay_elements

        @delay_elements.setter
        def delay_elements(self, delay_elements):
            self._delay_elements = delay_elements

        def set_delay_elements(self):
            self.TimeDelay.time_delay = (self._delay_elements * self.TimeDelay.time_delay)


        class TimeDelay(object):
            """Holds delay times for the firing sequence

                        Attributes
                        ----------
                        0) auto_time_primary : Collects time when IgnitorState is set to '1' for Active
                        1) ignition_delay : Delay on Ignition
                        2) ox_main_delay : Delay on Main Ox Valve getting set to '1' for Active
                        3) fuel_main_delay : Delay on Main Fuel getting set to '1' for Active
                        4) burn_duration : Total time of fire
                        5) purge_delay : Time between setting purge ValveState to '1' for Active to '0' for Safe
            """

            def __init__(self, time_delay=[0]):
                self._time_delay = time_delay

            @property
            def time_delay(self):
                return self._time_delay

            @time_delay.setter
            def time_delay(self, time_delay):
                self._time_delay = time_delay


        class TimeRegime(object):
            """Determines which regime a System is operating within.

            Attributes
            ----------
            time_regime : set to a value as follows to determine which regime a System is in:
            0) init_regime : Initialization Regime
            1) system_eval_regime : System Evaluation Regime
            2) combustion_regime : Combustion Regime
            3) drain_regime : Drain Regime
            4) abort_regime : Abort Regime
            """

            def __init__(self, time_regime=0):
                self._time_regime = time_regime

            @property
            def time_regime(self):
                return self._time_regime

            @time_regime.setter
            def time_regime(self, time_regime):
                self._time_regime = time_regime



if __name__ == '__main__':

    # Initialize the system

    a = UpperClass()


    ###

    ## Test Controls Class (valves, ignitor, abort, nanny, go)
    '''
    
    # Test ValveState
    
    a.Controls.set_valve_number(5)
    print(a.Controls.ValveState.valve_state)
    a.Controls.ValveState.valve_state = [0, 0, 1, 0, 0]
    print(a.Controls.ValveState.valve_state)
    
    # Test GoState
    
    a.Controls.set_go_elements(3)
    print(a.Controls.GoState.go_state)
    a.Controls.GoState.go_state = [0, 1, 0]
    print(a.Controls.GoState.go_state)
    
    # Test IgnitorState
    
    print(a.Controls.IgnitorState.ignitor_state)
    a.Controls.IgnitorState.ignitor_state = 1
    print(a.Controls.IgnitorState.ignitor_state)
    
    # Test AbortState
    
    print(a.Controls.AbortState.abort_state)
    a.Controls.AbortState.abort_state = 1
    print(a.Controls.AbortState.abort_state)
    
    # Test NannyState
    
    print(a.Controls.NannyState.nanny_state)
    a.Controls.NannyState.nanny_state = 1
    print(a.Controls.NannyState.nanny_state)
    '''

    ###

    ## Test Data Class (PTData, TCData, LCData, LSData)
    '''

    # Test PTData

    a.Data.set_pt_number(8)
    print(a.Data.PTData.pt_data)
    a.Data.PTData.pt_data = [0, 1, 2, 3, 4, 5, 6, 7]
    print(a.Data.PTData.pt_data)

    # Test TCData

    a.Data.set_tc_number(16)
    print(a.Data.TCData.tc_data)
    a.Data.TCData.tc_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(a.Data.TCData.tc_data)

    # Test LCData

    a.Data.set_lc_number(3)
    print(a.Data.LCData.lc_data)
    a.Data.LCData.lc_data = [0, 1, 2]
    print(a.Data.LCData.lc_data)

    # Test LSData

    a.Data.set_ls_number(11)
    print(a.Data.LSData.ls_data)
    a.Data.LSData.ls_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a.Data.LSData.ls_data)
    '''

    ###

    ## Test Limit Class (PTLimit, TCLimit, LCLimit, LSLimit)
    '''
    
    # Test PTLimit

    a.Limit.set_pt_number(8)
    print(a.Limit.PTLimit.pt_limit)
    a.Limit.PTLimit.pt_limit = [0, 1, 2, 3, 4, 5, 6, 7]
    print(a.Limit.PTLimit.pt_limit)

    # Test TCLimit

    a.Limit.set_tc_number(16)
    print(a.Limit.TCLimit.tc_limit)
    a.Limit.TCLimit.tc_limit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(a.Limit.TCLimit.tc_limit)

    # Test LCLimit

    a.Limit.set_lc_number(3)
    print(a.Limit.LCLimit.lc_limit)
    a.Limit.LCLimit.lc_limit = [0, 1, 2]
    print(a.Limit.LCLimit.lc_limit)

    # Test LSLimit

    a.Limit.set_ls_number(11)
    print(a.Limit.LSLimit.ls_limit)
    a.Limit.LSLimit.ls_limit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a.Limit.LSLimit.ls_limit)
    '''

    ###

    ## Test Time Class (TimeDelay, TimeRegime)


    # Test TimeDelay

    a.TimeState.set_delay_elements(6)
    print(a.TimeState.TimeDelay.time_delay)
    a.TimeState.TimeDelay.time_delay = [0, 1, 2, 3, 4, 5]
    print(a.TimeState.TimeDelay.time_delay)

    # Test TimeRegime

    print(a.TimeState.TimeRegime.time_regime)
    a.TimeState.TimeRegime.time_regime = 3
    print(a.TimeState.TimeRegime.time_regime)

