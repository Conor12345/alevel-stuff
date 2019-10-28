class Node():
    def __init__(self, contents):
        self.left = None
        self.right = None
        self.contents = contents

    def add(self, newItem):
        if newItem < self.contents:
            if self.left == None:
                self.left = Node(newItem)
            else:
                self.left.add(newItem)
        if newItem > self.contents:
            if self.right == None:
                self.right = Node(newItem)
            else:
                self.right.add(newItem)

    def find(self, target):
        if target == self.contents:
            return True
        if self.left != None and target < self.contents:
            return self.left.find(target)
        if self.right != None and target > self.contents:
            return self.right.find(target)
        else:
            return False

    def preOrderTraversal(self):
        print(self.contents)
        if self.left != None:
            self.left.preOrderTraversal()
        if self.right != None:
            self.right.preOrderTraversal()


    def inOrderTraversal(self):
        if self.left != None:
            self.left.inOrderTraversal()
        print(self.contents)
        if self.right != None:
            self.right.inOrderTraversal()

    def postOrderTraversal(self):
        if self.left != None:
            self.left.postOrderTraversal()
        if self.right != None:
            self.right.postOrderTraversal()
        print(self.contents)


Tree = Node("elk")

Tree.add("moose")
Tree.add("frog")
Tree.add("wolf")
Tree.add("lion")
Tree.add("tiger")
Tree.add("duck")
Tree.add("eel")
Tree.add("eagle")
Tree.add("snake")


Tree.preOrderTraversal()
print("")
Tree.inOrderTraversal()
print("")
Tree.postOrderTraversal()


while True:
    break
    x = input("Animal:")
    if x == "STOP":
        break
    print(Tree.find(x))


