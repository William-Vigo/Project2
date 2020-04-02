import random as rand
class Node:
    def __init__(self, value: str):
        self.val = value
        self.parent = None
        self.visited = False
        self.neighbors = []

class DirectedGraph:
    def __init__(self):
        self.vertexList = []

    def addNode(self, value):
        node = Node(value)
        self.vertexList.append(node)

    def addDirectedEdge(self, first: Node, second: Node):
        first.neighbors.append(second)

    def removeDirectedEdge(self, first: Node, second: Node):
        if(first in second.neighbors):
            second.neighbors.remove(first)
        

    def getAllNodes(self):
        return set(self.vertexList)

class TopSort:
    def inDegree(self, g: DirectedGraph) -> dict():
        dic = dict()
        for node in g.vertexList:
            dic[node] = 0
        
        for node in g.vertexList:
            for neighbor in node.neighbors:
                dic[neighbor] += 1

        return dic

    def Khans(self, g: DirectedGraph) -> list():
        inDegreeMap = self.inDegree(g)
        TopSort = []
        queue = []
        
        for key in inDegreeMap:
            if(inDegreeMap[key] == 0):
                queue.append(key)
                inDegreeMap[key] -= 1

        while queue:
            current = queue.pop(0)
            TopSort.append(current)

            for neighbor in current.neighbors:
                inDegreeMap[neighbor] -= 1
            
            for key in inDegreeMap:
                if(inDegreeMap[key] == 0):
                    queue.append(key)
                    inDegreeMap[key] -= 1

        return TopSort

    def mDFS(self, g :DirectedGraph):
        topSort = []
        
        for node in g.vertexList:
            if not node.visited:
                self.mDFSHelper(node,topSort)

        return topSort

    def mDFSHelper(self, node: Node, sort: list()):
        node.visited = True
        
        for neighbor in node.neighbors:
            if not neighbor.visited:
                self.mDFSHelper(neighbor,sort)

        sort.append(node)

#Question 4c
def createRandomDagIter(n: int) -> DirectedGraph:
    g = DirectedGraph()
    for i in range(n):
        g.addNode(i)

    numNodes = len(g.vertexList)
    for i in range(numNodes):
        randIndex = rand.randrange(i,numNodes)
        if(i != randIndex):
            g.addDirectedEdge(g.vertexList[i], g.vertexList[randIndex])
    return g

if __name__ == "__main__":
    g = createRandomDagIter(1000)

    for i in g.vertexList:
        print(i.val, end=" -> ")
        for j in i.neighbors:
            print(j.val, end=" -> ")
        print()


    s = TopSort()
    topsort = s.mDFS(g)
    khan = s.Khans(g)
    for i in topsort[::-1]:
        print( i.val , end =" -> ")
    print()

    for i in khan:
        print( i.val , end =" -> ")
    print()