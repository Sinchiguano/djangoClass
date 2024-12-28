# from library import salary_calculator

import library
from library import salary_calculator



# Leonel
bonus=0
hours = 40
status = "employee"
weekly_salary = salary_calculator(hours, status,bonus)
bonus=10
print(f"The weekly salary is the following:{weekly_salary}" )


import datetime


print(datetime.datetime.now())


# len() it is a function

# list.append()# Append is a method, come from a class


import random

random_numbers = [random.randint(1, 100) for _ in range(20)]  

print(random_numbers)  # To see the output, run the code.

import numpy as np

print(np.mean(random_numbers))