# Chapter 5: While Loops and Input

# Growing strength: increases strength until 10, then moves up one level.
strength = 5
print("Your strength is %d." %strength)

while strength < 10:
    print("Your current strength is %d." % strength)
    strength = strength + 2

print("You got too strong, so you move up one level.")

# Game preferences: append list of games with input from users.
games = ["x-box adventures", "catan settlers", "fazan", "mahjong"]
print("\nThese are the games I like:")
for game in games:
    print(game)

new_game = ""
while new_game != "quit":
    new_game = input("Please tell me what game you like: ")
    if new_game != "quit":
        games.append(new_game)

print("\nThese are the games we like:")
for game in games:
    print(game)

# Gaussian Addition: add numbers in a range, pop pairs of fist and last number.
partial_sums = []
def gauss_addition(range_list):
    """Add both ends of range, store them as partial sums, then multiply their number by their value."""
    # Calculate sum of first and last items, stop at 1 if length of range is an odd number.
    while len(range_list) > 1:
        partial_sum = list(range_list).pop(0) + list(range_list).pop(-1)
        print("Currently adding %d and %d, and their sum is %d." % (range_list.pop(0), range_list.pop(-1), partial_sum))
        # Keep track of all partial sums.
        partial_sums.append(partial_sum)
        print("There were %d sums until now." % len(partial_sums))
        result = partial_sum * len(partial_sums)
    # If length of range is an odd number, add item from middle of original list to result.
    while len(range_list) == 1:
        last_item = range_list.pop()
        result = result + last_item
    print("The final result is %d." % result)
    
gauss_addition(list(range(1,101)))

deserts = ["papanasi", "ana lugojana pancakes", "walnut cozonac", "dobrudja pie", "sour cherry cake"]