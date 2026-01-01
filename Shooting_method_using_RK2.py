#Shooting_method_using_RK2

import numpy as np
import matplotlib.pyplot as plt
def f(x, y, z):
    dydx = z
    dzdx = 8*x*(9-x) + 2*y
    return dydx, dzdx
x, y = 0, 0
yl = 0
xl = 9
h = 0.01
X = np.arange(0, xl + h, h)
# RK2 Solver
def rk2(x, y, z, h):
    Y = []
    for xi in X:
        k1y, k1z = f(xi, y, z)
        k2y, k2z = f(xi + h/2, y + h*k1y/2, z + h*k1z/2)
        y = y + h * k2y
        z = z + h * k2z
        Y.append(y)
    return Y
# Two guesses for slope
z1 = -1
z2 = 6
# Solve for both trial slopes
ya = rk2(x, y, z1, h)[-1]
yb = rk2(x, y, z2, h)[-1]
# Secant method correction for slope
z_des = z1 + (z2 - z1) * (yl - ya) / (yb - ya)
# Final correct solution
Y = rk2(x, y, z_des, h)
# Plot
plt.plot(X, Y)
plt.title("Shooting Method using RK2")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.grid(True)
plt.show()
print("Corrected Slope (z0) =", z_des)
print("Boundary Check y(9) =", Y[-1])