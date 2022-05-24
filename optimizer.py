###
# Optinizer definition
#
# © 2022, NeuroRestore
###

import optuna

class Optimizer:
    def __init__(self, cfg, objectives):

        assert len(objectives) > 0

        self.cfg = cfg

        self.study_name = cfg.STUDY_NAME
        self.objectives = objectives
        self.n_objectives = len(objectives)

        if len(objectives) > 1:
            if cfg.SAMPLER == 'NSGAII':
                self.sampler = optuna.samplers.NSGAIISampler()

            elif cfg.SAMPLER == 'MOTPE':
                self.sampler = optuna.samplers.MOTPESampler()

            else:
                print("Swiching to NSGA-II sampler for multi-objective optimization")
                self.sampler = optuna.samplers.NSGAIISampler()
        
        else:  #(len(objectives) == 1)
            if cfg.SAMPLER == 'GRID':
                self.sampler = optuna.samplers.GridSampler()

            elif cfg.SAMPLER == 'TPE':
                self.sampler = optuna.samplers.TPESampler()
            
            elif cfg.SAMPLER == 'CMAES':
                self.sampler = optuna.samplers.CmaEsSampler()
    
            elif cfg.SAMPLER == 'RANDOM':
                self.sampler = optuna.samplers.RandomSampler()

            else: 
                print("Using default TPE sampler")
                self.sampler = optuna.samplers.TPESampler()

        if cfg.STORAGE_NAME:
            self.study = optuna.create_study(study_name=cfg.STUDY_NAME, storage=cfg.STORAGE_NAME, load_if_exists=True, directions=objectives.directions, sampler = self.sampler)
        
        else:
            self.study = optuna.create_study(study_name=cfg.STUDY_NAME, directions=objectives.directions, sampler = self.sampler)

    def __suggest_variables(self, trial):
        try:
            params = {}
            for param in self.cfg.VARIABLES.keys():
                if self.cfg.VARIABLES[param]['type'] == 'float':
                    if 'step' in self.cfg.VARIABLES[param].keys():
                        params[param] = trial.suggest_float(param, self.cfg.VARIABLES[param]['values'][0], self.cfg.VARIABLES[param]['values'][1], step=self.cfg.VARIABLES[param]['step'])
                    else:
                        params[param] = trial.suggest_float(param, self.cfg.VARIABLES[param]['values'][0], self.cfg.VARIABLES[param]['values'][1])

                elif self.cfg.VARIABLES[param]['type'] == 'int':
                    if 'step' in self.cfg.VARIABLES[param].keys():
                        params[param] = trial.suggest_int(param, self.cfg.VARIABLES[param]['values'][0], self.cfg.VARIABLES[param]['values'][1], step=self.cfg.VARIABLES[param]['step'])
                    else:
                        params[param] = trial.suggest_int(param, self.cfg.VARIABLES[param]['values'][0], self.cfg.VARIABLES[param]['values'][1])

                elif self.cfg.VARIABLES[param]['type'] == 'categorical':
                    params[param] = trial.suggest_categorical(param, self.cfg.VARIABLES[param]['values'])

                else:
                    print("%s variable type not recognized" % param)
                    raise NotImplementedError
        
            return params

        except:
            return None
    
    def objective(self, trial):
        #print(trial)
        params = self.__suggest_variables(trial)

        if not params:
            raise(Exception("Error while suggesting variables, probably from config file?"))
        
        return self.objectives.evaluate(self.cfg, params)
    
    def optimize(self, n_trials = 500):
        self.study.optimize(self.objective, n_trials)

    def show_pareto(self):
        trials = sorted(self.study.best_trials, key=lambda t: t.values)
        print(" ----------------------- ")
        for trial in trials:
            print("  Trial#{}".format(trial.number))
            print("    Values:", end= '')
            for i in range(self.n_objectives):
                print(f" {self.objectives.names[i]}: {trial.values[i]}", end='')
                if i < self.n_objectives - 1:
                    print(f",", end='')
                else:
                    print()
            print("    Params: {}".format(trial.params))
            print(" ----------------------- ")
    
