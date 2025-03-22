
#Slide 12 Grocery Activity
# create an empty dictionary called groceries
# create a loop to use until we break out by pressing enter
# lowercase grocery items will will be the key   X

# if the user presses enter break out   X

# split the entered grocery name and value   X

# get the product name and apply as the key   X

# if no quantity or quantity is not a number, display an error message    X

# the quantity must be stored as an integer.    X

# add the key and the value to the dictionary    x

# add the key and the value to the dictionary     x

# print out the groceries

groceries = {}

def update_groceries(item, quantity):
    if item in groceries:
        groceries[item] += quantity
    else:
        groceries[item] = quantity

while True:
    user_input = input("Add to Groceries: ").lower()
    if user_input == "":
        break

    input_split = (user_input.split(" "))

    try:
        user_quantity = int(input_split[0])
    except ValueError:
        print("Invalid quantity!")
        continue

    user_item = input_split[1]

    update_groceries(user_item, user_quantity)


print("Here is your shopping list:")
print(groceries)


