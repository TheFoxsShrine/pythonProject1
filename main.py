
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100) 
y = np.log(x) + np.cos(x) 

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = log(x) + cos(x)')

plt.show()