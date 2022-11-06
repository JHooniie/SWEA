def dfs(x):
    global sum
    for i in range(len(x), N):
        for j in range(N):
            if j in x:
                continue
            x.append(j)
            sum += graph[i][j]
            if i == N:
                stack.append(sum)
                
            dfs(j)
    

T = int(input())


for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    x = []
    
    
    
        
    print('#', test_case, ' ', dfs(x), sep='')