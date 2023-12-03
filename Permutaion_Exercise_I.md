# Permutaion exercise

#### Suppose we want to make 6-digit numbers with numbers 1, 2, 3, 4, 5 and 6 without repetition. If we arrange the numbers in ascending order, what number will be the 319th number?

<br><br>

#### Answer:

$$
\begin{aligned}
& \text{Total Numbers} = \underline{6} \times \underline{5} \times \underline{4} \times \underline{3} \times \underline{2} \times \underline{1} = 720 \\
& \text{sort numbers:}~~ 123456, ~ 123465, ~ 123546, \dots,~ 165432, 213456, 213465, \dots,~ 265431, 312456, 312465,   \\
& \dots,~ 365432, 412356, \dots,~ 465432, 512346, \dots,~ 565432, 612345, \dots,~ 654321 \\
& \text{the number of numbers whose first digit on the left is 1:}~ \underline{5} \times \underline{4} \times \underline{3} \times \underline{2} \times \underline{1} = 120, \\
& \text{the number of numbers whose first digit on the left is 2:}~ \underline{5} \times \underline{4} \times \underline{3} \times \underline{2} \times \underline{1} = 120, \\
& \text{the number of numbers whose first digit on the left is 3:}~ \underline{5} \times \underline{4} \times \underline{3} \times \underline{2} \times \underline{3} = 120, \\
& 120 + 120 + 120 = 360 \implies \\
& \text{the number we want, the first digit on the left should be 3.} \\ 
& \text{the number of numbers whose first digit on the left is 3 and whose} \\ 
& \text{second digit on the left is 1:}~ \underline{4} \times \underline{3} \times \underline{2} \times \underline{3} = 24, \\
& 240 + 24 = 264, \quad 319 - 264 = 55 \implies  \\
& \text{So if the number 2 is the second digit on the left, the number of digits} \\
& \text{that can be created will reach 24 and the total digits will be 288 in ascending order and so on.} \\
& \text{If we continue after 2, the second digit on the left,} \\
& \text{considering that 3 is the first digit on the left, becomes 4, } \\
& \text{which again becomes the number in ascending order:} ~ 288 + 24 = 312 \\
& \text{we see that there are still 7 numbers left to reach the 319th number,}\\
& \text{so the second digit on the left side of the said number must be 5.} \\
& \text{The number of numbers whose first digit on the left is 3, second digit on the} \\
& \text{left is 5, and third digit on the left is 1:}~ \underline{3} \times \underline{2} \times \underline{1} = 6 \\
& 312 + 6 = 318 \implies \text{There is still one number left, so the third digit on the left is 2.}\\
& \text{According to the remaining digits, it is easy to see that The Answer is:}~ 352146
\end{aligned}
$$

<br><br>

<hr>
<hr>

<br>

#### Answer with python:

``` python
import itertools
import numpy as np
digit_list = [1, 2, 3, 4, 5, 6]
n = len(digit_list)
temp1 = list(itertools.permutations(digit_list, n))
n2 = len(temp1)
myarr = np.array(temp1).reshape(n2, n)
my_temp_list = np.array([1e+5, 1e+4, 1e+3, 1e+2, 1e+1, 1e+0])

def temp_fun(x):
    return int(sum(x * my_temp_list))
result = np.apply_along_axis(func1d = temp_fun, axis = 1, arr = myarr)
result.sort()

print(""" 
The number of permutations of six-digit numbers from numbers\n 1, 2, 3, 4, 5 and 6: {}, \n\n 
The first few digits of six-digit numbers are created:\n {}, \n\n
The 319th number: {}.
""".format(n2, result[0:4], result[318]))
```

     
    The number of permutations of six-digit numbers from numbers
     1, 2, 3, 4, 5 and 6: 720, 

     
    The first few digits of six-digit numbers are created:
     [123456 123465 123546 123564], 


    The 319th number: 352146.
