

import string

# 1- Given a string, write a Python program to check if it is a palindrome.


def palindrome(txt: str) -> bool:
    txtR = list(reversed(txt))
    txtR = "".join(txtR)
    return txt == txtR


# 2- Given a string, write a Python program to find the longest substring without repeating characters.
def longestSub(myList: list[str]) -> str:
    maxCharacters = ""
    maxWord = ""
    for txt in myList:
        string_list = list(txt)
        unique_strings = list(set(string_list))
        unique_strings = "".join(unique_strings)
        if len(unique_strings) > len(maxCharacters):
            maxWord = txt
            maxCharacters = unique_strings
    return maxWord


# 3 Given a string, write a Python program to remove all punctuation marks from it.
def removeAllPunctuation(txt: str):
    translator = str.maketrans('', '', string.punctuation)
    no_punct = txt.translate(translator)
    return no_punct

# 4 Given a string, write a Python program to check if it is a valid email address or not.


def emailValid(txt: str) -> bool:
    emails = ["@gmail", "@qq"]
    isValid = False
    for e in emails:
        if txt.__contains__(e):
            isValid = True
            break
    return isValid

# 5 Given a string, write a Python program to extract all the numbers from it.


def extractNumbers(txt: str) -> list:
    mylist = []
    for t in txt:
        try:
            num = int(t)
            mylist.append(num)
        except:
            print("{} was not a number ".format(t))
    return mylist

# 6 Given a string, write a Python program to check if it contains only digits.


def containsOnlyDigits(txt: str) -> bool:
    onlyDigits = True
    for t in txt:
        try:
            int(t)
        except:
            onlyDigits = False
    return onlyDigits


if __name__ == "__main__":
    #     print(palindrome("laval"))
    #     string_list = ["apple", "banana", "orange", "doumbouya"]
    #     print(longestSub(string_list))
    #     txt = "Hello you, How are you ?"
    #     print(removeAllPunctuation(txt=txt))
    #     print(emailValid("ddd@qq.com"))
    #     print(extractNumbers("hello12"))
    print(containsOnlyDigits("12345"))
