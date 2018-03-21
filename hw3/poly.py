from node import Node
from linkList import LinkList
import numpy as np


lines = []
f = open('inFile.txt','r')
for line in f.readlines():
    lines.append(line.rstrip("\n"))
f.close()

L1 = LinkList()
L2 = LinkList()
cout = 0
for line in reversed(lines):
    if cout == 0:
        L = L2
    if cout == 1:
        L = L1
    cout = cout + 1
    for index in range(len(line)):

        index_Reversed = len(line) - index -1
        #print(lines[1][index_Reversed])

        """last item"""
        if index_Reversed + 1 == len(line):
            if int(line[index_Reversed]) and line[index_Reversed - 1] == '+':
                L.append(int(line[index_Reversed]), 0)
            if int(line[index_Reversed]) and line[index_Reversed - 1] == '-':
                L.append(-int(line[index_Reversed]), 0)

        """power = 1 and coefficient = 1 or -1"""
        if line[index_Reversed] == 'x' and line[index_Reversed + 1] != '^' and line[index_Reversed-1] == '+' :
            L.append(1, 1)
        if line[index_Reversed] == 'x' and line[index_Reversed + 1] != '^' and line[index_Reversed-1] == '-' :
            L.append(-1, 1)

        if line[index_Reversed] == 'x' and line[index_Reversed + 1] != '^' and line[index_Reversed-2] == '+' :
            L.append(int(line[index_Reversed -1]), 1)
        if line[index_Reversed] == 'x' and line[index_Reversed + 1] != '^' and line[index_Reversed-2] == '-' :
            L.append(-int(line[index_Reversed -1]), 1)

        """power != 1 and coefficient != 1 or -1 (i.e.) coef = 2, 3, 4"""
        if line[index_Reversed] == 'x' and line[index_Reversed + 1] == '^' and not int(line[index_Reversed-1]) :
            if line[index_Reversed - 2] == '+':
                L.append(1, int(line[index_Reversed + 2]))
            if line[index_Reversed - 2] == '-':
                L.append(-1, int(line[index_Reversed + 2]))
        if line[index_Reversed] == 'x' and line[index_Reversed + 1] == '^' and int(line[index_Reversed-1]) :
            if line[index_Reversed - 2] == '-':
                L.append(-int(line[index_Reversed -1]), int(line[index_Reversed + 2]))
            else:
                L.append(int(line[index_Reversed -1]), int(line[index_Reversed + 2]))



def multiply(LinklistA, LinklistB, method):
    P1 = []
    P2 = []

    temp = -1
    node = LinklistA.head
    print("L1")
    while node:
        if temp != -1 and temp != node.power:
            P1.append(0)
        P1.append(node.coefficient)
        temp = node.power -1
        node = node.next

    node = LinklistB.head
    print("L2")
    while node:
        if temp != -1 and temp != node.power:
            P2.append(0)
        P2.append(node.coefficient)
        temp = node.power -1
        node = node.next

    print(P1)
    print(P2)
    Ans =[]
    s =[]
    if method == 1: #+
        len1 = len(P1)
        len2 = len(P2)
        if len1 > len2:
            for item in range(len1-len2):
                Ans.append(P1[item])
            for index in range(len2):
                Ans.append(P1[len1-len2+index] + P2[index])
        if len1 < len2:
            for item in range(len2-len1):
                Ans.append(P1[item])
            for index in range(len1):
                Ans.append(P2[len1-len2+index] + P1[index])
        s = ""
        for index in range(len(Ans)):
            if Ans[index] != 1:
                s += str(Ans[index])
            if index != len(Ans)-1:
                s += "x^"
                s += str(len(Ans)-index-1)
                if Ans[index+1]> 0:
                    s += "+"
        print(s)

        print(Ans)
    if method == 2: #-
        len1 = len(P1)
        len2 = len(P2)
        if len1 > len2:
            for item in range(len1-len2):
                Ans.append(P1[item])
            for index in range(len2):
                Ans.append(P1[len1-len2+index] - P2[index])
        if len1 < len2:
            for item in range(len2-len1):
                Ans.append(P1[item])
            for index in range(len1):
                Ans.append(P1[index] - P2[len1-len2+index])
        s = ""
        for index in range(len(Ans)):
            if Ans[index] != 1:
                s += str(Ans[index])
            if index != len(Ans)-1:
                s += "x^"
                s += str(len(Ans)-index-1)
                if Ans[index+1]> 0:
                    s += "+"
        print(s)
    if method == 3: #*
        Ans = np.polymul(P1, P2)
        s = ""
        for index in range(len(Ans)):
            if Ans[index] != 1:
                s += str(Ans[index])
            if index != len(Ans)-1:
                s += "x^"
                s += str(len(Ans)-index-1)
                if Ans[index+1]> 0:
                    s += "+"
        print(s)
        return True
    if method == 4: #/
        return True
multiply(L1,L2,3)

"""
node = L1.head
print("L1")
while node:
    print("coefficient is {}".format(node.coefficient))
    print("power is {}".format(node.power))
    node = node.next
print()

node = L2.head
print("L2")
while node:
    print("coefficient is {}".format(node.coefficient))
    print("power is {}".format(node.power))
    node = node.next



print()
operator = lines[0]
print()
print("method: {}".format(operator))
for index in range(len(lines)):
    if index != 0:
        print("poly is {}".format(lines[index]))

"""

"""
P1 = []
P2 = []

temp = -1
node = L1.head
print("L1")
while node:
    if temp != -1 and temp != node.power:
        P1.append(0)
    P1.append(node.coefficient)
    temp = node.power -1
    node = node.next

node = L2.head
print("L2")
while node:
    if temp != -1 and temp != node.power:
        P2.append(0)
    P2.append(node.coefficient)
    temp = node.power -1
    node = node.next

print(P1)
print(P2)

"""