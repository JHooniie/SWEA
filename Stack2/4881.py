def back(x, y, now_sum, visited):
    global min_sum
    if x == n:
        if now_sum < min_sum:
            min_sum = now_sum
    elif now_sum > min_sum:
        return
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                back(x + 1, i, now_sum + graph[x][i], visited)
                visited[i] = 0


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 99999
    visited = [0] * n
    back(0, n, 0, visited)

    print('#', test_case, ' ', min_sum, sep='')

# 오답
# def dfs(x):
#     global sum
#     for i in range(len(x), N):
#         for j in range(N):
#             if j in x:
#                 continue
#             x.append(j)
#             sum += graph[i][j]
#             if i == N:
#                 stack.append(sum)
                
#             dfs(j)
    

# T = int(input())


# for test_case in range(1, T + 1):
#     N = int(input())
#     graph = [list(map(int, input().split())) for _ in range(N)]
#     stack = []
#     x = []
    
    
    
        
#     print('#', test_case, ' ', dfs(x), sep='')