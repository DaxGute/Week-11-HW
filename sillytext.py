def stext_iterative(text, num):
    newString = ""
    for i in text:
        newString += i*num

    return newString

def stext_recursive(text, num):
    if len(text) != 1:
        newString = stext_recursive(text[1:], num)
        return text[0:1]*num + newString
    else:
        return text[0:1]*num




def main():
    text = input("string: ")
    num = int(input("num: "))

    print(stext_iterative(text, num))
    print(stext_recursive(text, num))

main()