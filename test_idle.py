# clean the shell
import subprocess as sp
sp.call('cls',shell=True)



# Create a parent clas of animal

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

print(emp_1.email)
print(emp_2.email)

result = emp_1.fullname()

print(result)


def another_newFunc():
     pass


Class NewClassForJustPullRequest:
     pass