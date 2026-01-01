#Newton Rapson Method
def f(x):
    return x**3 - x - 4
def g(x):
    return 3*x**2 - 1
def newton(x0, n):
    x = x0
    for i in range(n):
        x = x - f(x)/g(x)
        print(f"Iteration {i+1}: x = {x:.6f}")
    return x
x0 = float(input("Enter initial guess x0: "))
n = int(input("Enter number of iterations: "))
root = newton(x0, n)
print("\nApprox Root =", root)