from collections import deque

def bfs(graph, start):
    visited = []
    q = deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
    return visited

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': ['A', 'D']
    }
    start_node = 'C'
    print("BFS Traversal starting from node", start_node, ":", bfs(graph, start_node))