def clean_iterative(text, char):
    newString = ""
    for i in text:
        if i != char:
            newString += i

    return newString

def clean_recursive(text, char):
    if len(text) != 1:
        newString = clean_recursive(text[1:], char)
        if text[0] == char:
            return newString
        else:
            return text[0] + newString 
    else:
        if text[0] == char:
            return ""
        else:
            return text[0]




def main():
    text = input("string: ")
    char = input("char: ")

    print(clean_iterative(text, char))
    print(clean_recursive(text, char))

main()