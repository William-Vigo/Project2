class GraphNode:
    def __init__(self, Value: str):
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
        First.neighbors.append(Second)
        Second.neighbors.append(First)

    def removeUndirectedEdge(self, First: GraphNode, Second: GraphNode):
        First.neighbors.remove(Second)
        Second.neighbors.remove(First)

    def getAllNodes(self):
        return set(self.nodes)


if __name__ == "__main__":
    
    g = Graph()
    g.addNode('S')
    g.addNode('A')
    print(g.nodes[0].neighbors)
    g.addUndirectedEdge(g.nodes[0], g.nodes[1])
    print(g.nodes[0].neighbors)
    g.removeUndirectedEdge(g.nodes[0],g.nodes[1])
    print(g.nodes[0].neighbors)
  