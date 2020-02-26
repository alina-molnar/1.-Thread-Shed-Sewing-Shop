class Rocket1():
    """Class to store position of rocket and move up."""

    def __init__(self):
        """Set initial coordinates."""
        self.x = 0
        self.y = 0

    def move_up(self):
        """Move up rocket."""
        self.y += 1


# Create object, print one coordinate.
rocket_1 = Rocket1()
print(rocket_1)
print(rocket_1.y)
print("\n")

# Move up rocket then print same coordinate.
rocket_1.move_up()
print(rocket_1.y)
print("\n")

# Create list of 5 rockets.
original_rockets = [Rocket1() for x in range(0, 5)]

# Move up first rocket on the list.
original_rockets[0].move_up()

# Print same coordinate for each rocket.
for rocket in original_rockets:
    print(rocket.y)
