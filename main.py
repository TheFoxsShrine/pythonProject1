
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)  # Создаем массив x от 0 до 2*pi
y = np.sin(x) * np.cos(x)  # Вычисляем значения функции y = sin(x) * cos(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции y = sin(x) * cos(x)')

plt.show()