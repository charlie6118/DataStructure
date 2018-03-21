from stack import Stack

def Checking_palindrome(string):
    s = Stack()
    for char in string:
        s.push(char)

    for char in string:
        if char != s.pop():
            return False
    return True

print(Checking_palindrome("radar"))
print(Checking_palindrome("hollylloh"))
print(Checking_palindrome("lsdkjfskf"))
