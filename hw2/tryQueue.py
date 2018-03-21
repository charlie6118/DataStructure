from queue import Queue

Q = Queue()
Q.enqueue('Q')
Q.enqueue('R')
Q.enqueue('A')
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())


