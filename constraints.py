###
# Define constraints here
#
# © 2022, NeuroRestore
###

class Constraints:
    def __init__(self):
        self.n_constraints = 2
    
    def __len__(self):
        return self.n_constraints

    def evaluate(self, cfg = None, params = None):
        """
            Constraints objectives based on suggested parameters

            params: dict parameters names and values {'param_name': param_value, ...}
        """
        
        cstr1 = - (params['INT_VAR'] - params['FLOAT_VAR']) # INT_VAR < FLOAT_VAR constraint
        cstr2 = (params['CATEGORICAL_VAR'] == 'None')*(params['INT_VAR'] > 2) # FLOAT_VAR > 100 => CATEGORICAL_VAR != None constraint
        #probably normalize?
        return (cstr1, cstr2)

