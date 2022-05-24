
import optuna

class Optimizer:
    def __init__(self, study_name, cfg, objectives, sampler = 'NSGAII', storage_name = None):

        assert len(objectives) > 0

        self.cfg = cfg

        self.study_name = study_name
        self.objectives = objectives
        self.n_objectives = len(objectives)

        if sampler == 'NSGAII' or len(objectives) > 1:
            print("Using NSGA-II sampler multi-objective optimization")
            self.sampler = optuna.samplers.NSGAIISampler()
        
        else:
            self.sampler = None

        self.study = optuna.create_study(study_name=study_name, storage=storage_name, load_if_exists=True, directions=[objectives[i].direction for i in range(self.n_objectives)], sampler = sampler)

    def __suggest_variables(self, trial):
        try:
            params = {}
            for param in self.cfg.VARIABLES.keys():
                if self.cfg.VARIABLES[param]['type'] == 'float':
                    params[param] = trial.suggest_float(param, self.cfg.VARIABLES[param]['values'][0], self.cfg.VARIABLES[param]['values'][1], step=self.cfg.VARIABLES[param]['step'])

                elif self.cfg.VARIABLES[param]['type'] == 'int':
                    params[param] = trial.suggest_int(param, self.cfg.VARIABLES[param]['values'][0], self.cfg.VARIABLES[param]['values'][1], step=self.cfg.VARIABLES[param]['step'])

                elif self.cfg.VARIABLES[param]['type'] == 'categorical':
                    params[param] = trial.suggest_categorical(param, self.cfg.VARIABLES[param]['values'])

                else:
                    print("%s variable type not recognized" % param)
                    raise NotImplementedError
        
            return params

        except:
            return None
    
    def objective(self, trial):
        params = self.__suggest_variables(trial)
        
        return tuple([objective.evaluate(params) for objective in self.objectives])
    
    def optimize(self, n_trials = 500):
        self.study.optimize(self.objective, n_trials)
