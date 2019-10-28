# Breadth First Graph Traversal Example

# Based on the graph on page 352 of Heathcote OCR Book

class Node():
    def __init__(self, name):
        self.name = name
        self.links = []

    def makeLink(self, otherNode):			# this is just used for setting up the node links at the start
        if not otherNode in self.links:
            self.links.append(otherNode) 	# it creates a bidirectional link of the same distance between both
            otherNode.links.append(self)


    def __str__(self):
        return "Node " + str(self.name)
    


# We create the nodes A - G
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")

# We build links according to the diagram

nodeA.makeLink(nodeB)  # These are two-way links, so we don't have to worry about linking B to A. It's already done
nodeA.makeLink(nodeD)
nodeA.makeLink(nodeE)
nodeB.makeLink(nodeD)
nodeB.makeLink(nodeC)
nodeC.makeLink(nodeG)
nodeD.makeLink(nodeE)
nodeD.makeLink(nodeF)
# Nodes E F and G have already had their links made in earlier commands, so we don't need to do it again


def BreadthFirstTraversal(startNode):
    Queue = []
    Visited = []
    
    Queue.append(startNode) # add the first node to the queue
    
    while len(Queue) > 0:   # While we still have places to visit
        currentNode = Queue.pop(0)  # take a node fro the queue
        Visited.append(currentNode) # mark it as visited
        print("Taken", currentNode, "off the Queue")
        # Adding any unvisited neighbours to the queue
        for neighbour in currentNode.links:
            if neighbour not in Visited and neighbour not in Queue:
                print("Adding", neighbour, "to the Queue")
                Queue.append(neighbour)  
        print()
    return Visited


Visited = BreadthFirstTraversal(nodeA)

print("Visited:")
for node in Visited:
    print(node)
    