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

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

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
xx <- dat$x
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

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

## R programming Method 3

``` r
set.seed(200)
cr_data <- function(size = 100, tau, beta) {
    samp1 <- rpois(size, lambda = tau)
    samp2 <- rpois(size, lambda = tau * beta)
    return (data.frame(x = samp1, y = samp2))
}

n <- 100
T <- sample(1:100, size = n, replace = TRUE)

dataa <- cr_data(size = n, tau = T, beta = 5)
x <- dataa[['x']]
y <- dataa[['y']]
x[1] <- NA
t0 = 25; sampx = x; sampy = y; tolerance = 1e-9; num = 1e+4
Em_algorithm <- function(t0 = 25, sampx = x, sampy = y, tolerance = 1e-9, num = 1e+4) {
    k <- 0
    n <- length(sampx)
    tk <- t0
    tvec <- numeric((n-1))
    bk <- sum(sampy) / (sum(sampx, na.rm = TRUE) + tk)
    for (j in 2:n) {
        res1 <- (sampx[j] + sampy[j]) / (bk + 1)
        tvec[j-1] <- res1
    }

    tempresult_k <- c(bk, tk, tvec)
    Tempp <- TRUE
    while (Tempp) {
        # Expetation Step 
        k <- k + 1
        sampx[1] <- tk

        # Maximization Step 
        bkp1 <- sum(sampy) / sum(sampx)
        tkp1 <- (tk + sampy[1]) / (bkp1 + 1)
        tvec <- numeric(n-1)
        for (j in 2:n) {
            ress <- (sampy[j] + sampx[j]) / (bkp1 + 1)
            tvec[j-1] <- ress
        }

        # define a vector for gather results 
        tempresult_kp1 <- c(bkp1, tkp1, tvec)
        
        ress2 <- abs(tempresult_k - tempresult_kp1)
        if (all(ress2 < tolerance) || k >= num) {
            FResult <- list('Number_Iteration' = k, 'betahat' = bkp1, 'That' = c(tkp1, tvec) |> 
            setNames(paste0("tauHat", 1:100)))
            Tempp = !Tempp
        }
        tempresult_k <- tempresult_kp1
        tk <- tkp1
    }

    # return results
    return(FResult)
}

# check function 
t0 <- 25
Em_algorithm(t0 = t0, sampx = x, sampy = y, tolerance = 1e-9, num = 1e+4)
```

    $Number_Iteration
    [1] 15

    $betahat
    [1] 4.992459

    $That
        tauHat1     tauHat2     tauHat3     tauHat4     tauHat5     tauHat6 
     37.0558847  85.9413416  89.7794986  43.0541090  56.0704675  25.0314587 
        tauHat7     tauHat8     tauHat9    tauHat10    tauHat11    tauHat12 
     65.4155454  81.6025554  53.5673217  92.9501500  62.5786468  28.5358629 
       tauHat13    tauHat14    tauHat15    tauHat16    tauHat17    tauHat18 
     44.7228729  21.8608073  61.4105121  19.1907850  89.7794986  70.9224664 
       tauHat19    tauHat20    tauHat21    tauHat22    tauHat23    tauHat24 
    103.6302391  26.3664698  70.0880844  40.8847159  88.6113639  91.9488917 
       tauHat25    tauHat26    tauHat27    tauHat28    tauHat29    tauHat30 
      5.3400445   3.3375278  40.3840867  98.1233182   0.5006292  50.5635466 
       tauHat31    tauHat32    tauHat33    tauHat34    tauHat35    tauHat36 
     63.2461524  17.6888975  22.8620656  83.4381957 105.7996322   2.6700223 
       tauHat37    tauHat38    tauHat39    tauHat40    tauHat41    tauHat42 
     72.2574775  51.3979286  53.4004453  94.2851612  89.7794986  90.2801278 
       tauHat43    tauHat44    tauHat45    tauHat46    tauHat47    tauHat48 
     84.2725777  54.7354564  78.7656568  33.5421547  63.0792760  20.3589198 
       tauHat49    tauHat50    tauHat51    tauHat52    tauHat53    tauHat54 
     35.3777950  86.1082180  23.3626948  94.7857903  13.0163585  50.8972994 
       tauHat55    tauHat56    tauHat57    tauHat58    tauHat59    tauHat60 
     89.7794986  66.5836802  96.2876779  91.4482625  57.7392314  19.3576614 
       tauHat61    tauHat62    tauHat63    tauHat64    tauHat65    tauHat66 
     18.8570322  33.0415255  33.0415255  87.1094763  61.7442648  84.1057013 
       tauHat67    tauHat68    tauHat69    tauHat70    tauHat71    tauHat72 
     25.0314587  22.0276837  91.6151389  75.0943761  38.0478172  93.6176556 
       tauHat73    tauHat74    tauHat75    tauHat76    tauHat77    tauHat78 
     59.7417481  92.4495209  76.0956345   1.8356403  50.0629174  55.2360856 
       tauHat79    tauHat80    tauHat81    tauHat82    tauHat83    tauHat84 
      1.0012583  60.9098829  21.1933017  16.8545155  37.0465589  35.3777950 
       tauHat85    tauHat86    tauHat87    tauHat88    tauHat89    tauHat90 
      6.3413029   3.5044042  15.8532572   9.0113251   9.6788307   4.3387862 
       tauHat91    tauHat92    tauHat93    tauHat94    tauHat95    tauHat96 
     53.7341980  21.5270545  57.5723550 100.9602168  71.9237247  77.0968928 
       tauHat97    tauHat98    tauHat99   tauHat100 
     54.4017036  25.1983351  48.0604007  22.8620656 
