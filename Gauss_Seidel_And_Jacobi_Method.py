# Code for Gauss-Seidel Method
x1, x2, x3 = 0, 0, 0
err = 0.01
i = 0
print("Gauss-Seidel Iteration Results:")
while True:
    i=i+1
    x1_old, x2_old, x3_old = x1, x2, x3    
    x1 = (14 - 3*x2 + 3*x3) / 8
    x2 = (5 + 2*x1 - 5*x3) / -8
    x3 = (-8 - 3*x1 - 5*x2) / 10
    print(f"Iteration {i}: x1={x1:.4f}, x2={x2:.4f}, x3={x3:.4f}")
    if abs(x1 - x1_old) < err and abs(x2 - x2_old) < err and abs(x3 - x3_old) < err:
        break
print("\nFinal Gauss-Seidel Solution:")
print("x1 =", x1)
print("x2 =", x2)
print("x3 =", x3)
# Code for Gauss-Jacobi Method
x1, x2, x3 = 0, 0, 0
err = 0.01
i = 0
print("\nGauss-Jacobi Iteration Results:")
while True:
    i += 1
    x1_old, x2_old, x3_old = x1, x2, x3
    x1_new = (14 - 3*x2_old + 3*x3_old) / 8
    x2_new = (5 + 2*x1_old - 5*x3_old) / -8
    x3_new = (-8 - 3*x1_old - 5*x2_old) / 10
    print(f"Iteration {i}: x1={x1_new:.4f}, x2={x2_new:.4f}, x3={x3_new:.4f}")
    if abs(x1_new - x1_old) < err and abs(x2_new - x2_old) < err and abs(x3_new - x3_old) < err:
        break
    x1, x2, x3 = x1_new, x2_new, x3_new
print("\nFinal Gauss-Jacobi Solution:")
print("x1 =", x1_new)
print("x2 =", x2_new)
print("x3 =", x3_new)