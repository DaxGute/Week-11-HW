"""
Description: For Part 1, this program creates a silly text effect in the terminal window. 
After getting the user's input, it calls a recursive function that creates and returns a 
string, where each letter of the original text is repeated n times.
Name: Daxton Gutekunst
Date: Sep. 25 2021
"""

def stext_iterative(text, num):
    """
    Purpose: This function is passed in a string and number. For each charecter in the string
    it is repeated the amount of times the number specifies. This is the test implementation with
    a for loop.
    Parameters: the text, the number of times each charecter should be repeated
    Return Val: the reformated text
    """
    newString = ""
    for i in text:
        newString += i*num

    return newString

def stext_recursive(text, num):
    """
    Purpose: This function is passed in a string and number. For each charecter in the string
    it is repeated the amount of times the number specifies. This is the recursive implementation 
    as specified from the project description.
    Parameters: the text, the number of times each charecter should be repeated
    Return Val: the reformated text
    """
    if len(text) != 1:
        newString = stext_recursive(text[1:], num)
        return text[0:1]*num + newString
    else:
        return text[0:1]*num


def main():
    text = input("string: ")
    num = int(input("num: "))

    print("\nfor_loop: " + stext_iterative(text, num))
    print("recursive: " + stext_recursive(text, num))

main()