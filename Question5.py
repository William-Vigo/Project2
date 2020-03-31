import random as rand
class Node:
    def __init__(self, val):
        self.val = val
        self.visited = False
        self.neighbors = []

class Edge:
    def __init__(self, dest: Node, weight: int):
        self.dest = dest
        self.weight = weight

class WeightedGraph:
    def __init__(self):
        self.vertexList = []

    def addNode(self, value):
        node = Node(value)
        self.vertexList.append(node)

    def addWeightedEdge(self, first: Node, second: Node, weight: int):
        if(first == second):
            return
        edge = Edge(second, weight)
        first.neighbors.append(edge)

    def removeDirectedEdge(self, first: Node, second: Node):
        if(first in second.neighbors):
            second.neighbors.remove(first)
        

    def getAllNodes(self):
        return set(self.vertexList)
class TreadmillMazeSolver:
    def dijkstras(self, node: Node):
        minDist = dict()
        queue = []
        queue.append(node)
        minDist[node.val] = 0
        while queue:
            node = queue.pop(0)
            node.visited = True
            for neighbor in node.neighbors:
                if(not neighbor.dest.visited):
                    queue.append(neighbor.dest)
                    
                if neighbor.dest.val in minDist:
                    distance = minDist.get(node.val) + neighbor.weight
                    if(minDist.get(neighbor.dest.val) > distance):
                        minDist[neighbor.dest.val] = distance
                else:
                    minDist[neighbor.dest.val] = minDist[node.val] + neighbor.weight

        return minDist        

#Problem 5c
def createRandomCompleteWeightedGraph(n: int) -> WeightedGraph:
    g = WeightedGraph()
    for i in range(n):
        g.addNode(i)

    for i in range(len(g.vertexList)):
        for j in range(len(g.vertexList)):
            weight = rand.randrange(1,10)
            g.addWeightedEdge(g.vertexList[i], g.vertexList[j], weight)
    return g

#Problem 5d
def createLinkedList(n: int) -> WeightedGraph:
    g = WeightedGraph()
    for i in range(n):
        g.addNode(i)

    for i in range(len(g.vertexList) - 1):
        weight = rand.randrange(1,10)
        g.addWeightedEdge(g.vertexList[i], g.vertexList[i+1], weight)
    return g

if __name__ == "__main__":
    
    g = createRandomCompleteWeightedGraph(4)
    #g = createLinkedList(1)
    for node in g.vertexList:
        print(node.val, end = ' -> ')
        for neighbor in node.neighbors:
            print(neighbor.dest.val , ' w:' + str(neighbor.weight), end=' -> ') 
        print()
    '''
    g = WeightedGraph()
    g.addNode(0)
    g.addNode(1)
    g.addNode(2)
    g.addNode(3)

    g.addWeightedEdge(g.vertexList[0],g.vertexList[1], 5)
    g.addWeightedEdge(g.vertexList[0],g.vertexList[2], 7)
    g.addWeightedEdge(g.vertexList[0],g.vertexList[3], 9)

    g.addWeightedEdge(g.vertexList[1],g.vertexList[0], 1)
    g.addWeightedEdge(g.vertexList[1],g.vertexList[2], 2)
    g.addWeightedEdge(g.vertexList[1],g.vertexList[3], 2)

    g.addWeightedEdge(g.vertexList[2],g.vertexList[0], 8)
    g.addWeightedEdge(g.vertexList[2],g.vertexList[1], 5)
    g.addWeightedEdge(g.vertexList[2],g.vertexList[3], 2)

    g.addWeightedEdge(g.vertexList[3],g.vertexList[0], 4)
    g.addWeightedEdge(g.vertexList[3],g.vertexList[1], 5)
    g.addWeightedEdge(g.vertexList[3],g.vertexList[2], 7)
    '''
    solve = TreadmillMazeSolver()
    answer = solve.dijkstras(g.vertexList[0])
    
    print(answer)
