import os

"""
could directly read all of the files under current 
but cannot recursively get all the subfolders 
"""

# files = os.listdir("logs")
# print(files)

def read_dir(dir):
    res = []
    files = os.listdir(dir)
    
    for file in files: 
        f = dir + '/' + file
        if os.path.isdir(f):
            # merge the current list with the resulted list from 
            # the subfolder
            res += read_dir(f)
        else: 
            res.append(f)
    
    return res 