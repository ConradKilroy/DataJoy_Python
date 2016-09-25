# First, the module is imported with the alias `np`
import numpy as np

# Read Numpy Array From  File
# ---------------------------

# Read the file `sample.csv` and store some of it contents in the numpy array
# `thedata` by means of the `genfromtxt()` function.
thedata = np.genfromtxt(
    'sample.csv',           # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=',',          # column delimiter
    dtype='float32',        # data type
    filling_values=0,       # fill missing values with 0
    usecols = (0,2,3,5),    # columns to read
    names=['first', 'second', 'third', 'last'])     # column names
                        
print("\n Printing the data from the csv file.\n")
for row in thedata:
    print(row)

# **Output**:

# ```
#  Printing the data from the csv file.
#  
# (10.399999618530273, 13.0, 0.0, 16.540000915527344)
# (9.0, 52.0, 93.0, 6.0)
# (1.0, 4.0, 4.0, -3.0)
# (14.0, 13.0, 67.0, 43.0)
# (21.0, 14.0, 44.0, 0.0)
# (3.200000047683716, 5.0, 14.0, 1.0)
# ```

# ---

# Save Numpy Array To File
# ------------------------

# In this example the data in the array `thedata` is saved to the file
# `mydata.csv` by the `savetxtx()` routine.

np.savetxt(
    'mydata.csv',           # file name
    thedata,                # array to save
    fmt='%.2f',             # formatting, 2 digits in this case
    delimiter=',',          # column delimiter
    newline='\n',           # new line character
    footer='end of file',   # file footer
    comments='# ',          # character to use for comments
    header='Data generated by numpy')      # file header
         
# This is the contents of the generated file:

# ```
# # Data generated by numpy
# 10.40,13.00,0.00,16.54
# 9.00,52.00,93.00,6.00
# 1.00,4.00,4.00,-3.00
# 14.00,13.00,67.00,43.00
# 21.00,14.00,44.00,0.00
# 3.20,5.00,14.00,1.00
# # end of file
# ```
