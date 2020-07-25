# =============================================================================
# Using os to locate the directory containing all the files
# =============================================================================
import os

path = os.chdir("C:\\Users\\amita\\Desktop\\test")

i = 0
# =============================================================================
# Running a for loop to iterate through all files in the directory.
# Declaring a format for how we want the files to be named, suffixed by the extension.
# =============================================================================
for file in os.listdir(path):
    new_file_name = "pic{}.jpg".format(i)
    os.rename(file, new_file_name)
    i = i+1
