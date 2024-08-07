# Simulation of the probability space of the maximum or minimum value
for simultaneous throwing of several dice

## In this text, we want to simulate the probability space for the maximum value or the minimum value obtained by throwing several dices (one or more).

<br><br>

#### Total Probablity Space $\Omega$ for two dices

$$
\Omega = \left\{
\begin{aligned}
& (1, 1), ~(1, 2), ~(1, 3), ~(1, 4), ~(1, 5),~(1, 6), \\
& (2, 1),~(2, 2)~, (2, 3),~(2, 4),~(2, 5),~(2, 6), \\
& (3, 1),~(3, 2),~(3, 3),~(3, 4),~(3, 5),~(3, 6), \\
& (4, 1), ~(4, 2),~(4, 3),~(4, 4),~(4, 5),~(4, 6), \\
& (5, 1), ~(5, 2), ~(5, 3), ~(5, 4),~(5,5), ~(5, 6), \\
& (6, 1), ~(6, 2), ~(6, 3), ~(6, 4), ~(6, 5), ~(6, 6) \\
\end{aligned}
\right\} \implies 
$$

#### for example:

$$
\text{Pr}\left(\max(X, Y) = z\right) = \begin{cases} 
\frac{1}{36} & \text{if}\quad z = 1,  \\
\frac{3}{36} & \text{if} \quad z = 2, \\
\frac{5}{36} & \text{if} \quad z = 3, \\
\frac{7}{36} & \text{if} \quad z = 4, \\
\frac{9}{36} & \text{if} \quad z = 5, \\
\frac{11}{36} & \text{if} \quad z = 6.
\end{cases} \implies 
$$

$$
\text{Pr}(\max(X, Y) \geq 5) = \text{Pr}(\max(X, Y) = 5) + \text{Pr}(\max(X, Y) = 6) = \frac{9}{36} + \frac{11}{36} = \frac{20}{36} = 0.5555556 
$$

<br><br>

<hr>
<hr>

<br><br>

#### Simulate with R programming:

``` r
Start = Sys.time()
sim_fun <- function(nSim = 1e+3, numDice = 2, num = 5, level = "max",
                        operator = ">=", seed = 412) {
    set.seed(seed)
    if (!(level %in% c("max", "min"))) stop("level must be max or min")
    if (!(operator %in% c(">", ">=", "<=", "<", "=="))) 
        stop("operator must be in c(>, >=, <=, <, ==)")
    mat_sim <- matrix(sample(1:6, size = nSim * numDice, replace = TRUE), 
                nrow = nSim, ncol = numDice)
    temp1 <- apply(mat_sim, MARGIN = 1, FUN = function(x) get(level)(x))
    temp2 <- get(operator)(temp1, num) 
    return(mean(temp2))
}

result <- sim_fun(nSim = 1e+7, numDice = 2, num = 5, 
            level = "max", operator = ">=")

End = Sys.time()
cat("Pr(max(x, y) >= 5) = ", result, "\n", 
"Duration Time: ", difftime(End, Start, units = "secs")[[1]], 
" seconds", "\n", sep = "")
```

    Pr(max(x, y) >= 5) = 0.5551159
    Duration Time: 25.17979 seconds

<br><br>
<hr>
<hr>

#### Using Python Programming

``` python
import time

Start = time.time()
import numpy as np
import operator
def sim_fun(nSim = 10**3, numDice = 2, num = 5, level = "max", operand = ">=", 
            seed = 412): 
    np.random.seed(seed)
    if level not in ("max", "min"): 
        raise ValueError("level must be 'max' or 'min'")
    if operand not in (">=", "<=", "==", ">", "<"):
        raise ValueError("operator must be '>=', '<=', '==', '>', or '<'")
    if not isinstance(seed, int): 
        raise ValueError("seed must be an integer")
    if not isinstance(nSim, int):
        raise ValueError("nSim must be an integer")
    if not isinstance(numDice, int):
        raise ValueError("numDice must be an integer")
    if not isinstance(num, int):
        raise ValueError("num must be an integer")
    my_mat = np.random.choice([1, 2, 3, 4, 5, 6], size = numDice * nSim, 
                              replace = True).reshape(nSim, numDice)
    mydict = {">=": "ge", "<=": "le", "==": "eq", 
          "!=": "ne", ">": "gt", "<": "lt"}
    cond_fun = getattr(operator, mydict[operand])
    mydict2 = {'max': max, 'min': min}
    myfun = mydict2[level]
    result1 = np.apply_along_axis(func1d = myfun, axis = 1, arr = my_mat)
    result2 = cond_fun(result1, num)
    return result2.mean()

python_sim_result = sim_fun(nSim = 10**7)
End = time.time()
print("""Pr(max(x, y) >= 5) = {}, \n
        Duration Time: {} seconds, \n
    """.format(python_sim_result, End - Start))
```

    Pr(max(x, y) >= 5) = 0.5555567, 

            Duration Time: 10.821958780288696 seconds, 

        
