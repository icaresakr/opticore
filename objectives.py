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
    
    def evaluate(self, cfg = None, params = None):
        """
            Evaluate objectives based on suggested parameters

            params: dict parameters names and values {'param_name': param_value, ...}
        """
        try: 
            #Do something
            return (1., 1.)

        except:
            return (0., 0.)