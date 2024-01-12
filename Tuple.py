# Creating a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')
print("Original Tuple:", my_tuple)

# Accessing elements in a tuple
print("\nAccessing Elements:")
print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])

# Slicing a tuple
sliced_tuple = my_tuple[1:4]
print("\nSliced Tuple:", sliced_tuple)

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print("\nConcatenated Tuple:", concatenated_tuple)

# Repetition of a tuple
repeated_tuple = tuple1 * 3
print("\nRepeated Tuple:", repeated_tuple)

# Finding the index of an element
index_of_b = my_tuple.index('b')
print("\nIndex of 'b':", index_of_b)

# Counting occurrences of an element
count_of_2 = my_tuple.count(2)
print("\nCount of 2:", count_of_2)

# Tuple unpacking
a, b, c, *rest = my_tuple
print("\nUnpacked Variables:", a, b, c, rest)

# Checking if an element exists in a tuple
element_exists = 'a' in my_tuple
print("\nDoes 'a' exist in the tuple?", element_exists)

# Getting the length of a tuple
tuple_length = len(my_tuple)
print("\nLength of Tuple:", tuple_length)

# Nested tuple
nested_tuple = ((1, 2, 3), ('a', 'b', 'c'))
print("\nNested Tuple:", nested_tuple)

# Converting a tuple to a list
tuple_as_list = list(my_tuple)
print("\nTuple as List:", tuple_as_list)

# Converting a list to a tuple
list_as_tuple = tuple(tuple_as_list)
print("\nList as Tuple:", list_as_tuple)
