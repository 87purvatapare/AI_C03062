class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []  # List to store graph edges

    # Function to add an edge to the graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # Find function (for Disjoint Set Union - DSU)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Union function (for DSU)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Kruskal's Minimum Spanning Tree Algorithm
    def KruskalMST(self):
        result = []  # Store the final MST
        i, e = 0, 0  # `i` is used for sorted edges, `e` counts edges in MST

        # Step 1: Sort all the edges in increasing order of weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Initialize parent and rank for each vertex
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Step 2: Pick the smallest edge and check if it forms a cycle
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does not cause a cycle, include it in the result
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Print the final MST
        minimumCost = sum(weight for _, _, weight in result)
        print(f'\nKruskal’s Minimum Spanning Tree:')
        print(f'Edge\tWeight')
        for u, v, weight in result:
            print(f'{u} -- {v} == {weight}')
        print(f'\nMinimum cost = {minimumCost}')

# Example Usage
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()
