visited = [] 
queue = []     
class Graph:
    
    def __init__(self, num_of_nodes, directed=True):
     self.m_num_of_nodes = num_of_nodes
     self.m_directed = directed
        # Different representations of a graph
     self.m_list_of_edges = []
     # Initialize the adjacency matrix
     # Create a matrix with `num_of_nodes` rows and columns
     self.m_adj_matrix = [[0 for column in range(num_of_nodes)] for row in range(num_of_nodes)]
	
    # Add edge to a graph
    def add_edge(self, node1, node2, weight=1):        
        # Add the edge from node1 to node2
        self.m_list_of_edges.append([node1, node2, weight])
        self.m_adj_matrix[node1][node2] = weight
        # If a graph is undirected, add the same edge,but also in the opposite direction
        if not self.m_directed:
            self.m_list_of_edges.append([node1, node2, weight])
            self.m_adj_matrix[node1][node2] = weight

	
    def print_edge_list(self):
        num_of_edges = len(self.m_list_of_edges)
        for i in range(num_of_edges):
            print("edge ", i+1, ": ", self.m_list_of_edges[i])
        print("The adjacency matrix :")
        for i in range(len(self.m_adj_matrix)):
          print(self.m_adj_matrix[i])    

    def bfs (self,visited, only_edge, nd): #function for BFS
      visited.append(nd)
      queue.append(nd)
      while queue:          # Creating loop to visit each node
        m = queue.pop(0) 
        print (m, end = " ") 
        for neighbour in only_edge[m]:
         if neighbour not in visited:
          visited.append(neighbour)
          queue.append(neighbour)

graph = Graph(5)
graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)
only_edge={0:[0,1,2], 1:[3,4], 2:[], 3:[], 4:[2,3]}
n = int(input("Enter the starting node for bfs traversal"))
print("Following is the Breadth-First Search")
graph.bfs(visited,only_edge, n)    # function calling
print()
graph.print_edge_list()
 
