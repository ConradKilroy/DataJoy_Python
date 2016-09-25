# First we import the **pandas** module with the alias `pd`
import pandas as pd

# The data file used in this example has 258 000 records of the
# most popular names in the US from 1880 to 2008, is divided in columns:
# `year`, `name`, `percent`, `sex`
thenames = pd.read_csv(
    'baby-names.csv',           # file name
    sep=',',                    # column separator
    quotechar='"',              # quoting character
    na_values=0,                # fill missing values with 0
    usecols=[0,1,2,3],          # columns to use
    decimal='.')                # symbol for decimals

# Below a list of some data manipulation and printing commands:

# ---

# `head()` prints the first 5 records
print('\n First 5 records')
print thenames.head() 

# **Output**:
# ```
#  First 5 records
#    year     name   percent  sex
# 0  1880     John  0.081541  boy
# 1  1880  William  0.080511  boy
# 2  1880    James  0.050057  boy
# 3  1880  Charles  0.045167  boy
# 4  1880   George  0.043292  boy
# ```

# ---

# `tail()` prints the last 5 records
print('\n Last 5 records')
print thenames.tail() 

# **Output**:
# ```
#  Last 5 records
#         year      name   percent   sex
# 257995  2008  Carleigh  0.000128  girl
# 257996  2008     Iyana  0.000128  girl
# 257997  2008    Kenley  0.000127  girl
# 257998  2008    Sloane  0.000127  girl
# 257999  2008   Elianna  0.000127  girl
# ```

# ---

# Slice rows from 3 to 8
print('\n Slice rows from 3 to 8')
slice1 = thenames[3:9]
print slice1

# **Output**:
# ```
# Slice rows from 3 to 8
#       year     name   percent  sex
#    3  1880  Charles  0.045167  boy
#    4  1880   George  0.043292  boy
#    5  1880    Frank  0.027380  boy
#    6  1880   Joseph  0.022229  boy
#    7  1880   Thomas  0.021401  boy
#    8  1880    Henry  0.020641  boy
# ```

# ---

# Slice columns year and sex only
print('\n Slice columns year and sex only')
slice2 = thenames[['year', 'sex']]
print slice2.head()

# **Output**
# ```
#  Slice columns year and sex only
#       year  sex
#    0  1880  boy
#    1  1880  boy
#    2  1880  boy
#    3  1880  boy
#    4  1880  boy
# ```

# ---

# Slice rows 5-11 and columns `name` and `sex`
print('\n Slice rows 5-11 and columns "name" and "sex"')
slice3 = thenames.ix[5:12,['year','sex']]
print slice3

# **Output**:
# ```
#  Slice rows 5-11 and columns name and sex
#         year  sex
#     5   1880  boy
#     6   1880  boy
#     7   1880  boy
#     8   1880  boy
#     9   1880  boy
#     10  1880  boy
#     11  1880  boy
#     12  1880  boy
# ```

# ---

# Select only people called Peter
print('\n Select only persons called Peter')
Peter = thenames[thenames['name'] == 'Peter']
print Peter.head()

#  **Output**:
# ```
#  Select only persons called Peter
#             year   name   percent  sex
#       30    1880  Peter  0.004189  boy
#       1036  1881  Peter  0.003952  boy
#       2035  1882  Peter  0.003778  boy
#       3035  1883  Peter  0.004000  boy
#       4033  1884  Peter  0.004269  boy
# ```

# ---

# Keep only `year` and `percent` of the name Peter
print('\n Keep only "year" and "percent"of the name Peter')
Peter = Peter.ix[0:,['year','percent']]
print Peter.head()

# **Output**
# ```
# Keep only year and percent of the name Peter
#             year   percent
#       30    1880  0.004189
#       1036  1881  0.003952
#       2035  1882  0.003778
#       3035  1883  0.004000
#       4033  1884  0.004269
# ```
