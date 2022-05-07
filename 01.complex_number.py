# Create a complex number class
# From "Now you are a python expert"

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
