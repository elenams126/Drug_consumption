## Overview of Data Exploration

### Dataset Overview:
- The dataset contains **1885 entries** and **32 columns**.
- The first 13 columns are **numerical** (with types int64 and float64), while columns 13 to 31 are **categorical** (type object), which seem to hold values like `CL0`, `CL1`, etc.
- No missing values were detected in the dataset, as all columns have a full count of non-null values.
- There are no duplicate rows in the dataset.

### Numerical Data Insights:
- The numerical columns show a wide range of values, with some having extreme values (e.g., column 9 with a minimum value of -3.46 and a maximum of 3.46).
- The summary statistics (mean, standard deviation, min, max, etc.) provide insight into the distribution of these numerical features.
- The correlation matrix shows some moderate correlations between variables, particularly between:
  - Columns 1 and 4 (correlation = 0.354)
  - Columns 11 and 12 (correlation = 0.623)
  - Columns 8 and 12 (correlation = 0.421)
- This suggests there might be interdependencies between some of the numerical features.

### Categorical Data Insights:
- Categorical columns (13 to 31) have **7 unique values** (ranging from `CL0` to `CL6`), with frequencies indicating some dominant categories like `CL0` and `CL6`.
- For example:
  - Column 13 has `CL5` as the most frequent value, with 759 occurrences.
  - Column 31 has `CL0` as the most frequent value, with 1455 occurrences.
- This could indicate a skewness in categorical variables, with some categories being much more common than others.

## First Few Rows of the Dataset

```plaintext
   0        1        2        3        4        5        6   ...   25   26   27   28   29   30   31
0   1  0.49788  0.48246 -0.05921  0.96082  0.12600  0.31287  ...  CL0  CL0  CL0  CL0  CL2  CL0  CL0
1   2 -0.07854 -0.48246  1.98437  0.96082 -0.31685 -0.67825  ...  CL0  CL2  CL3  CL0  CL4  CL0  CL0
2   3  0.49788 -0.48246 -0.05921  0.96082 -0.31685 -0.46725  ...  CL0  CL0  CL0  CL1  CL0  CL0  CL0
3   4 -0.95197  0.48246  1.16365  0.96082 -0.31685 -0.14882  ...  CL0  CL0  CL0  CL0  CL2  CL0  CL0
4   5  0.49788  0.48246  1.98437  0.96082 -0.31685  0.73545  ...  CL1  CL0  CL0  CL2  CL2  CL0  CL0

[5 rows x 32 columns]
```

## Summary Statistics for Numerical Columns

```plaintext
                0           1            2   ...           10           11           12
count  1885.000000  1885.00000  1885.000000  ...  1885.000000  1885.000000  1885.000000
mean    945.294960     0.03461    -0.000256  ...    -0.000386     0.007216    -0.003292
std     545.167641     0.87836     0.482588  ...     0.997523     0.954435     0.963701
min       1.000000    -0.95197    -0.482460  ...    -3.464360    -2.555240    -2.078480
25%     474.000000    -0.95197    -0.482460  ...    -0.652530    -0.711260    -0.525930
50%     946.000000    -0.07854    -0.482460  ...    -0.006650    -0.217120     0.079870
75%    1417.000000     0.49788     0.482460  ...     0.584890     0.529750     0.765400
max    1888.000000     2.59171     0.482460  ...     3.464360     2.901610     1.921730

[8 rows x 13 columns]
```

## Summary Statistics for Categorical Columns

```plaintext
          13    14    15    16    17    18    19  ...    25    26    27    28    29    30    31
count   1885  1885  1885  1885  1885  1885  1885  ...  1885  1885  1885  1885  1885  1885  1885
unique     7     7     7     7     7     7     7  ...     7     7     7     7     7     5     7
top      CL5   CL0   CL0   CL0   CL6   CL6   CL6  ...   CL0   CL0   CL0   CL0   CL6   CL0   CL0
freq     759   976  1305  1000  1385   463   807  ...  1094  1069  1429   982   610  1877  1455

[4 rows x 19 columns]
```

## Missing Values in Each Column

```plaintext
0     0
1     0
2     0
3     0
4     0
5     0
6     0
7     0
8     0
9     0
10    0
11    0
12    0
13    0
14    0
15    0
16    0
17    0
18    0
19    0
20    0
21    0
22    0
23    0
24    0
25    0
26    0
27    0
28    0
29    0
30    0
31    0
dtype: int64
```

## Number of Duplicate Rows: 0

## Correlation Matrix for Numerical Columns

```plaintext
          0         1         2         3   ...        9         10        11        12
0   1.000000 -0.271395 -0.025467 -0.025253  ... -0.028782 -0.072094  0.119663  0.165882
1  -0.271395  1.000000  0.110286  0.158811  ...  0.063504  0.183564 -0.190939 -0.332188
2  -0.025467  0.110286  1.000000  0.196774  ...  0.219743  0.183831 -0.167492 -0.244277
3  -0.025253  0.158811  0.196774  1.000000  ...  0.091088  0.240417 -0.132482 -0.131146
4  -0.340751  0.354241  0.216271  0.225311  ...  0.150921  0.214000 -0.231572 -0.345415
5   0.059309 -0.069753 -0.001213 -0.036099  ... -0.038726 -0.029923  0.082411  0.100304
6   0.018639 -0.136654  0.074646 -0.100993  ... -0.216964 -0.391088  0.174399  0.079988
7  -0.046960 -0.033849  0.057864  0.115645  ...  0.157336  0.308024  0.114151  0.210130
8   0.173565 -0.226778 -0.131021  0.057994  ...  0.038516 -0.056811  0.277512  0.421709
9  -0.028782  0.063504  0.219743  0.091088  ...  1.000000  0.247482 -0.229690 -0.208061
10 -0.072094  0.183564  0.183831  0.240417  ...  0.247482  1.000000 -0.335133 -0.229038
11  0.119663 -0.190939 -0.167492 -0.132482  ... -0.229690 -0.335133  1.000000  0.623120
12  0.165882 -0.332188 -0.244277 -0.131146  ... -0.208061 -0.229038  0.623120  1.000000

[13 rows x 13 columns]
```

## Distribution Plots for Numerical Columns
![Distribution of Column 0](distribution_column_0.png)

![Distribution of Column 1](distribution_column_1.png)

![Distribution of Column 2](distribution_column_2.png)

![Distribution of Column 3](distribution_column_3.png)

![Distribution of Column 4](distribution_column_4.png)

![Distribution of Column 5](distribution_column_5.png)

![Distribution of Column 6](distribution_column_6.png)

![Distribution of Column 7](distribution_column_7.png)

![Distribution of Column 8](distribution_column_8.png)

![Distribution of Column 9](distribution_column_9.png)

![Distribution of Column 10](distribution_column_10.png)

![Distribution of Column 11](distribution_column_11.png)

![Distribution of Column 12](distribution_column_12.png)

## Correlation Heatmap
![Correlation Matrix](correlation_matrix.png)

## Bar Plots for Categorical Columns
![Categorical Column 13](categorical_column_13.png)

![Categorical Column 14](categorical_column_14.png)

![Categorical Column 15](categorical_column_15.png)

![Categorical Column 16](categorical_column_16.png)

![Categorical Column 17](categorical_column_17.png)

![Categorical Column 18](categorical_column_18.png)

![Categorical Column 19](categorical_column_19.png)

![Categorical Column 20](categorical_column_20.png)

![Categorical Column 21](categorical_column_21.png)

![Categorical Column 22](categorical_column_22.png)

![Categorical Column 23](categorical_column_23.png)

![Categorical Column 24](categorical_column_24.png)

![Categorical Column 25](categorical_column_25.png)

![Categorical Column 26](categorical_column_26.png)

![Categorical Column 27](categorical_column_27.png)

![Categorical Column 28](categorical_column_28.png)

![Categorical Column 29](categorical_column_29.png)

![Categorical Column 30](categorical_column_30.png)

![Categorical Column 31](categorical_column_31.png)

