# Chapter 8: Functions

# Games - Function with one default argument.
def favorite_game(name="catan settlers"):
    """Print statement about a game."""
    print("I like playing %s!" % name.title())

print(favorite_game("mahjong"))
print(favorite_game("x-box adventures"))
print(favorite_game())
print("\n")

# Favorite movie - Function with one default argument.
def favorite_movie(name="de ce eu?"):
    """Print statement about a movie."""
    print("My favorite movie is %s." % name.title())

print(favorite_movie("usturoi"))
print(favorite_movie("ghost in the shell"))
print(favorite_movie())
print("\n")

# Favorite color - Function with two positional arguments.
def favorite_color(name, color):
    """Print statement about a person's favorite color."""
    print("%s's favorite color is %s." % (name.title(), color))

print(favorite_color("mary", "blue"))
print(favorite_color("john", "pink"))
print(favorite_color("ann", "red"))
print("\n")

# Phone brand - Function with two positional arguments.
def phone_name(brand, model):
    """Print phone brand and model."""
    print("%s %s" % (brand.title(), model.title()))
print(phone_name("siemens", "a50"))
print(phone_name("motorola", "w230"))
print(phone_name("nokia", "3310"))
print("\n")

# Sports teams - Fuction with mixed positional and keyword arguments.
def sports_teams(city, team=None):
    """Print city and sports team."""
    print("City: %s" % city)
    if team:
        print("Team: %s" % team)

print(sports_teams("Glasgow"))
print(sports_teams("Glasgow", team="Rangers"))
print(sports_teams("Sevilla", team="Real Betis Balompie"))
print("\n")

# World languages - Fuction with mixed positional and keyword arguments.
def world_languages_1(country, language=None):
    """Print country and language."""
    print("Country: %s" % country)
    if language:
        print("Language: %s" % language)

print(world_languages_1("USA", language="English"))
print(world_languages_1("Portugal"))
print(world_languages_1("Croatia", language="Croatian"))
print("\n")

# Worls languages - Fuction with mixed positional and arbitrary number of keyword arguments.
def world_languages_2(country, major_language, **other_languages):
    """Print country and languages."""
    print("Country: %s" % country.title())
    print("Major Language: %s" % major_language.title())
    for lang in other_languages:
        print("%s: %s" % (lang.title().replace("_", " "), other_languages[lang].title()))

print(world_languages_2("u.s.a.", "english", other_language_1="mandan", other_language_2="sioux"))