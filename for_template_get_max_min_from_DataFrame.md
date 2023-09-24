# Stats9 Template Code

## Here I want to include a code example that shows how to extract minimum and maximum values from part of the rows of a data structure and add them to the data frame as separate

## columns at the end.

``` python
import numpy as np
import pandas as pd
dict = {'year' : list(np.repeat(1991, 5)),
'month' : list(np.repeat(4, 5)), 'day': list(np.arange(21, 26))}
df = pd.DataFrame(dict)
date_col = pd.to_datetime(df)
dat = {'case': list(np.repeat(1, 5)), 
                    'Reg_ins': [8, 6.33, 9, 6.33, 5.5], 
                    'NPH_ins': [13, 13, 13, 14, 14], 
                    'Pr_brkfst_glu': [100, 216, 257, 239, 67], 
                    'Pr_lnch_glu': [135, 59, 73, 41, 100], 
                    'Pr_sup_glu': [119, 211, 129, 129, 206]}
dat = pd.DataFrame(dat)
dat['date'] = date_col
clist = np.array(list(dat.columns))
clist_new = list(clist[np.array([-1, 0, 1, 2, 3, 4, 5])])
df_new = dat[clist_new]
def get_min(x):
    y = x[[1, 2, 3]]
    y.min()
cols = list(df_new.columns)

nrow = df_new.shape[0]
min_glu = []
for i in range(nrow):
    x = df_new.iloc[i, 4:7]
    min_glu.append(x.min())
    
max_glu = []
for i in range(nrow):
    x = df_new.iloc[i, 4:7]
    max_glu.append(x.max())

df_new.loc[:, 'min_glu'] = pd.Series(min_glu, index = df_new.index) 
df_new.loc[:, 'max_glu'] = pd.Series(max_glu, index = df_new.index)
df_new
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
&#10;    .dataframe tbody tr th {
        vertical-align: top;
    }
&#10;    .dataframe thead th {
        text-align: right;
    }
</style>

|     | date       | case | Reg_ins | NPH_ins | Pr_brkfst_glu | Pr_lnch_glu | Pr_sup_glu | min_glu | max_glu |
|-----|------------|------|---------|---------|---------------|-------------|------------|---------|---------|
| 0   | 1991-04-21 | 1    | 8.00    | 13      | 100           | 135         | 119        | 100     | 135     |
| 1   | 1991-04-22 | 1    | 6.33    | 13      | 216           | 59          | 211        | 59      | 216     |
| 2   | 1991-04-23 | 1    | 9.00    | 13      | 257           | 73          | 129        | 73      | 257     |
| 3   | 1991-04-24 | 1    | 6.33    | 14      | 239           | 41          | 129        | 41      | 239     |
| 4   | 1991-04-25 | 1    | 5.50    | 14      | 67            | 100         | 206        | 67      | 206     |

</div>
