import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent = {}
        self.visited = False
        self.distance = float('inf')
        self.parent = None

    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight

    def get_neighbors(self):
        return self.adjacent.keys()

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def get_node(self, name):
        return self.nodes.get(name)

def astar(graph, start, goal):
    # Set of nodes already evaluated
    closed_set = set()
    # Set of tentative nodes to be evaluated
    open_set = []
    # Add the start node to open set
    heapq.heappush(open_set, (0, start))
    
    # Cost from start along best known path
    start.distance = 0
    # Estimated total cost from start to goal through y
    start.total_distance = heuristic(start, goal)

    while open_set:
        # Pop the node with the smallest total_distance
        current_distance, current_node = heapq.heappop(open_set)

        if current_node == goal:
            return reconstruct_path(goal)

        current_node.visited = True

        for neighbor in current_node.get_neighbors():
            if neighbor.visited:
                continue
            
            tentative_distance = current_node.distance + current_node.adjacent[neighbor]
            if tentative_distance < neighbor.distance:
                neighbor.parent = current_node
                neighbor.distance = tentative_distance
                neighbor.total_distance = tentative_distance + heuristic(neighbor, goal)
                heapq.heappush(open_set, (neighbor.total_distance, neighbor))

    return None

def heuristic(node, goal):
    # Heuristic function, in this case, Euclidean distance
    return 0

def reconstruct_path(goal):
    path = []
    current = goal
    while current.parent:
        path.append(current.name)
        current = current.parent
    path.append(current.name)
    return path[::-1]

# Example usage
if __name__ == "__main__":
    # Create graph
    graph = Graph()
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")

    A.add_neighbor(B, 5)
    A.add_neighbor(C, 10)
    B.add_neighbor(D, 3)
    C.add_neighbor(D, 2)
    D.add_neighbor(E, 7)

    graph.add_node(A)
    graph.add_node(B)
    graph.add_node(C)
    graph.add_node(D)
    graph.add_node(E)

    # Find shortest path
    path = astar(graph, A, E)
    print("Shortest path:", path)
