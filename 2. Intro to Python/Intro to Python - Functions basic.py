# Chapter 3: Functions

# Greeter: define function to greet and use placeholders.
def greeter(name):
    """Add 3 greetings for each name."""
    print("\nHello, %s!" % name.title())
    print("Nice to meet you, %s!" % name.title())
    print("Welcome home, %s!" % name.title())
    
names = ["robin", "agatha", "rechinul"]
for name in names:
    print(greeter(name))
print("\n")

# Full name: define function to capitalize and combine first and last names, then greet.
def full_name(first_name, last_name):
    """Concatenate string with first and last name."""
    print("Hello, " + first_name.title() + " " + last_name.title() + "!")

full_name("elena", "ferrante")
full_name("sailor", "moon")
full_name("pat", "benatar")
print("\n")

# Addition calculator: use tuple to store placeholders
def addition_calculator(a, b):
    """Add 2 variables, print result."""
    result = a+b
    print("Adding %d and %d results in %d." % (a, b, result))

addition_calculator(1, 2)
addition_calculator(3, 6)
addition_calculator(114, 839)

# Return calculator: use return inside function.

def return_calculator(a, b):
    """Add 2 variables, return result."""
    result = a+b
    return result

print(return_calculator(1, 3))

# Ordered working list: define function, sort list.
# Define function to print title message and each item.
careers = ["writer", "programmer", "truck driver", "cat sitter", "welder", "painter"]

def print_career_list(career_list, message):
    """Print message and each item of the list."""
    print(message)
    for career in career_list:
        print(career)

# Call function on sorted list in various ways, print original after each sort.
print_career_list(careers, "\nThis is the original list:")
print_career_list(sorted(careers), "\nThis is the alphabetically sorted list:")
print_career_list(careers, "\nThis is the original list:")
print_career_list(sorted(careers, reverse=True), "\nThis is the reverse alphabetical sorted list:")
print_career_list(careers, "\nThis is the original list:")
careers.reverse()
print_career_list(careers, "\nThis is the reverse of the original list:")
careers.reverse()
print_career_list(careers, "\nThis is the original list:")
careers.sort()
print_career_list(careers, "\nThis is the permanently alphabetically sorted list:")
careers.sort(reverse=True)
print_career_list(sorted(careers, reverse=True), "\nThis is the permanently reversed alphabetical sorted list:")

# Ordered numbers list: define function, sort list.
# Define function to print title message and each item.
numbers = [235, 76, 17, 591, 380]

def print_numbers_list(numbers_list, message):
    """Print message and each item of the list."""
    print(message)
    for number in numbers_list:
        print(number)

print_numbers_list(numbers, "\nThis is the original list:")
print_numbers_list(sorted(numbers), "\nThis is the list in increasing order:")
print_numbers_list(numbers, "\nThis is the original list:")
print_numbers_list(sorted(numbers, reverse=True), "\nThis is the list in decreasing order:")
print_numbers_list(numbers, "\nThis is the original list:")
numbers.reverse()
print_numbers_list(numbers, "\nThis is the reverse of the original list:")
numbers.reverse()
print_numbers_list(numbers, "\nThis is the original list:")
numbers.sort()
print_numbers_list(numbers, "\nThis is the permanent list in increasing order:")
numbers.sort(reverse=True)
print_numbers_list(numbers, "\nThis is the permanent list in decreasing order:")

# Function for printing lyrics
def gather_lyrics(song_title, artist, verse_1, verse_2, verse_3, refrain):
    """Print title, artist and song."""
    print("\n%s by %s" % (song_title, artist))
    print(verse_1, refrain, verse_2, refrain, verse_3, refrain)

song_title = "Love & Understanding"
artist = "Cher"
verse_1 = "\n\nHere, here in this world \nWhere do we go? Where can we turn? \nWhen we need some love \nIt seems that love just can't be found \nWhere, where do we stand? \nWhen love's supply don't meet love's demand \n\nWe got enough stars to light the sky at night \nEnough sun to make to make the whole world bright \nWe got more than enough \nBut there's one thing there's just not enough of"
verse_2 = "\n\nSpend all of our time \nBuilding buildings up to the sky \nReaching everywhere \nBut where we need to reach the most \nHearts never can win \nOh, in this race, this race that we're in \n\nWe've got enough cars to drive around the world \nEnough planes to take us anywhere \nWe got more than enough \nBut there's one thing there's just not enough of"
verse_3 = "\n\nWe need some understandin' \nWe need a little more love \nSome love and understandin' \n\nEnough stars to light the sky at night \nEnough sun to make the whole world bright \nEnough hearts to find some love inside \nWe got more than enough \nBut there's one thing there's just not enough of"
refrain = "\n\nNot enough love and understanding \nWe could use some love to ease these troubled times \nNot enough love and understanding \nWhy, oh why?"
   
gather_lyrics(song_title, artist, verse_1, verse_2, verse_3, refrain)