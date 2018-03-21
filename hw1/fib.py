import sys
import timeit
from timeit import Timer
call = 0

def main():
    while True:
        print("Type the char: ")
        print("B for binary_fib")
        print("L for linea_fib")
        print("I for iterative_fib")
        choose = input("else for exit: ")
        output = 0
        if choose != 'L' and choose != 'B' and choose != 'I':
            print("Bye")
            sys.exit(1)
        else:
            num = input('Please type an integer: ')
            num = int(num) -1
            if choose == 'L':
                timer_start = timeit.default_timer()
                ppap = linea_fib(int(num))
                timer_end = timeit.default_timer()
                if int(num) < 2:
                    output = ppap[int(num)]
                else:
                    output = ppap[1]
            if choose == 'B':
                timer_start = timeit.default_timer()
                output = binary_fib(int(num))
                timer_end = timeit.default_timer()
            if choose == 'I':
                timer_start = timeit.default_timer()
                output = iterative_fib(int(num))
                timer_end = timeit.default_timer()
            print("output is {}".format(output))
            print("number of recursive calls is {}".format(call))
            print("execution time is ", round(100 *(timer_end - timer_start), 5), "ms")
        print()

def linea_fib(n):
    global call
    call =  call + 1
    pair = [0, 1]
    temp = 0
    if n == 0 or n == 1:
        return pair
    else:
        pair = linea_fib(n-1)
        temp = pair[1]
        pair[1] = pair[0] + pair[1]
        pair[0] = temp
        return pair

def binary_fib(n):
    global call
    if n == 0 or n == 1:
        return int(n)
    else:
        return binary_fib(n-1) + binary_fib(n-2)

def iterative_fib(n):
    fn = f1 = f2 = 1
    for i in range(2, n):
        fn = f1 + f2
        f2, f1 = f1, fn
    return fn

if __name__ == "__main__":
    main()
