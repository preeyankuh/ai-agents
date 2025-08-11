import random

class ModelBasedReflexVacuum:
  def __init__(self, width, height, battery):
    # initializes the width and height of world
    self.width = width
    self.height = height

    # randomly assigns each square in grid True or False
    # True means that square is dirty, False means it's clean
    self.world = [[random.choice([True, False]) for _ in range(self.width)] for _ in range(self.height)]

    # what the agent believes about which squares aree dirty
    # initially doesn't know anything so everything is set to None
    self.state = [[None for _ in range(self.width)] for _ in range(self.height)]

    # initial position is set to a random location
    self.x = random.randint(0, width - 1)
    self.y = random.randint(0, height - 1)

    # battery life of vacuum is originally full 
    self.battery = battery
    self.max_battery = battery

  def sense(self):
    """Sense if the current square is dirty."""
    return self.world[self.y][self.x]
  
  def update_state(self, precept):
    """Update internal state based on precept."""
    self.state[self.y][self.x] = precept

  def clean(self):
    """Clean current square."""
    if self.battery > 0 and self.world[self.y][self.x]:
    # if there is some charge and if the square is dirty
      self.world[self.y][self.x] = False
      self.state[self.y][self.x] = False
      self.battery -= 1
      print(f"Cleaned square ({self.x}, {self.y}). \nBattery left: {self.battery}")
    elif self.battery == 0:
      print(f"Cannot clean ({self.x}, {self.y}). Battery dead.")

  def recharge(self):
    """Recharge battery to full."""
    if self.x == 0 and self.y == 0 and self.battery < self.max_battery:
      print(f"Recharging at home.")
      self.battery = self.max_battery

  def move_toward(self, target_x, target_y):
    """Move toward a specific square on grid."""
    if self.x < target_x:
      self.x += 1
    elif self.x > target_x:
      self.x -= 1
    elif self.y < target_y:
      self.y += 1
    elif self.y > target_y:
      self.y -= 1
    
    print(f"Move towards ({target_x}, {target_y})")

  def move_randomly(self):
    """Move to random square within grid bounds."""
    directions = []
    if self.x < self.width - 1:
      directions.append((1, 0))
    if self.x > 0:
      directions.append((-1, 0))
    if self.y < self.height - 1:
      directions.append((0, 1))
    if self.y > 0:
      directions.append((0, -1))

    dx, dy = random.choice(directions)
    self.x += dx
    self.y += dy

    print(f"Moved to ({self.x}, {self.y})")

  def choose_action(self):
    """Decide what to do. Clean if square is dirty or move to a new square if square is clean."""
    if self.battery <= 0:
      print(f"Battery empty. Heading home to recharge.")
      self.move_toward(0, 0)

    if self.sense():
      self.clean()
      return
    
    for row in range(self.height):
      for col in range(self.width):
        if self.state[row][col] is True:
          print(f"Moving to dirty square from memory: ({row}, {col})")
          self.move_toward(col, row)
          return

    self.move_randomly()
    
  def run(self, steps=20):
    for step in range(steps):
      print(f"\nStep {step + 1}: Position: {self.x, self.y} Battery: {self.battery}")
      self.recharge()
      precept = self.sense()
      self.update_state(precept)
      self.choose_action()

vacuum = ModelBasedReflexVacuum(width=5, height=5, battery=3)
vacuum.run(steps=40)







  