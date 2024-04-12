import numpy as np

def rosen_gradient(x):
    grad = np.zeros_like(x)
    grad[0] = 2 * x[0]
    grad[1] = -2 * x[1]
    return grad

def projection_constraint(x):
    constraint = 2 * x[0] + x[1] - 3
    if constraint <= 0:
        return x
    else:
        alpha = constraint / (2 + 1)
        return np.array([x[0] - alpha * 2, x[1] - alpha * 1])

def rosen_gradient_projection_constraint(x0, alpha, max_iter, epsilon):
    x = np.copy(x0)
    for i in range(max_iter):
        grad = rosen_gradient(x)
        x -= alpha * grad
        x = projection_constraint(x)
        if np.linalg.norm(grad) < epsilon:
            break
    return x

x0 = np.array([0.8, 0.8])
alpha = 0.01
max_iter = 1000
epsilon = 1e-6

result = rosen_gradient_projection_constraint(x0, alpha, max_iter, epsilon)
print("Минимум найден в точке:", result)
minimum_point = result
value_at_minimum = minimum_point[0]**2 - minimum_point[1]**2
print("Значение функции в точке минимума:", value_at_minimum)