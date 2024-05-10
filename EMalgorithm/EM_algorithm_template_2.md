# EM algorithm Template Code II


## Problem II

$$
\begin{aligned}
& X_1, X_2, \dots, X_n \overset{\text{iid}}{\sim} \text{Pois}(\tau_i), \\
& Y_1, Y_2, \dots, Y_n \overset{\text{iid}}{\sim} \text{Pois}(\beta \tau_i), \\
& \text{Dataset}: \biggl\{(x_i, y_i) \bigg | i = 1, 2, \dots, n\biggr\}, \\
& \text{let}~~ x_1 ~\text{is missing, We want to use the EM algorithm for estimation } \bigl(\beta, \tau_1, \dots, \tau_n\bigr)~ 
\end{aligned}
$$

``` python
import numpy as np 
import pandas as pd 
from scipy import stats 

def Gen_data(n, beta, Tau, seed = 1234): 
    x = stats.poisson.rvs(size = n, mu = Tau, random_state = seed)
    y = stats.poisson.rvs(size = n, mu = beta * Tau, random_state = seed)
    return pd.DataFrame({'x': x, 'y': y})

Tau = np.array([1, 1.5, 2, 3, 4, 5, 0.5, 1, 2, 1])
dat = Gen_data(10, 2, Tau)
dat
```

       x   y
    0  0   1
    1  2   4
    2  2   8
    3  7   4
    4  2  10
    5  5  13
    6  2   2
    7  1   3
    8  4   1
    9  2   3

``` python
xx = dat['x'].values
yy = dat['y'].values
xx = xx.astype(float)
xx[0] = np.nan
xx
```

    array([nan,  2.,  2.,  7.,  2.,  5.,  2.,  1.,  4.,  2.])

``` python
def EM_2(tau_init, xData, yData, tol = 1e-7, numIter = int(1e+3)): 
    # set Initial values    
    k = 0
    n = len(xData)
    tauk = tau_init
    tauveck = []
    betak = yData.sum() / (np.nansum(xData) + tauk)
    for j in range(n): 
        if j == 0: 
            continue
        temp = (xData[j] + yData[j]) / (betak + 1)
        tauveck.append(temp) 
    listResultk = np.hstack([[betak, tauk], tauveck])
    while True: 
        k += 1
        ## Expectaiton Step
        xData[0] = tauk

        ## Maximization Step 
        betakplus1 = yData.sum() / xData.sum()
        taukplus1 = (tauk + yData[0]) / (betakplus1 + 1)
        tauveckplus1 = list()
        for j in range(n): 
            if j == 0: 
                continue
            temp = (xData[j] + yData[j]) / (betakplus1 + 1)
            tauveckplus1.append(temp) 
        listResultkplu1 = np.hstack([[betakplus1, taukplus1], tauveckplus1])
        temp2 = np.abs(listResultkplu1 - listResultk)
        if (np.all(temp2 < tol) or k >= numIter): 
            final_result = {'Num_Iter': k, 
            'betahat': betakplus1, 
            'tauhat': list(np.hstack([taukplus1, tauveckplus1]))}
            break 
        listResultk = listResultkplu1.copy() 
        tauk = taukplus1
    return final_result        
init_tau = 10
EM_2(tau_init = init_tau, xData = xx, yData = yy, tol = 1e-7, numIter = int(1e+3))
```

    {'Num_Iter': 20, 'betahat': 1.7777777717066237, 'tauhat': [0.5625000351149861, 2.1600000047209296, 3.600000007868216, 3.9600000086550375, 4.320000009441859, 6.480000014162789, 1.4400000031472864, 1.4400000031472864, 1.800000003934108, 1.800000003934108]}

## R programming Using method I

``` r
# define a function for generate data 
Gen_data <- function(n, beta, Tau, seed = 1234) {
    set.seed(seed)
    x <- rpois(n, lambda = Tau)
    y <- rpois(n, lambda = beta * Tau)
    return(data.frame(x = x, y = y))
}

Tau <- c(1, 1.5, 2, 3, 4, 5, 0.5, 1, 2, 1)
dat <- Gen_data(10, 2, Tau)
xx <- as.numeric(dat$x)
yy <- dat$y
xx[1] <- NA

EM_2 <- function(tau_init, xData, yData, tol = 1e-7, numIter = 1e+3) {
    # set initialize
    k <- 0
    n <- length(xData)
    tauk <- tau_init
    tauveck <- c()
    betak <- sum(yData, na.rm = TRUE) / (sum(xData, na.rm = TRUE) + tauk)
    for (j in 2:n) {
        temp <- (xData[j] + yData[j]) / (betak + 1)
        tauveck <- c(tauveck, temp)
    }
  # define vector of results for intial step 
  listResultk <- c(betak, tauk, tauveck)

    while (TRUE) {
        # Expetation Step 
        k <- k + 1
        xData[1] <- tauk

        # Maximization Step 
        betakplus1 <- sum(yData) / sum(xData, na.rm = TRUE)
        taukplus1 <- (tauk + yData[1]) / (betakplus1 + 1)
        tauveckplus1 <- c()
        for (j in 2:n) {
            temp <- (xData[j] + yData[j]) / (betakplus1 + 1)
            tauveckplus1 <- c(tauveckplus1, temp)
        }

        # define a vector for gather results 
        listResultkplu1 <- c(betakplus1, taukplus1, tauveckplus1)
        # check condition for stop algorithm 
        temp2 <- abs(listResultkplu1 - listResultk)
        if (all(temp2 < tol) || k >= numIter) {
            final_result <- list('Num_Iter' = k, 'betahat' = betakplus1, 'tauhat' = c(taukplus1, tauveckplus1))
            break
        }
        listResultk <- listResultkplu1
        tauk <- taukplus1
    }

    # return results
    return(final_result)
}

# check function 
init_tau <- 10
EM_2(tau_init = init_tau, xData = xx, yData = yy, tol = 1e-7, numIter = 1e+3)
```

    $Num_Iter
    [1] 21

    $betahat
    [1] 1.772727

    $tauhat
     [1] 1.6923078 1.8032787 1.8032787 4.6885246 4.3278689 6.8524590 0.0000000
     [8] 0.3606557 1.4426230 0.7213115
