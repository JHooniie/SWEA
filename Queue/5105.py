def search(queue):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    nx = 0
    ny = 0
    
  
    # 큐 확인 후 0개면 탐색 실패(0) 반환
    # 1개 이상일 때 탐색 시작
    if len(queue) < 1:
        return 0
    else:
        while queue:
            #방향 이동
            print('queue 시작 : ', queue)
            buff.append(deQueue())
            x = buff[0][0]
            y = buff[0][1]
            buff.pop(0) 
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 이동 범위 제한
                if nx >= n or nx < 0 or ny >= n or ny < 0:
                    continue
                # 벽 확인
                if miro[nx][ny] == 1:
                    continue
                # 목적지(3) 도착
                if miro[nx][ny] == 3:
                    return visited[x][y]
                # 통로 확인
                if miro[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
                
                # else:
                #     continue
                # if not miro[nx][ny] == 0 and visited[nx][ny] == 0:
                #     print('예외 확인 : ', nx, ny)
                    
                #     continue
    #cnt -= 1
    return 0

def enQueue(item):
    queue.append(item)

def isEmpty():
    return len(queue) == 0

def deQueue():
    if isEmpty():
        print('empty')
    else:
        v = queue.pop(0)
        return v
    
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    miro = [list(map(int,input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    print(miro)
    queue = []
    buff = []
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                queue.append([i,j])
    print('#',test_case, ' ', search(queue), sep='')

# 오답
# def BFS(x, y):
#     global cnt
#     print('재귀 queue : ', queue)
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
    
#     #방향 이동
#     print('queue 시작 : ', queue)
#     print('cnt : ',cnt)
#     # buff.append(deQueue())
#     # x = buff[0][0]
#     # y = buff[0][1]
#     # buff.pop(0)
#     visited[x][y] = 1
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 이동 범위 제한
#         if nx >= n or nx < 0 or ny >= n or ny < 0:
#             continue
#         # 벽 확인
#         if miro[nx][ny] == 1:
#             continue
#         # 목적지(3) 도착
#         if miro[nx][ny] == 3:
#             print('3 도착', nx, ny)
#             print(cnt)
#             return cnt    
#         # 통로 확인
#         if miro[nx][ny] == 0 and visited[nx][ny] == 0:
#             visited[nx][ny] = 1
#             queue.append([nx, ny])

    
#     for _ in range(len(queue)):
#         buff.append(deQueue())
#         x = buff[0][0]
#         y = buff[0][1]
#         buff.pop(0)
#         BFS(x, y)
#     cnt += 1
#         # elif visited[nx][ny] == 1:
#         #     print('예외 확인 : ', nx,ny)
#         # if not miro[nx][ny] == 0 and visited[nx][ny] == 0:
#         #     print('예외 확인 : ', nx, ny)
            
#         #     continue
#     #BFS(queue)
        
#     print(cnt, 'end')
#     #return cnt
  

# def enQueue(item):
#     queue.append(item)

# def isEmpty():
#     return len(queue) == 0

# def deQueue():
#     if isEmpty():
#         print('empty')
#     else:
#         v = queue.pop(0)
#         return v
    
# T = int(input())

# for test_case in range(1, T + 1):
#     n = int(input())
#     miro = [list(map(int,input())) for _ in range(n)]
#     visited = [[0]*n for _ in range(n)]
#     print(miro)
#     queue = []
#     buff = []
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if miro[i][j] == 2:
#                 queue.append([i,j])
#     buff.append(deQueue())
#     x = buff[0][0]
#     y = buff[0][1]
#     buff.pop(0)            
           
#     print('#',test_case, ' ', BFS(x, y), sep='')



# def BFS(queue):
#     global cnt
#     print('재귀 queue : ', queue)
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     nx = 0
#     ny = 0
#     # 큐 확인 후 0개면 탐색 실패(0) 반환
#     # 1개 이상일 때 탐색 시작
#     if len(queue) < 1:
#         return 0
#     else:
#         cnt += 1
#         #방향 이동
#         print('queue 시작 : ', queue)
#         print('cnt : ',cnt)
#         buff.append(deQueue())
#         x = buff[0][0]
#         y = buff[0][1]
#         buff.pop(0)
#         visited[x][y] = 1
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 이동 범위 제한
#             if nx >= n or nx < 0 or ny >= n or ny < 0:
#                 continue
#             # 벽 확인
#             if miro[nx][ny] == 1:
#                 continue
#             # 목적지(3) 도착
#             if miro[nx][ny] == 3:
#                 print('3 도착', nx, ny)
#                 print(cnt)
#                 return cnt    
#             # 통로 확인
#             if miro[nx][ny] == 0 and visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 queue.append([nx, ny])
#         print(queue)
#         for _ in range(len(queue)):
#             BFS(queue)

        
#     print(cnt, 'end')
#     #return cnt
  

# def enQueue(item):
#     queue.append(item)

# def isEmpty():
#     return len(queue) == 0

# def deQueue():
#     if isEmpty():
#         print('empty')
#     else:
#         v = queue.pop(0)
#         return v
    
# T = int(input())

# for test_case in range(1, T + 1):
#     n = int(input())
#     miro = [list(map(int,input())) for _ in range(n)]
#     visited = [[0]*n for _ in range(n)]
#     print(miro)
#     queue = []
#     buff = []
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if miro[i][j] == 2:
#                 queue.append([i,j])
                
           
#     print('#',test_case, ' ', BFS(queue), sep='')