class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def print(self):
        if self.next == None:
            print(self.data)
        else:
            print(self.data)
            self.next.print()

    def add(self, newData):
        if self.next is None or self.next.data > newData:
            newNode = Node(newData)
            newNode.next = self.next
            self.next = newNode
        else:
            self.next.add(newData)

head = Node("cat")
head.add("dog")
head.add("egg")
head.add("al")
head.add("frank")
head.print()