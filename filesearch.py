from os import listdir
from os.path import isdir, expanduser

def fsearch_recursive(path, pattern):
  #  print(listdir(path))
    for filename in listdir(path):
        fullpath = path+"/"+filename
        if isdir(fullpath):
            fsearch_recursive(fullpath, pattern)
        else:
            if (filename.find(pattern) != -1):
                print(fullpath)
        

      


def main():
    path = input("path: ")
    pattern = input("pattern: ")
    fullPath = expanduser("~/")[:-1] + path

    fsearch_recursive(fullPath, pattern)

main()