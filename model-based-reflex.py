import random

class ModelBasedReflexVacuum:
  def __init__(self, width, height):
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

  def sense(self):
    """Sense if the current square is dirty."""
    return self.world[self.y][self.x]
  
  def update_state(self, precept):
    """Update internal state based on precept."""
    self.state[self.y][self.x] = precept

  def clean(self):
    """Clean current square."""
    self.world[self.y][self.x] = False
    self.state[self.y][self.x] = False
    print(f"Cleaned square ({self.x}, {self.y})")

  def move(self):
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
    if self.sense() is True:
      return "CLEAN"
    elif self.sense() is False:
      for row in range(self.height):
        for col in range(self.width):
          if self.state[row][col] is True:
            if self.x < col:
              self.x += 1
            elif self.x > col:
              self.x -= 1
            elif self.y < row:
              self.y += 1
            elif self.y > row:
              self.y -= 1
            
            print(f"Moving to dirty square: ({row}, {col})")
            return "MOVE"

      self.move()
      return "MOVE"
    
  
  def run(self, steps=20):
    for step in range(steps):
      print(f"\nStep {step + 1}: Position: {self.x, self.y}")
      precept = self.sense()
      self.update_state(precept)

      action = self.choose_action()

      if action == "CLEAN":
        self.clean()


vacuum = ModelBasedReflexVacuum(width=4, height=4)
vacuum.run()







  