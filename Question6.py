import random as rand
import heapq
class GridNode:
    def __init__(self, x_coord, y_coord, value):
        self.val = value
        self.x = x_coord
        self.y = y_coord
        self.parent = None
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
        for j in range(n):
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
def calculateF(curr: GridNode, start: GridNode, end:GridNode):
    #manhatton distance
    g = abs(curr.x - start.x) + abs(curr.y - start.y)
    h = abs(end.x-curr.x) + abs(end.y - curr.y)
    return g + h

def astar(start: GridNode, end: GridNode):
    nodeMap = dict()
    curr = start
    nodeMap[start] = calculateF(curr, start, end)
    while(curr != end):
        curr.visited = True
        nodeMap.pop(curr)
        for neighbor in curr.neighbors:
            f_cost = calculateF(neighbor,start,end)
            if(neighbor.visited):
                continue
            if(neighbor not in nodeMap or f_cost < nodeMap[neighbor]):
                nodeMap[neighbor] = f_cost
                neighbor.parent = curr
                
        if(not nodeMap):
            print('not found')
            return None
        curr = min(nodeMap, key=nodeMap.get)
        

    answer = []
    while end:
        answer.insert(0,end)
        end = end.parent

    return answer
    
if __name__ == "__main__":
    g = createRandomGridGraph(6)
    x = astar(g.vertexList[0][0], g.vertexList[2][0])

    for i in x:
        print(i.x, i.y)
    pass    
    