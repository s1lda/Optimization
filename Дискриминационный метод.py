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

nl1 = NonlinearConstraint(f1, -np.inf, 200)
nl2 = NonlinearConstraint(f2, -np.inf, 62)
nl3 = NonlinearConstraint(f3, -np.inf, 180)
def discrim(a,x0):
    x=x0
    result=minimize(F_create, x,a, method='SLSQP',
               constraints=[nl1,nl2,nl3])
    return result.x
x0=[0,0]
a=[0.3,0.3,0.3]
print(discrim(a,x0))