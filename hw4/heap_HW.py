import re
from Heap import Heap
from Hnode import Hnode


# decimal to binary using yield
def d2by(x):
    while x>0 :
        x,r=divmod(x,2)
        yield r

# function for starting the task
def HeapwithEntriesInserted():
    #
    # read the input information from the default input text file into an
    # entry list, entry_list
    #
    entry_list = []
    f = open('inFile1.txt','r')
    for line in f.readlines():
        entry_list.append(line.rstrip("\n").split())
    f.close()

    #
    # initiating a heap object h
    #
    h=Heap()

    #
    # Do something here to build the heap
    #

    for elements in entry_list:
        key = elements[0]
        data = elements[1]
        h.Insert(Hnode(key, data))


    #---------------------Print as the example on the homework sheet --------
    #                       will be adapted with the input
    #
    print("Heap size=", h.getSize(), "The highest priority is ", h.getHighestPriority())
    print("pre-order traversal:")
    h.printHeapPreOrder(h.getRoot())

    print("deleteMin")
    h.removeMin()

    print("deleteMin")
    h.removeMin()

    print("deleteMin")
    h.removeMin()

    print("deleteMin")
    h.removeMin()

    print("deleteMin")
    h.removeMin()

    print("insert 35, resume")
    h.Insert(Hnode(35, "resume"))

    print("insert 15, second")
    h.Insert(Hnode(15, "second"))

    print("insert 20, fourth")
    h.Insert(Hnode(20, "fourth"))

    print("Heap size=", h.getSize(), "The highest priority is ", h.getHighestPriority())
    print("pre-order traversal:")
    h.printHeapPreOrder(h.getRoot())

    print("deleteMin")
    h.removeMin()

    print("insert 40, nineth")
    h.Insert(Hnode(40, "nineth"))

if __name__ == "__main__":
    HeapwithEntriesInserted()