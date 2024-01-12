# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Original Dictionary:", my_dict)

# Accessing values by key
print("\nAccessing Values:")
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])

# Modifying values by key
my_dict['age'] = 26
print("\nModified Dictionary:", my_dict)

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'
print("\nDictionary After Addition:", my_dict)

# Removing a key-value pair by key
removed_value = my_dict.pop('city')
print("\nDictionary After Removal:", my_dict)
print("Removed Value:", removed_value)

# Checking if a key exists
if 'age' in my_dict:
    print("\nThe key 'age' exists in the dictionary.")

# Getting a list of all keys
keys_list = list(my_dict.keys())
print("\nList of Keys:", keys_list)

# Getting a list of all values
values_list = list(my_dict.values())
print("\nList of Values:", values_list)

# Getting a list of key-value pairs (items)
items_list = list(my_dict.items())
print("\nList of Items:", items_list)

# Clearing all key-value pairs from a dictionary
my_dict.clear()
print("\nCleared Dictionary:", my_dict)
