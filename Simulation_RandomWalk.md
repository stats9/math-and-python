# Random Walk


- [Define Prolbem](#define-prolbem)
  - [section (a)](#section-a)
    - [python coding](#python-coding)
  - [section (b):](#section-b)
    - [Generate Plots](#generate-plots)
    - [Generate Bell Shaped Graph](#generate-bell-shaped-graph)

# Define Prolbem

$$
\begin{aligned} 
& X_i = \pm 1, \quad X_i = \begin{cases}+ 1: & p \\ -1: & q = (1-p) \end{cases}\to \\
& S_n = \sum_{i = 1}^n X_i, \\
& N: 10, \quad n = 100. 
\end{aligned} 
$$

## section (a)

### python coding

``` python
## load libraries
import numpy as np 
import matplotlib.pyplot as plt 

def RanodmWalk(N = 10, n = 100, prob = 0.5): 
    Person_randomWalk = np.zeros([N, n], dtype = int)
    for i in range(N): 
        Person_randomWalk[i, :] = np.random.choice((1, -1), 
            size = n, replace = True, p = [prob, 1- prob])
    Person_sn = np.zeros([N, n], dtype = float)
    for i in range(N):
        temp = Person_randomWalk[i, :]  
        Person_sn[i, :] = temp.cumsum() 
    Person_sn_scale = 1/np.sqrt(n) * Person_sn
    result = {'Person_randomWalk': Person_randomWalk, 
                'Person_sn': Person_sn, 
                'Person_sn_scale': Person_sn_scale}
    return result
simulation = RanodmWalk(N = 10, n = 100, prob = 0.5)

Person_RandomWalk = simulation['Person_randomWalk']

for j in range(10): 
    print(f'random Walk of Person {(j + 1)}:\n')
    print(Person_RandomWalk[j, :])
    print("\n")
```

    random Walk of Person 1:

    [-1  1  1  1 -1 -1  1  1  1  1 -1  1  1  1  1  1  1 -1 -1 -1  1  1 -1  1
     -1 -1  1  1 -1  1  1  1 -1  1  1  1 -1  1 -1  1  1  1 -1 -1  1  1 -1  1
      1 -1 -1  1  1 -1 -1 -1  1 -1 -1 -1 -1  1 -1  1  1 -1 -1  1  1 -1 -1  1
     -1 -1  1  1  1  1  1 -1  1 -1 -1  1 -1 -1  1 -1  1  1  1 -1 -1  1  1 -1
      1 -1 -1  1]


    random Walk of Person 2:

    [-1  1  1 -1  1 -1 -1 -1 -1 -1  1 -1 -1 -1 -1 -1  1 -1  1 -1  1 -1  1 -1
     -1 -1  1 -1  1  1  1 -1  1 -1 -1  1 -1  1  1  1 -1  1  1  1  1  1  1  1
     -1 -1  1 -1  1  1  1 -1  1 -1  1 -1 -1  1  1  1  1  1  1  1  1 -1  1  1
      1 -1 -1  1  1 -1 -1  1  1 -1 -1  1  1 -1 -1  1 -1 -1  1  1  1  1 -1  1
      1 -1  1 -1]


    random Walk of Person 3:

    [ 1 -1 -1 -1  1 -1 -1  1  1 -1  1  1 -1  1  1  1  1  1 -1  1  1 -1  1 -1
      1 -1 -1 -1  1 -1 -1  1 -1  1  1  1 -1 -1  1  1  1  1  1  1  1  1  1  1
      1 -1  1  1  1 -1 -1 -1 -1  1  1  1  1  1 -1 -1 -1  1 -1  1  1 -1  1  1
      1 -1 -1 -1 -1 -1 -1  1 -1 -1 -1 -1  1 -1  1 -1  1 -1 -1 -1 -1 -1 -1 -1
      1 -1 -1 -1]


    random Walk of Person 4:

    [-1  1 -1  1  1 -1  1  1  1  1  1  1  1 -1  1  1  1  1  1  1  1  1  1 -1
     -1 -1  1 -1 -1 -1 -1  1  1 -1  1 -1  1 -1 -1 -1 -1 -1 -1  1 -1  1 -1  1
     -1  1  1 -1 -1 -1  1 -1 -1 -1  1 -1 -1  1 -1 -1 -1  1 -1 -1  1 -1  1  1
      1  1  1 -1  1 -1  1  1 -1  1  1 -1 -1 -1 -1 -1 -1  1 -1  1 -1  1 -1 -1
      1  1  1  1]


    random Walk of Person 5:

    [ 1  1  1  1  1  1 -1  1 -1 -1  1  1 -1  1  1  1 -1  1 -1  1  1 -1  1 -1
     -1  1  1 -1 -1 -1  1  1 -1 -1 -1 -1 -1  1  1 -1  1 -1  1  1 -1 -1 -1 -1
      1 -1 -1  1  1  1  1 -1 -1  1  1 -1  1 -1  1  1  1  1  1 -1 -1 -1  1  1
      1  1 -1 -1  1  1 -1  1 -1  1  1 -1 -1  1  1 -1  1 -1 -1 -1  1 -1  1 -1
      1 -1  1  1]


    random Walk of Person 6:

    [ 1  1 -1  1  1  1 -1  1 -1  1 -1  1 -1  1 -1  1 -1  1 -1 -1 -1  1  1  1
     -1  1  1 -1 -1  1 -1 -1  1  1 -1 -1 -1 -1 -1  1  1  1 -1  1  1  1  1  1
     -1 -1 -1 -1 -1  1  1  1  1 -1  1 -1  1  1 -1 -1  1  1  1  1 -1  1 -1  1
      1 -1  1 -1 -1 -1  1 -1  1  1  1  1 -1 -1 -1  1  1  1 -1 -1 -1  1 -1 -1
     -1  1 -1 -1]


    random Walk of Person 7:

    [ 1  1  1  1 -1 -1 -1 -1 -1 -1  1  1 -1 -1 -1  1 -1 -1 -1  1 -1 -1  1  1
     -1  1 -1  1 -1  1  1  1  1  1 -1  1  1 -1  1 -1 -1 -1  1 -1 -1  1 -1  1
      1 -1  1 -1  1  1  1  1  1 -1 -1  1  1 -1  1  1  1 -1 -1 -1  1 -1  1 -1
     -1  1 -1 -1 -1 -1  1  1 -1  1 -1 -1 -1 -1  1  1 -1  1 -1 -1 -1  1  1 -1
      1 -1 -1  1]


    random Walk of Person 8:

    [ 1 -1 -1  1 -1  1 -1  1  1 -1  1  1  1  1 -1 -1  1  1  1 -1  1 -1 -1 -1
      1  1  1  1 -1 -1 -1  1  1 -1 -1  1 -1  1 -1  1  1 -1 -1 -1 -1 -1 -1 -1
      1 -1  1 -1  1  1 -1 -1  1 -1 -1 -1  1 -1  1 -1  1 -1  1  1  1  1 -1  1
     -1 -1 -1  1  1 -1 -1  1  1 -1 -1 -1  1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1  1
      1 -1  1 -1]


    random Walk of Person 9:

    [ 1 -1  1  1  1 -1  1  1  1 -1  1  1  1  1  1 -1  1  1  1  1  1 -1 -1 -1
     -1 -1  1  1 -1 -1 -1 -1  1 -1 -1  1 -1 -1  1 -1 -1 -1 -1 -1 -1  1 -1 -1
     -1 -1 -1  1  1  1  1  1 -1 -1 -1  1 -1  1 -1 -1  1 -1 -1  1  1 -1 -1  1
     -1 -1 -1 -1  1  1 -1  1 -1  1 -1  1  1  1  1 -1  1 -1  1 -1  1 -1  1  1
     -1 -1  1 -1]


    random Walk of Person 10:

    [-1 -1  1 -1 -1  1 -1 -1  1  1  1  1  1  1 -1 -1  1 -1 -1  1 -1 -1 -1  1
     -1 -1 -1 -1 -1 -1 -1  1 -1 -1  1 -1  1 -1  1 -1 -1  1 -1  1 -1  1 -1 -1
     -1  1  1 -1  1 -1 -1  1  1 -1 -1  1 -1  1 -1  1  1 -1  1 -1  1  1 -1  1
     -1 -1  1  1  1  1  1 -1  1 -1  1  1 -1  1  1 -1 -1  1 -1  1  1  1  1 -1
      1  1  1 -1]

## section (b):

### Generate Plots

``` python
nn = np.arange(1, 101)
Person_sn_scale = simulation['Person_sn_scale']
fig, ax = plt.subplots(4, 3, figsize = (24, 24))
plt.subplots_adjust(left=0.1, bottom=0.5, 
    right = 0.4, top = 0.8, wspace = 0.5, hspace = 0.5)
count = 0 
for i in range(4): 
    for j in range(3):
        if (i == 3):
            y = Person_sn_scale[9, :]
            ax[i, 1].plot(nn, y)
            ax[i, 1].set_title("Person: 10")
            ax[i, 1].set_xlabel(r"$n$")
            ax[i, 1].set_ylabel(r"$\frac{S_n}{\sqrt{n}}$")
            break 
        y = Person_sn_scale[count, :]
        count += 1
        tit = "Person: " + str(count)
        ax[i, j].plot(nn, y)
        ax[i, j].set_title(tit)
        ax[i, j].set_xlabel(r"$n$")
        ax[i, j].set_ylabel(r"$\frac{S_n}{\sqrt{n}}$")

lis = ['top', 'right', 'left', 'bottom']
for i in lis: 
    ax[3, 0].spines[i].set_visible(False)
    ax[3, 2].spines[i].set_visible(False)
ax[3, 0].set_xticks([])
ax[3, 0].set_yticks([])
ax[3, 2].set_xticks([])
ax[3, 2].set_yticks([])

plt.show()
```

![scale Sn for Random Walk by
Person](Simulation_RandomWalk_files/figure-commonmark/cell-3-output-1.png)

### Generate Bell Shaped Graph

``` python
from scipy import stats
def nsim_simulation(nsim = int(1e+4), prob = 0.5, n = 100, N = 10): 
    sum_Person = np.zeros([N, nsim], dtype = int)
    for i in range(nsim): 
        temp = RanodmWalk(N = N, n = n, prob = prob)
        res_person = temp['Person_randomWalk']
        for j in range(N):
            temp2 = res_person[j, :]
            temp3 = temp2.sum()
            sum_Person[j, i] = temp3 
    return sum_Person 


Person_sn = nsim_simulation() 
fig, ax = plt.subplots(4, 3, figsize = (24, 24))
plt.subplots_adjust(left=0.1, bottom=0.5, 
    right = 0.4, top = 0.8, wspace = 0.5, hspace = 0.5)
count = 0 
for i in range(4): 
    for j in range(3):
        if (i == 3):
            y = Person_sn[9, :]
            stdd = y.std() 
            mm = y.mean() 
            minn = y.min() 
            maxx = y.max() 
            xx = np.linspace(minn, maxx, num = 500)
            y2 = stats.norm.pdf(xx, loc = mm, scale = stdd)
            ax[i, 1].hist(y, density = True)
            ax[i, 1].plot(xx, y2, color = 'red')
            ax[i, 1].set_title("Person: 10")
            ax[i, 1].set_xlabel("")
            ax[i, 1].set_ylabel(r"$S_n$")
            break 
        y = Person_sn[count, :]
        stdd = y.std() 
        mm = y.mean() 
        minn = y.min() 
        maxx = y.max() 
        xx = np.linspace(minn, maxx, num = 500)
        y2 = stats.norm.pdf(xx, loc = mm, scale = stdd)
        count += 1
        tit = "Person: " + str(count)
        ax[i, j].hist(y, density = True)
        ax[i, j].plot(xx, y2, color = 'red')
        ax[i, j].set_title(tit)
        ax[i, j].set_xlabel(r"$S_n$")
        ax[i, j].set_ylabel("")

lis = ['top', 'right', 'left', 'bottom']
for i in lis: 
    ax[3, 0].spines[i].set_visible(False)
    ax[3, 2].spines[i].set_visible(False)
ax[3, 0].set_xticks([])
ax[3, 0].set_yticks([])
ax[3, 2].set_xticks([])
ax[3, 2].set_yticks([])

plt.show()
```

![Bell-Shaped Graph for Simulation Sn by
Persons](Simulation_RandomWalk_files/figure-commonmark/cell-4-output-1.png)
