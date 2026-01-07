def dfs_graph(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs_graph(graph, next, visited)
    return visited

if __name__ == "__main__":
    graph = {'A': {'B', 'C'},
            'B': {'C', 'E'},
            'C': {'D', 'B'},
            'D': {'A'},
            'E': {'A'}}
    
    dfs_graph(graph, 'E')