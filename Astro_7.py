import matplotlib.pyplot as plt
import numpy as np

T = 2.7255
c = 3 * 10**8
h = 6.626 * 10**(-34)
k = 1.380649 * 10**(-23)

def f(v, z):
    return (8 * np.pi * h * (v**3) * (1 + z)**(3)) / (c**2 * (np.exp(h * v / (k * T)) - 1))

z = [0, 6, 20, 1090, 10000]

v = np.linspace(1e7, 1e12, 10000)

# If we plot them together, we won't be able to see the black body spectrum shape, so we will plot them seperately for seperate z
for i in range (len(z)):
    plt.plot(v, f(v, z[i]))
    plt.title(f'Black Body spectrum at z = {z[i]}')
    plt.xlabel('Frequency(Hz)')
    plt.ylabel('Spectral Energy Density(/m^2)')
    plt.show()

'''
plt.title('Black Body spectrum at z = {z[i]}')
plt.xlabel('Frequency')
plt.ylabel('Spectral Energy Density')
plt.legend()
plt.show()
'''


