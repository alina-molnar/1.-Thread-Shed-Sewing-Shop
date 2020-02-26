# Chapter 2: Lists, Tuples

# Programming languages: make a list, capitalize names and concatenate string.
programming_languages = ["python", "c", "java"]
print(programming_languages[0])
print(programming_languages[1])
print(programming_languages[2])
print("A nice programming language is " + programming_languages[0].title() + ".")
print("A nice programming language is " + programming_languages[1].title() + ".")
print("A nice programming language is " + programming_languages[2].title() + ".")

# Fruits: make a list, concatenate string.
fruits = ["plum", "apple", "pear", "walnut"]
print("One item in fruits is " + str(fruits[-1]) + ".")

# Loop in a list: concatenate index, element and string.
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    grading = str(index)
    print("Number " + grading + " coresponds to " + fruit + ".")

careers = ["programmer", "truck driver", "cat sitter", "welder"]

# Find index in list: find index of element in list.
for index, career in enumerate(careers):
    print(careers[index].title() + " is number " + str(careers.index(careers[index])) + " on my list.")

# Check if career in list: check if element is in list.
print("cat sitter" in careers)

# Add new career in list: add new item in list using append.
careers.append("painter")

# Insert career at beginning of list: add new item in list using index.
careers.insert(0, "writer")

for career in careers:
    print(career)

# Create from scratch the list of careers, append it, print the first and the last.

careers_2 = []
careers_2.append("writer")
careers_2.append("programmer")
careers_2.append("truck driver")
careers_2.append("cat sitter")
careers_2.append("painter")
print("\nThe first carrer I have thought of is " + str(careers_2[0]) + ".")
print("The last carrer I have thought of is " + str(careers_2[-1]) + ".")

# Order career list in various ways and print the original after each sorting.
# Display the original list.
print("\nThis is the original list:")
for career in careers:
    print(career)

# Display the list in alphabetical order.
print("\nThis is the list in alphabetical order:")
for career in sorted(careers):
    print(career)

# Display the original list.
print("\nThis is the original list:")
for career in careers:
    print(career)

# Display the list in reverse alphabetical order.
print("\nThis is the list in reverse alphabetical order:")
for career in sorted(careers, reverse=True):
    print(career)

# Display the original list.
print("\nThis is the original list:")
for career in careers:
    print(career)

# Display the list in reverse of original order.
print("\nThis is the list in reverse of original order:")
careers.reverse()
for career in careers:
    print(career)

# Display the original list.
print("\nThis is the original list:")
careers.reverse()
for career in careers:
    print(career)

# Display the permanent list in alphabetical order.
careers.sort()
print("\nThis is the permanent list in alphabetical order:")
for career in careers:
    print(career)

# Display the permanent list in reverse alphabetical order.
careers.sort(reverse=True)
print("\nThis is the permanent list in reverse alphabetical order:")
for career in careers:
    print(career)

# Order numbers in various ways and print the original after each.
numbers = [235, 76, 17, 591, 380]
# Display the original list.
print("\nThis is the original list:")
for number in numbers:
    print(number)

# Display the list in increasing order.
print("\nThis is the list in increasing order:")
for number in sorted(numbers):
    print(number)

# Display the original list.
print("\nThis is the original list:")
for number in numbers:
    print(number)

# Display the list in decreasing order.
print("\nThis is the list in decreasing order:")
for number in sorted(numbers, reverse=True):
    print(number)

# Display the original list.
print("\nThis is the original list:")
for number in numbers:
    print(number)

# Display the list in reverse of original order.
print("\nThis is the list in reverse of original order:")
numbers.reverse()
for number in numbers:
    print(number)

# Display the original list.
print("\nThis is the original list:")
numbers.reverse()
for number in numbers:
    print(number)

# Display the permanent list in increasing order.
numbers.sort()
print("\nThis is the permanent list in increasing order:")
for number in numbers:
    print(number)

# Display the permanent list in decreasing order.
numbers.sort(reverse=True)
print("\nThis is the permanent list in decreasing order:")
for number in numbers:
    print(number)

# List lengths: calculate length, add string.
print("\nThe list of careers has " + str(len(careers)) + " items.")
print("The list of numbers has " + str(len(numbers)) + " items.")

# Remove items from list: use pop with or without index, del and remove.
famous_people = ["Ada Lovelace", "Ecaterina Teodoroiu", "Ion Minulescu", "Neil deGras Tyson"]
famous_people.pop()
famous_people.pop(0)
del famous_people[1]
famous_people.remove("Ecaterina Teodoroiu")

print("\nThere is nobody left on this list.")
for person in famous_people:
    print(person)

# Slicing: from beginning, middle and end.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[:3])
print(letters[3:6])
print(letters[7:])

# Protecting a list: copy list, add new items in the new one, print original and copy.
protect_me = ["John", "Mary", "Steve"]
duplicate_of_protect = protect_me[:]
duplicate_of_protect.append("Lana")
duplicate_of_protect.append("Mike")
print("\nThis is protect_me list:")
for name in protect_me:
    print(name)

print("\nThis is duplicate of protect_me list:")
for name in duplicate_of_protect:
    print(name)
print("\n")

# Numerical lists: create list using range.
first_twenty = list(range(1, 21))
print(first_twenty)

# Large set of numbers: create large list, see how it prints until last item.
large_set = list(range(1, 1231231))
# print(large_set)

# Min, max, sum: concatenate with string.
five_wallets = [12, 5, 8, 13, 9]
print("\nThe fattest wallet has $" + str(max(five_wallets)) + " in it.")
print("The fattest wallet has $" + str(min(five_wallets)) + " in it.")
print("All together, these wallets have $" + str(sum(five_wallets)) + " in them.\n")

# List comprehensions.
# Create list of the first 10 multiples.
multiples_of_ten = [number*10 for number in range(1, 11)]
print(multiples_of_ten)

# Create list of the first 10 cubes.
first_ten_cubes = [number**3 for number in range(1, 11)]
print(first_ten_cubes)
print("\n")

# List comprehension, capitalize, concatenate string.
five_names = ["robin", "agatha", "rechinul", "loredana", "florentina"]
five_names_awesome = [name.title() + " is awesome!" for name in five_names]
print(five_names_awesome)
print("\n")

# For loop: add constant number to all items of a list.
plus_thirteen = []
for number in range(1, 11):
    plus_thirteen.append(number+13)
print(plus_thirteen)
print("\n")

# Strings.
# Print each character of a string on a new line.
sentence_1 = "I like programming in Python."
for char in sentence_1:
    print(char)

# Create list of each separate character of a string.
list_from_sentence_1 = list(sentence_1)
print(list_from_sentence_1)

# Slice the list: beginning, middle, end.
print(list_from_sentence_1[:5])
print(list_from_sentence_1[12:17])
print(list_from_sentence_1[-5:])
print("\n")

# Search index of all occurences of "Python", then count occurences.
sentence_2 = "Let's use Python once, and then use Python again."
print("Python" in sentence_2)
print(sentence_2.find("Python"))
print(sentence_2.rfind("Python"))
print(sentence_2.count("Python"))
print("\n")

# Split sentence into words, store as a list.
list_from_sentence_2 = sentence_2.split(" ")

# Print list containing items.
print(list_from_sentence_2)

# Print each item in the list.
for word in list_from_sentence_2:
    print(word)

# Replace one item with another.
sentence_2 = sentence_2.replace("Python", "Ruby")
print(sentence_2)
print("\n")

# Counting DNA nucleotids: how many from each.
string_1 = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
count_A_nucleotid = string_1.count("A")
count_C_nucleotid = string_1.count("C")
count_G_nucleotid = string_1.count("G")
count_T_nucleotid = string_1.count("T")
print(count_A_nucleotid, count_C_nucleotid, count_G_nucleotid, count_T_nucleotid)
print("\n")

# Transcribing DNA into RNA: replace thiamine with uracil.
string_2 = "GATGGAACTTGACTACGTAAATT"
string_3 = string_2.replace("T", "U")
print(string_3)
print("GAUGGAACUUGACUACGUAAAUU" in string_3)
print("\n")

# Complementing a strand of DNA, UNFINISHED
string_4 = "AAAACCCGGT"
list_2 = list(string_4)
list_3 = list_2[:]
list_3.reverse()
list_4 = []
print(list_2)
print(list_3)
print(list_4)

# Tuples
# Create tuple and use placeholders when printing.
scores = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("\nThe lowest possible score is %d, and the highest possible score is %d.\n" % (min(scores), max(scores)))

# Use placeholders in a for loop.
for score in scores[0:1]:
    print("A judge can give a gymnast %d point." % score)

for score in scores[1:]:
    print("A judge can give a gymnast %d points." % score)

# Use index of list and placeholders.
print("\nThe first carrer I have thought of is %s." % careers_2[0])
print("The last carrer I have thought of is %s." % careers_2[-1])

# List of important words I have learned in the first 2 chapters and their definition.
important_words = ["list", "tuple", "string", "loop", "placeholder", "variable"]
list_definition = "A sequence of elements that can be rearranged, replaced, removed or added to."
tuple_definition = "An immutable sequence of elements."
string = "A sequence of characters that can be searched, split, accessed and transformed into a list."
loop_definition = "A block of code that keeps running until the list of variables is exhausted or until a condition is met."
placeholder_definition = "A convention written as %d or %s that uses the first element after the string for filling, under the condition that % sign appears between string and above-mentioned first element."
variable_definition = "A sequence of lowercase letters, numbers, underscores, or a combination of them to store an object."