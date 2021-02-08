# http://cs.mipt.ru/python/lessons/lab1.html
import numpy as np

x = np.array([1, 10, 1000])
a = (1 / np.e ** np.sin(x) + 1) / ((5 / 4) + (1 / 15))
base = (1 + x ** 2)
exponent = np.log10(a) / np.log(base)

print(exponent)
