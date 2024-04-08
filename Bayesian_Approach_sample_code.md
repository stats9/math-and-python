# using R and python for estimate mean of normal distribution with prior
normal


## Using R and stan

``` r
# download require packages 

if(!require(rstan)){ 
    options(download.file.method = "libcurl", download.file.extra = "-k")
    chooseCRANmirror(ind = 1, graphics = FALSE)
    install.packages("rstan")
    library(rstan)
}
```

``` r
Init_time <- Sys.time()
library(rstan) # using rstan library

# in window system for using parallel computaion 
options(mc.cores = parallel::detectCores()) 

rstan_options(auto_write = TRUE) # for reduction or avoid reompliation programs

data <- c(2, 4, 6, 8, 1, 3, 5, 7, 9, 10) # my sample data

stan_model <- "
data {
  int<lower=0> N; 
  vector[N] y; 
}
parameters {
  real mu; 
  real<lower=0> sigma;
}
model {
  y ~ normal(mu, sigma);
  mu ~ normal(0, 1);
}
" # define stan model, we can using seperate file for define stan model with 'stan' profix

# Compile the model
sm <- stan_model(model_code = stan_model)

# Perform Bayesian inference
fit <- sampling(sm, data = list(N = length(data), y = data), iter = 1000, chains = 4)

# Print the summary of the inference results
print(summary(fit)$summary)
```

                mean    se_mean       sd        2.5%         25%        50%
    mu      1.450857 0.03756829 1.044504  -0.6658947   0.7872005   1.463015
    sigma   5.771127 0.08045965 1.857379   3.1798358   4.5362943   5.479870
    lp__  -21.476579 0.03919826 1.053638 -24.4801912 -21.8417866 -21.136028
                 75%      97.5%    n_eff     Rhat
    mu      2.172952   3.435238 772.9968 1.004204
    sigma   6.608999  10.226383 532.8986 1.003919
    lp__  -20.733573 -20.472272 722.5188 1.001032

``` r
End_time <- Sys.time()
(R_Elapse_time <- difftime(End_time, Init_time, units = 'sec'))
```

    Time difference of 37.49169 secs

------------------------------------------------------------------------

------------------------------------------------------------------------

## Using Python and PyMC

``` python
import time
start_time = time.process_time() # for get elapsed runnig time in python

data = (2, 4, 6, 8, 1, 3, 5, 7, 9, 10)
import pymc as pm
```

    WARNING (pytensor.tensor.blas): Using NumPy C-API based implementation for BLAS functions.

``` python
# Define the model
with pm.Model() as model:
    # Define the prior
    mu = pm.Normal('mu', mu=0, sigma=1)
    
    # Define the likelihood
    likelihood = pm.Normal('likelihood', mu=mu, sigma=1, observed=data)
    
    # Perform Bayesian inference
    trace = pm.sample(1000)
```

    █

     |----------------------------------------| 0.00% [0/8000 00:00<? Sampling 4 chains, 0 divergences]

     |-------------------------------------| 0.01% [1/8000 00:00<00:00 Sampling 4 chains, 0 divergences]

     |-------------------------------------| 0.03% [2/8000 00:00<00:00 Sampling 4 chains, 0 divergences]

     |-------------------------------------| 0.04% [3/8000 00:00<00:00 Sampling 4 chains, 0 divergences]

     |-------------------------------------| 0.05% [4/8000 00:00<00:00 Sampling 4 chains, 0 divergences]

     |-------------------------------------| 0.06% [5/8000 00:00<00:00 Sampling 4 chains, 0 divergences]

     |████████████████████████████████| 100.00% [8000/8000 00:02<00:00 Sampling 4 chains, 0 divergences]
    Auto-assigning NUTS sampler...
    Initializing NUTS using jitter+adapt_diag...
    Multiprocess sampling (4 chains in 4 jobs)
    NUTS: [mu]
    Sampling 4 chains for 1_000 tune and 1_000 draw iterations (4_000 + 4_000 draws total) took 10 seconds.

``` python
    
# Print the summary of the inference results
print(pm.summary(trace))
```

         mean     sd  hdi_3%  hdi_97%  ...  mcse_sd  ess_bulk  ess_tail  r_hat
    mu  5.008  0.305   4.412     5.55  ...    0.006    1483.0    2627.0    1.0

    [1 rows x 9 columns]

``` python
end_time = time.process_time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
```

    Elapsed time: 1.84375 seconds
