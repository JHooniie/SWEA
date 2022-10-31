def dfs(S):
    visited[S] = True
    for i in graph[S]:
        if not visited[i]:
            dfs(i)


def asc_sort(graph):
    for i in range(len(graph)):
        min_n = 0
        for j in range(len(graph[i])):
            if graph[i][min_n] > graph[i][j]:
                graph[i][min_n], graph[i][j] = graph[i][j], graph[i][min_n]


T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)

    for i in range(E):
        N, M = map(int, input().split())
        graph[N].append(M)
        #graph[M].append(N) 방향성 때문에 기입할 시 오답

    asc_sort(graph)
    S, G = map(int, input().split())
    dfs(S)
    if visited[G]:
        ans = 1
    else:
        ans = 0
    print('#', test_case, ' ', ans, sep='')
