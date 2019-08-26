# https://github.com/nashville-software-school/bangazon-llc/blob/master/book-1-orientation/chapters/DATA_STRUCTURES_DICTIONARY.md

# Create an empty dictionary
animal = dict()

# Add key/value pairs
animal["name"] = "Kevin"
animal["breed"] = "Bulldog"
animal["age"] = 5

# Create the dictionary with k/v pairs and assign to variable
animal = {
    "name": "Kevin",
    "breed": "Bulldog",
    "age": 5
}

# Dictionaries are iterable.

for (key, value) in animal.items():
    print(f"{key}: {value}")

# Output Below

# name: Kevin
# breed: Bulldog
# age: 5


