import os

print(os.listdir())


##from.import states

#class InputDataOpen(object):
    #def __init__(self, filename):
        #self.file = open(filename)

    #def __enter__(self):
        #return self.file

    #def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        #self.file.close()

#with InputDataOpen('file') as f:
    #in_data = f.read()
