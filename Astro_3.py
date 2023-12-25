import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#defining some values
omega_m_val = [0.3, 0.3, 0.3, 0.8]
omega_r = 1e-4      # This value is very small, so it will stay more or less the same for every model
omega_de_val = [0.7, 0.7, 0.7, 0.2]
gamma = [0, 0.9, -0.6, 0]
Ho = 70
words_array = ["Flat Lambda CDM model", "Flat dark energy (with an equation of state w_de = -0.7) CDM model", "Flat dark energy (with an equation of state w_de = -1.2) CDM model", "Flat Lambda Cold Dark Matter model with \u03A9\u2098 = 0.8"]

z_val = [0, 2, 6, 1100]

#Formula which needs to be integrated
def formula(z,omega_m, omega_de, gamma):
    return (1/(  Ho * (1+z) * np.sqrt( omega_m*(1+z)**(3) + omega_r*(1+z)**(4) + omega_de*(1+z)**(gamma))  ))  

for i in range(len(gamma)):
    univ_age_old = []
    univ_age = []
    print(f"For {words_array[i]} :")
    for z in z_val:
        age, _ = quad(formula, z, 100000, args=(omega_m_val[i], omega_de_val[i], gamma[i]))
        univ_age_old.append(age)
        univ_age = [x*(3e10/3.15e7) for x in univ_age_old]    #For converting to Gyr
    print(f'At z = {z_val}')
    print("Age of the universe is ", univ_age, " in Gyr correspondingly")
    plt.scatter(z_val, univ_age)
    plt.ylabel('Age of the Universe in Gyr')
    plt.xlabel('Redshift(z)')
    plt.title(f"Age of the Universe vs Redshift for {words_array[i]}")
    plt.show()

# Fifth question
z_val_fifth_question = [35.69, 37.69, 41.69, 1135.69]
omega_m_val = [0.987]
omega_r = 1.2e-2     
omega_de_val = [4.67e-5]
gamma = [0]
Ho = 8568.04
words_array = ["Flat Lambda CDM model with T0 = 100k"]

for i in range(len(gamma)):
    univ_age_old = []
    univ_age = []
    print(f"For {words_array[i]} :")
    for z in z_val_fifth_question:
        age, _ = quad(formula, z, 100000, args=(omega_m_val[i], omega_de_val[i], gamma[i]))
        univ_age_old.append(age)
        univ_age = [x*(3e10/3.15e7) for x in univ_age_old]    #For converting to Gyr
    print(f'At z = {z_val_fifth_question}')
    print("Age of the universe is ", univ_age, " in Gyr correspondingly")
    plt.scatter(z_val_fifth_question, univ_age)
    plt.ylabel('Age of the Universe in Gyr')
    plt.xlabel('Redshift(z)')
    plt.title(f"Age of the Universe vs Redshift for {words_array[i]}")
    plt.show()
