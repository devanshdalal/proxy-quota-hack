# Author: Devansh Dalal, Ashish Ranjan
# License: GNU GENERAL PUBLIC LICENSE Version 3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
# Version: 1.0

# For Ubuntu
# import os

# os.system('cat abc* > abc.mp4')

import glob

# If your parts have name as abc_1, abc_2, etc. use FILE_PARTS_NAME as abc*
FILE_PARTS_NAME = "abc*"
# Set the original file name here, with extension. In this case the original file was abc.mp4
ORIGINAL_FILE_NAME = "abc.mp4"

read_files = glob.glob(FILE_PARTS_NAME)

with open(ORIGINAL_FILE_NAME, "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
