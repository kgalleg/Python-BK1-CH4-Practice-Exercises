#Practice Dictionary of Words

# You are going to build a Python Dictionary to represent an actual dictionary. Each key/value pair within the Dictionary will contain a single word as the key, and a definition as the value. Below is some starter code. You need to add a few more words and definitions to the dictionary.

# After you have added them, use square bracket notation to output the definition of two of the words to the console.

# Lastly, use the for in loop to iterate over the KeyValuePairs and display the entire dictionary to the console.

# """
# Create a dictionary with key value pairs to
# represent words (key) and its definition (value)
# """
word_definitions = dict()

# """
# Add several more words and their definitions
#    Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
# """

word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Tree"] = "a woody perennial plant"
word_definitions["Python"] = "a large heavy-bodied nonvenomous snake"
word_definitions["JavaScript"]= "an object-oriented computer programming language commonly used to create interactive effects within web browsers."
word_definitions["Dog"] = "an animal that is super  cute and cuddly"

#can also do it like this:
# word_definitions = {
#     "Awesome":"The feeling of students when they are learning",
#     "Tree": "a woody perennial plant"
# }


# """
# Use square bracket lookup to get the definition of two
# words and output them to the console with `print()`
# """

print(f"Dog - {word_definitions ['Dog']}")
print(f"JavaScript - {word_definitions ['Dog']}")

#printing just the definition
print(word_definitions ['Dog'])



# print(f"Hello, my name is {my_pairs['name']}")




# """
# Loop over the dictionary to get the following output:
#     The definition of [WORD] is [DEFINITION]
#     The definition of [WORD] is [DEFINITION]
#     The definition of [WORD] is [DEFINITION]
#

# print(f"The difinition of - {word_definitions ['Word']}")


for (key, value) in word_definitions.items():
     print(f"The definition of {key} is: {value}")