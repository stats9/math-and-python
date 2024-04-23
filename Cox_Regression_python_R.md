# sample code for implement cox regression using python and R


``` r
if (!require(gtsummary)) {
    chooseCRANmirror(ind = 1, graphics = FALSE)
    install.packages("gtsummary")
    library(gtsummary)
}

if (!require(stargazer)) {
    chooseCRANmirror(ind = 1, graphics = FALSE)
    install.packages("stargazer")
    library(stargazer)
}

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
Model |> tbl_regression()
```

<div id="rslvumbjwg" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>#rslvumbjwg table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
&#10;#rslvumbjwg thead, #rslvumbjwg tbody, #rslvumbjwg tfoot, #rslvumbjwg tr, #rslvumbjwg td, #rslvumbjwg th {
  border-style: none;
}
&#10;#rslvumbjwg p {
  margin: 0;
  padding: 0;
}
&#10;#rslvumbjwg .gt_table {
  display: table;
  border-collapse: collapse;
  line-height: normal;
  margin-left: auto;
  margin-right: auto;
  color: #333333;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  background-color: #FFFFFF;
  width: auto;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #A8A8A8;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #A8A8A8;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
}
&#10;#rslvumbjwg .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}
&#10;#rslvumbjwg .gt_title {
  color: #333333;
  font-size: 125%;
  font-weight: initial;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-color: #FFFFFF;
  border-bottom-width: 0;
}
&#10;#rslvumbjwg .gt_subtitle {
  color: #333333;
  font-size: 85%;
  font-weight: initial;
  padding-top: 3px;
  padding-bottom: 5px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-color: #FFFFFF;
  border-top-width: 0;
}
&#10;#rslvumbjwg .gt_heading {
  background-color: #FFFFFF;
  text-align: center;
  border-bottom-color: #FFFFFF;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}
&#10;#rslvumbjwg .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}
&#10;#rslvumbjwg .gt_col_headings {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
}
&#10;#rslvumbjwg .gt_col_heading {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 6px;
  padding-left: 5px;
  padding-right: 5px;
  overflow-x: hidden;
}
&#10;#rslvumbjwg .gt_column_spanner_outer {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: normal;
  text-transform: inherit;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
}
&#10;#rslvumbjwg .gt_column_spanner_outer:first-child {
  padding-left: 0;
}
&#10;#rslvumbjwg .gt_column_spanner_outer:last-child {
  padding-right: 0;
}
&#10;#rslvumbjwg .gt_column_spanner {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: bottom;
  padding-top: 5px;
  padding-bottom: 5px;
  overflow-x: hidden;
  display: inline-block;
  width: 100%;
}
&#10;#rslvumbjwg .gt_spanner_row {
  border-bottom-style: hidden;
}
&#10;#rslvumbjwg .gt_group_heading {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  text-align: left;
}
&#10;#rslvumbjwg .gt_empty_group_heading {
  padding: 0.5px;
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  vertical-align: middle;
}
&#10;#rslvumbjwg .gt_from_md > :first-child {
  margin-top: 0;
}
&#10;#rslvumbjwg .gt_from_md > :last-child {
  margin-bottom: 0;
}
&#10;#rslvumbjwg .gt_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  margin: 10px;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 1px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 1px;
  border-right-color: #D3D3D3;
  vertical-align: middle;
  overflow-x: hidden;
}
&#10;#rslvumbjwg .gt_stub {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#rslvumbjwg .gt_stub_row_group {
  color: #333333;
  background-color: #FFFFFF;
  font-size: 100%;
  font-weight: initial;
  text-transform: inherit;
  border-right-style: solid;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
  padding-left: 5px;
  padding-right: 5px;
  vertical-align: top;
}
&#10;#rslvumbjwg .gt_row_group_first td {
  border-top-width: 2px;
}
&#10;#rslvumbjwg .gt_row_group_first th {
  border-top-width: 2px;
}
&#10;#rslvumbjwg .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#rslvumbjwg .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}
&#10;#rslvumbjwg .gt_first_summary_row.thick {
  border-top-width: 2px;
}
&#10;#rslvumbjwg .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}
&#10;#rslvumbjwg .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#rslvumbjwg .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}
&#10;#rslvumbjwg .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}
&#10;#rslvumbjwg .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}
&#10;#rslvumbjwg .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}
&#10;#rslvumbjwg .gt_footnotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}
&#10;#rslvumbjwg .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#rslvumbjwg .gt_sourcenotes {
  color: #333333;
  background-color: #FFFFFF;
  border-bottom-style: none;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
  border-left-style: none;
  border-left-width: 2px;
  border-left-color: #D3D3D3;
  border-right-style: none;
  border-right-width: 2px;
  border-right-color: #D3D3D3;
}
&#10;#rslvumbjwg .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#rslvumbjwg .gt_left {
  text-align: left;
}
&#10;#rslvumbjwg .gt_center {
  text-align: center;
}
&#10;#rslvumbjwg .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
&#10;#rslvumbjwg .gt_font_normal {
  font-weight: normal;
}
&#10;#rslvumbjwg .gt_font_bold {
  font-weight: bold;
}
&#10;#rslvumbjwg .gt_font_italic {
  font-style: italic;
}
&#10;#rslvumbjwg .gt_super {
  font-size: 65%;
}
&#10;#rslvumbjwg .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}
&#10;#rslvumbjwg .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}
&#10;#rslvumbjwg .gt_indent_1 {
  text-indent: 5px;
}
&#10;#rslvumbjwg .gt_indent_2 {
  text-indent: 10px;
}
&#10;#rslvumbjwg .gt_indent_3 {
  text-indent: 15px;
}
&#10;#rslvumbjwg .gt_indent_4 {
  text-indent: 20px;
}
&#10;#rslvumbjwg .gt_indent_5 {
  text-indent: 25px;
}
</style>

| **Characteristic**                                                                                                                                               | **log(HR)**<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;"><sup>1</sup></span> | **95% CI**<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;"><sup>1</sup></span> | **p-value** |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------|
| ph.ecog                                                                                                                                                          | 0.71                                                                                                                            | 0.29, 1.1                                                                                                                      | \<0.001     |
| ph.karno                                                                                                                                                         | 0.02                                                                                                                            | -0.01, 0.04                                                                                                                    | 0.2         |
| <span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;"><sup>1</sup></span> HR = Hazard Ratio, CI = Confidence Interval |                                                                                                                                 |                                                                                                                                |             |

</div>

``` r
# stargazer(Model)
```

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
             time fit was run = 2024-04-23 00:54:51 UTC

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
