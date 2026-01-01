#Diffrential equation using RK-2 and RK-4 Methods
import numpy as np
import matplotlib.pyplot as plt
x, y = 0, 5
h = 0.1
X1, Y1 = [], []
X2, Y2 = [], []
def f(x, y):
    return (x + y) * np.sin(x)
def rk2(x, y, f):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    y = y + k2
    x = x + h
    return x, y
def rk4(x, y, f):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)
    y = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    x = x + h
    return x, y
print("RK2 Method Results:")
x, y = 0, 5
while x <= 6:
    x, y = rk2(x, y, f)
    X1.append(x)
    Y1.append(y)
    print(f"x = {x:.2f}, y = {y:.4f}")
print("\nRK4 Method Results:")
x, y = 0, 5
while x <= 6:
    x, y = rk4(x, y, f)
    X2.append(x)
    Y2.append(y)
    print(f"x = {x:.2f}, y = {y:.4f}")
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.title("RK2 Method")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(X1, Y1)
plt.subplot(1,2,2)
plt.title("RK4 Method")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(X2, Y2)
plt.tight_layout()
plt.show()
print("\nFinal RK2 Value: y(6) ≈", Y1[-1])
print("Final RK4 Value: y(6) ≈", Y2[-1])