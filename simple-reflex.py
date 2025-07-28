import random

MIN_PSI = 32
MAX_PSI = 35

def read_pressure():
  starting_pressure = random.uniform(28, 38)
  starting_pressure = round(starting_pressure, 1)
  return starting_pressure

def inflate(current_psi):
  return MIN_PSI

def deflate(current_psi):
  return MAX_PSI

def adjust_pressure(current_psi):
  if current_psi < MIN_PSI:
    return inflate(current_psi)
  elif current_psi > MAX_PSI:
    return deflate(current_psi)
  else:
    return current_psi
  
for i in range(5):
  print(f"\nCycle {i+1}")
  psi = read_pressure()
  print(f"Current PSI: {psi}")
  psi = adjust_pressure(psi)
  print(f"Adjusted pressure: {psi}")