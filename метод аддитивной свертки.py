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

a=[0.33,0.33,0.33]
def additive(a,x0):
    x=x0
    result=minimize(F_create,x,a)
    return result.x
x0=[0,0]
print(additive(a,x0))