# os module in python provide funtion for interactting with the operating system 
import os

# os.mkdir() creates a directory, error comes if directory already asists
#os.mkdir("c:/class-python/class-99/myfolder1")

directory="myfloder"
parent_dir="c:/class-python/class-99"
mode=0o666
path=os.path.join(parent_dir,directory)
#os.mkdir(path,mode)
#print("directory '%s' created"%directory)

# listing out files and directory
# os.listdir()

path="c:/class-python/class-99"
dir_list=os.listdir(path)
print("files and directory in ",path,":")
print(dir_list)

# deleting directory
#os.remove() removes a file
#os.remove("C:/class-python/class-99/myfloder/file1.txt")

# os.rmdir() is use to remove an empty directory
# OSERROR is rased if not an empty directory 
directory="myfloder"
parent="c:/class-python/class-99"
path=os.path.join(parent,directory)
#os.rmdir(path)

import os
try:
    filename="xyz.txt"
    f=open(filename,'rU')
    text=f.read()
    f.close()
except IOError:
    print("Problem in reading: "+filename)    


import os
result=os.path.exists("abc.txt")
print(result)

# os.walk()
# this meathod generate a file name in  a directory tree by walking the tree in either in top down or bottom, up or manner
# is returns a geerater that create a tupple of values(dirpath, dirnames, filesnames)
for dirpath, dirnames, filenames in os.walk("c:/class-python/class-99"):
    print(dirpath)
    print(dirnames)
    print(filenames)

os.path.split("c:/class-python/class-99/myfolder1")
# returns a tupple of head and tail of the specified path