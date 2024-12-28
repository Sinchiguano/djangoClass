
weeklysalary=0
hours=0
status=""
bonus=0

def salary_calculator(hours:float, status:str,bonus:float=0.0) -> float:
  if status == "CEO":
    rate = 25
  elif status == "Manager":
    rate = 20
  elif status == "Employee":
    rate = 15
  else:
    rate = 10
  return (hours * rate)+bonus

# Leonel
hours = 40
status = "CEO"
weekly_salary = salary_calculator(hours, status,bonus)
bonus=10
print(f"The weekly salary is the following:{weekly_salary}" )

# Cesar
hours = 40
status = "Manager"
weekly_salary = salary_calculator(hours, status,bonus)
bonus=10
print(f"The weekly salary is the following:{weekly_salary}" )

# Cesar
hours = 40
status = "Employee"
weekly_salary = salary_calculator(hours, status,bonus)
bonus=10
print(f"The weekly salary is the following:{weekly_salary}" )




def adding(a:float, b:float, c:float,*additional_number) -> float:
  try:
    total_sum=a+b+c
    for item in additional_number:
      total_sum+=item
  except Exception as e:
    print(f"There is an error, {e}")
  return total_sum

print(adding(1,23,3,7))

print("**************************")

print("**************************")
print("#################################################")

dividend=0
divisor=0

def division(**components):
  try:
    if dividend not in components:
      print(f"There is a missed components!!!!")
      return 
    print(components)
    print(type(components))
    return components['dividend']/components['divisor']

  except Exception as e:
    print(f"There is an error, division by zero... {e}") 
  except ZeroDivisionError as tmp1:
    print(f"new error. {tmp1}")
  
print(division(dividend=20))

print("222222222222222222")
print(division())

