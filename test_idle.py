# clean the shell

import subprocess as sp
sp.call('cls',shell=True)

class  Employee:
     def __init__(self, first, last, pay):
          self.first = first
          self.last  = last
          self.pay = pay
          self.email = first + '.' + last + '@company.com'

     def fullname(self):
          return '{} {}'.format(self.first, self.last)
     
                              
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

result = emp_1.fullname()
result = emp_1.fullname()
