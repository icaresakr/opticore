### OPTIMIZER CONFIGURATION FILE

## VARIABLES TO OPTIMIZE
VARIABLES = { 

    'FLOAT_VAR': {
                'type': 'float',
                'values': [0., 1.],
                'step': 0.1 #optional, float 
                },

    'INT_VAR': {
                'type': 'int',
                'values': [0, 10],
                },

    'CATEGORICAL_VAR': {
                'type': 'categorical',
                'values': ['None', "'car'"],
                },

}


""" Not implemented yet
CONSTRAINTS = {
    1: "'FLOAT_VAR' < 'INT_VAR'"

}
"""

LOAD_PATH = ''

SAVE_PATH = ''

## ADD OTHER PARAMETERS HERE