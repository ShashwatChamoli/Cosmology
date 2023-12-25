import numpy as np
import matplotlib.pyplot as plt

# Writing the given values
z_o_val = [0.01, 0.012, 0.016, 0.02167, 0.0343, 0.0593]
d_L_val = [38.8, 60.6, 73.8, 87.0, 140.4, 268.7]
c = 3e5        #Velocity of light in km/s

y_val = np.array(z_o_val) * c
x_val = np.array(d_L_val)

# Linear regression
slope, intercept = np.polyfit(x_val, y_val, 1)
print(f"Slope (H_o) in km/s/Mpc: {slope}")
print(f"Intercept (V_pec) in km/s: {intercept}")

# Regression line
regression_line = slope * x_val + intercept

# Plotting
plt.scatter(x_val, y_val, label='Data points')
plt.plot(x_val, regression_line, color='red', label='Linear fit')
plt.xlabel('d_L values in Mpc')
plt.ylabel('c * z_o values in km/s')
plt.legend()
plt.show()
