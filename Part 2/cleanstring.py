"""
Description: For Part 2, this program prompts the user to enter a string and a character
to remove and removes all occurrences of the character from the string. It also checks the
character entered is indeed a single character.
Name: Daxton Gutekunst
Date: Sep. 25 2021
"""

def clean_iterative(text, char):
    """
    Purpose: This function is passed in a string and char. For each charecter in the string
    that matches the passed charecter, it is removed. This is the test implementation with
    a for loop.
    Parameters: the text (str), the char that should be eliminated (str)
    Return Val: the reformated text
    """
    newString = ""
    for i in text:
        if i != char:
            newString += i

    return newString

def clean_recursive(text, char):
    """
    Purpose: This function is passed in a string and char. For each charecter in the string
    that matches the passed charecter, it is removed. This is the implementation with a recursive
    function.
    Parameters: the text (str), the char that should be eliminated (str)
    Return Val: the reformated text (str)
    """
    if len(text) == 0:
        return ""
    else:
        newString = clean_recursive(text[1:], char)
        if text[0] == char:
            return newString
        else:
            return text[0] + newString
       
def getChar():
    while True:
        char = input("ch    : ")
        if len(char) == 1:
            return char
        else:
            print("Invalid. Please enter a single character")
        

def main():
    text = input("string: ")
    char = getChar()

    print("\nfor_loop: " + clean_iterative(text, char))
    print("recursive: " + clean_recursive(text, char))

main()
