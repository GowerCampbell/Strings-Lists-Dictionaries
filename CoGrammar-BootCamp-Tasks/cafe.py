# Cafe.py written by Gower Campbell.

# Objective: Use lists, dictionaries, and loops to create and manage 
# data structures that represent items in a café menu. Implement loops 
# to iterate through the data structures and perform necessary operations, 
# such as calculating total values and manipulating stock and pricing 
# information.


# Imagine you're managing a café. 
# Start by creating a list called 'menu' that includes at least four 
# items sold in your café.

"--------- Step 1 -----------"
''' Create a list called 'menu' with at least 4 items 
sold in the cafe'''

menu = [
    "Turkey Toastie", # (Greene King, 2024)
    "Maple Glazed Pigs in Blanket",
    "Crispy Camembert Dumplings",
    "Festive Burger"
]

"--------- Step 2  -----------"
'''Create a dictionary called 'stock' that 
contains the stock value for each item'''

stock = {
    "Turkey Toastie": 100,  # 100 units in stock
    "Maple Glazed Pigs in Blanket": 90,
    "Crispy Camembert Dumplings": 40,
    "Festive Burger": 66
}

"--------- Step 3  -----------"
'''Create a dictionary called 'price' that 
contains the prices for each item'''

price = {
    "Turkey Toastie": 8.95,  # price per unit
    "Maple Glazed Pigs in Blanket": 7.25,
    "Crispy Camembert Dumplings": 6.95,
    "Festive Burger": 12.95
}

"--------- Step 4 -----------"
'''Calculate the total stock value in the cafe'''
total_stock_value = 0  
# Remember: 'Initialize' a variable to hold the total value of all stock

# Print a header for the item details
print("FESTIVE ITEMS FOR SALE")
print("-------------------")

# Index over each 'item' in the 'menu' list
for item in menu:
    try:
        # Get the stock quantity and price of the item 
        # using the item name as the key.
        item_stock = stock[item]
        item_price = price[item]

        # Calculate the item value (stock * price)
        item_value = item_stock * item_price
        
        # Add the item value to the total stock value
        total_stock_value += item_value

        # Print out the details of the item
        print(f"\n{item}:")
        print(f"Stock = {item_stock}")
        print(f"Price = £{item_price:.2f}")
        print(f"Item Value = £{item_value:.2f}")
    except KeyError:
        # Handle missing stock or price data gracefully
        print(f"\n{item}:")
        print("Error: Missing stock or price data for this item.")

print("-------------------")

" ---------- Step 5 -----------"
''' Print out the total stock value of the cafe '''
print(f"\nTotal Stock Value of the Cafe: £{total_stock_value:.2f}")

# Knote: The :.2f portion specifies that the number should be represented 
# as a fixed-point number with exactly two digits after the decimal. 
# For example, if total_stock_value is 100.5, it will be printed as £100.50.


# Apologies for the late submission. I was still going over my notes and 
# trying some challenges to make my code more flexible. I've now completed
# the task with the notes and references included. I work part-time at 
# Green King, so I thought it would be useful to reference their menu here.

# From this task, I learned how to loop through dictionaries, access their
# values, and use them to calculate things like the total stock value. 
# It helped me understand how to work with different data structures, 
# making my code more dynamic and efficient.

# Green King (2024) 'Coach House Festive Menu', Green King. 
# Available at: [https://www.greeneking.co.uk/christmas/festive-menu] 
# (Accessed: 11 December 2024).
