
import numpy as np
from scipy.optimize import minimize

def objective_function(x):
    x1, x2 = x
    return x1**2 + x2**2 - 3*x1 + 15*x2

def constraint(x):
    x1, x2 = x
    return (x1 + x2)**2 - 4*(x1 - x2)

def barrier_function(x, f, constraint, t):
    penalty = -1 / constraint(x)
    return f(x) + t * penalty

def barrier_method(f, grad_f, initial_point, constraint, t0=1, mu=10, tol=1e-6, max_iter=100):
    x = initial_point
    t = t0
    for _ in range(max_iter):
        # Минимизируем барьерную функцию
        result = minimize(lambda x: barrier_function(x, f, constraint, t), x, jac=grad_f, tol=tol)
        x = result.x

        # Уменьшаем параметр барьерной функции
        t *= mu

        # Проверяем условие остановки
        if constraint(x) < tol:
            break
    return x

# Начальная точка
initial_point = [1, 1]

# Решение задачи с использованием метода барьерных функций
solution = barrier_method(objective_function, None, initial_point, constraint)

print("Решение:", solution)
print("Значение целевой функции в решении:", objective_function(solution))
print("Значение ограничения в решении:", constraint(solution))
