# Chapter 1: Variables, Strings, Numbers

# Define a variable, then update its content.
hello1 = "Hello World!"
print(hello1)
hello2 = "Hello World! ver 2"
print(hello2)

# Use tabs and newlines.
hello3 = "This is a \ttab"
hello4 = "This is a \nnewline"
print(hello3)
print(hello4)

# Quote
someone_said = "This is a quote."
print(someone_said)

# Master of my computer: combine and capitalize first and last name.
first_name = "alina"
print(first_name, first_name.title(), first_name.upper())
last_name = "molnar"
full_name=first_name.title() + " " + last_name.title()
print(full_name)

# The person I look up to: combine and capitalize first and last name.
look_up_first_name = "greta"
look_up_last_name = "thunberg"
sentence="I love the new generation of climate activists and " + look_up_first_name.title() + " "+look_up_last_name.title() + " is one of them."
print(sentence)

# Strip whitespace, add dash to see the original better.
first_name_whitespace = " alina "
print(first_name_whitespace)
print("-" + first_name_whitespace + "-")
print("-" + first_name_whitespace.lstrip() + "-")
print("-" + first_name_whitespace.rstrip() + "-")
print("-" + first_name_whitespace.strip() + "-")

# Basic arithmetics: perform simple calculations.
addition = 2+3
subtraction = 2-3
multiplication = 2*3
division = 2/3
exponents = 2**3
print(addition, subtraction, multiplication, division, exponents)
print("The results of the calculation 2+3 is " + str(addition) + ".")
print("The results of the calculation 2-3 is " + str(subtraction) + ".")
print("The results of the calculation 2*3 is " + str(multiplication) + ".")
print("The results of the calculation 2/3 is " + str(division) + ".")
print("The results of the calculation 2**3 is " + str(exponents) + ".")

# Order of operations: use standard order of operations.
standard_order = 2-3*5
print(standard_order)
print("The results of the calculation 2-3*5 is " + str(standard_order))

# Change order of operations: use paranthesis to change the order.
my_order = (2-3)*5
print(my_order)
print("The results of the calculation (2-3)*5 is " + str(my_order) + " because I have modified the order of operations.")

# Test long digits: find out which result in long digits.
print(0.05+0.1)
print(0.1+0.2)
print(0.2+0.4)
print(0.3+0.6)
print(0.4+0.8)
print(0.5+1.0)
print(0.6+1.2)
print(1.2+2.4)
print(1+2)
print(6/3)