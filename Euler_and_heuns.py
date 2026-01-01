# Code For Euler & Heun's Method
import matplotlib.pyplot as plt
import numpy as np
x, y = 0, 0
h = 0.1
X1 = []
Y1 = []
X2 = []
Y2 = []
def f(x, y):
    return x 
def euler(x, y, f):
    y = y + h*f(x, y)
    x = x + h
    return x, y
def huens(x, y, f):
    y = y + h*f(x + h/2, y)
    x = x + h
    return x, y
print("Euler Method Results:")
x, y = 0, 0
while x < 10:
    x, y = euler(x, y, f)
    X1.append(x)
    Y1.append(y)
    print(f"x = {x:.2f}, y = {y:.4f}")
print("\nHeun's Method Results:")
x, y = 0, 0
while x < 10:
    x, y = huens(x, y, f)
    X2.append(x)
    Y2.append(y)
    print(f"x = {x:.2f}, y = {y:.4f}")
plt.subplot(2,2,1)
plt.title("Euler Method")
plt.plot(X1, Y1)
plt.subplot(2,2,2)
plt.title("Heun's Method")
plt.plot(X2, Y2)
plt.show()