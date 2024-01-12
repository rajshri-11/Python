import numpy as np

# Creating arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([[1, 2, 3], [4, 5, 6]])

# Basic array operations
print("\nBasic Array Operations:")
print("Array 1:", array1)
print("Array 2:\n", array2)
print("Shape of Array 2:", array2.shape)
print("Transpose of Array 2:\n", array2.T)

# Arithmetic operations
print("\nArithmetic Operations:")
result_add = np.add(array1, 10)
print("Addition:", result_add)
result_mul = np.multiply(array1, 2)
print("Multiplication:", result_mul)

# Universal functions (ufunc)
print("\nUniversal Functions (ufunc):")
array3 = np.array([1.5, 2.6, 3.7, 4.8, 5.9])
print("Original Array:", array3)
print("Square Root:", np.sqrt(array3))
print("Exponential:", np.exp(array3))
print("Sine:", np.sin(array3))
print("Cosine:", np.cos(array3))

# Indexing and slicing
print("\nIndexing and Slicing:")
print("Element at index 2 of Array 1:", array1[2])
print("Slice of Array 1 from index 1 to 3:", array1[1:4])

# Reshaping arrays
array4 = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = np.reshape(array4, (2, 3))
print("\nReshaped Array:\n", reshaped_array)

# Concatenation and stacking
array5 = np.array([[1, 2], [3, 4]])
array6 = np.array([[5, 6]])
concatenated_array = np.concatenate((array5, array6), axis=0)
stacked_array = np.vstack((array5, array6))
print("\nConcatenated Array:\n", concatenated_array)
print("Vertically Stacked Array:\n", stacked_array)

# Statistical functions
print("\nStatistical Functions:")
print("Mean of Array 1:", np.mean(array1))
print("Sum of Array 2:", np.sum(array2))
print("Standard Deviation of Array 1:", np.std(array1))

# Linear Algebra operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
product_matrix = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:\n", product_matrix)

# Random module in NumPy
print("\nRandom Module:")
random_array = np.random.rand(3, 3)
print("Random 3x3 Array:\n", random_array)

# Save and load arrays
np.save('saved_array.npy', array1)
loaded_array = np.load('saved_array.npy')
print("\nLoaded Array from File:", loaded_array)
