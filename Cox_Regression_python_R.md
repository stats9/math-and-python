# sample code for implement cox regression using python and R


``` r
if (!require(gtsummary)) {
    chooseCRANmirror(ind = 1, graphics = FALSE)
    install.packages("gtsummary")
    library(gtsummary)
}
```

    Loading required package: gtsummary

    Warning: package 'gtsummary' was built under R version 4.3.3

``` r
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

dat |> 
    mutate(inst = factor(inst))
```

        inst time status age sex ph.ecog ph.karno pat.karno meal.cal wt.loss
    2      3  455      2  68   1       0       90        90     1225      15
    4      5  210      2  57   1       1       90        60     1150      11
    6     12 1022      1  74   1       1       50        80      513       0
    7      7  310      2  68   2       2       70        60      384      10
    8     11  361      2  71   2       2       60        80      538       1
    9      1  218      2  53   1       1       70        80      825      16
    10     7  166      2  61   1       2       70        70      271      34
    11     6  170      2  57   1       1       80        80     1025      27
    15    12  567      2  57   1       1       80        70     2600      60
    17    22  613      2  70   1       1       90       100     1150      -5
    18    16  707      2  63   1       2       50        70     1025      22
    19     1   61      2  56   2       2       60        60      238      10
    21    11  301      2  67   1       1       80        80     1025      17
    22     6   81      2  49   2       0      100        70     1175      -8
    24    15  371      2  58   1       0       90       100      975      13
    26    12  520      2  70   2       1       90        80      825       6
    27     4  574      2  60   1       0      100       100     1025     -13
    28    13  118      2  70   1       3       60        70     1075      20
    29    13  390      2  53   1       1       80        70      875      -7
    30     1   12      2  74   1       2       70        50      305      20
    31    12  473      2  69   2       1       90        90     1025      -1
    32     1   26      2  73   1       2       60        70      388      20
    34    16  107      2  60   2       2       50        60      925     -15
    35    12   53      2  61   1       2       70       100     1075      10
    37    22  814      2  65   1       2       70        60      513      28
    38    15  965      1  66   2       1       70        90      875       4
    39     1   93      2  74   1       2       50        40     1225      24
    40     1  731      2  64   2       1       80       100     1175      15
    41     5  460      2  70   1       1       80        60      975      10
    42    11  153      2  73   2       2       60        70     1075      11
    43    10  433      2  59   2       0       90        90      363      27
    45     7  583      2  68   1       1       60        70     1025       7
    46     7   95      2  76   2       2       60        60      625     -24
    47     1  303      2  74   1       0       90        70      463      30
    48     3  519      2  63   1       1       80        70     1025      10
    49    13  643      2  74   1       0       90        90     1425       2
    50    22  765      2  50   2       1       90       100     1175       4
    53    21   53      2  68   1       0       90       100     1025       0
    54     1  246      2  58   1       0      100        90     1175       7
    55     6  689      2  59   1       1       90        80     1300      15
    57     5    5      2  65   2       0      100        80      338       5
    59     3  687      2  58   2       1       80        80     1225      10
    60     1  345      2  64   2       1       90        80     1075      -3
    61    22  444      2  75   2       2       70        70      438       8
    62    12  223      2  48   1       1       90        80     1300      68
    64    11   60      2  65   2       1       90        80     1025       0
    65     3  163      2  69   1       1       80        60     1125       0
    66     3   65      2  68   1       2       70        50      825       8
    68     5  821      1  64   2       0       90        70     1025       3
    69    22  428      2  68   1       0      100        80     1039       0
    70     6  230      2  67   1       1       80       100      488      23
    71    13  840      1  63   1       0       90        90     1175      -1
    72     3  305      2  48   2       1       80        90      538      29
    73     5   11      2  74   1       2       70       100     1175       0
    75    21  226      2  53   2       1       90        80      825       3
    76    12  426      2  71   2       1       90        90     1075      19
    77     1  705      2  51   2       0      100        80     1300       0
    78     6  363      2  56   2       1       80        70     1225      -2
    80     1  176      2  73   1       0       90        70      169      30
    81     4  791      2  59   1       0      100        80      768       5
    82    13   95      2  55   1       1       70        90     1500      15
    83    11  196      1  42   1       1       80        80     1425       8
    84    21  167      2  44   2       1       80        90      588      -1
    85    16  806      1  44   1       1       80        80     1025       1
    86     6  284      2  71   1       1       80        90     1100      14
    87    22  641      2  62   2       1       80        80     1150       1
    88    21  147      2  61   1       0      100        90     1175       4
    89    13  740      1  44   2       1       90        80      588      39
    90     1  163      2  72   1       2       70        70      910       2
    91    11  655      2  63   1       0      100        90      975      -1
    93     5   88      2  66   1       1       90        80      875       8
    94    10  245      2  57   2       1       80        60      280      14
    96    12   30      2  72   1       2       80        60      288       7
    99    11  477      2  64   1       1       90       100      910       0
    101    1  559      1  58   2       0      100       100      710      15
    102    6  450      2  69   2       1       80        90     1175       3
    106   12  156      2  66   1       1       80        90      875      14
    107   26  529      1  54   2       1       80       100      975      -3
    109   21  429      2  55   1       1      100        80      975       5
    110    3  351      2  75   2       2       60        50      925      11
    111   13   15      2  69   1       0       90        70      575      10
    112    1  181      2  44   1       1       80        90     1175       5
    113   10  283      2  80   1       1       80       100     1030       6
    116    1   13      2  76   1       2       70        70      413      20
    117    3  212      2  49   1       2       70        60      675      20
    118    1  524      2  68   1       2       60        70     1300      30
    119   16  288      2  66   1       2       70        60      613      24
    120   15  363      2  80   1       1       80        90      346      11
    122   26  199      2  60   2       2       70        80      675      10
    123    3  550      2  69   2       1       70        80      910       0
    124   11   54      2  72   1       2       60        60      768      -3
    125    1  558      2  70   1       0       90        90     1025      17
    126   22  207      2  66   1       1       80        80      925      20
    127    7   92      2  50   1       1       80        60     1075      13
    128   12   60      2  64   1       1       80        90      993       0
    129   16  551      1  77   2       2       80        60      750      28
    131    4  293      2  59   2       1       80        80      925      52
    133    6  353      2  47   1       0      100        90     1225       5
    135    1  267      2  67   1       0       90        70      313       6
    136   22  511      1  74   2       2       60        40       96      37
    139    1  457      2  54   1       1       90        90      975      -5
    140    5  337      2  56   1       0      100       100     1500      15
    141   21  201      2  73   2       2       70        60     1225     -16
    142    3  404      1  74   1       1       80        70      413      38
    143   26  222      2  76   1       2       70        70     1500       8
    144    1   62      2  65   2       1       80        90     1075       0
    145   11  458      1  57   1       1       80       100      513      30
    147   16  353      2  71   1       0      100        80      775       2
    148   16  163      2  54   1       1       90        80     1225      13
    149   12   31      2  82   1       0      100        90      413      27
    151   13  229      2  70   1       1       70        60     1175      -2
    155   32  156      2  55   1       2       70        30     1025      10
    158    4  291      2  62   1       2       70        60      475      27
    159   12  179      2  63   1       1       80        70      538      -2
    160    1  376      1  56   2       1       80        90      825      17
    161   32  384      1  62   2       0       90        90      588       8
    162   10  268      2  44   2       1       90       100     2450       2
    163   11  292      1  69   1       2       60        70     2450      36
    164    6  142      2  63   1       1       90        80      875       2
    165    7  413      1  64   1       1       80        70      413      16
    166   16  266      1  57   2       0       90        90     1075       3
    168   21  320      2  46   1       0      100       100      860       4
    169    6  181      2  61   1       1       90        90      730       0
    170   12  285      2  65   1       0      100        90     1025       0
    171   13  301      1  61   1       1       90       100      825       2
    172    2  348      2  58   2       0       90        80     1225      10
    173    2  197      2  56   1       1       90        60      768      37
    174   16  382      1  43   2       0      100        90      338       6
    175    1  303      1  53   1       1       90        80     1225      12
    176   13  296      1  59   2       1       80       100     1025       0
    177    1  180      2  56   1       2       60        80     1225      -2
    179    1  145      2  53   2       1       80        90      588      13
    180    7  269      1  74   2       0      100       100      588       0
    181   13  300      1  60   1       0      100       100      975       5
    182    1  284      1  39   1       0      100        90     1225      -5
    185   12  292      1  51   2       0       90        80     1225       0
    186   12  332      1  45   2       0       90       100      975       5
    187    2  285      2  72   2       2       70        90      463      20
    188    3  259      1  58   1       0       90        80     1300       8
    189   15  110      2  64   1       1       80        60     1025      12
    190   22  286      2  53   1       0       90        90     1225       8
    191   16  270      2  72   1       1       80        90      488      14
    194    1  225      1  64   1       1       90        80      825      33
    195   22  269      2  71   1       1       90        90     1300      -2
    196   12  225      1  70   1       0      100       100     1175       6
    197   32  243      1  63   2       1       80        90      825       0
    199    1  276      1  52   2       0      100        80      975       0
    200   32  135      2  60   1       1       90        70     1275       0
    201   15   79      2  64   2       1       90        90      488      37
    202   22   59      2  73   1       1       60        60     2200       5
    203   32  240      1  63   2       0       90       100     1025       0
    204    3  202      1  50   2       0      100       100      635       1
    205   26  235      1  63   2       0      100        90      413       0
    208   13  239      2  50   2       2       60        60     1025      -3
    211    1  252      1  60   2       0      100        90      488      -2
    212    6  221      1  67   1       1       80        70      413      23
    213   15  185      1  69   1       1       90        70     1075       0
    216   11  222      1  65   1       1       90        70     1025      18
    218   21  183      2  76   1       2       80        60      825       7
    219   11  211      1  70   2       2       70        30      131       3
    220    2  175      1  57   2       0       80        80      725      11
    221   22  197      1  67   1       1       80        90     1500       2
    222   11  203      1  71   2       1       80        90     1025       0
    225   13  191      1  39   1       0       90        90     2350      -5
    226   32  105      1  75   2       2       60        70     1025       5
    227    6  174      1  66   1       1       90       100     1075       1
    228   22  177      1  58   2       1       80        90     1060       0

``` r
names(dat)
```

     [1] "inst"      "time"      "status"    "age"       "sex"       "ph.ecog"  
     [7] "ph.karno"  "pat.karno" "meal.cal"  "wt.loss"  

``` r
Model <- coxph(Y ~ ph.ecog + ph.karno + inst, data = dat)
Model |> tbl_regression()
```

<div id="wjtlunszxl" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>#wjtlunszxl table {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
&#10;#wjtlunszxl thead, #wjtlunszxl tbody, #wjtlunszxl tfoot, #wjtlunszxl tr, #wjtlunszxl td, #wjtlunszxl th {
  border-style: none;
}
&#10;#wjtlunszxl p {
  margin: 0;
  padding: 0;
}
&#10;#wjtlunszxl .gt_table {
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
&#10;#wjtlunszxl .gt_caption {
  padding-top: 4px;
  padding-bottom: 4px;
}
&#10;#wjtlunszxl .gt_title {
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
&#10;#wjtlunszxl .gt_subtitle {
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
&#10;#wjtlunszxl .gt_heading {
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
&#10;#wjtlunszxl .gt_bottom_border {
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}
&#10;#wjtlunszxl .gt_col_headings {
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
&#10;#wjtlunszxl .gt_col_heading {
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
&#10;#wjtlunszxl .gt_column_spanner_outer {
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
&#10;#wjtlunszxl .gt_column_spanner_outer:first-child {
  padding-left: 0;
}
&#10;#wjtlunszxl .gt_column_spanner_outer:last-child {
  padding-right: 0;
}
&#10;#wjtlunszxl .gt_column_spanner {
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
&#10;#wjtlunszxl .gt_spanner_row {
  border-bottom-style: hidden;
}
&#10;#wjtlunszxl .gt_group_heading {
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
&#10;#wjtlunszxl .gt_empty_group_heading {
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
&#10;#wjtlunszxl .gt_from_md > :first-child {
  margin-top: 0;
}
&#10;#wjtlunszxl .gt_from_md > :last-child {
  margin-bottom: 0;
}
&#10;#wjtlunszxl .gt_row {
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
&#10;#wjtlunszxl .gt_stub {
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
&#10;#wjtlunszxl .gt_stub_row_group {
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
&#10;#wjtlunszxl .gt_row_group_first td {
  border-top-width: 2px;
}
&#10;#wjtlunszxl .gt_row_group_first th {
  border-top-width: 2px;
}
&#10;#wjtlunszxl .gt_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#wjtlunszxl .gt_first_summary_row {
  border-top-style: solid;
  border-top-color: #D3D3D3;
}
&#10;#wjtlunszxl .gt_first_summary_row.thick {
  border-top-width: 2px;
}
&#10;#wjtlunszxl .gt_last_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}
&#10;#wjtlunszxl .gt_grand_summary_row {
  color: #333333;
  background-color: #FFFFFF;
  text-transform: inherit;
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#wjtlunszxl .gt_first_grand_summary_row {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-top-style: double;
  border-top-width: 6px;
  border-top-color: #D3D3D3;
}
&#10;#wjtlunszxl .gt_last_grand_summary_row_top {
  padding-top: 8px;
  padding-bottom: 8px;
  padding-left: 5px;
  padding-right: 5px;
  border-bottom-style: double;
  border-bottom-width: 6px;
  border-bottom-color: #D3D3D3;
}
&#10;#wjtlunszxl .gt_striped {
  background-color: rgba(128, 128, 128, 0.05);
}
&#10;#wjtlunszxl .gt_table_body {
  border-top-style: solid;
  border-top-width: 2px;
  border-top-color: #D3D3D3;
  border-bottom-style: solid;
  border-bottom-width: 2px;
  border-bottom-color: #D3D3D3;
}
&#10;#wjtlunszxl .gt_footnotes {
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
&#10;#wjtlunszxl .gt_footnote {
  margin: 0px;
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#wjtlunszxl .gt_sourcenotes {
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
&#10;#wjtlunszxl .gt_sourcenote {
  font-size: 90%;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 5px;
  padding-right: 5px;
}
&#10;#wjtlunszxl .gt_left {
  text-align: left;
}
&#10;#wjtlunszxl .gt_center {
  text-align: center;
}
&#10;#wjtlunszxl .gt_right {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
&#10;#wjtlunszxl .gt_font_normal {
  font-weight: normal;
}
&#10;#wjtlunszxl .gt_font_bold {
  font-weight: bold;
}
&#10;#wjtlunszxl .gt_font_italic {
  font-style: italic;
}
&#10;#wjtlunszxl .gt_super {
  font-size: 65%;
}
&#10;#wjtlunszxl .gt_footnote_marks {
  font-size: 75%;
  vertical-align: 0.4em;
  position: initial;
}
&#10;#wjtlunszxl .gt_asterisk {
  font-size: 100%;
  vertical-align: 0;
}
&#10;#wjtlunszxl .gt_indent_1 {
  text-indent: 5px;
}
&#10;#wjtlunszxl .gt_indent_2 {
  text-indent: 10px;
}
&#10;#wjtlunszxl .gt_indent_3 {
  text-indent: 15px;
}
&#10;#wjtlunszxl .gt_indent_4 {
  text-indent: 20px;
}
&#10;#wjtlunszxl .gt_indent_5 {
  text-indent: 25px;
}
</style>

| **Characteristic**                                                                                                                                               | **log(HR)**<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;"><sup>1</sup></span> | **95% CI**<span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;"><sup>1</sup></span> | **p-value** |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------|
| ph.ecog                                                                                                                                                          | 0.83                                                                                                                            | 0.38, 1.3                                                                                                                      | \<0.001     |
| ph.karno                                                                                                                                                         | 0.02                                                                                                                            | 0.00, 0.04                                                                                                                     | 0.10        |
| inst                                                                                                                                                             | -0.03                                                                                                                           | -0.05, 0.00                                                                                                                    | 0.036       |
| <span class="gt_footnote_marks" style="white-space:nowrap;font-style:italic;font-weight:normal;"><sup>1</sup></span> HR = Hazard Ratio, CI = Confidence Interval |                                                                                                                                 |                                                                                                                                |             |

</div>
