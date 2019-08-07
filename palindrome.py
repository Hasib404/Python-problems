"""
#PROBLEM
A palindrome is a word that reads the same backward or forward.
Write a function that checks if a given word is a palindrome. Character case should be ignored.

def is_palindrome(word)

For example, isPalindrome("Deleveled") should return true as character case should be ignored, resulting in "deleveled", which is a palindrome since it reads the same backward and forward.

#INPUT
Deleveled
adam 
"""


#ANSWER

# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
  
  
# Driver code 
s = "Deleveled".lower()
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 

s = "adam"
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 
