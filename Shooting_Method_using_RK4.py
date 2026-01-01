#Shooting Method using RK-4
import numpy as np
import matplotlib.pyplot as plt
def f(x, y, z):
    dydx = z
    dzdx = 8*x*(9-x) + 2*y
    return dydx, dzdx
# RK4 solver
def rk4(x, y, z, h):
    Y = []
    for x in X:
        k1y, k1z = f(x, y, z)
        k2y, k2z = f(x + h/2, y + h*k1y/2, z + h*k1z/2)
        k3y, k3z = f(x + h/2, y + h*k2y/2, z + h*k2z/2)
        k4y, k4z = f(x + h, y + h*k3y, z + h*k3z)
        y = y + h*(1/6)*(k1y + 2*k2y + 2*k3y + k4y)
        z = z + h*(1/6)*(k1z + 2*k2z + 2*k3z + k4z)
        Y.append(y)
    return Y
x = 0
y = 0
xl = 9
yl = 0
h = 0.01
X = np.arange(0, xl + h, h)
# Two guesses for z
z1 = -1
z2 = 6
# Solve for both z guesses
Y1 = rk4(x, y, z1, h)
Y2 = rk4(x, y, z2, h)
# Linear interpolation to correct z
y1 = Y1[-1]
y2 = Y2[-1]
z = z1 + (z2 - z1) * (yl - y1) / (y2 - y1)
# Final solution with corrected z
Y = rk4(x, y, z, h)
plt.plot(X, Y)
plt.title("Shooting Method using RK4")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.grid(True)
plt.show()
print("Final Corrected Initial Slope (z) =", z)
print("y(9) ≈", Y[-1])