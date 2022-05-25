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
            #FIXME: define objectives here
            #Do something
            #e.g.
            obj1 = params['INT_VAR']**2 + params['FLOAT_VAR']
            obj2 =  params['INT_VAR'] * params['FLOAT_VAR']**2

            return (obj1, obj2)

        except:
            return (0., 0.)