# Chapter 7: Dictionaries

# Loop through a dictionary with at least 3 key-value pairs.
pet_names_1 = {"agatha": "cat", "rechinul": "cat", "cocutza": "cat", "mowgli": "dog"}

for name, animal in pet_names_1.items():
    print("%s is a %s." % (name.title(), animal))
print("\n")

# Loop through a dictionary where value is a long string.
polling_friends = {"mary" : "Wolves are beautiful animals.",
                   "john": "Lynxes are beautiful animals.",
                   "edith": "Squirrels are beautiful animals."
                   }

for name, animal in polling_friends.items():
    print("%s has recently said: %s" % (name.title(), animal))
print("\n")

# Change value of a key.
pet_names_2 = {"agatha": "cat", "rechinul": "cat", "cocutza": "cat", "mowgli": "dog"}

pet_names_2["rechinul"] = "tuxedo cat"

for name, animal in pet_names_2.items():
    print("%s is a %s." % (name.title(), animal))
print("\n")

# Add a new key-value pair.
pet_names_2["Fanica"] = "dog"

for name, animal in pet_names_2.items():
    print("%s is a %s." % (name.title(), animal))
print("\n")

# Remove key-value pair.
del pet_names_2["mowgli"]

for name, animal in pet_names_2.items():
    print("%s is a %s." % (name.title(), animal))
print("\n")

# Create function for looping and printing
def name_animal(my_dict):
    """Loop through dictionary."""
    for name, animal, in my_dict.items():
        print("%s is a %s." % (name.title(), animal))

name_animal(pet_names_2)

# Mountain Heights
mountain_heights_1 = {"moldoveanu": 2544, 
                      "negoiu": 2535, 
                      "vistea mare": 2527, 
                      "parangu mare": 2519, 
                      "peleaga": 2509 
                      }

# Loop through keys and print them.
print("\nHere are the tallest mountains in Romania:")

for peak in mountain_heights_1.keys():
    print(peak.title())

# Loop through values and print them.
print("\nHere are the heights of the tallest mountains in Romania:")

for height in mountain_heights_1.values():
    print(height)

# Print statements about peaks and heights.
print("\nHere are the names and heights of the tallest mountains in Romania:")

for peak, height in mountain_heights_1.items():
    print("%s is %d meters tall." % (peak.title(), height))

# Print statements about alphabetically sorted peaks and their heights.
mountain_heights_2 = {"moldoveanu": 2544, 
                      "negoiu": 2535, 
                      "vistea mare": 2527, 
                      "parangu mare": 2519, 
                      "peleaga": 2509 
                      }
print("\nAlphabetically sorted peaks and heights of the tallest mountains in Romania:")
for peak in sorted(mountain_heights_2.keys()):
    print("%s is %d meters tall." % (peak.title(), mountain_heights_2[peak]))

# List in dictionary
# Loop through keys and list of values in meters and feet. Print them one by one.
mountain_heights_3 = {"moldoveanu": [2544, 8346], 
                      "negoiu": [2535, 8317], 
                      "vistea mare": [2527, 8291], 
                      "parangu mare": [2519, 8264], 
                      "peleaga": [2509, 8232] 
                      }

print("\nHere are the tallest mountains in Romania:")
for peak in mountain_heights_3.keys():
    print(peak.title())

print("\nHere are the heights in meters of the tallest mountains in Romania:")
for peak, height in mountain_heights_3.items():
    print(height[0])

print("\nHere are the heights in feet of the tallest mountains in Romania:")
for peak, height in mountain_heights_3.items():
    print(height[1])

# Print statements about peaks and heights.
print("\nHere are the names and heights in meters and feet of the tallest mountains in Romania:")
for peak, height in mountain_heights_3.items():
    print("%s is %d meters tall, or %d feet." % (peak.title(), height[0], height[1]))

# Function to transform meters in feet, store in list, use it to create dictionary.
def meters_to_feet(my_dict):
    """Transform meters in feet, store in list, use it to create dictionary."""
    for key, value_meters in my_dict.items():
        value_feet = round(value_meters * 3.28084)
        my_dict[key] = [value_meters, value_feet]

meters_to_feet(mountain_heights_1)

mountain_heights_4 = {"moldoveanu": {"height": 2544, "range": "fagaras, carpathians"},
                      "negoiu": {"height": 2535, "range": "fagaras, carpathians"}, 
                      "vistea mare": {"height": 2527, "range": "fagaras, carpathians"}, 
                      "parangu mare": {"height": 2519, "range": "parang, carpathians"}, 
                      "peleaga": {"height": 2509, "range": "retezat, carpathians"}
                      }

print("\nThe tallest peaks in Romania are:")
for peak in mountain_heights_4.keys():
    print(peak.title())

print("\nThe highest elevations in Romania are:")
for peak, details in mountain_heights_4.items():
    for key in details:
        if key == "height":
            print(details[key])

print("\nThe highest peaks in Romania belong to the following mountains:")
for peak, details in mountain_heights_4.items():
    for key in details:
        if key == "range":
            print(details[key].title())

# Function for looping through a dictionary of dictionaries.
def mountain_statement(my_dict):
    """Loop through a dictionary of dictionaries."""
    for peak, details in my_dict.items():
        for key in details:
            if key == "height":
               my_height = details[key]
            elif key == "range":
                my_range = details[key]
                print("%s is a %d-meter tall mountain in the %s range." % (peak.title(), my_height, my_range.title()))

print("\nStatements about various peaks:\n")
print(mountain_statement(mountain_heights_4))