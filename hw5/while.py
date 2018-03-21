import re
import random
from SLnode import SLnode
from SLlist import SLlist
from SkipList import Skip_Lists


SL = Skip_Lists()

newNode = SLnode(40, "boo")
SL.insert(newNode)

newNode = SLnode(30, "yoo")
SL.insert(newNode)

#print(SL.S[0].findPosition(SLnode(3, "yo")))

'''
for i in range(0,SL.getHeight()):
    SL.S[i].print_List()
    print(i)
    if i > 10:
        break
'''