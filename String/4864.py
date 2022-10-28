def str_search(N, M):
    cnt = 0
    #range의 경우 반복할 횟수 기입
    for i in range(len(M) - len(N) + 1):
        if N == M[i:i+len(N)]:
            cnt = 1
            return cnt
        else:
            continue
    return cnt
T = int(input())

for test_case in range(1, T + 1):
    N = str(input())
    M = str(input())
    
    print('#',test_case, ' ', str_search(N, M), sep='')