a = int(input("Enter Number: "))


def factorial(a):
    if a == 0:
        return 1
    else:
        return a*factorial(a-1)

print (factorial(a))