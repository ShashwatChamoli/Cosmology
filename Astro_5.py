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
    return (1/(  Ho * np.sqrt( omega_m*(1+z)**(3) + omega_r*(1+z)**(4) + omega_de*(1+z)**(gamma))  ))  

for i in range(len(gamma)):
    comoving_dist = []
    proper_dist = []
    lum_dist = []
    ang_dist = []
    print(f"For {words_array[i]} :")
    for z in z_val:
        dist, _ = quad(formula, 0, z, args=(omega_m_val[i], omega_de_val[i], gamma[i]))
        comoving_dist.append(dist)
        proper_dist.append(dist/(1+z))
        lum_dist.append((1+z)*dist)
        ang_dist.append(dist/(1+z))
    #Comoving distance
    print(f"At z = ", z_val)
    print("Comoving distance is(in terms of 1/H0) ", comoving_dist, "correspondingly")
    plt.scatter(z_val, comoving_dist)
    plt.ylabel('Comoving dist in 1/H0')
    plt.xlabel('Redshift(z)')
    plt.title(f"Comoving distance vs Redshift for {words_array[i]}")
    plt.show()
    #Proper distance
    print("Proper distance is(in terms of 1/H0) ", proper_dist, "correspondingly")
    plt.scatter(z_val, proper_dist)
    plt.ylabel('Proper dist in 1/H0')
    plt.xlabel('Redshift(z)')
    plt.title(f"Proper distance vs Redshift for {words_array[i]}")
    plt.show()
    #Luminosity distance
    print("Luminosity distance is(in terms of 1/H0) ", lum_dist, "correspondingly")
    plt.scatter(z_val, lum_dist)
    plt.ylabel('Luminosity distance in 1/H0')
    plt.xlabel('Redshift(z)')
    plt.title(f"Luminosity distance vs Redshift for {words_array[i]}")
    plt.show()
    #Angular distance
    print("Angular distance is(in terms of 1/H0) ", ang_dist, "correspondingly")
    plt.scatter(z_val, ang_dist)
    plt.ylabel('Angular Diameter distance in 1/H0')
    plt.xlabel('Redshift(z)')
    plt.title(f"Angular Diameter distance vs Redshift for {words_array[i]}")
    plt.show()


# Fifth Question
z_val_fifth_question = [35.69, 37.69, 41.69, 1135.69]
omega_m_val = [0.987]
omega_r = 1.2e-2     
omega_de_val = [4.67e-5]
gamma = [0]
Ho = 8568.04
words_array = ["Flat Lambda CDM model with T0 = 100k"]

for i in range(len(gamma)):
    comoving_dist = []
    proper_dist = []
    lum_dist = []
    ang_dist = []
    print(f"For {words_array[i]} :")
    for z in z_val_fifth_question:
        dist, _ = quad(formula, 0, z, args=(omega_m_val[i], omega_de_val[i], gamma[i]))
        comoving_dist.append(dist)
        proper_dist.append(dist/(1+z))
        lum_dist.append((1+z)*dist)
        ang_dist.append(dist/(1+z))
    #Comoving distance
    print(f"At z = ", z_val_fifth_question)
    print("Comoving distance is(in terms of 1/H0) ", comoving_dist, "correspondingly")
    plt.scatter(z_val_fifth_question, comoving_dist)
    plt.ylabel('Comoving dist in 1/H0')
    plt.xlabel('Redshift(z)')
    plt.title(f"Comoving distance vs Redshift for {words_array[i]}")
    plt.show()
    #Proper distance
    print("Proper distance is(in terms of 1/H0) ", proper_dist, "correspondingly")
    plt.scatter(z_val_fifth_question, proper_dist)
    plt.ylabel('Proper dist in 1/H0')
    plt.xlabel('Redshift(z)')
    plt.title(f"Proper distance vs Redshift for {words_array[i]}")
    plt.show()
    #Luminosity distance
    print("Luminosity distance is(in terms of 1/H0) ", lum_dist, "correspondingly")
    plt.scatter(z_val_fifth_question, lum_dist)
    plt.ylabel('Luminosity distance in 1/H0')
    plt.xlabel('Redshift(z)')
    plt.title(f"Luminosity distance vs Redshift for {words_array[i]}")
    plt.show()
    #Angular Diameter distance
    print("Angular distance is(in terms of 1/H0) ", ang_dist, "correspondingly")
    plt.scatter(z_val_fifth_question, ang_dist)
    plt.ylabel('Angular Diameter distance in 1/H0')
    plt.xlabel('Redshift(z)')
    plt.title(f"Angular Diameter distance vs Redshift for {words_array[i]}")
    plt.show()
