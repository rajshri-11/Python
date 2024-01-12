# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

# Accessing elements in a list
print("\nAccessing Elements:")
print("First Element:", my_list[0])
print("Last Element:", my_list[-1])

# Slicing a list
sliced_list = my_list[1:4]
print("\nSliced List:", sliced_list)

# Modifying elements in a list
my_list[2] = 10
print("\nModified List:", my_list)

# Appending elements to a list
my_list.append(6)
print("\nList After Appending:", my_list)

# Extending a list with another list
extension_list = [7, 8, 9]
my_list.extend(extension_list)
print("\nExtended List:", my_list)

# Inserting an element at a specific position
my_list.insert(2, 20)
print("\nList After Insertion:", my_list)

# Removing an element by value
my_list.remove(10)
print("\nList After Removal:", my_list)

# Removing an element by index
removed_element = my_list.pop(4)
print("\nList After Pop:", my_list)
print("Removed Element:", removed_element)

# Finding the index of an element
index_of_4 = my_list.index(4)
print("\nIndex of 4:", index_of_4)

# Counting occurrences of an element
count_of_5 = my_list.count(5)
print("\nCount of 5:", count_of_5)

# Sorting a list (in-place)
my_list.sort()
print("\nSorted List:", my_list)

# Reversing a list (in-place)
my_list.reverse()
print("\nReversed List:", my_list)

# Copying a list (shallow copy)
copied_list = my_list.copy()
print("\nCopied List:", copied_list)

# Clearing all elements from a list
my_list.clear()
print("\nCleared List:", my_list)
