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


def adding() -> float:  
    pass

def multiplier (hours:float, status:str,) -> float:
    pass