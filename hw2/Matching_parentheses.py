from stack import Stack

char_remember = '('
def Matching_parentheses(string):
    s = Stack()
    pushChars = "([{'"
    popChars = ")]}'"

    for char in string:
        if char in pushChars:
            s.push(char)
            #print(s.top())
        elif char in popChars:
            if s.isEmpty() == True:
                return False
            else:
                stackTop = s.top()
                #print(s.top())
                comp = pushChars[popChars.index(char)]
                #print(comp)
                if stackTop != comp:
                    return False
                else:
                    s.pop()
                #print()
        else:
            return False
    return s.isEmpty()

#print(Matching_parentheses("(())"))
#print(Matching_parentheses("{()}"))
#print(Matching_parentheses("(()}"))
#print(Matching_parentheses("{"))
print(Matching_parentheses("{{([][])}()}"))
print(Matching_parentheses("[{()]"))


