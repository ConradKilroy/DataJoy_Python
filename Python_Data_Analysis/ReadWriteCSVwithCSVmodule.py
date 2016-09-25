# This example reads a file named *smallsample.cvs* whose column labels are
# `first_name`, `last_name`, `company_name`, `address`, `city`, `county`,
# `postal`, `phone1`, `phone2`, `email`, `web`. First the **csv** module is
# imported.
import csv

# Now a new dialect called `mydialect` is created, the default dialect is
# *excel*
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)
    
# Now we open and print the file and create an iterable object with the
# `reader()` routine, then we use a `for` loop to print the data.
#The `with` statement automatically closes the file when finished.
print('\n Output from an iterable object created from the csv file')
with open('smallsample.csv', 'rb') as mycsvfile:
    thedata = csv.reader(mycsvfile, dialect='mydialect')
    for row in thedata:
        print(row[0]+"\t \t"+row[1]+"\t \t"+row[4])

# **Output**:
# ```
#  Output from an iterable object created from the csv file
# first_name      last_name               city
# Aleshia         Tomkiewicz              St. Stephens Ward
# Evan            Zigomalas               Abbey Ward
# France          Andrade                 East Southbourne and Tuckton W
# Ulysses         Mcwalters               Hawerby cum Beesby
# Tyisha          Veness                  Greets Green and Lyng Ward
# Eric            Rampy                   Desborough
# Marg            Grasmick                Bargate Ward
# Laquita         Hisaw                   Chirton Ward
# Lura            Manzella                Staple Hill Ward
# ```

# ---

# Dictionary From CSV File
# ------------------------

# This example opens the file and makes a dictionary whose keys are the
# entries in the first row of the data file. The `DictReader()` routine
# accomplished this.
# The `with` statement automatically closes the file when finished
print("\n Now the output from a dictionary created from the csv file")
with open('smallsample.csv', 'rb') as mycsvfile:
    dictofdata = csv.DictReader(mycsvfile, dialect='mydialect')
    for row in dictofdata:
        print(row['first_name']+"\t "+row['phone1']+"\t "+row['city'])

# **Output**:
# ```
#  Now the output from a dictionary created from the csv file
# Aleshia  01835-703597    St. Stephens Ward
# Evan     01937-864715    Abbey Ward
# France   01347-368222    East Southbourne and Tuckton W
# Ulysses  01912-771311    Hawerby cum Beesby
# Tyisha   01547-429341    Greets Green and Lyng Ward
# Eric     01969-886290    Desborough
# Marg     01865-582516    Bargate Ward
# Laquita  01746-394243    Chirton Ward
# Lura     01907-538509    Staple Hill Ward
# ```

# ---

# Write An Array To A CSV File
# ----------------------------

# Now an example about writing, a file called *mydata.csv* with the contents of
# the array `arrayofdata` will be created. The file is created by the
# `writer()` routine, then each row is written with `writerow()`.
# The `with` statement automatically closes the file when finished
arrayofdata=[[1,2,4,5,'something','spam',2.334],
             [3,1,6,3,'anything','spam',0]]
             
with open('mydata.csv', 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
    for row in arrayofdata:
        thedatawriter.writerow(row)
