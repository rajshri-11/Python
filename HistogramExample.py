import numpy as np
import matplotlib.pyplot as plt

# Generating random data for the histogram
data = np.random.randn(1000)

# Creating a histogram
plt.hist(data, bins=30, color='green', edgecolor='black')

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram Example')

# Displaying the plot
plt.show()
