# sample code for implement cox regression using python and R


# Using R

``` r
# if (!require(gtsummary)) {
#     chooseCRANmirror(ind = 1, graphics = FALSE)
#     install.packages("gtsummary")
#     library(gtsummary)
# }

# if (!require(stargazer)) {
#     chooseCRANmirror(ind = 1, graphics = FALSE)
#     install.packages("stargazer")
#     library(stargazer)
# }

library(survival)
lung |> names()
```

     [1] "inst"      "time"      "status"    "age"       "sex"       "ph.ecog"  
     [7] "ph.karno"  "pat.karno" "meal.cal"  "wt.loss"  

``` r
lung$status |> table()
```


      1   2 
     63 165 

``` r
dat <- na.omit(lung)
Y <- with(dat, Surv(time, status == 2))



names(dat)
```

     [1] "inst"      "time"      "status"    "age"       "sex"       "ph.ecog"  
     [7] "ph.karno"  "pat.karno" "meal.cal"  "wt.loss"  

``` r
Model <- coxph(Y ~ ph.ecog + ph.karno, data = dat)
Model |> summary()
```

    Call:
    coxph(formula = Y ~ ph.ecog + ph.karno, data = dat)

      n= 167, number of events= 120 

                coef exp(coef) se(coef)     z Pr(>|z|)    
    ph.ecog  0.70837   2.03067  0.21362 3.316 0.000913 ***
    ph.karno 0.01615   1.01628  0.01138 1.419 0.155816    
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

             exp(coef) exp(-coef) lower .95 upper .95
    ph.ecog      2.031     0.4924    1.3360     3.087
    ph.karno     1.016     0.9840    0.9939     1.039

    Concordance= 0.62  (se = 0.03 )
    Likelihood ratio test= 14.51  on 2 df,   p=7e-04
    Wald test            = 14.48  on 2 df,   p=7e-04
    Score (logrank) test = 14.7  on 2 df,   p=6e-04

``` r
# Model |> tbl_regression()
# stargazer(Model)
```

------------------------------------------------------------------------

------------------------------------------------------------------------

# Using Python

``` python
import numpy as np
import pandas as pd
from lifelines import CoxPHFitter

cph = CoxPHFitter()
dat_py = r.dat
dat_py.head()
```

       inst    time  status   age  ...  ph.karno  pat.karno  meal.cal  wt.loss
    2   3.0   455.0     2.0  68.0  ...      90.0       90.0    1225.0     15.0
    4   5.0   210.0     2.0  57.0  ...      90.0       60.0    1150.0     11.0
    6  12.0  1022.0     1.0  74.0  ...      50.0       80.0     513.0      0.0
    7   7.0   310.0     2.0  68.0  ...      70.0       60.0     384.0     10.0
    8  11.0   361.0     2.0  71.0  ...      60.0       80.0     538.0      1.0

    [5 rows x 10 columns]

``` python
dat2 = dat_py[['time', 'status', 'ph.ecog', 'ph.karno']]
dat2.head()
```

         time  status  ph.ecog  ph.karno
    2   455.0     2.0      0.0      90.0
    4   210.0     2.0      1.0      90.0
    6  1022.0     1.0      1.0      50.0
    7   310.0     2.0      2.0      70.0
    8   361.0     2.0      2.0      60.0

``` python
dat2['status'] = dat2['status'].replace([1, 2], [0, 1])
dat2.head()
```

         time  status  ph.ecog  ph.karno
    2   455.0     1.0      0.0      90.0
    4   210.0     1.0      1.0      90.0
    6  1022.0     0.0      1.0      50.0
    7   310.0     1.0      2.0      70.0
    8   361.0     1.0      2.0      60.0

``` python
model_cardio_cox_ph = cph.fit(df = dat2, duration_col = 'time', event_col = 'status')
model_cardio_cox_ph.print_summary()  # access the individual results using cph.summary
```

    <lifelines.CoxPHFitter: fitted with 167 total observations, 47 right-censored observations>
                 duration col = 'time'
                    event col = 'status'
          baseline estimation = breslow
       number of observations = 167
    number of events observed = 120
       partial log-likelihood = -500.86
             time fit was run = 2024-04-23 00:59:11 UTC

    ---
               coef exp(coef)  se(coef)  coef lower 95%  coef upper 95% exp(coef) lower 95% exp(coef) upper 95%
    covariate                                                                                                  
    ph.ecog    0.71      2.03      0.21            0.29            1.13                1.34                3.09
    ph.karno   0.02      1.02      0.01           -0.01            0.04                0.99                1.04

               cmp to    z      p  -log2(p)
    covariate                              
    ph.ecog      0.00 3.32 <0.005     10.10
    ph.karno     0.00 1.42   0.16      2.68
    ---
    Concordance = 0.62
    Partial AIC = 1005.73
    log-likelihood ratio test = 14.51 on 2 df
    -log2(p) of ll-ratio test = 10.47
