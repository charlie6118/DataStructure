import re
from Heap import Heap
from Hnode import Hnode

#####
#
# insert not ordered
#
#####
h = Heap()
print("insert 10, resume")
h.Insert(Hnode(10, "resume"))

print("insert 15, second")
h.Insert(Hnode(15, "second"))

print("insert 20, fourth")
h.Insert(Hnode(20, "fourth"))

print("insert 25, fourth")
h.Insert(Hnode(25, "ourth"))

print("insert 30, yoooth")
h.Insert(Hnode(30, "yoooth"))


h.printHeapPreOrder(h.getRoot())
print()

leafs = h.findLeafs(h.getRoot())
for leaf in leafs:
    print("Leaf is ", leaf.key,  leaf.item, " depth is ", leaf.depth)
    print()

lastNode = h.findLast()
print("Last is ", lastNode.key, lastNode.item)


'''
#####
#
# read file test
#
#####
entry_list = []
f = open('inFile.txt','r')
for line in f.readlines():
    entry_list.append(line.rstrip("\n").split())
f.close()


#####
#
#Insert test
#
#####
h=Heap()

for elements in entry_list:
    key = elements[0]
    data = elements[1]
    h.Insert(Hnode(key, data))
'''

'''
#####
#
# printHeapPreOrder test
#
#####
h.printHeapPreOrder(h.getRoot())
print()
h.removeMin()
print()
print()
h.printHeapPreOrder(h.getRoot())
print()
h.removeMin()
print()
print()
h.printHeapPreOrder(h.getRoot())
print()
h.removeMin()
print()
print()
h.printHeapPreOrder(h.getRoot())
print()
h.removeMin()
h.removeMin()
'''


"""

#####
#
# show elements
#
#####
print("root node is", h.getRoot().getKey(), h.getRoot().getItem())
print("left of root is",h.getRoot().getLeftChild().getKey(), h.getRoot().getLeftChild().getItem())
print("right of rootis", h.getRoot().getRightChild().getKey(), h.getRoot().getRightChild().getItem())
print("forth node is", h.getRoot().getLeftChild().getLeftChild().getKey(), h.getRoot().getLeftChild().getLeftChild().getItem())
print("fifth node is", h.getRoot().getLeftChild().getRightChild().getKey(), h.getRoot().getLeftChild().getRightChild().getItem())
print("sixth node is", h.getRoot().getRightChild().getLeftChild().getKey(), h.getRoot().getRightChild().getLeftChild().getItem())
print("last node is", h.getLast().getKey(), h.getLast().getItem())
print(h.size)
"""