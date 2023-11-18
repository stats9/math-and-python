# Halton Sequence

To generate random numbers using Halton’s method, I have implemented a
function from scratch and then compared the results with the Halton
method that is included in the scipy package. We will see the results
together.

``` python
import numpy as np

def get_halton_num(base, num):
    base_list = []
    i = 0
    while num > 0:
        if num // (base ** i) >= base:
             i += 1
        else:
            if num // (base ** i) == 0:
                base_list.append(0)
                i -= 1
            else:
                base_list.append(num // (base ** i))
                num = num % (base ** i)
                if num == 0 and i != 0:
                    for j in range(i):
                        base_list.append(0)
                    break
                else: 
                    i -= 1
    base_list2 = np.array(base_list)
    base_list2 = base_list2[::-1]
    nn = len(base_list2)
    temp_init = (np.arange(nn) + 1)
    temp_init2 = base ** temp_init
    temp_init2 = 1 / temp_init2
    halton_num = base_list2 * temp_init2
    halton_num = halton_num.sum()
    return halton_num

def get_seq_halton(base, n):
    mylist = np.arange(n) + 1
    mylist = mylist[:(n-1)]
    result = list(map(lambda x: get_halton_num(base = base, num = x), mylist))
    result.insert(0, 0)
    return result

def get_seq_halton2(base1, base2, n, dim = 2):
    xx = get_seq_halton(base = base1, n = n)
    yy = get_seq_halton(base = base2, n = n)
    final_result = np.stack((xx, yy), axis = 1)
    return final_result
get_seq_halton2(base1 = 2, base2 = 3, n = 4, dim = 2)





my_mat = get_seq_halton2(base1 = 2, base2 = 3, n = 10 ** 5, dim = 2)
def f(x):
    res = x[0] ** 2 + x[1] ** 2
    return res
int_result = np.apply_along_axis(f, 1, my_mat)
int_result.mean()




## with package

from scipy.stats.qmc import Halton    
samp = Halton(d = 2, scramble = False, seed = 1)
my_mat2 = samp.random(n = 10 **5)

def f(x):
    res = x[0] ** 2 + x[1] ** 2
    return res
int_result2 = np.apply_along_axis(f, 1, my_mat2)
int_result2.mean()
```

    0.6666154594225222
