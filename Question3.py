import random as rand
class GraphNode:
    def __init__(self, Value: int):
        self.value = Value
        self.visited = False
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, Value: str):
        node = GraphNode(Value)
        self.nodes.append(node)

    def addUndirectedEdge(self, First: GraphNode, Second: GraphNode):
        #if first graph node is not connected with Second GraphNode
        if(not (First in Second.neighbors)):
            First.neighbors.append(Second)
            Second.neighbors.append(First)

    def removeUndirectedEdge(self, First: GraphNode, Second: GraphNode):
        #if first graph node is connected with Second GraphNode
        if(First in Second.neighbors):
            First.neighbors.remove(Second) 
            Second.neighbors.remove(First)

    def getAllNodes(self):
        return set(self.nodes)

def createRandomUnweightedGraphIter(n: int) -> Graph:
    g = Graph()
    for i in range(n):
        g.addNode(i)

    for node in g.nodes:
        #each node has to have at least 1 edge
        edges = rand.randint(1,1)
        #connect nodes
        connections = 0
        while(connections != edges):
            randIndex = rand.randint(0, n-1)
            #if random node is not equal to current node
            if(g.nodes[randIndex] != node):
                connections += 1
                g.addUndirectedEdge(g.nodes[randIndex], node)

    return g

def createLinkedList(n: int) -> Graph:
    g = Graph()
    for i in range(n):
        g.addNode(i)
    
    for i in range(n-1):
        g.addUndirectedEdge(g.nodes[i], g.nodes[i+1])

    return g

if __name__ == "__main__":
    graph = createRandomUnweightedGraphIter(5)
    graph1 = createLinkedList(5)

    nodes1 = graph1.getAllNodes()
    nodes = graph.getAllNodes()
    for i in nodes1:
        print(i.value, end =" -> ")
        for x in i.neighbors:
            print(x.value, end=" ->")
        print()