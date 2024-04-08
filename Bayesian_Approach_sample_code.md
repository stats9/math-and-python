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

                mean    se_mean       sd        2.5%        25%        50%
    mu      1.468024 0.03581471 1.027171  -0.5256586   0.771898   1.468235
    sigma   5.680435 0.06422639 1.817603   3.1604211   4.460527   5.391058
    lp__  -21.415562 0.03390003 0.974238 -23.9876929 -21.811615 -21.117385
                 75%      97.5%    n_eff     Rhat
    mu      2.204107   3.414318 822.5499 1.007008
    sigma   6.465182  10.004080 800.8867 1.005766
    lp__  -20.721916 -20.471456 825.9049 1.002122

``` r
End_time <- Sys.time()
(R_Elapse_time <- difftime(End_time, Init_time, units = 'sec'))
```

    Time difference of 40.62546 secs

``` r
install.packages("reticulate")
```

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
    trace = pm.sample(500)
```

    █

     |----------------------------------------| 0.00% [0/6000 00:00<? Sampling 4 chains, 0 divergences]

     |-------------------------------------| 0.02% [1/6000 00:00<00:00 Sampling 4 chains, 0 divergences]

     |-------------------------------------| 0.03% [2/6000 00:00<00:00 Sampling 4 chains, 0 divergences]

     |-------------------------------------| 0.05% [3/6000 00:00<00:00 Sampling 4 chains, 0 divergences]

     |-------------------------------------| 0.07% [4/6000 00:00<00:00 Sampling 4 chains, 0 divergences]

     |-------------------------------------| 0.08% [5/6000 00:00<00:00 Sampling 4 chains, 0 divergences]

     |████████████████████████████████| 100.00% [6000/6000 00:01<00:00 Sampling 4 chains, 0 divergences]
    Auto-assigning NUTS sampler...
    Initializing NUTS using jitter+adapt_diag...
    Multiprocess sampling (4 chains in 4 jobs)
    NUTS: [mu]
    Sampling 4 chains for 1_000 tune and 500 draw iterations (4_000 + 2_000 draws total) took 9 seconds.

``` python
    
# Print the summary of the inference results
print(pm.summary(trace))
```

         mean     sd  hdi_3%  hdi_97%  ...  mcse_sd  ess_bulk  ess_tail  r_hat
    mu  4.996  0.301   4.475    5.565  ...    0.007     908.0    1442.0    1.0

    [1 rows x 9 columns]

``` python
end_time = time.process_time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
```

    Elapsed time: 1.703125 seconds
