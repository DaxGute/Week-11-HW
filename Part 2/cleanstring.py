"""
    Description: For Part 2, this program prompts the user to enter a string and a character
    to remove and removes all occurrences of the character from the string. It also checks the
    character entered is indeed a single character.
    Author: Daxton Gutekunst
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
        if text[0] == char:
            return clean_recursive(text[1:], char)
        else:
            return text[0] + clean_recursive(text[1:], char)
       
def getChar():
    """
    Purpose: This function gets the input of a user and checks that it has the correct format
    Parameters: None
    Return Val: Valid input (string)"""
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
