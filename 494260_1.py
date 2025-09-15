import sys
from collections import deque

def solve_infection_path():
    # Read N and M
    try:
        n_str, m_str = sys.stdin.readline().split()
        N = int(n_str)
        M = int(m_str)
    except (IOError, ValueError):
        # Handle empty line at the end of input
        return

    # Create adjacency list
    adj = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        u_str, v_str = sys.stdin.readline().split()
        u, v = int(u_str), int(v_str)
        adj[u].append(v)
        adj[v].append(u)

    # Read source and target
    s_str, t_str = sys.stdin.readline().split()
    S = int(s_str)
    T = int(t_str)

    # --- BFS Implementation ---
    queue = deque([S])
    visited = {S}
    parent = {S: None}

    path_found = False
    while queue:
        current_node = queue.popleft()
        if current_node == T:
            path_found = True
            break
        
        for neighbor in adj[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_node
                queue.append(neighbor)
    
    # --- Reconstruct Path ---
    if path_found:
        path = []
        curr = T
        while curr is not None:
            path.append(str(curr))
            curr = parent.get(curr)
        
        print(" ".join(path[::-1]))
    else:
        print(-1)

# The following is just for local testing
# In a real submission system, the function will be called directly.
# For example, you would have a main block like this:
if __name__ == "__main__":
    solve_infection_path()
