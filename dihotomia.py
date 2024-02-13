e =1e-7
def f(x):
    return x**3-x
a = 0
b = 1
while abs(b-a)>2*e:
    x=(a+b)/2
    x1=x-e/2
    x2=x+e/2
    if (f(x1)>f(x2)):
        a=x1
    else:
        b=x2
print(f((a+b)/2))