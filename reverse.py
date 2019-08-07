# def reverse(string):
#     string = string[::-1]
#     return string
#
#
# s = "Bangladesh"
#
# print("The original string  is : ", end="")
# print(s)
#
# print("The reversed string(using extended slice syntax) is : ", end="")
# print(reverse(s))


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = input("Enter Word to Reverse: ")

print("The original string  is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))