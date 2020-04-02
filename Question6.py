import random as rand
import heapq
class GridNode:
    def __init__(self, x_coord, y_coord, value):
        self.val = value
        self.x = x_coord
        self.y = y_coord
        self.parent = None
        self.f_cost = float('inf')
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

def astar(start: GridNode, end: GridNode):
    nodes = []
    start.f_cost = 0
    nodes.append(start)
    found = False
    while nodes:
        nodes.sort(key=lambda x: x.f_cost, reverse=True)
        curr = nodes.pop(0)
        curr.visited = True
        if(curr == end):
            found = True
            break
        for neighbor in curr.neighbors:
            if len(neighbor.neighbors) == 0 or neighbor.visited:
                continue
            #calculate heuristic (manhatton distance)
            h_cost = abs(end.x - neighbor.x) + abs(end.y - neighbor.y)
            g_cost = abs(neighbor.x - start.x) + abs(neighbor.y - start.y)
            f_cost = h_cost + g_cost

            if(f_cost < neighbor.f_cost) or not neighbor.visited:
                neighbor.f_cost = f_cost
                neighbor.parent = curr
                if not neighbor.visited:
                    nodes.append(neighbor)
                    

    if found:
        answer = []
        while end.parent:
            answer.insert(0, end)
            end = end.parent

        return answer
           
    
if __name__ == "__main__":
    g = createRandomGridGraph(9)
    x = astar(g.vertexList[0][0], g.vertexList[8][8])

    for i in x:
        print(i.x, i.y)
    pass    
    