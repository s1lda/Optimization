e =1e-7
def f(x):
    return x**3-x
a = 0
b = 1
n = 0
L=b-a
def fib(n):
    fibonaci = [0, 1]
    for i in range(2, n + 1):
        fibonaci.append(fibonaci[- 1] + fibonaci[- 2])
    return fibonaci
while fib(n)[-1] < L / e:
    n += 1
fibonaci = fib(n)
while n>2:
    L = b - a
    fibonaci = fib(n)
    x1=a+(fibonaci[n-1]*L)/fibonaci[n]
    x2=b-(fibonaci[n-1]*L)/fibonaci[n]
    f1=f(x1)
    f2=f(x2)
    if (f1>f2):
        b=x1
        f1=f2
        x1=x2
        L=b-a
        x2=a+(b-x1)
        f2=f(x2)
    else:
        a=x2
        f2=f1
        x2=x1
        L=b-a
        x1=b-(x2-a)
        f1=f(x1)
    n=n-1
print(min(f1,f2))



