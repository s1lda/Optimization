import numpy as np

def objective_function(x, y):
    return x ** 2 + y ** 2 - 3 * x + 15 * y

def inequality_constraint_1(x, y):
    return (x + y)**2 - 4 * (x - y)

def penalty_function(x, y, c):
    return objective_function(x, y) + c * max(0, inequality_constraint_1(x, y)) ** 2

def gradient_objective_function(x, y):
    return np.array([2 * x - 3, 2 * y + 15])

def gradient_penalty_function(x, y, c):
    return gradient_objective_function(x, y) + 2 * c * np.array([max(0, inequality_constraint_1(x, y))])

def backtracking_line_search(x, y, d, c):
    alpha = 1
    while penalty_function(x + alpha * d[0], y + alpha * d[1], c) > penalty_function(x, y, c) - 0.5 * alpha * np.linalg.norm(gradient_penalty_function(x, y, c)) ** 2:
        alpha /= 2
    return alpha

def method_of_penalty_functions(x0, y0, epsilon):
    x = x0
    y = y0
    c = 1

    while True:
        d = -gradient_penalty_function(x, y, c)
        alpha = backtracking_line_search(x, y, d, c)
        if np.linalg.norm(alpha * d) < epsilon:
            break
        x += alpha * d[0]
        y += alpha * d[1]
        c *= 2

    return x, y

x0 = 1
y0 = 1
epsilon = 0.01

x, y = method_of_penalty_functions(x0, y0, epsilon)
print(f"x = {x}, y = {y}")
print(f"f = {x ** 2 - 2 * x + y ** 2 - y}")