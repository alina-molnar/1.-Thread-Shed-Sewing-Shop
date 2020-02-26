# Chapter 4: If Statements

# Program of at least 10 logical statements, 5 True and 5 False.
grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(1>2)
print(4>=4)
print(7<5)
print(6>3)
print(16==13)
print(14==14)
print(9!=9)
print(9!=8)
print(13 in grades)
print(3 in grades)

# If test with 1 condition and a list with fluctuating length, then store it as function.
people_1 = ["mary", "james", "john", "adriana"]
if len(people_1) > 3:
    print("\nWow, what a crowd we have here!")

del people_1[-1]
del people_1[-1]

if len(people_1) > 3:
    print("\nWow, what a crowd we have here!")

def crowd_test(list_to_test):
    """Test if list has more than 3 times."""
    if len(people_1) > 3:
        print("\nWow, what a crowd we have here!")

crowd_test(people_1)

# If test with 2 conditions stored in a function.
def size_test(list_to_test):
    """"Test if list has more than 3 times, else not crowded."""
    if len(people_1) > 3:
        print("\nWow, what a crowd we have here!")
    else:
        print("\nNot that crowded after all.")

size_test(people_1)

# If test with multiple conditions stored in a function.
people_1.append("ann")
people_1.append("sarah")
people_1.append("george")
people_1.append("mathew")

def count_people(list_to_test):
    """Group list lengths in multiple conditions."""
    if len(people_1) > 5:
        print("\nThere's a mob in this room!")
    elif len(people_1) >= 3:
        print("\nWow, the room is crowded!")
    elif len(people_1) >= 1:
        print("\nNot that crowded after all.")
    else:
        print("\nHey, why is this room empty?")

count_people(people_1)

# Alien list: award 5 points for red, 10 for green, 20 for blue and count the total points.
aliens = ["red", "blue", "green", "blue", "green", "red", "red", "green", "blue", "blue"]
points = 0
for alien in aliens:
    if alien == "red":
        points += 5
    elif alien == "green":
        points += 10
    elif alien == "blue":
        points += 20
    else:
        points += 0

print("\nTotal number of points is %d." % points)