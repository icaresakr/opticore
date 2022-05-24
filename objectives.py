"""
Define objective functions here

"""
class Objective:
    def __init__(self, direction = 'minimize'):
        self.direction = direction
    
    def evaluate(self, params = None):
        return 0.0

class Accuracy(Objective):
    def __init__(self, direction = 'maximize', name = 'Accuracy'):
        super().__init__(direction)
        self.name = name
    
    def evaluate(self, params = None):
        try: 
            # Do something
            return 1.

        except:
            return 0.

class F1score(Objective):
    def __init__(self, direction = 'maximize', name = 'F1score'):
        super().__init__(direction)
        self.name = name
    
    def evaluate(self, params = None):
        try: 
            # Do something
            return 1.

        except:
            return 0.
    

