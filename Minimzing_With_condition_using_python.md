# Minimizing a function with a condition

## Problem:

$$
\begin{aligned}
& f_X(x) = 12x^2 (1- x), \quad 0 < x < 1, \\
& A = \underset{b - a}{\min}\{(a, b)~|~\mathcal{P}(a < X < b) = 0.5\}\\
& \implies A = ?
\end{aligned}
$$

#### Soloution:

$$
\begin{aligned}
& X \sim \text{Beta}(3, 2), \\
& \mathcal{P}(a < X < b) = \int_a^b 12x^2 (1 - x) dx = \\
& 3(a^4 - b^4) + 4(b^3 - a^3) = 0.5 \implies \\
& \text{Using Lagrange Method:}\quad \gamma(a, b, \lambda) = b - a + \lambda \left[\int_a^b f(x)dx - 0.5\right] \implies  \\
& (\hat{a}, \hat{b}): ~~ \begin{cases} \frac{\partial \gamma}{\partial \lambda} = 0 \\
 \frac{\partial \gamma}{\partial a} = 0 \\
 \frac{\partial \gamma}{\partial b} = 0\end{cases} \implies \\
& \begin{cases}3(a^4 - b^4) + 4(b^3 - a^3) = 0.5\\
b^2 - b^3 = a^2 - a^3 \end{cases}\quad \overset{\text{Using Numerical Method with python}}{\to}
\end{aligned}
$$

------------------------------------------------------------------------

#### Using python

``` python
import numpy as np
import sympy
from sympy import symbols, simplify, integrate, diff 

x, a, b, l = symbols(['x', 'a', 'b', 'lambda'])
fx = 12 * x**2 * (1 - x) 
ress = integrate(fx, (x, a, b))
ress
```

$\displaystyle 3 a^{4} - 4 a^{3} - 3 b^{4} + 4 b^{3}$

``` python
gam = b - a + l * (ress - 0.5)
eq1 = diff(gam, l)
eq2 = diff(gam, a)
eq3 = diff(gam, b)
eq1
```

$\displaystyle 3 a^{4} - 4 a^{3} - 3 b^{4} + 4 b^{3} - 0.5$

``` python
eq2
```

$\displaystyle \lambda \left(12 a^{3} - 12 a^{2}\right) - 1$

``` python
eq3
```

$\displaystyle \lambda \left(- 12 b^{3} + 12 b^{2}\right) + 1$

#### soloution

``` python
from scipy.optimize import minimize

# Define the function to minimize
def func(x):
    return x[1] - x[0]

# Define the constraint
cons = ({'type': 'eq', 'fun': lambda x:  3 * (x[0]**4 - x[1]**4) + 
        4 * (x[1]**3 - x[0]**3) - 0.5}, 
        {'type': 'ineq', 'fun': lambda x:  x[0] - 0}, 
        {'type': 'ineq', 'fun': lambda x:  x[1] - 0}, 
        {'type': 'ineq', 'fun': lambda x:  x[1] - x[0] - 0}, 
        {'type': 'ineq', 'fun': lambda x:  1 - x[0] - 0}, 
        {'type': 'ineq', 'fun': lambda x:  1 - x[1] - 0})


x0 = [0.75, 0.4]

# Call the minimize function with the method 'SLSQP' (Sequential Least Squares Programming)

res = minimize(func, x0, method = 'SLSQP', constraints = cons)

result = res.x
print(f"""
        The solution is: \n\n 
        a: {result[0]}, \n 
        b: {result[1]}""")
```


            The solution is: 

     
            a: 0.5078008199349001, 
     
            b: 0.8033287954165255

## check soloution:

``` python
round(integrate(fx, (x, result[0], result[1])), 6)
```

$\displaystyle 0.5$

``` python
a = result[0]; b = result[1]

print(f"""
a**2 - a**3: { round(a**2 - a**3, 6)}, \n
b**2 - b**3: { round(b**2 - b**3, 6)}
""")
```


    a**2 - a**3: 0.126919, 

    b**2 - b**3: 0.126919
