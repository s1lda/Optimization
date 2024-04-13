from scipy.optimize import minimize
import numpy as np

def lagrange_multiplier_method(objective_function, equality_constraints, initial_guess):
    def lagrange_function(x, lambda_):
        return objective_function(x) + np.dot(lambda_, [constraint(x) for constraint in equality_constraints])

    initial_lambda = np.ones(len(equality_constraints))

    result = minimize(lambda x: lagrange_function(x, initial_lambda), initial_guess)

    return result.x

def objective_function(x):
    return x[0]**2 - x[1]**2

def equality_constraint(x):
    return 2*x[0] + x[1] - 3  # Уравнение ограничения

equality_constraints = [equality_constraint]
initial_guess = [0, 0]

result = lagrange_multiplier_method(objective_function, equality_constraints, initial_guess)
print("Результат оптимизации:", result)
