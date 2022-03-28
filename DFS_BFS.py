import time

# Example 1
## factorial problem

def factorial_iterative(n):
    result = 1
    
    for i in range(1, n + 1):
        result *= i
    
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    
    return n * factorial_recursive(n - 1)

start_time = time.time()
result = factorial_iterative(100)
end_time = time.time()
print(f'result : {result}, {end_time - start_time:.5f}')

start_time = time.time()
result = factorial_recursive(100)
end_time = time.time()
print(f'result : {result}, {end_time - start_time:.5f}')

# Example 2
## great common devisor

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
print(gcd(192, 162))

# Example 3
## DFS (Depth-First Search)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph = [
      []
    , [2, 3, 8]
    , [1, 7]
    , [1, 4, 5]
    , [3, 5]
    , [3, 4]
    , [7]
    , [2, 6, 8]
    , [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)

# Example 4
## BFS (Breadth-First Search)

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
graph = [
      []
    , [2, 3, 8]
    , [1, 7]
    , [1, 4, 5]
    , [3, 5]
    , [3, 4]
    , [7]
    , [2, 6, 8]
    , [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)

# Problem 1
## grouping zeroes in N x M matrix
## input : 4 5
##       : 00110
##       : 00011
##       : 11111
##       : 00000
## ouput : 3

### My Answer

from collections import deque

def row_idx_list(row):
    idx_list = []
    for idx, col in enumerate(row):
        if col == 0:
            idx_list.append(idx)
    return idx_list

def pack_idx(idx_list):
    if len(idx_list) == 0:
        return []
  
    queue = deque(idx_list)
    
    pack = []
    tmp_list = []
    
    idx = queue.popleft()
    tmp_list.append(idx)

    
    while queue:
        idx_n = queue.popleft()
        
        if idx_n - tmp_list[-1] == 1:
            tmp_list.append(idx_n)
        else:
            pack.append(tmp_list)
            tmp_list = [idx_n]
            
    pack.append(tmp_list)
        
    return pack

def compare_idx(pack_idx_before, pack_idx_after):
    count = 0
    if len(pack_idx_before) == 0:
        return len(pack_idx_after)
    elif len(pack_idx_before) == 0:
        return 0
    else:
        for pack_a in pack_idx_after:
            if len(set(pack_a) & set(i for l in pack_idx_before for i in l)) == 0:
                count += 1
        return count
    
def grouping_icecream(graph):
    
    graph = [pack_idx(row_idx_list(row)) for row in graph]
    print(graph)
    count = 0
    for n in range(len(graph)-1):
        count += compare_idx(graph[n], graph[n+1])
        
    return count

n, m = map(int, input().split())

graph = [[]]

for i in range(n):
    graph.append(list(map(int, list(input()))))

start_time = time.time()

result = grouping_icecream(graph)

end_time = time.time()
print(f"result : {result}, {end_time - start_time:.5f}")

### Solution

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        
        graph[x][y] = 1
        
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

start_time = time.time()

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            
end_time = time.time()
print(f"result : {result}, {end_time - start_time:.5f}")


# Problem 2
## escape a maze without confronting zeroes
## input : 5 6
##       : 101010
##       : 111111
##       : 000001
##       : 111111
##       : 111111
## ouput : 10

### My Answer

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)

start_time = time.time()

visited = [[False] * m for _ in range(n)]
count = [[0] * m for _ in range(n)]

def bfs(graph, start, visited, count):
    queue = deque([start])

    visited[start[0]][start[1]] = True
    
    count[start[0]][start[1]] = 1
  
    while queue:
        
        x, y = queue.popleft()
        count_tmp = count[x][y]
        print(f'{(x, y)}, {count[x][y]}')
      
        
        xy_list = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        xy_list = [xy for xy in xy_list if (0 <= xy[0] <= n-1) and (0 <= xy[1] <= m-1)]
        next_xy_list = [xy for xy in xy_list if graph[xy[0]][xy[1]] == 1]
        
        if sum([True for xy in next_xy_list if visited[xy[0]][xy[1]] == True]) == len(next_xy_list):
            pass
            
        else:
            for xy in next_xy_list:
                if not visited[xy[0]][xy[1]]:
                    queue.append(xy)
                  
                    visited[xy[0]][xy[1]] = True
                  
                    count[xy[0]][xy[1]] += count_tmp + 1

    return count[n-1][m-1]

result = bfs(graph, (0, 0), visited, count)

end_time = time.time()
print(f"result : {result}, {end_time - start_time:.5f}")

### Solution

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
start_time = time.time()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = bfs(0, 0)
end_time = time.time()
print(f"result : {result}, {end_time - start_time:.5f}")
