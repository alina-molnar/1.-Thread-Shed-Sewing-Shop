class Rocket3():
    """Class to store coordinates, crew size, rocket height and speed, and to move rocket in all directions."""
    
    def __init__(self, x=0, y=0, crew=5, height=2, speed=5):
        """Set initial values of attributes."""
        self.x = x
        self.y = y
        self.crew = crew
        self.height = height
        self.speed = speed

    def move_rocket(self, x_increment=0, y_increment=0):
        """Move rocket left, right, up and down."""
        self.x += x_increment
        self.y += y_increment


# Create one object with default values of all attributes.
rocket_3 = Rocket3()
print("Rocket 0 has a height of %d, speed %d and crew of %d." %
      (rocket_3.height, rocket_3.speed, rocket_3.crew))
print("\n")

# Create new objects with different value of one attribute and default values for the rest of attributes.
rocket_4 = Rocket3(crew=10)
rocket_5 = Rocket3(crew=20)
rocket_6 = Rocket3(crew=30)
rocket_7 = Rocket3(crew=40)

# Create list to store all objects.
improved_rockets = [rocket_3, rocket_4, rocket_5, rocket_6, rocket_7]

# Print attribute with fluctuating values of each object.
for index, rocket in enumerate(improved_rockets):
    print("Rocket %d has a crew of %d people." %
          (index, improved_rockets[index].crew))
