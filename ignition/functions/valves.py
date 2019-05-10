#class ValveState(object):
    #def __init__(self, state):
        #self.s = state

    #def valve_state(self):
        #self.name = new_name



class ValveState(object):
    def __init__(self):
        self.a = [0, 0, 0, 0, 0, 0, 0]  #Safe
        self.b = [0, 0, 0, 0, 0, 0, 1]  #LOX Fill
        self.c = [1, 1, 0, 0, 0, 0, 0]  #Loaded
        self.d = [1, 1, 1, 1, 0, 0, 0]  #Pressurized
        self.e = [1, 1, 1, 1, 1, 1, 0]  #Fire
        self.f = [0, 0, 0, 0, 1, 1, 0]  #Shutdown
        self.g = [0, 0, 1, 0, 0, 0, 0]  #LOX Purge
        self.h = [0, 0, 0, 0, 1, 0, 0]  #LOX Dump


    def valve_state(self):
        self.name = new_name
