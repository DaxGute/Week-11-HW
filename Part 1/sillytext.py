"""
Description: For Part 1, this program creates a silly text effect in the terminal window.
After getting the user's input, it calls a recursive function that creates and returns a
string, where each letter of the original text is repeated n times.
Name: Daxton Gutekunst
Date: Sep. 25 2021
"""

def repeatText_iterative(text, num):
    """
    Purpose: This function is passed in a string and number. For each charecter in the string
    it is repeated the amount of times the number specifies. This is the test implementation with
    a for loop.
    Parameters: the text (str), the number of times each charecter should be repeated (int)
    Return Val: the reformated text (str)
    """
    newString = ""
    for i in text:
        newString += i*num

    return newString

def repeatText_recursive(text, num):
    """
    Purpose: This function is passed in a string and number. For each charecter in the string
    it is repeated the amount of times the number specifies. This is the recursive implementation
    as specified from the project description.
    Parameters: the text (str), the number of times each charecter should be repeated (int)
    Return Val: the reformated text (str)
    """
    if len(text) == 1:
        return text[0:1]*num
    else:
        return text[0:1]*num + repeatText_recursive(text[1:], num)

def getNum(): 
    while True:
        userInput = input("num: ")

        try: 
            num = int(userInput)
            if 0 <= num:
                return num
            else:
                print("Please enter a number greater than or equal to 0!")
        except:
            print("Please enter a number!")


def main():
    text = input("string: ")
    num = getNum()

    print("\nfor_loop: " + repeatText_iterative(text, num))
    print("recursive: " + repeatText_recursive(text, num))

main()
