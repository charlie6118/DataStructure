import re
import random

# Two special values for boundary nodes
PLUS_INF = 99999
MINUS_INF = -99999

# Node class definition: a quadraic node having four links
class SLnode:
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.up = None
        self.down = None
        self.next = None
        self.prev = None

    def getKey(self):
        return self.key

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def getUp(self):
        return self.up

    def getDown(self):
        return self.down

    def hasNext(self):
        return (self.next!=None)

    def hasPrev(self):
        return (self.prev!=None)

    def setKey(self, key):
        self.key = key

    def setItem(self, item):
        self.item = item

    def setNext(self, p):
        self.next = p

    def setPrev(self, p):
        self.prev =p

    def setUp(self, p):
        self.up = p

    def setDown(self, p):
        self.down = p

# List class definition used in the skip list
class SLlist:
    def __init__(self):
        self.leftDummy=SLnode(MINUS_INF,"")
        self.rightDummy=SLnode(PLUS_INF,"")
        self.leftDummy.setNext(self.rightDummy)
        self.rightDummy.setPrev(self.leftDummy)
        self.size = 0
        self.insert_cursor = self.getleftDummy()

    def getleftDummy(self):
        return self.leftDummy

    def getrightDummy(self):
        return self.rightDummy

    def getSize(self):
        return self.size

    def increaseSize(self):
        self.size=self.size + 1

    def decreaseSize(self):
        self.size=self.size - 1

    def insertAfter(self, p, SLnode):
        SLnode.setNext(p.getNext())
        SLnode.setPrev(p)
        p.getNext().setPrev(SLnode)
        p.setNext(SLnode)
        self.increaseSize()

    def print_List(self):
        current = self.leftDummy
        while (current != None):
            print("(",current.getKey(),",",current.getItem(),")",sep='',end="")
            current = current.getNext()
        print("")

    def findPosition(self, node):
        cursor = self.leftDummy
        while node.key > cursor.key:
            cursor = cursor.next
        return cursor.prev

    def findPositionForLink(self, node):
        cursor = self.leftDummy
        while node.key == cursor.key:
            cursor = cursor.next
        return cursor

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

    '''
    method addEmptyList(): padding the skip list when the number of copies of the inserted node
    is more than the height of the current  skip list
    '''
    def addEmptyList(self):

        # link the dummy nodes downward and upward on the both sides respectively
        newSLlist = SLlist()

        newSLlist.leftDummy.down = self.getTopList().leftDummy
        self.getTopList().leftDummy.up = newSLlist.leftDummy

        newSLlist.rightDummy.down = self.getTopList().rightDummy
        self.getTopList().rightDummy.up = newSLlist.rightDummy

        # add the new empty list to the list S in the skip list
        self.S.append(newSLlist)

    '''
    method search(node): search the skip list with the given node using the key
    '''
    def search(self, node):

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
    method delete(node): delete the given node from the skip list
    '''
    def delete(self, node):
        # search the node first to see if the node exists in the skip list
        if not self.search(node):
            print("there is no such a node.")
        # when the deleted node is in the skip list, use the result of search to delete the node, or a list of this nodes if necessary
        else:
            for i in range(self.getHeight()):
                p = self.S[i].findPositionForLink(node)
                p.up = None
                p.down = None
                p.prev.next = p.next
                p.next.prev = p.prev
        # when the last node is deleted, we reset the skip list
        if self.isEmpty():
            self.S = None
            self.S = [SLlist()]

        # remove the unnecessary empty lists from the skip list
        for i in range(1, self.getHeight()):
            if self.S[self.getHeight()-i].getSize()== 2 and self.S[self.getHeight()-i-1].getSize() == 2:
                self.S[self.getHeight()-i-1].leftDummy.up = None
                self.S[self.getHeight()-i-1].rightDummy.up = None
            else:
                break


    '''
    method insert(node): insert the given node to the skip list
    '''
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
            num = coin_tossing()
        # if the number of heads is large than or equal to the height of the skip list,
        # we add some necessary empty lists
            if num >= self.getHeight():
                for i in range(num-self.getHeight() + 1):
                    self.addEmptyList()

        # do the insertion from the bottom list upwards and link the nodes up and down

            for i in range(num):
                p = self.S[i+1].findPosition(node)
                self.S[i+1].insertAfter(p, node)


            for j in range(num):
                if num > 0:
                    p2 = self.S[j+1].findPositionForLink(node)
                    p.up = p2
                    p2.down = p
                p = self.S[j].findPositionForLink(node)


'''
function for coin tossing with the number of heads returned
'''
def coin_tossing():
    count = 0
    while (True):
        if (random.randint(0, 1)==1):
            return count
        count = count + 1
'''
function for reading lines (entries) in the input text file into a list of strings
'''
def read_lines():
    #f=open('inFile.txt', 'r')
    with open('inFile.txt', "r+") as f:
        entry_list = [x.strip() for x in f.readlines()]
    #string_list=f.readlines()
    f.close()
    return entry_list
'''
function for starting the task
'''
def create_SkipLists():
    #
    # read the input information from the default input text file into an
    # entry list, entry_list
    #
    entry_list=read_lines()
    #
    # initiating a skip list object SL
    #
    SL=Skip_Lists()
    for index in range(0, len(entry_list)):
        # splitting the string by " " symbol for deriving the entry
        pairs = re.split(" ",entry_list[index])
        # making a new node for the entry
        newnode=SLnode(int(pairs[0]), pairs[1])
        # inserting the new node to the skip list SL
        SL.insert(newnode)

    #--------------dynamic operations with result printed -----------------------------------
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()
    '''
    print("Insert (88, luke)")
    SL.insert(SLnode(88, "luke"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("delete (40, kite)")
    SL.delete(SLnode(40, "kite"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("Insert (27, eric)")
    SL.insert(SLnode(27, "eric"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("delete (45, lisa)")
    SL.delete(SLnode(45, "lisa"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("delete (27, luis)")
    SL.delete(SLnode(27, "luis"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("delete (8, kids)")
    SL.delete(SLnode(8, "kids"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    print("delete (88, luke)")
    SL.delete(SLnode(88, "luke"))
    for i in range(0,SL.getHeight()):
        SL.S[i].print_List()

    '''
if __name__ == "__main__":
    create_SkipLists()

