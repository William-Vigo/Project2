import random as rand
class GraphNode:
    def __init__(self, Value: int):
        self.value = Value
        self.visited = False
        self.neighbors = []
#Question 3a
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

#Question 3b
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
#Question 3c
def createLinkedList(n: int) -> Graph:
    g = Graph()
    for i in range(n):
        g.addNode(i)
    
    for i in range(n-1):
        g.addUndirectedEdge(g.nodes[i], g.nodes[i+1])

    return g


class GraphSearch:

    def DFSRec(self, start: GraphNode, end: GraphNode) -> list():
        answer = []
        self.DFSRecHelper(start, end, answer)
        if(len(answer) == 0):
            return None
        else:
            return answer
    
    def DFSRecHelper(self, start: GraphNode, end: GraphNode, Answer: list):
        start.visited = True
        if(end not in Answer):
            Answer.append(start) 

        for neighbor in start.neighbors:
            if(not neighbor.visited):
                neighbor.visited = True
                self.DFSRecHelper(neighbor, end, Answer)

        if(end not in Answer):
            Answer.pop()

        return Answer

if __name__ == "__main__":
    g = Graph()
    for i in range(9):
        g.addNode(i)
    g.addNode(9)
    g.addUndirectedEdge(g.nodes[0],g.nodes[1])
    g.addUndirectedEdge(g.nodes[0],g.nodes[2])
    g.addUndirectedEdge(g.nodes[2],g.nodes[3])
    g.addUndirectedEdge(g.nodes[2],g.nodes[6])
    g.addUndirectedEdge(g.nodes[3],g.nodes[4])
    g.addUndirectedEdge(g.nodes[5],g.nodes[3])
    g.addUndirectedEdge(g.nodes[3],g.nodes[7])
    g.addUndirectedEdge(g.nodes[5],g.nodes[6])
    g.addUndirectedEdge(g.nodes[6],g.nodes[8])
    g.addUndirectedEdge(g.nodes[8],g.nodes[7])

    nodes1 = g.getAllNodes()
    for i in nodes1:
        print(i.value, end =" -> ")
        for x in i.neighbors:
            print(x.value, end=" ->")
        print()

    search = GraphSearch()
    print(search.DFSRec(g.nodes[0],g.nodes[9]))
    x = search.DFSRec(g.nodes[0],g.nodes[8])
    for i in x:
        print(i.value)