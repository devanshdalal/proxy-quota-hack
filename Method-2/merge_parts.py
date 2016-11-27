# For Ubuntu
# import os

# os.system('cat file* > merged.zip')

import glob

# For your parts with name as abc_1, abc_2, etc. use name as abc*
FILE_PARTS_NAME = "abc*"
# Set the original file name here, with extension. In this case the origin file was abc.mp4
ORIGINAL_FILE_NAME = "abc.mp4"

read_files = glob.glob(FILE_PARTS_NAME)

with open(ORIGINAL_FILE_NAME, "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
