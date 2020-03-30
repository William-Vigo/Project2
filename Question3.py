import random as rand
class GraphNode:
    def __init__(self, Value: int):
        self.value = Value
        self.visited = False
        self.parent = None
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
    def BFTRec(self, g: Graph) -> list():
        nodes = []
        queue = []
        queue.append(g.nodes[0])
        return self.BFTRecHelper(queue[0], nodes, queue)
    def BFTRecHelper(self, cur: GraphNode, nodes: list(), queue: list()):
        while queue:
            nodes.append(cur)
            cur.visited = True
            for neighbor in cur.neighbors:
                if(not neighbor.visited):
                    neighbor.visited = True
                    queue.append(neighbor)
            queue.pop(0)
            if(queue):
                self.BFTRecHelper(queue[0],nodes, queue)
            
        return nodes

    def BFTIter(self, g: Graph) -> list():
        nodes = []
        queue = []
        queue.append(g.nodes[0])
        while queue:
            node = queue.pop(0)
            node.visited = True
            for neighbor in node.neighbors:
                if(not neighbor.visited):
                    neighbor.visited = True
                    queue.append(neighbor)
            nodes.append(node)
        return nodes
    def DFSIter(self, start: GraphNode, end: GraphNode):
        path = []
        stack = []
        stack.append(start)
        found = False
        while stack:
            node = stack.pop()
            node.visited = True
            if(node == end):
                found = True
                break
            for neighbor in node.neighbors:
                if(not neighbor.visited):
                    stack.append(neighbor)
                    neighbor.parent = node

        if(found):
            path.insert(0,end)
            while(end.parent):
                path.insert(0,end.parent)
                end = end.parent
        return path 
           

        return None
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

#Question 3h
def BFTRecLinkedList(g: Graph) -> list():
    solve = GraphSearch()
    return solve.BFTRec(g)

def BFTIterLinkedList(g: Graph) -> list():
    solve = GraphSearch()
    return solve.BFTIter(g)

if __name__ == "__main__":
    '''
    g = createLinkedList(10000)

    bft = BFTIterLinkedList(g)
    
    for i in bft:
        print(i.value, end= " ")
    '''
    cheeseGraph = Graph()
    for i in range(25):
        cheeseGraph.addNode(i)

    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[0], cheeseGraph.nodes[1])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[0], cheeseGraph.nodes[5])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[1], cheeseGraph.nodes[6])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[2], cheeseGraph.nodes[3])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[3], cheeseGraph.nodes[8])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[4], cheeseGraph.nodes[9])

    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[6], cheeseGraph.nodes[7])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[6], cheeseGraph.nodes[11])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[7], cheeseGraph.nodes[12])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[8], cheeseGraph.nodes[9])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[9], cheeseGraph.nodes[14])

    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[10], cheeseGraph.nodes[11])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[10], cheeseGraph.nodes[15])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[11], cheeseGraph.nodes[16])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[12], cheeseGraph.nodes[13])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[14], cheeseGraph.nodes[19])

    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[15], cheeseGraph.nodes[20])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[17], cheeseGraph.nodes[18])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[17], cheeseGraph.nodes[22])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[18], cheeseGraph.nodes[19])
    
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[20], cheeseGraph.nodes[21])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[21], cheeseGraph.nodes[22])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[22], cheeseGraph.nodes[23])
    cheeseGraph.addUndirectedEdge(cheeseGraph.nodes[23], cheeseGraph.nodes[24])
    
    search = GraphSearch()
    path = search.DFSRec(cheeseGraph.nodes[2],cheeseGraph.nodes[22])

    for i in path:
        print(i.value, end=" -> ")
    print()

