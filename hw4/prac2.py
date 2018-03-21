import re
from Heap import Heap
from Hnode import Hnode

entry_list = []
f = open('inFile.txt','r')
for line in f.readlines():
    entry_list.append(line.rstrip("\n").split())
f.close()

h=Heap()
for elements in entry_list:
    key = int(elements[0])
    data = elements[1]
    print(type(key))
    print(key)
    print(data, "yee")
    print()
