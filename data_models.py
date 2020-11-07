# Python talk - James Powell
# So you want to be A Python Expert?
# Data Models

class Polynomial:
    def __init__(self):
        self.coeffs =coeffs
    
    def __repr__(self):
        return 'Polynomial(*(!r)' .format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x +y for x, y in zip(self.coeffs,other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass


def add(x, y):
    return x + y

def addNewFunct():
    pass


def another_function(args*, kwargs*):
    pass


