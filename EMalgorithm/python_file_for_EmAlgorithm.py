import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

n = 1000
m = 100
seed = 1234
x = stats.norm.rvs(size = n, loc = 10, scale = 2, 
                   random_state = seed)
Missing = np.random.choice(np.arange(0, n), size = m) 
x[Missing] = np.nan


def EM(dat, mu0, sd0, tol = 1e-6, iter = 2e+3): 
    x_impute = dat.copy()
    k = 0
    muk = []
    muk.append(mu0)
    sdd = []
    sdd.append(sd0)
    while True: 
        # Expectation step 
        x_impute[Missing] = muk[k]
        # Maximization step 
        k += 1
        muk.append(x_impute.mean())
        sdd.append(x_impute.std())
        temp = np.abs(np.array([muk[k] - muk[k-1], sdd[k] - sdd[k-1]]))
        if np.all(temp < tol) or k > iter:
            break
    return dict(Mean_estimate = muk, STD_esimate = sdd, Num_Iteration = k + 1)



# define Initial values
mu0 = 8
sd0 = 1

result = EM(dat = x, mu0 = mu0, sd0 = sd0)
    
print(f"""
      Estimate of mu: {result['Mean_estimate'][-1]}, \n 
      Estimate of mu: {result['STD_esimate'][-1]}, \n
      Number of Iteration: {result['Num_Iteration']}
      """)
    

# visualize estimates across iteration 
fig, ax = plt.subplots(2, 1, figsize = (9, 9))
xx = np.arange(0, 9)
# x
ax[0].plot(xx, result["Mean_estimate"])
ax[0].plot((0, 4, 9), (10, 10, 10), c = 'red', linestyle = 'dotted', label = r"$\mu = 10$")
ax[0].set_xlabel("Iteration")
ax[0].set_ylabel(r"$\mu$")
ax[0].legend()

# x
ax[1].plot(xx, result["STD_esimate"])
ax[1].plot((0, 4, 9), (2, 2, 2), c = 'red', linestyle = 'dotted', label = r"$\sigma = 2$")
ax[1].set_xlabel("Iteration")
ax[1].set_ylabel(r"$\mu$")
ax[1].legend()
plt.show()