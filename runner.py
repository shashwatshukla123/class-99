#shutil.copy() method
import shutil
#source="C:/class-python/sample1.txt"
#destination="C:/class-python/class-99/myfolder1/sample1.txt"

try:
    #shutil.copy(source,destination)
    print("File copied successfully")

except shutil.SameFileError:
    print("Source and destination represents the same file.")

except PermissionError:
    print("Permission denied")
except:
    print("Error occurred while copying file")

#----------------------------------------------------------------

#to know the permission of the file
import os
source="C:/class-python/sample1.txt"
perm=os.stat(source).st_mode
print(perm)

#------------------------------------------------------------------

#if destination is a directory
import os
import shutil
#source="C:/class-python/sample2.txt"
#destination="C:/class-python/class-99/myfolder1"
#dest=shutil.copy(source,destination)

#print(os.listdir(destination))
#print("destination path:",dest)

#------------------------------------------------

#shutil.move() method
#moves file from source to destination
import os
import shutil

path="C:/class-python"
print("Before moving files: ")
print(os.listdir(path))

#moves folder(folder2 with its content --to the destination folder)
#source="C:/class-python/samples"
#destination="C:/class-python/class-99/myfolder1"
#
#dest=shutil.move(source,destination)

print("After moving files: ")
print(os.listdir(path))

#--------------------------------------------------

#shutil.copyfile
#copy the contents of the source file to destination file

#source="C:/class-python/sample3.txt"
#destination="C:/class-python/class-99/myfolder1/sample4.txt"
#
#dest=shutil.copyfile(source,destination)

#-----------------------------------------------
# the below gives error as it is shutil.copyfile 
import shutil

source="C:/class-python/file.txt"
destination="C:/class-python/class-99/myfolder1"

try:
   shutil.copyfile(source,destination)
   print("file copied successfully")
except shutil.SameFileError:
    print("source and destination represents the same file")
except IsADirectoryError:
    print("destination is a directory")
except PermissionError:
    print("Permission denied")
except:
    print("Error occurred while copying file")

#------------------------------------------------------
