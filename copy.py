import os
import shutil

source = input("enter the folder to be copied: ")
dest = input("enter the destination folder: ")

source = source + '/'
dest = dest + '/'

filelist = os.listdir(source)

for file in filelist:
    shutil.copy((source + file), dest)


