

def Finding_seafood(list, int):

    FindIt = True
    while not FindIt:
        if len(list) < int:
            temp = int % len(list)
        list.pop(temp)
        if len(list) > 1:
            FindIt == False
        else:
            FindIt == True
    return list.pop()

print(Finding_seafood(["Bill","David","Susan","Jane","Kent","Bred"],7))