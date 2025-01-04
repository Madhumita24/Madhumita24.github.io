import numpy as np
import matplotlib.pyplot as plt

# Define the constraints as equations of x1 and x2
x1 = np.linspace(0, 20, 400)
x2_1 = (120 - 12 * x1) / 24  # From 12x1 + 24x2 >= 120
x2_2 = (120 - 16 * x1) / 16  # From 16x1 + 16x2 >= 120
x2_3 = (120 - 30 * x1) / 12  # From 30x1 + 12x2 >= 120

# Set up the plot
plt.figure(figsize=(8, 6))

# Plot each of the constraint lines
plt.plot(x1, x2_1, label=r'$12x_1 + 24x_2 \geq 120$', color='blue')
plt.plot(x1, x2_2, label=r'$16x_1 + 16x_2 \geq 120$', color='green')
plt.plot(x1, x2_3, label=r'$30x_1 + 12x_2 \geq 120$', color='red')

# Fill the feasible region
plt.fill_between(x1, np.maximum.reduce([x2_1, x2_2, x2_3]), 20, where=(x1 >= 0), color='gray', alpha=0.3)

# Define labels and limits
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title('Feasible Region and Constraints')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()