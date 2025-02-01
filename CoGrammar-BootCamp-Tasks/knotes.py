# Strings, Lists & Dictionaries with Flowcharts Witten by Gower Campbell

# ()      | Start/End    | Represents the beginning or end  
# ->      | Arrows       | An Action or Calculation  
# /   /   | Input/Output | Input & Output Operations  
# [   ]   | Process      | Represents a Condition for outcomes  
# ↵<>↴    | Decision     | Boolean (Yes or No) (True or False)  

#         (Start)  
#            ↓  
#    /  Enter the width /  
#            ↓  
#    /  Enter the height /  
#            ↓  
#   ↓  < Width equals height >    ↴  
# [      ]                     [       ]  

#          (Start)  
#            ↓  
#    /  Enter the username /  
#            ↓  
#    /  Enter the password /  
#            ↓  
#   ↓  < Username & Password Match >    ↴  
# [   No   ]                        [   Yes    ]  
#   Repeat                         Access Granted  
# Forever Loop                            ↓  
#                                  [View Profile]  
#                                         ↓  
#                                       (End)  

# Data Structures  
# Organized structure to keep our digital world running smoothly  
# Definition:  
# Organized ways to store & manage data efficiently.  

# Why are they important?  
# Access, organize, and modify information easily.  
# Problem-solving  

# Key Data Structures  
# [Arrays]   |     [List]  

# Lists or Arrays  
# Uses an "Index" to access an element by its position.  
# Index (programming) the first one is "0", the first one  
# not "1"...  

# Arrays are contiguous (no space/lookup power)  

# Key Data Structures  
# [Dictionaries]  
# (Key) which is the label  
# (Value) is what the key is paired to  
# For example: Gower (key) and my phone number (value).  

# LookUp Hashmaps  
# Much like an actual dictionary  
# pol-i-ti-cian  
# political science  
# and so on... looking up common words  

# Key Data Structures: Stacks  
# Most Recent...  
# A pile of items where you can add or remove things from the top.  
# It follows Last In, First Out (LIFO) - the last thing you add is the first  
# thing you take out.  
# Imagine a vending machine or the contact -> mom -> back -> contact  
# Working with one element that is put in  

# Key Data Structures: Queues  
# Follows the First In, First Out (FIFO) principle.  
# Example: Printing going from each document sent.  

# List, Dictionary, Stack, or Queue.  

# Online flowchart tools  
# draw.io  
# lucidchart  

# Immutable (Can Never Change)  

# Strings are sequences of characters that are enclosed within single and  
# double quotes. Common operations we perform on strings are concatenation,  
# slicing, and formatting.  

# Mutable (Can Change)  
# Lists are mutable, ordered collections of items (any type).  
# Lists allow indexing, slicing, appending, and more.  
# Disconnects, hooks, and work with addresses  

# Dictionaries are collections of key-value pairs, where each key maps  
# to a value. Dictionaries are unordered and are accessed using keys, not indices.  

# Unordered and are accessed using keys. Only difference "name of the key"  
# in the string.  

# Useful Methods  

# String Methods: split(), join(), and replace()  
# List Methods: append(), pop(), sort()  
# Dictionary Methods: get(), keys(), values()  

# String Handling  
# (To create more advanced programs using various functions)  
# Including indexing strings, string methods, and escape characters.  
# String building lists (nested lists and list comprehension)  
# Concrete understanding of dictionaries (Hash Maps)  

# STRING INDEX  

# H e l l o   w o r l d  !  
# 0 1 2 3 4 5 6 7 8 9 10 11  

string = "Hello"  
print(string[0]) # H  
print(string[1]) # e  
print(string[2]) # l  
print(string[3]) # l  
print(string[4]) # o  

# Remember: specify an index you'll get the character at that position in  
# the string. You can also slice strings by specifying a range from one index  
# to another, remember that the character at the starting index is included  
# and the character at the ending is not.  

# Note that slicing a string does not modify the original string.  
# You only capture a slice from one variable in a separate variable.  

# Pseudocode is a planning tool for algorithms; hold release data  
# Data structure for organizing and managing data efficiently.  
# Store, manipulate, and manage a particular problem  
# Problem-solving techniques involve breaking problems into manageable steps  
# and designing structured solutions.  

original_string = "Hello world!"  
new_string = original_string[0:5]  
print(new_string) # prints 'Hello'  

# By slicing and storing the resulting substring in another variable,  
# you can have both the whole string and the substring handy for quick, easy  
# access.  

# String Methods  
# Built-in modules of code that perform certain operations on string methods.  
# (where s is the variable that contains the string) implemented  
# using "dot notation."  

# DOT Notation (access methods (functions)) are used with a string object.  
# s.lower() - converts all characters in the string s to lowercase  
# s.upper() - converts all characters in the string s to uppercase  
# s.strip() - removes any whitespace from the beginning and end of the string  
            # stored within s  
# s.strip('chars') - removes any characters present in the string chars from  
#                  both the beginning and the end of the string s. e.g.  
#                  s.strip(',') removes all leading and trailing commas  
# s.find('text') - searches for the substring 'text' in the string s and  
#                  returns the index of the first occurrence. If the  
#                  substring is not found, it returns -1.  
# s.replace('old_text', 'new_text') - Replaces all occurrences of old_text  
#                  with new_text.  
# s.split('word') - breaks down a string into a list of smaller pieces. The  
                #  string is based on what is called a delimiter. This is a  
                #  string or value that is passed to the method. If no value  
                #  is given, it will auto-split the string using whitespace as  
                # the delimiter and create a list of the characters.  
# delimiter.join(string_list) - Takes a list of strings or characters (string_list)  
                #   and joins them to create one string, with the delimiter  
                #  inserted between each element.  
                # For example,  
                "@".join(["apples", "bananas", "carrots"]) # would output  
#               apples@bananas@carrots.  

# Escape character  
# Python uses the backslash (\\) as an escape character.  
# Telling the compiler/interpreter that the next character has a special meaning  

# \\n - newline  
# \\t - tab  

# This can help include quotation marks within a string  
print("hello \\n\\"bob\\"")  
# Output:  
# Hello  
# "bob"  

# You can also put a backslash in front of another backslash to include a  
# backslash in a string.  

print("The escape sequence \\\\n creates a new line in a print statement")  
# Output: The escape sequence \\n creates a new line in a print statement  

# The F-String: Including variables in strings  
# Insert values using empty placeholders:  

num_days = 22  
pay_per_day = 50  
print(  
        "You worked {} this month and earned £{} per day".format(  
                num_days, pay_per_day)  
)  

# Insert values using index references  

num_days = 22  
pay_per_day = 50  
print(  
        "You worked {0} this month and earned £{1} per day".format(  
                num_days, pay_per_day)  
)  

# Insert values directly into the string using an f-string  

num_days = 22  
pay_per_day = 50  
print(f"You worked {num_days} this month and earned £{pay_per_day} per day")  

# Output: I worked 28 days this month. I earned $50 per day.  

# Key Word Interpolating (inserting) values inside string literals  

# String Building  
# Form of concatenation (merging strings together) to build a string.  
# Writing a program is to manipulate information.  
# Turning data into a format that can be used to provide information  
# or complete a task. When we send data from the back end to the front end.  

number_builder = ""  
i = 0  
while i <= 50:  
        if i % 2 == 0:  
                number_builder += str(i) + " "  
                i += 1  
                print(number_builder)  

# The 'i' gets cast as a string and added to the number_builder string  
# (which starts off empty) until i is greater than 50.  

# Another way is with the .join() method you've just learned about  
# Takes a list and joins the elements together to make a string.  

number_builder = [] # Note the variable has to be a list rather than a string  
i = 0  

while i <= 50:  
        if i % 2 == 0:  
                number_builder.append(str(i))  
                i += 1  
                print(" ".join(number_builder))  

# For each iteration of the loop, an even number gets appended to the list.  
# Finally, all the elements are joined together with a space in between.  
# You may not have noticed that i is cast to a string before appended.  
# You cannot make an integer act like a string without casting it; only strings  
# and characters can be joined together.  

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50  

# A Look at Lists  
# Have indexes that you can use to call, change, add, or delete elements.  

# Creating a list:  
string_list = ["John", "Mary", "Harry"]  
# print(string_list[0])  

# Indexing a list:  
pet_list = ["cat", "dog", "hamster", "goldfish", "parrot"]  
print(pet_list[0])  

# Slicing a List:  
num_list = [1, 4, 2, 7, 5, 9, 10]  
print(num_list[1:2])  
# Output: 4  

# Changing an element in a list:  
name_list = ["James", "Molly", "Chris", "Peter", "Kim"]  
name_list[2] = "Tom"  
print(name_list)  
# Output: ['James', 'Molly', 'Tom', 'Peter', 'Kim']  

# Adding an element to a list:  
new_list = [35, 34, 37, "coffee", 98.8]  
new_list.append("Tea")  
print(new_list)  
# Output: [35, 34, 37, 'coffee', 98.8, 'Tea']  

# Deleting an element in a list:  
char_list = ["p", "y", "t", "h", "o", "n"]  
del char_list[3]  
print(char_list)  
# Output: ['p', 'y', 't', 'o', 'n']  

# Python List Methods  

# append() - adds a new element to the end of the list.  
# extend() - adds all elements of a list to another list.  
# insert() - inserts an item at the defined index.  
# remove() - removes an item from the list.  
# pop() - removes and returns an element at a given index.  
# count() - returns the count of the first matched items.  
# index() - returns the index of the first matched item.  
# sort() - sorts items in a list in ascending order.  
# reverse() - reverses the order of items in the list.  

# Nested Lists  
# Lists can include other lists as elements. These inner lists are called  
# nested lists.  

a = [1, 2, 3]  
b = [4, 9, 8]  
c = [a, b, "tea", 16]  
print(c) # prints [[1, 2, 3], [4, 9, 8], 'tea', 16]  
c.remove(b)  
print(c) # prints [[1, 2, 3], 'tea', 16]  

# Copying Lists  
# One approach is using the slice operator [:]  
# Duplicates without specifying the start or end indexes.  

a = [1, 2, 3]  
b = a[:] # 'b' will contain a copy of the list stored within 'a'  
b[1] = 10  
print(a) # Prints [1, 2, 3]  
print(b) # Prints [1, 10, 3]  

# [:] only copies the outer list.  
# Any sublist creates a shallow copy of the original list.  

a = [4, 5, 6]  
b = a  
a[0] = 10  

# prints [10, 5, 6] showing b reflects a's current state.  
print(b)  

# Using the Copy Module  
# copy() method ensures that if you modify the copied list (list b)  
# the original list remains the same.  
# However, if list a contains other lists as items, those inner lists  
# can still be modified if the corresponding inner lists in b are modified.  
# The copy module contains a function called deepcopy().  

import copy  
a = [[1, 2, 3], [4, 5, 6]]  
b = a.copy() # Creates a shallow copy of 'a'  
c = copy.deepcopy(a) # Creates a deep copy of 'a'  

b[0][1] = 10 # Changes position [0][1] in both 'b' and 'a'  
c[1][1] = 12 # Changes [1][1] only in 'c'  

print(a) # Prints [[1, 10, 3], [4, 5, 6]]  
print(b) # Prints [[1, 10, 3], [4, 5, 6]]  
print(c) # Prints [[1, 2, 3], [4, 12, 6]]  

# Using a slice operator, the copy() method, or the copy module.  

# List Comprehension  
# Apply an operation to every element in a list  
# Expression followed by a 'for' statement inside [square brackets]  

num_list = ['1', '5', '8', '14', '25', '31']  
new_num_list_ints = [int(element) for element in num_list]  
print(new_num_list_ints) # Prints [1, 5, 8, 14, 25, 31]  

# For each element in num_list, we are casting them as an integer and putting  
# it in a new list called new_num_list_int.  

num_list = ['1', '5', '8', '14', '25', '31']  
new_num_list_ints = [int(element) * 2 for element in num_list]  
print(new_num_list_ints) # Prints [2, 10, 16, 28, 50, 62]  

# Lists  
# An ordered collection of elements in a contiguous manner  

# Key Features  
# Indexing: direct access to the elements using indices (e.g., 'arr[0]')  
# Contiguity: stored in 'adjacent memory', enabling fast access.  
# Efficiency: Best for scenarios needing 'frequent reads' or updates at  
# specific indices  

# Use Case: Suitable for applications requiring sequential data storage and  
# indexed access  

list_items = ['a', "cat", 0, "dog", 'No', 'Yes', 2, 3, 4] # Values  
# Imagine a grid assigning to the column numbers  
# |    |       |      |       |      |     |       |  
#  0 1 2 3 4 5 6 7 8 index  
# Scalability? There are performance issues when everything scales up  

# Dictionaries/Hashmaps (Two Keys?)  
# Unordered Collections of key-value pairs.  
# Accessed via keys rather than index positions.  

# Create a dictionary  
# Inside curly braces ({}) and separate them with commas (,)  
# (key: value) The Key must be immutable (not changeable)  
# This includes data types like strings, numbers, and tuples  

int_key_dict = {  
        1: "apple",  
        2: "banana",  
        3: "orange"  
}  

# Using a dict() function  

int_key_list = [(1, 'apple'), (2, 'banana'), (3, 'orange')]  
# Creating three tuples then makes it a dictionary with three entries  
int_key_dict = dict(int_key_list)  

# The first element of the list at int_key_list[0], containing (1, 'apple')  
# This data type called a tuple, it is immutable and it is ordered.  

# Tuples Often called pattern matching. You assign values to certain variables  

my_tuple = (1, "apple")  
key, value = my_tuple  
print(key) # Prints 1  
print(value) # Prints apple  

# The tuple must contain two values  

# Access elements from a dictionary  
# You can access them through keys inside [brackets]  
# With indices in a list, or with the get() method  

profile_dict = {  
        "name": "Chris",  
        "surname": "Smith",  
        "age": 28,  
        "cell": "07714935387"  
}  

print(profile_dict["surname"]) # Prints 'Smith'  
print(profile_dict.get("cell")) # Prints 'Phone
print(profile_dict["surname"])  # Prints 'Smith'
print(profile_dict.get("cell"))  # Prints 'Phone number'

# You can also retrieve all the keys and values using .keys() or .values()
keys = profile_dict.keys()
values = profile_dict.values()
print(keys)
print(values)
# Output
# dict_keys(['name', 'surname', 'age', 'cell'])
# dict_values(['Chris', 'Smith', 28, '083 233 3242'])

# Change elements in a dictionary
# Add new items or change using assignment operator (=)
# If the key is present, the value gets updated. If no key, a new key-value pair is added.

# Create a dictionary
my_dict = {'apple': 1, 'banana': 2}

# Update the value for an existing key
my_dict['apple'] = 3

# Add a new key-value pair
my_dict['cherry'] = 5

print(my_dict)

# Output
# {'apple': 3, 'banana': 2, 'cherry': 5}

# Dictionary Membership test.
# Using the keyword 'in' and lastly the name of the dictionary
# Returns either True or False

doubles = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
print(1 in doubles)  # Prints out True

lecturers = {
    "Armand": {"Role": "Lecturer", "Phone Number": "0123456789"},
    # Key       Key     Value          Key              Value
    "Rian": {"Role": "Lecturer", "Phone Number": "0123456789"},
    "Julian": {"Role": "Lecturer", "Phone Number": "0123456789"}
}

# STACKS
# A data structure following the 'Last in, First out' (LIFO) principle
# Key Features
# Push: Adds an element to the top
# Pop: Removes the top element
# Peek: Retrieves the top element without removing it.

# Access: Restricted to the top element only.
# Efficiency: Operations are quick for both push & pop.

# QUEUES
# A data structure following the First In, First Out (FIFO) principles
# where the first element added is the first to be removed.
# Key Features
# Operations
# Enqueue: Adds an element to the rear.
# Dequeue: Removes the front element.
# Peek: Retrieves the front element without removing it.
# Access: Restricted to the front and rear elements.
# Efficiency: Operations are quick for both enqueue and dequeue.

# Insertions
# Purpose: Adding new elements to the data structure
# arrays:
arr.append(6)
# stacks:
stack.push(5)
# queues:
queue.enqueue(3)

# Deletions
# Purpose: Removing elements from the data structure
# arrays:
arr.remove(6)
# stacks:
stack.pop(5)
# queues:
queue.dequeue(3)

# Crash resolutions ()

# Update

# Arrays:
arr[2] = 10
# Dictionaries
dict['key'] = 'new_value'

# Pseudocode: Simple language using terms like IF, WHILE, and FOR
# Focus on flow to prioritize the logical steps

# Finding the largest number in a list

# Key Steps
# 1. Initialize the max variable
# 2. Iterate through the list
# 3. Update max when a larger number is found
# 4. Print the largest number

# SET max = first number in list
# FOR each number in list
#   IF number > max THEN
#    SET max = number
# END FOR
# PRINT max

# SET list_items = set of numbers
# SET min = first number in list
# FOR each number in list
# IF number < num THEN
# SET MIN = number_builder
# END FOR
# PRINT min

# SET list_items = set of numbers
# SET total = 0
# FOR each number IN list_items
# SET total = total + number
# END FOR
# PRINT total

# Reverse a List
[100, 2, -50] = [-50, 2, 100]

# SET reversed_list = []
# FOR i FROM length of list - 1
# DOWN TO 0
# APPEND list[i] to reversed_list
# END FOR
# PRINT reversed_list

num_list = ['1', '5', '8', '14', '25', '31']
new_num_lists_ints = [int(element) * 2 for element in num_list]

print(new_num_lists_ints)
