from math import sqrt


class Rocket2():
    """Class to store coordinates, move rocket in all directions, calculate distance between all rockets."""

    def __init__(self, x=0, y=0):
        """Set initial coordinates."""
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=0):
        """Move rocket left, right, up and down."""
        self.x += x_increment
        self.y += y_increment

    def get_distance(self, other_rocket):
        """Calculate distance between two rockets."""
        distance = sqrt((self.x - other_rocket.x)**2 +
                        (self.y - other_rocket.y)**2)
        if self != other_rocket:
            print("Distance between %s and %s is %d." %
                  (self, other_rocket, distance))
        return distance


# Create object, move it, then print new coordinates.
rocket_2 = Rocket2()
rocket_2.move_rocket(-1, 3)
print(rocket_2.x)
print(rocket_2.y)
print("\n")

# Create list of 5 rockets.
improved_rockets = [Rocket2() for x in range(0, 5)]

# Move all rockets.
improved_rockets[0].move_rocket(-2, 1)
improved_rockets[1].move_rocket(2, 4)
improved_rockets[2].move_rocket(1, -2)
improved_rockets[3].move_rocket(3, 2)
improved_rockets[4].move_rocket(5, 3)

# Print coordinates of each rocket
for index, rocket in enumerate(improved_rockets):
    print("Coordinates of rocket %d: %d, %d" % (index, rocket.x, rocket.y))

# ??????Maybe use **kwargs when defining get_distance function, then use pop method to calculate distance between one element in the list and all others???????????????????????????
# Print distance between rockets using for loops, problem is they are shown both ways (like A to B, and B to A).
for index, rocket in enumerate(improved_rockets):
    improved_rockets[0].get_distance(rocket)
    improved_rockets[1].get_distance(rocket)
    improved_rockets[2].get_distance(rocket)
    improved_rockets[3].get_distance(rocket)
    improved_rockets[4].get_distance(rocket)

# Print distance between rockets using for loops, problem is I have to write them by hand.
print("\nDistances between rockets:")
improved_rockets[0].get_distance(improved_rockets[1])
improved_rockets[0].get_distance(improved_rockets[2])
improved_rockets[0].get_distance(improved_rockets[3])
improved_rockets[0].get_distance(improved_rockets[4])
improved_rockets[1].get_distance(improved_rockets[2])
improved_rockets[1].get_distance(improved_rockets[3])
improved_rockets[1].get_distance(improved_rockets[4])
improved_rockets[2].get_distance(improved_rockets[3])
improved_rockets[2].get_distance(improved_rockets[4])
improved_rockets[3].get_distance(improved_rockets[4])
