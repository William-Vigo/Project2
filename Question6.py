import random as rand
class GridNode:
    def __init__(self, x, y, value):
        self.val = value
        self.x = x
        self.y = y
        self.parent = None
        self.Fcost = 0
        self.visited = False
        self.neighbors = []

class GridGraph:
    def __init__(self, size: int):
        self.vertexList = [0] * size
        for i in range(len(self.vertexList)):
            self.vertexList[i] = [0] * size

    def addGridNode(self, x: int, y: int , value):
        node = GridNode(x,y,value)
        self.vertexList[x][y] = node
   
    def addUndirectedEdge(self, first: GridNode, second: GridNode):
        if first not in second.neighbors:
            first.neighbors.append(second)
            second.neighbors.append(first)
    
    def removeUndirectedEdge(self, first: GridNode, second: GridNode):
        if first in second.neighbors:
            first.neighbors.remove(second)
            second.neighbors.remove(first)

    def getAllNodes(self):
        return set(self.vertexList)

    #Question 6b
def createRandomGridGraph(n: int):
    g = GridGraph(n)
    count = 0
    for i in range(n):
        for j in range(n):
            g.addGridNode(i,j,count)

    for i in range(n):
        for j in range(i, n):
            #check up
            if (i-1) >= 0 and rand.randint(0, 1):
                g.addUndirectedEdge(g.vertexList[i-1][j], g.vertexList[i][j])
            #check down
            if (i+1) < n and rand.randint(0, 1):
                g.addUndirectedEdge(g.vertexList[i+1][j], g.vertexList[i][j])
            #check left
            if (j-1) >= 0 and rand.randint(0, 1):
                g.addUndirectedEdge(g.vertexList[i][j-1], g.vertexList[i][j])
            #check right            
            if (j+1) < n and rand.randint(0, 1):
                g.addUndirectedEdge(g.vertexList[i][j+1], g.vertexList[i][j])
    return g

if __name__ == "__main__":
    g = createRandomGridGraph(3)

    pass    
    