# EM algorithm Template Code II


- [Problem I](#problem-i)
  - [Using Python](#using-python)
  - [R Programming Method I](#r-programming-method-i)
  - [R Programming Method II](#r-programming-method-ii)
- [Problem II](#problem-ii)
  - [R programm Method I](#r-programm-method-i)
  - [R programm Method II](#r-programm-method-ii)

# Problem I

$$
\begin{aligned}
& X_1, X_2, \dots, X_n \overset{\text{iid}}{\sim} \text{Pois}(\tau_i), \\
& Y_1, Y_2, \dots, Y_n \overset{\text{iid}}{\sim} \text{Pois}(\beta \tau_i), \\
& \text{Dataset}: \biggl[(x_i, y_i) \bigg | i = 1, 2, \dots, n\biggr], \\
& \text{let}~~ x_1 ~\text{is missing, We want to use the EM algorithm for estimation } \bigl(\beta, \tau_1, \dots, \tau_n\bigr)~ 
\end{aligned}
$$

<br>
<hr>
<hr>

## Using Python

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

## R Programming Method I

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

## R Programming Method II

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

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------



# Problem II

The data used for the example is called faithful implemented in R. It
contains waiting time between eruptions and the duration of the eruption
for the Old Faithful geyser in Yellowstone National Park, Wyoming, USA.
From this data, we use the waiting time part. The histogram of the
waifing time resembles the mixture Gaussian distribution; short and long
waiting times. We set indicators which mixture component each
observation belongs to as a missing data and the EM algorithm will find
the proportion of observations belonging to each nor- mal distribution
along with other unknown parameters for means and variances.

$$
f_{\text{W}}(w) = p \times \frac{1}{\sigma_1} \phi\left(\frac{w - \mu_1}{\sigma_1}\right) + (1-p) \times \frac{1}{\sigma_2} \phi\left(\frac{w - \mu_2}{\sigma_2}\right). 
$$

<br>

And, our unknown parameters are
$p, \mu_1, \mu_2, \sigma_1^2, \sigma_2^2$ where $\mu_1$ and $\sigma_1^2$
indicate the mean and the variance from the normal distribution with the
shorter waiting time and $\mu_2$ and $\sigma_2^2$ represent the mean and
the variance from the longer waiting time. Our $p$ represents the
proportion an observation comes from the normal distribution with the
shorter waiting time. We let
$\theta = \biggl(p, \mu_1, \mu_2, \sigma_1^2, \sigma_2^2\biggr)$.

<br>

The indicator variable as a missing data is

$$
Y_i = 
\begin{cases}1 &  W_i ~~\text{belongs to distribution of shorter waiting times}, \\
0 & W_i~~ \text{belongs to distribution of longer waiting times}
\end{cases} 
$$

where $Y_i$ is Bernoulli distribued with parameter $p$.

<br>

Therefare the likelihood expression for the complete-data is given by:

$$
L_n(\theta|W, Y) = \prod_{i=1}^{n} p^{Y_i} \times (1-p)^{1-Y_i} \times \frac{1}{\sigma_1^{Y_i}} \times \phi\left(\frac{W_i - \mu_1}{\sigma_1}\right)^{Y_i} \times 
\frac{1}{\sigma_2^{1- Y_i}}\times 
\phi\left( \frac{W_i - \mu_2}{\sigma_2} \right)^{1-Y_i} 
$$

And, the corresponding log-likelihood function for the density from the
data faithful becomes:

$$
\begin{aligned} 
\ell_n(\theta|W, Y) & = \sum_{i = 1}^n Y_i \times \log(p) + \sum_{i = 1}^n (1 - Y_i) \times \log(1-p) \\
& - \frac{1}{2} \sum_{i = 1}^n Y_i \times \log(2\pi \sigma_1^2) - \frac{1}{2\sigma_1^2}\sum_{i = 1}^n Y_i\times (W_i-\mu_1)^2 \\
& - \frac{1}{2} \sum_{i = 1}^n (1- Y_i) \times \log(2\pi \sigma_2^2) - \frac{1}{2\sigma_2^2}\sum_{i =1}^n (1-Y_i) \times (W_i - \mu_2)^2. 
\end{aligned}
$$

From now, we apply the EM algorithm and find the expectation of $Y_i$,
Since the conditional distribution of $Y_i$ given $W$ is

$$
Y_i \bigg | W_i, \theta^{(k)} \sim \text{Bin}(1, p_i^{(k)})
$$

With

$$
p_i^{(k)} = \frac{p^{(k)} \times \frac{1}{\sigma_1^{(k)}\phi\left(\frac{w_i - \mu_1^{(k)}}{\sigma_1^{(k)}}\right)}}{p^{(k)} \times \frac{1}{\sigma_1^{(k)}\phi\left(\frac{w_i - \mu_1^{(k)}}{\sigma_1^{(k)}}\right)} + (1-p^{(k)}) \times \frac{1}{\sigma_2^{(k)}\phi\left(\frac{w_i - \mu_2^{(k)}}{\sigma_2^{(k)}}\right)}}
$$

where $p^{(K)}$ is a set of known or estimated parameters at kth step.
$p^{(0)}$ is an initial values. Thus, by the property of the Binomial
distribution, the conditional mean is

$$
\mathcal{E}(Y_i \bigg | W_i, \theta^{(k)}) = p_i^{(k)}. 
$$

By substituting $p^{(k)}$ for $Y_i$, We obtain the expectaion function
as

$$
\begin{aligned} 
Q\biggl(\theta \bigg | \theta^{(k)}\biggr) = & \sum_{i = 1}^n p_i^{(k)} \times \log(p) + \sum_{i = 1}^n ( 1- p_i^{(k)}) \times \log(1 - p)\\ 
& -\frac{1}{2} \sum_{i = 1}^n p_i^{(k)} \times \log(2\pi \sigma_1^2) - \frac{1}{2\sigma_1^2} \sum_{i = 1}^n p_i^{(k)} \times (W_i - \mu_1)^2\\
& - \frac{1}{2}\sum_{i = 1}^n (1-p_i^{(k)}) \times \log(2\pi\sigma_2^2)-\frac{1}{2\sigma_2^2}\sum_{i = 1}^n (1-pi_i^{(k)}) \times (W_i - \mu_2)^2
\end{aligned}
$$

In the maximization step, setting the first derivatives of
$Q\left(\theta\bigg | \theta^{(k)}\right)$ with respect to each
parameter equal to zero results in following equations for each
parameter.

$$
\begin{aligned}
& p^{(k+1)} = \frac{1}{n} \sum_{i=1}^{n} p_i^{(k)}, \\ 
& \mu_1^{(k+1)} = \frac{\sum_{i=1}^{n} p_i^{(k)} W_i}{\sum_{i=1}^{n} p_i^{(k)}}, \\ 
& \mu_2^{(k+1)} = \frac{\sum_{i=1}^{n}(1 - p_i^{(k)}) W_i}{\sum_{i=1}^{n}(1 - p_i^{(k)})}, \\
& (\sigma_1^2)^{(k+1)} = \frac{\sum_{i=1}^{n}p_i^{(k)} (W_i - \mu_1^{(k+1)})^2}{\sum_{i=1}^{n}p_i^{(k)}},\\
& (\sigma_2^2)^{(k+1)} = \frac{\sum_{i=1}^{n}(1-p_i^{(k)}) (W_i - \mu_2^{(k+1)})^2}{\sum_{i=1}^{n}(1-p_i^{(k)})},
\end{aligned}
$$

![Histogram of
Waiting](EM_algorithm_template_2_files/figure-commonmark/unnamed-chunk-5-1.png)

After the EM algorithm, our estimates for unknown parameters are
described in the Table 1. In addition, Table2 shows the results form the
combination of EM algorithm and Bootstrap.

<center>

|     $p$     |   $\mu_1$    |   $\mu_2$    | $\sigma_1^2$ | $\sigma_2^2$ |
|:-----------:|:------------:|:------------:|:------------:|:------------:|
| $0.3608856$ | $54.6148403$ | $80.0910594$ | $34.4710583$ | $34.4304249$ |

Table.1   Estimate Using the combination of EM Algorithm

</center>
<br>
<hr>
<center>

|   $\mu_1$    |   $\mu_2$    | $\sigma_1^2$ | $\sigma_2^2$ |
|:------------:|:------------:|:------------:|:------------:|
| $54.6300598$ | $34.4104298$ | $80.0568343$ | $34.173397$  |

Table.2   Estimate Using the combination of EM Algorithm and Bootstrap

</center>

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

## R programm Method I

``` r
rm(list = ls())

dat <- faithful[['waiting']]

init_values <- c(0.5, 40, 90, 16, 16)


EM <- function(data, Initials) {
    k <- 0
    Sk = Initials
    while (TRUE) {
        # Expectation-Step (E-Step)
        Expect <- Sk[1] * dnorm(data, Sk[2], sqrt(Sk[4])) / 
            (Sk[1] * dnorm(data, Sk[2], sqrt(Sk[4])) + (1 - Sk[1]) * 
            dnorm(data, Sk[3], sqrt(Sk[5])))
    
        # Maximization step (M-Step)
        a1 <- mean(Expect)
        a2 <- sum(Expect * data) / sum(Expect) 
        a3 <- sum((1-Expect) * data) / (sum(1-Expect))
        a4 <- sum(Expect * (data - a2) ** 2) / sum(Expect)
        a5 <- sum((1-Expect) * (data - a3) ** 2) / sum(1 - Expect)
        Skp1 <- c(a1, a2, a3, a4, a5)
        temp <- abs(Sk - Skp1)
        if(all(temp < 1e-4)) break 
        Sk <- Skp1
        k <- k + 1
    }
    names(Skp1) <- c("Prob", "mu1", "mu2", "sigma2_1", "sigma2_2")
    list(Number_Iteration = k, Result = Skp1)
}


EM(dat, init_values)
```

    $Number_Iteration
    [1] 24

    $Result
          Prob        mu1        mu2   sigma2_1   sigma2_2 
     0.3608856 54.6148403 80.0910594 34.4710583 34.4304249 

``` r
## BootStrap section 


P <- EM(dat, init_values) |> 
        _$Result

pr1 <- P[1] 
pr2 <- P[2]
pr3 <- P[3]
pr4 <- P[4]
pr5 <- P[5]

n1 <- (pr1 * nrow(faithful)) |> floor()
n2 <- nrow(faithful) - n1 
boot_fun <- function(B) {
    f1 <- function() {
        u <- runif(1) 
        if (u <= pr1) {
            b <- rnorm(n1, pr2, sqrt(pr4))
            bmean <- mean(b) 
            bvar <- var(b)
            ID <- 1
        } else {
            b <- rnorm(n2, pr3, sqrt(pr5))
            bmean <- mean(b) 
            bvar <- var(b)
            ID <- 2
        }
        return(c(bmean, bvar, ID))
    }
    Result <- replicate(B, f1())
    return(Result)
}
res <- boot_fun(1e+3) |> 
        t() |> 
        as.data.frame() |> 
        setNames(c("Mean", "Variance", "ID"))

res |> 
    dplyr :: group_by(ID) |> 
        dplyr :: summarize(Mean = mean(Mean), Variance = mean(Variance))
```

    # A tibble: 2 × 3
         ID  Mean Variance
      <dbl> <dbl>    <dbl>
    1     1  54.7     34.5
    2     2  80.1     34.3

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

## R programm Method II

``` r
rm(list = ls())

em_algorithm <- function(d, val0) {
        # (E-Step)
        E <- val0[1] * dnorm(d, val0[2], sqrt(val0[4])) / 
            (val0[1] * dnorm(d, val0[2], sqrt(val0[4])) + (1 - val0[1]) * 
            dnorm(d, val0[3], sqrt(val0[5])))
    
        # (M-Step) 
        valk <- numeric(5)
        valk[1] <- mean(E)
        valk[2] <- sum(E * d) / sum(E) 
        valk[3] <- sum((1-E) * d) / (sum(1-E))
        valk[4] <- sum(E * (d - valk[2]) ** 2) / sum(E)
        valk[5] <- sum((1-E) * (d - valk[3]) ** 2) / sum(1 - E)
        return(valk)
}


Get_EM <- function(Data, s0, tolerance = 1e-4) {
    I <- function() {
        k <<- k + 1
    }
    Temp <- em_algorithm(Data, s0)
    if (all(abs(Temp - s0) < tolerance)) {
        names(Temp) <- c("Pr", "Mu:1", "Mu:2", "Variance:1", "Variance:2")
        return(list(Iter = k, Res = Temp))
    } else {
        I()
        s0 <- Temp 
        Get_EM(Data, s0)
    }

}


x <- faithful$waiting
s0 <- c(0.5, 40, 90, 16, 16)
k <- 0
Get_EM(Data = x, s0 = s0)
```

    $Iter
    [1] 24

    $Res
            Pr       Mu:1       Mu:2 Variance:1 Variance:2 
     0.3608856 54.6148403 80.0910594 34.4710583 34.4304249 

``` r
## BootStrap section 
result <- Get_EM(Data = x, s0 = s0)$Res 

prob <- result[1] 
m1 <- result[2]
m2 <- result[3]
s1 <- result[4]
s2 <- result[5]

N1 <- round(prob * dim(faithful)[1], 0)
N2 <- dim(faithful)[1] - N1
library(plyr)
Boot_result <- raply(1e+3, {
                pr <- runif(1)
                if (pr <= prob) {
                temp <- rnorm(N1, m1, sqrt(s1))
                c(
                    MEAN = mean(temp), 
                    Variance = var(temp),
                    INDEX = 1
                )
            } else {
                temp <- rnorm(N1, m2, sqrt(s2))
            c(
                MEAN = mean(temp), 
                Variance = var(temp), 
                INDEX = 2
            )   
            }   
        }) |> as.data.frame()


dim(Boot_result)
```

    [1] 1000    3

``` r
head(Boot_result)
```

          MEAN Variance INDEX
    1 55.02490 39.32665     1
    2 54.69535 29.82158     1
    3 79.85845 45.71665     2
    4 55.16395 22.70279     1
    5 80.54149 31.52718     2
    6 80.31668 29.70273     2

``` r
dat <- Boot_result[, c("MEAN", "Variance")]

aggregate(dat, by = list(Boot_result$INDEX), FUN = mean)
```

      Group.1     MEAN Variance
    1       1 54.61540 34.39032
    2       2 80.07389 34.48049
