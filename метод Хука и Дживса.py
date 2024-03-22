import numpy as np

# Определите целевую функцию
A = 30
a = 2
b = 3
f = lambda x: A - (x[0] - a) * np.exp(-(x[0] - a)) - (x[1] - b) * np.exp(-(x[1] - b))

# Установите начальную точку, шаг и точность
x_start = np.array([0.0, 0.0])
delta = 0.01
epsilon = 1e-6

# Инициализируйте переменные
x = x_start.copy()
x_new = x_start.copy()

while True:
    # Исследовательский поиск
    for i in range(len(x)):
        x_plus = x.copy()
        x_plus[i] += delta
        x_minus = x.copy()
        x_minus[i] -= delta

        # Выберите лучшую точку из трех (x, x_plus, x_minus)
        best_x = min([x, x_plus, x_minus], key=f)
        x_new[i] = best_x[i]

    # Узловой поиск
    x_pattern = 2 * x_new - x
    if f(x_pattern) < f(x):
        x = x_pattern.copy()
    else:
        # Уменьшите шаг, если не найдено улучшение
        if np.linalg.norm(delta) < epsilon:
            break
        delta /= 2
        x_new = x.copy()

# Выведите найденную точку минимума
print(x)
print((f(x)))