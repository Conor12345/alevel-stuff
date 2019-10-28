# Depth First Graph Traversal Example

# Based on the graph on page 352 of Heathcote OCR Book

class Node():
    def __init__(self, name):
        self.name = name
        self.links = []

    def makeLink(self, otherNode):			# this is just used for setting up the node links at the start
        if not otherNode in self.links:
            self.links.append(otherNode)  	# it creates a bidirectional link of the same distance between both
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


def DepthFirstTraversal(currentNode, Visited, Stack):
    Visited.append(currentNode)   # mark this node as visited
    print("Currently at", currentNode)
    for neighbour in currentNode.links:  # go through each node that this node is linked to
        if neighbour not in Visited:  # Only follow the path to an unvisited node
            print("I haven't been to ", neighbour, "yet, so going there\n")
            Stack.append(currentNode) # Add myself to the stack, so I remember to come back
            Visited, Stack = DepthFirstTraversal(neighbour, Visited, Stack)
            
        # This will repeat for each neighbour, until we have run out of unvisited neighbours
        
    print("I've run out of neighbours at ", currentNode)
    if len(Stack) > 0:
        print("Falling back to ", Stack.pop())
    else:
        print("I've gone everywhere I can go")
    print()
    return Visited,Stack


Visited, Stack = DepthFirstTraversal(nodeA, [],[])

print("Visited:")
for node in Visited:
    print(node)
    