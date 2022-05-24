###
# Define objective functions here
#
# © 2022, NeuroRestore
###

class Objectives:
    def __init__(self):
        self.directions = ['minimize','maximize']
        self.names = ['MSE', 'Accuracy']
        self.n_targets = len(self.names)
    
    def __len__(self):
        return self.n_targets
    
    def evaluate(self, params = None):
        try: 
            #Do something
            return (1., 1.)

        except:
            return (0., 0.)