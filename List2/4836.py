T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    visited = [[0]*10 for _ in range(10)]
    cnt = 0
    
    for _ in range(N):
        rx1, cy1, rx2, cy2, col = map(int, input().split())
        for i in range(rx1, rx2 + 1):
            for j in range(cy1, cy2 + 1):
                if not visited[i][j] == 0:
                    if visited[i][j] == col:
                        continue
                    else:
                        visited[i][j] = 99999
                else:
                    visited[i][j] = col
    print(visited)
    for i in range(10):
        for j in range(10):
            if visited[i][j] == 99999:
                cnt +=1
          
    print('#',test_case, ' ', cnt, sep='')