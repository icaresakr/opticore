###
# Main optimization script
#
# © 2022, NeuroRestore
###

import imp
import os
import sys

import utils.q_common as qc
import objectives as obj
import optimizer as opt

def load_config(cfg_file):
    cfg_file = qc.forward_slashify(cfg_file)
    if not (os.path.exists(cfg_file) and os.path.isfile(cfg_file)):
        print('%s cannot be loaded.' % os.path.realpath(cfg_file))
        raise IOError
    return imp.load_source(cfg_file, cfg_file)

if __name__ == "__main__":
    # Load parameters
    if len(sys.argv) < 2:
        cfg_file = input('Config file name? ')
    else:
        cfg_file = sys.argv[1]
    
    cfg = load_config(cfg_file)

    objectives = obj.Objectives()

    optimizer = opt.Optimizer(
                    cfg = cfg, 
                    objectives = objectives
                    )

    optimizer.optimize(n_trials = cfg.N_TRIALS)
    optimizer.show_pareto()

    ## Plots




