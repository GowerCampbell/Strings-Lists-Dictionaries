
# Objective: Demonstrate my understanding of string manipulation, loops, 
# and conditional logic. This exercise involves using loops and 
# conditional statements to modify a string by applying alternating patterns.

# Apply practical string manipulation techniques:

print("\n ------------ Step 1 ------------")
print('''Transform each alternate character to 
uppercase and the others to lowercase.''')

# Input string
hello_world = " \n Hello World \n"

# Create an empty string to store the result
modified_string = ""

# Number each character in the string with its iteration
for index, character in enumerate(hello_world):
    if index % 2 == 0:
        # Uppercase for even positions
        modified_string += character.upper()
    else:
        # Lowercase for odd positions
        modified_string += character.lower()

# Output the modified string
print(modified_string)

# "Hello World" would become "HeLlO WoRlD"

print("------------ Step 2 ------------")
print('''Reapply the logic by making each alternative word
lowercase and uppercase.\n''')

code_sentence = "\n I am learning to code \n"

# .strip() removes leading/trailing whitespace
# .split() breaks the sentence into a list of individual words
words = code_sentence.strip().split(" ")

# An empty list where the processed words will be stored
modified_sentence = []

# Like before, we index each word e.g. 0, word = "I" & 1, word = "am"
for index, word in enumerate(words):  # Renamed loop variable to 'word'
    if index % 2 == 0:  # Setting the condition for every even/odd number
        modified_sentence.append(word.lower())
    else:
        modified_sentence.append(word.upper())

# " ".join(modified_sentence) combines the processed words 
# in modified_sentence into a single string, separated by spaces
alternative_word = " ".join(modified_sentence)  # (GeeksforGeeks, 2024)

print(f"\nResult: {alternative_word} \n")

# The string "I am learning to code" would become "i AM learning TO code"
# Using split() and join() functions helps with this transformation

# In this exercise, I learned how to change the letters in a string by using 
# loops and rules. I used upper() and lower() to make letters 
# alternate between uppercase and lowercase. I also used split() 
# to break a sentence into words and join() to put them back together 
# after changing them.

# Basically, I learned how to work with strings by looking at each letter 
# or word and changing it based on its position. It was a good way to 
# practice how to modify text using simple rules. This will help me keep 
# getting better at coding.

# GeeksforGeeks. (2024). Python program to split and join a string. 
# GeeksforGeeks. Available at: 
# https://www.geeksforgeeks.org/python-program-split-join-string/ 
# [Accessed 11 Dec. 2024].
