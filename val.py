import os
import shutil

source = input("C:/Users/suman/Downloads/Test.txt")
destination = input('C:/Users/suman/Downloads/Test(copy).txt')

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file), destination)