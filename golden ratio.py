e =1e-7
def f(x):
    return x**3-x
a = 0
b = 1
L=b-a
while L>e:
    t=0.618
    x1=a+L*t
    x2=b-L*t
    f1=f(x1)
    f2=f(x2)
    if f1>f2:
        b=x1
        f1=f2
        x1=x2
        L=b-a
        x2=b-L*t
        f2=f(x2)
    else:
        a=x2
        f2=f1
        x2=x1
        L=b-a
        x1=a+L*t
        f1=f(x1)
print(min(f1,f2))

