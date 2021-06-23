# Create a complex number class
import math
import os

class Complex(object):
     def __init__(self, real, imag):
          self.real = real
          self.imag = imag

     def __add__(self, other):
          return Complex(self.real + other.real,
                         self.imag + other.imag)

     def __sub__(self, other):
          return Complex(self.real - other.real,
                         self.imag - other.imag)

     def __div__(self, other):
          return Complex(self.real / other.real,
                         self.imag / other.imag)

     def __str__(self):
          return '<'+str(self.real)+ ',' +str(self.imag)+'>'
      
    
U = Complex(2, -1)
V = Complex(1, 0)
W = U / V

def _dbscan_minimal_distance():
     pass

def learnHowToNameFunctions():
     pass


def _high_probability_density_region():
     pass

def _adjusted_turkey():
     pass


