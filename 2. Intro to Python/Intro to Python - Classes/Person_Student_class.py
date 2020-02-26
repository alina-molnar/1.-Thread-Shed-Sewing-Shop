class Person():
    """Class to store name, age and birthplace of a person, to introduce them and to increase their age."""

    def __init__(self, name="john doe", age=1000, birthplace="saturn"):
        """Set personal attributes."""
        self.name = name
        self.age = age
        self.birthplace = birthplace

    def introduce_yourself(self):
        """Introduce a person."""
        print("Hi, my name is %s." % self.name.title())

    def get_older(self, years):
        """Add years to a person's age."""
        self.age += years
        print("%s is now %d years old." % (self.name.title(), self.age))
        return self.age


# Create person with specific parameters.
person_0 = Person(name="mary", age=30, birthplace="ohaba de sub piatra")
print(person_0.name.title(), person_0.age, person_0.birthplace.title())
print("\n")

# Introduce person.
print(person_0.introduce_yourself())
print("\n")

# Increase age and print it.
print(person_0.get_older(years=2))
print("\n")


# Student class - inherit from Person class, add new attributes.


class Student(Person):
    """Inherit attributes from Person class, add new ones specific to students."""

    def __init__(self, name="john doe", age=1000, birthplace="saturn", school="sheepfold", graduation_year=1900, gpa=100):
        """Set default name, age, birthplace, school, graduation year and gpa."""
        super().__init__(name, age, birthplace)
        self.school = school
        self.graduation_year = graduation_year
        self.gpa = gpa


# Create object with default values and print all attributes.
student_0 = Student()
print(student_0.name)
print(student_0.age)
print(student_0.birthplace)
print(student_0.school)
print(student_0.graduation_year)
print(student_0.gpa)
print("\n")

# Create object with specific values of some attributes.
student_1 = Student(name="mary", birthplace="nevada")
print(student_1.name)
print(student_1.birthplace)
print("\n")

# Create new object with specific values of other attributes.
student_2 = Student(school="mit", gpa=2)
print(student_2.school)
print(student_2.gpa)
print("\n")
