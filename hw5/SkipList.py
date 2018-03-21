import re
import random
from SLnode import SLnode
from SLlist import SLlist

# Skip list definition: a list of lists is used
class Skip_Lists:
    def __init__(self):
        self.S=[SLlist()]

    def getLists(self):
        return self.S

    # use the number of nodes in the bottom list to denote the Size
    def getSize(self):
        return self.S[0].getSize()

    # use Height to denote the number of lists used in the skip list
    def getHeight(self):
        return len(self.S)

    def isEmpty(self):
        return ((self.getHeight()==1) and (self.getSize()==0))

    # Derive the top list in the skip list
    def getTopList(self):
        return self.S[self.getHeight()-1]

    # Derive the topleft node in the skip list
    def getTopleft(self):
        topList=self.getTopList()
        return topList.getleftDummy()


    #method addEmptyList(): padding the skip list when the number of copies of the inserted node is more than the height of the current  skip list

    def addEmptyList(self):

        # link the dummy nodes downward and upward on the both sides respectively
        newSList = SLlist()
        selfTopList = self.getTopList()

        selfTopList.leftDummy.up = newSList.leftDummy
        newSList.leftDummy.down = selfTopList.leftDummy

        selfTopList.rightDummy.up = newSList.rightDummy
        newSList.rightDummy.down = selfTopList.rightDummy

        # add the new empty list to the list S in the skip list
        self.S.append(newSList)


    #method search(node): search the skip list with the given node using the key

    def search(self, node):
        '''
        # derive the topleft node and the search starts from here
        cursorNode = self.getTopList().leftDummy
        Found = False
        while not Found:
            if node.key == cursorNode.key:
                Found = True
                break
            else:
                if node.key > cursorNode.next.key:
                    cursorNode = cursorNode.next
                if node.key < cursorNode.next.key:
                    if cursorNode.down == None:
                        break
                    else:
                        cursorNode = cursorNode.down
        return Found
        '''
        return False



    #method delete(node): delete the given node from the skip list

#    def delete(self, node):
        # search the node first to see if the node exists in the skip list

        # when the deleted node is in the skip list, use the result of search to delete
        # the node, or a list of this nodes if necessary

        # when the last node is deleted, we reset the skip list

        # remove the unnecessary empty lists from the skip list



   # method insert(node): insert the given node to the skip list

    def insert(self, node):
        # search the node first to see if the node exists in the skip list
        Found = self.search(node)

        # if the node is found, we give up the insertion and return with warning
        if Found:
            print("this node is existed")

        # if the node is not found, we do the insertion and first toss a coin
        else:
            p = self.S[0].findPosition(node)
            self.S[0].insertAfter(p, node)
            num = 1

        # if the number of heads is large than or equal to the height of the skip list,
        # we add some necessary empty lists
            if num >= self.getHeight():
                for i in range(num - self.getHeight() + 1):
                    self.addEmptyList()

            p2 = self.S[1].findPosition(node)
            self.S[1].insertAfter(p2, node)


#all good upon

#some problems happend that the findPosition reach the right limitation


"""
        # do the insertion from the bottom list upwards and link the nodes up and down
            for i in range(1, num + 1):
                p = self.S[1].findPosition(node)
                self.S[1].insertAfter(p, node)



            for i in range(num):
                nodeBase = self.S[i].findPosition(node)
                nodeUp = self.S[i+1].findPosition(node)
                nodeBase.up = nodeUp
                nodeUp.down = nodeBase
"""


#function for coin tossing with the number of heads returned

def coin_tossing():
    count = 0
    while (True):
        if (random.randint(0, 1)==1):
            return count
        count = count + 1
