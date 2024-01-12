import numpy as np

# Create a NumPy array from a Python list
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print("\nFirst element:", my_array[0])
print("Last element:", my_array[-1])

double_array = my_array * 2
print("\nArray after doubling each element:")
print(double_array)
