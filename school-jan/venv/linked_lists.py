class Node():
    def __init__(self, contents = None, nextPointer = None):
        self.contents = contents
        self.nextPointer = nextPointer


def printList(start):
    currentNode = start
    while currentNode != None:
        print(currentNode.contents)
        currentNode = currentNode.nextPointer
    print("")

def addToStart(start, newNode):
    newNode.nextPointer = start
    return newNode

def addToEnd(start, newNode):
    currentNode = start
    while currentNode.nextPointer != None:
        currentNode = currentNode.nextPointer
    currentNode.nextPointer = newNode

def find(start, item):
    currentNode = start
    while currentNode != None:
        if currentNode.contents == item:
            return True
        currentNode = currentNode.nextPointer
    return False

def insertInPlace(start, newNode):
    if start.contents > newNode.contents:
        addToStart(start, newNode)
        return newNode
    currentNode = start
    previousNode = start
    while currentNode != None:
        if newNode.contents < currentNode.contents:
            break
        previousNode = currentNode
        currentNode = currentNode.nextPointer
    previousNode.nextPointer = newNode
    newNode.nextPointer = currentNode
    return start

def deleteItem(start, itemToDelete):
    if itemToDelete == start.contents:
        return start.nextPointer
    currentNode = start
    previousNode = start
    while currentNode != None:
        if itemToDelete == currentNode.contents:
            previousNode.nextPointer = currentNode.nextPointer
            break
        previousNode = currentNode
        currentNode = currentNode.nextPointer
    return start

n1 = Node("Adam")
n2 = Node("Barry")
n3 = Node("Callumn")
n4 = Node("Derak")
start = n1

n1.nextPointer = n2
n2.nextPointer = n3
n3.nextPointer = n4

n5 = Node("Aaron")
start = insertInPlace(start, n5)
printList(start)

n6 = Node("Ellen")
start = insertInPlace(start, n6)
printList(start)

n7 = Node("Carolin")
start = insertInPlace(start, n7)
printList(start)

start = deleteItem(start, "Derak")
printList(start)

start = deleteItem(start, "Aaron")
printList(start)