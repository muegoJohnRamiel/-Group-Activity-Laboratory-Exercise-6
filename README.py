# ----------------------
# CHECK TRUE/FALSE WITH IF
# ----------------------
print("--- CHECK CONDITION ---")

# Variables with different types
my_name = "Luna"    # TEXT (string)
my_age = 18         # NUMBER (int)
i_like_python = True# YES/NO (boolean)

# Check if all things below are true
if my_age >= 18 and len(my_name) == 4 and i_like_python:
    print("Result: TRUE")
else:
    print("Result: FALSE")


# ----------------------
# LIST - things in order (can change later)
# ----------------------
print("\n--- MY LIST ---")
my_things = ["Book", 5, False]  # text, number, yes/no
print("My list:", my_things)
# Change the number to 7
my_things[1] = 7
print("Changed list:", my_things)


# ----------------------
# TUPLE - things in order (CAN'T change)
# ----------------------
print("\n--- MY TUPLE ---")
my_food = ("Pizza", 2, True)  # text, number, yes/no
print("My food tuple:", my_food)
# Just show the first thing
print("First food:", my_food[0])


# ----------------------
# SET - no order, no copies
# ----------------------
print("\n--- MY SET ---")
my_toys = {"Doll", 3, False}  # text, number, yes/no
print("My toys set:", my_toys)
# Add a new toy (copies get ignored!)
my_toys.add("Ball")
my_toys.add(3)  # This won't add again
print("Toys now:", my_toys)


# ----------------------
# DICTIONARY - pairs (key:value)
# ----------------------
print("\n--- MY DICTIONARY ---")
my_dog = {
    "name": "Buddy",  # key="name", value=text
    "age": 4,         # key="age", value=number
    "is_cute": True   # key="is_cute", value=yes/no
}
print("My dog info:", my_dog)
# Change dog's age to 5
my_dog["age"] = 5
print("Updated dog info:", my_dog)
