from os import listdir
from os.path import isdir, expanduser

"""
Description: For Part 3, this progra allows the user to search for filenames containing a given 
pattern in a given directory. It prompts the user to enter a directory to search and a pattern 
to look for, then prints the names of all filenames contained within the given directory that
contains the given pattern.
Name: Daxton Gutekunst
Date: Sep. 25 2021
"""

def fsearch_recursive(path, pattern):
    """
    Purpose: This function is passed in a file path and a string. The computer iterates through
    every directory and subdirectory in this file path and then prints out all full paths that 
    contain the string.
    Parameters: the full path to search through, the string that should be looked for
    Return Val: None (just the print statements)
    """
    for filename in listdir(path):
        fullpath = path+"/"+filename
        if isdir(fullpath):
            fsearch_recursive(fullpath, pattern)
        else:
            if (filename.find(pattern) != -1):
                print(fullpath)
        

def main():
    fullPath = input("path: ")
    pattern = input("pattern: ")
    if fullPath[0] == "~": # if there a ~, it signals the computer to fill in the path before it
        fullPath = expanduser("~/")[:-1] + fullPath[1:]
    

    # there is in for_loop version as it actually seems that recursive might be the way to go
    fsearch_recursive(fullPath, pattern)

main()