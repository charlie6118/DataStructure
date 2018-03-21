from stack import Stack

def Finding_seafood(list, int):
    s = Stack()
    count = 0
    while True:
        if len(list) < int and len(list) != 0:
            temp = int % len(list) -1

        print("temp is {}".format(temp))


        if len(list) > 0:
            print(list[temp+count])
            s.push(list.pop(temp+count))
        if len(list) == 0:
            break
        count = temp+count
        if count >= len(list):
            count = count % len(list)
        print("count is {}".format(count))
        print()


    return s.pop()

print(Finding_seafood(["Bill","David","Susan","Jane","Kent","Bred"],7))