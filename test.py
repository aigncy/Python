import numpy as np
from scipy.optimize import curve_fit
# Creating a function to model and create data 
def func(x, a, b):
    return a * x + b

x = np.linspace(0, 10, 100)
y = func(x, 1, 2)

# Adding noise to the data
yn = y + 0.9 * np.random.normal(size=len(x))
# Executing curve_fit on noisy data 
popt, pcov = curve_fit(func, x, yn)
print(popt)
