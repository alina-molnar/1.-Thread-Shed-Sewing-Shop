class Car:
    """Class to store details about car and its owner."""

    def __init__(self, make="subaru", year=1954, owner="john doe"):
        """Set initial attributes."""
        self.make = make
        self.year = year
        self.owner = owner

    def describe_car(self):
        """Describe all known attributes."""
        print("This car produced by %s in %d is owned by %s." %
              (self.make.title(), self.year, self.owner.title()))


# Create objects with different details.
car_0 = Car(make="toyota", year=1989, owner="mike")
car_1 = Car(make="honda", year=1997, owner="sarah")
car_2 = Car(make="suzuki", year=2013, owner="annie")
car_3 = Car(make="mitsubishi", year=2020, owner="dave")

# Store all objects in a list.
cars = [car_0, car_1, car_2, car_3]

# Print description of each car.
for index, car in enumerate(cars):
    car.describe_car()
