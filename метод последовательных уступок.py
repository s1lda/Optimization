from scipy.optimize import minimize,rosen,NonlinearConstraint
import numpy as np
from sympy import symbols, diff, solve

def f1(x):
    return 2*(x[0]-6)**2+3*(x[1]-6)**2
def f2(x):
    return 3*(x[0]+4)**2+(x[1]+6)**2
def f3(x):
    return (x[0]+7)**2+2*(x[1]-8)**2

def F_create(x,a):
    return  a[0]*f1(x)+a[1]*f2(x)+a[2]*f3(x)
x0=[0,0]
a=[0.3,0.3,0.3]
nl1 = NonlinearConstraint(f1, -np.inf, 200)
nl2 = NonlinearConstraint(f2, -np.inf, 62)
nl3 = NonlinearConstraint(f3, -np.inf, 180)
def compomiss(a, x0):
    x = x0

    res1 = minimize(f1, x)
    x = res1.x
    d1 = 10
    nl1 = NonlinearConstraint(f1, -np.inf, d1 + f1(x))

    res2 = minimize(f2, x, method='SLSQP', constraints=nl1)
    x = res2.x
    d2 = 100
    nl2 = NonlinearConstraint(f2, -np.inf, d2 + f2(x))

    res3 = minimize(f3, x, method='SLSQP', constraints=[nl1, nl2])
    x = res3.x

    return res3.x


print(compomiss(a, x0))