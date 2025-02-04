import numpy as np
import matplotlib.pyplot as plt

# Generate an array of x values from 0 to 2π
x = np.linspace(0, 2 * np.pi, 100)

# Calculate the sine and cosine of each x value
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.plot(x, y_cos, label='cos(x)', color='red')

# Add title and labels
plt.title('Sine and Cosine Functions')
plt.xlabel('x (radians)')
plt.ylabel('Function value')

# Add a legend
plt.legend()

# Show the grid
plt.grid()

# Display the plot
plt.show()   
