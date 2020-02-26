from math import sqrt


class Rocket4():
    """Class to store coordinates, crew size, rocket height and speed, to move rocket in all directions, to accelerate rocket and to check distance towards all of them."""

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

    def accelerate_rocket(self, speed=5):
        """Accelerate rocket."""
        self.speed = speed*3

    def safety_check(self, other_rocket):
        """Check distance between rockets."""
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        if distance <= 1:
            print("The rockets have crashed!")
        elif distance <= 3:
            print("Red allert! Prepare for impact!")
        else:
            print("Cruising through the stars.")


# Create one object with default values of all attributes.
rocket_8 = Rocket4()

# Create new objects with different coordinates.
rocket_9 = Rocket4(x=2, y=2)
rocket_10 = Rocket4(x=3, y=7)
rocket_11 = Rocket4(x=0, y=1)

# Print speed before and after accelerating one object.
print(rocket_8.speed)
rocket_8.accelerate_rocket()
print(rocket_8.speed)
print("\n")

# Check distance between an object and the others and print status.
print(rocket_8.safety_check(rocket_9))
print(rocket_8.safety_check(rocket_10))
print(rocket_8.safety_check(rocket_11))
print("\n")


# Create Shuttle class - inherit from Rocket, add new attributes and methods.


class Shuttle(Rocket4):
    """Inherit attributes from Rocket class, add new attributes specific to shuttles."""

    def __init__(self, x=0, y=0, crew=5, height=2, speed=5, flights=0, max_flights=1000, spacewalks=True, docking=True):
        """Set initial values of attributes."""
        super().__init__(x, y, crew, height, speed)
        self.flights = flights
        self.max_flights = max_flights
        self.spacewalks = spacewalks
        self.docking = docking

    def stop_shuttle(self):
        """Decrease speed to zero."""
        self.speed = 0
        print("The shuttle has stopped.")


# Create object with specific parameters and print some of them.
shuttle = Shuttle(3, 4, 8, 1, 6, 9, 500, False, True)
print(shuttle.crew)
print(shuttle.max_flights)
print(shuttle.spacewalks)
print(shuttle.docking)

# Print speed before and after stopping the shuttle.
print(shuttle.speed)
shuttle.stop_shuttle()
print(shuttle.speed)
