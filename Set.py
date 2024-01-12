# Creating a set
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 5, 6, 7}
print("Set 1:", my_set1)
print("Set 2:", my_set2)

# Adding elements to a set
my_set1.add(6)
print("\nSet 1 After Addition:", my_set1)

# Removing an element from a set
my_set1.remove(3)
print("Set 1 After Removal:", my_set1)

# Union of sets
union_set = my_set1.union(my_set2)
print("\nUnion of Set 1 and Set 2:", union_set)

# Intersection of sets
intersection_set = my_set1.intersection(my_set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# Difference of sets
difference_set = my_set1.difference(my_set2)
print("Difference of Set 1 and Set 2:", difference_set)

# Symmetric difference of sets
symmetric_difference_set = my_set1.symmetric_difference(my_set2)
print("Symmetric Difference of Set 1 and Set 2:", symmetric_difference_set)

# Checking if a set is a subset
is_subset = my_set1.issubset(my_set2)
print("\nIs Set 1 a Subset of Set 2?", is_subset)

# Checking if a set is a superset
is_superset = my_set1.issuperset(my_set2)
print("Is Set 1 a Superset of Set 2?", is_superset)

# Removing all elements from a set
my_set1.clear()
print("\nCleared Set 1:", my_set1)

# Converting a list to a set
list_as_set = set([1, 2, 3, 4, 5])
print("\nList as Set:", list_as_set)

# Converting a set to a list
set_as_list = list(list_as_set)
print("Set as List:", set_as_list)
