import re
import random
from SLnode import SLnode
from SLlist import SLlist
from SkipList import Skip_Lists


#function for reading lines (entries) in the input text file into a list of strings
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
        print(i)

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