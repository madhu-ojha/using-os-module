import os
import sys

fileName = "add.py"

# Checks whether the file exists or not
path1 = os.access(fileName, os.F_OK)
print("Exist path: ", path1)     

# Checks whether the file can be read or not
path2 = os.access(fileName, os.R_OK)
print("Acccess to read the file: ", path2)

# Checks whether the file can be  written or not
path3 = os.access(fileName, os.W_OK)
print("Access to write the file: ", path3)

# Checks whether the file has the permission to execute
path4 = os.access(fileName, os.X_OK)
print("Access to execute the file: ", path4)
 