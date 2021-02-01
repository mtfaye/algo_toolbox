# -*- coding: utf-8 -*-
"""
@author: Mouhameth T Faye

# **Dunnhumby - Python Test**

"""

basket_values = [3.43,9.73,7.56,9.52,15.23,2.25,6.44,7.38]

""" 1 - a. Print out whether each basket is:
small (basket value < £5),
medium (£5 ≤ basket value < £10) 
or large (basket value ≥ £10)
"""

def basket_size(given_list):
  # Re-usable function for any given list of values

  for i in given_list:
    if i < 5:
      print("Small : ",i)
    if i >= 10:
      print("Large : ",i)
    if i >= 5 and i <10:
      print("Medium: ",i)

# Give it the list basket_values 
basket_size(basket_values)

""" 1 - b. Sum and print the value of the medium value baskets:"""

def mysum(basket_values):
    # sum all the medium values and return the total
    
    running_total = 0
    for i in basket_values:
      if i >= 5 and i <10:
        running_total = running_total + i
    return running_total

mysum(basket_values)

""" 2. You are given the following nested dictionaries, which represent items in a basket:"""

basket = {
          '2624': {'price': 0.5, 'prod_name': 'salt'},
          '2894': {'price': 3.25, 'prod_name': 'yeast'},
          '7527': {'price': 2.5, 'prod_name': 'flour'}
          }

""" 2 - a. Return the product name for item 7527"""

# access nested dict using indexing 
basket['7527']['prod_name']

""" 2 - b. Return the total value of this basket"""

sum = 0
# iterating key value pair 
for key, value in basket.items(): 

    if value and 'price' in value.keys(): 
        # adding value of price to sum 
        sum += value['price']

# print sum of value
sum

""" 2 - c. Add another entry for a product that costs £4.95, has ID 7524 and name ‘poppy seeds’"""

# insert new dict into basket
basket['7524'] = {'price': 4.95, 'prod_name': 'poppy seeds'}

# result
basket

""" 3. Below is the source code for a function called ‘get_sql_string’"""

def get_sql_string(stores):
  store_names = [x.split(', ')[0] for x in stores]
  store_names = [x.replace(' ', '_') for x in store_names]
  store_regions = [x.split(',')[1] for x in stores]
  locations = store_names + store_regions
  columns = ['sales_' + x.lower() for x in locations]

  return ', '.join(columns)

""" 3 - a. There is a bug in line 4. What should the line be?"""

# split function separate string 
 store_regions = [x.split(', ')[1] for x in stores]

""" 3 - Assuming this bug was fixed, what would be returned if the following command was executed:

my_stores = ['Fulham Palace Rd, Hammersmith', 'Crown St, Reading', 'Leavesden Green, Watford']

get_sql_string(my_stores)
"""



"""## 4. Write a function that:

         a. accepts a list of strings as input;

         b. returns an alphabetically ordered list of unique strings;

         c. prints the string(s) with maximum length in the console.
"""

# create a list of string
lst_string = ["dgddfg", "sdf", "ffs", "asdd", "hdfsdgsdggsdgdgd"]

def get_maxsort(lst_string):
# function that take a list of strings, sort it and return the max length
  # use built-in sort function to order element alphabetically
  new_list = sorted(lst_string)
  print("Alphabetically ordered:\n")
  print(new_list)
  print("\n")
  
  # use built-in max function to get the max length
  print("Max length:\n")
  return max(new_list, key=len)

# result
get_maxsort(lst_string)
