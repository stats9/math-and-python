# A counting question


- [Question](#question)
  - [python Answer](#python-answer)

# Question

In how many ways can we divide five different books among three people
(the people are different) so that each person gets at least one book?

## python Answer

``` python
import numpy as np
import copy

# Initialization
ketab = ['a', 'b', 'c', 'd', 'e']
Sett = {'a', 'b', 'c', 'd', 'e'}
Persons = ['one', 'two', 'three']
Result = []

# Generate initial combinations
for i in range(5):
    for j in range(5):
        if i == j:
            continue
        for k in range(5):
            if k == j or k == i:
                continue

            # Assign books to persons
            ashkhas = {'one': {ketab[i]}, 'two': {ketab[j]}, 'three': {ketab[k]}}
            tempSet = {ketab[i], ketab[j], ketab[k]}
            Notassign = Sett.difference(tempSet)

            for person in Persons:
                ashkhas_copy = copy.deepcopy(ashkhas)
                ashkhas_copy[person].update(Notassign)
                Result.append(copy.deepcopy(ashkhas_copy))

                tempList = list(Notassign)
                Person_temp = [p for p in Persons if p != person]

                ashkhas2 = copy.deepcopy(ashkhas)
                ashkhas2[Person_temp[0]].add(tempList[0])
                ashkhas2[Person_temp[1]].add(tempList[1])
                Result.append(copy.deepcopy(ashkhas2))

                ashkhas3 = copy.deepcopy(ashkhas)
                ashkhas3[Person_temp[1]].add(tempList[0])
                ashkhas3[Person_temp[0]].add(tempList[1])
                Result.append(copy.deepcopy(ashkhas3))

# Deduplicate results
Result2 = Result.copy()
len(Result2)
while True:
    n = len(Result2)
    RangeList = list(range(n))
    to_remove = set()

    for i in RangeList:
        for j in RangeList:
            if i >= j:
                continue
            x = Result2[i]
            y = Result2[j]

            # Calculate differences
            num1 = x[Persons[0]].difference(y[Persons[0]])
            num2 = x[Persons[1]].difference(y[Persons[1]])
            num3 = x[Persons[2]].difference(y[Persons[2]])

            res = len(num1) + len(num2) + len(num3)
            if res == 0:
                to_remove.add(j)

    # Remove duplicates
    Result2 = [r for idx, r in enumerate(Result2) if idx not in to_remove]

    # Terminate loop if no changes
    if len(to_remove) == 0:
        break

print(""" 
      The answer to the number of possible ways to distribute five different books among three people varies:
      """, len(Result2))
```

     
          The answer to the number of possible ways to distribute five different books among three people varies:
           150
