# Python talk - James Powell
# So you want to be A Python Expert?

# Canada Day weekend push!

class Polynomial:
    def __init__(self):
        self.coeffs =coeffs
    
    def __repr__(self):
        return 'Polynomial(*(!r)' .format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x +y for x, y in zip(self.coeffs,other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

# Top level syntax, function -> underscore methods
from dis import dis

def add(x, y):
    return x + y

def compute():
    rv =[]
    for i in range(10):
        sleep(.5)
        rv.append()
    return rv

# Generators functions
from sqlite3 import connect

def sql_connect():
    with connect('test.db') as conn:
        cur = conn.cursor()
        cur.execute('create table points(x int, y int)')
        cur.execute('insert inot points (x, y), values(1, 1)')
        cur.execute('create table points(x int, y int)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('selectsum(x * y ) from points'):
            pass

with connect('test.db') as conn:
    cur = conn.cursor()
    cur.execute('create table points(x int, y int)')
    cur.execute('insert inot points (x, y), values(1, 1)')
    cur.execute('create table points(x int, y int)')
    for row in cur.execute('select x, y from points'):
        print(row)
    for row in cur.execute('selectsum(x * y ) from points'):
        pass
    
    
    def __init__():
        pass
    
    
