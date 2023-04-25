import os
import shutil

path = input("Enter the path to the directory: ")
type = input("Specify if you what to organize by\n 1 - first letter\n 2 - by extension: ")
files = os.listdir(path)

if type == "1":
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]
        if extension:
            if os.path.exists(path+'/'+file[0]):
                shutil.move(path+'/'+file, path+'/'+file[0]+'/'+file)
            else:
                os.makedirs(path+'/'+file[0])
                shutil.move(path+'/'+file, path+'/'+file[0]+'/'+file)
                                              
elif type == "2":
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]
        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        else:
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
                                    