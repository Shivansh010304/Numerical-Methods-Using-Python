#Integration using Trapezoidal,Simpson Method
import numpy as np
def f(x):
    return 4/(1 + x**2)
def Trapezoidal(a, b, n, f):
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        s = s + 2*f(a + i*h)
    return (h/2)*s
def Simpson(a, b, n, f):
    if n % 2 != 0:
        n = n + 1
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            s = s + 2*f(a + i*h)
        else:
            s = s + 4*f(a + i*h)
    return (h/3)*s
def Simpson38(a, b, n, f):
    if n % 3 != 0:
        n = n + (3 - n%3)
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            s = s + 2*f(a + i*h)
        else:
            s = s + 3*f(a + i*h)
    return (3*h/8)*s
a = 0
b = 1
n = 12
trapezoidal = Trapezoidal(a, b, n, f)
print("Trapezoidal=", trapezoidal)
simpson = Simpson(a, b, n, f)
print("Simpson=", simpson)
simpson38 = Simpson38(a, b, n, f)
print("Simpson38=", simpson38)