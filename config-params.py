###
# Optimizer configuration file
#
# © 2022, NeuroRestore
###

## STUDY PARAMETERS
'''
optimization method 
mono-objective samplers: 'GRID', 'RANDOM', 'TPE', 'CMAES'
multi-objective samplers: 'NSGAII', 'MOTPE'
'''
SAMPLER = 'NSGAII'

N_TRIALS = 100 # number of optimization trials
STUDY_NAME = "example_optimization"
STORAGE_NAME = "sqlite:///{}.db".format(STUDY_NAME) # database to store study information
LOAD = False #load study if already exists (if false, will continue from checkpoint)


## VARIABLES TO OPTIMIZE
VARIABLES = { 

    'FLOAT_VAR': {
                'type': 'float',
                'values': [0., 1.], #values range
                'step': 0.1 #optional step, float 
                },

    'INT_VAR': {
                'type': 'int',
                'values': [0, 10], #values range
                'step': 1 #optional step, int
                },

    'CATEGORICAL_VAR': {
                'type': 'categorical',
                'values': ['None', "'car'"], #possible values
                },

}



USE_CONSTRAINTS = True

""" Not implemented yet
CONSTRAINTS = {
    1: "'FLOAT_VAR' < 'INT_VAR'"

}
"""

LOAD_PATH = ''
SAVE_PATH = ''

## ADD OTHER PARAMETERS HERE