#Secant Method
def f(x):
    return 2*x**3 - 2*x - 5
x0 = float(input("Enter first guess x0: "))
x1 = float(input("Enter second guess x1: "))
n = int(input("Enter maximum iterations: "))
for i in range(n):
    f0 = f(x0)
    f1 = f(x1)
    x2 = x1 - (f1 * (x1 - x0)) / (f1 - f0)
    print(f"Iteration {i+1}: x = {x2:.6f}")
    if abs(x2 - x1) < 1e-6:
        print("\nConverged successfully!")
        break
    x0, x1 = x1, x2
print("\nApprox Root =", x2)