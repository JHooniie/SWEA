def my_sum(subset):
    sum = 0
    for i in subset:
        sum += i
    return sum

T = int(input())
for test_case in range(1, T + 1):
    A = []
    for i in range(1, 13):
        A.append(int(i))

    N, K = map(int, input().split())
    cnt = 0
    
    for i in range(1 << len(A)):
        subset = []
        for j in range(len(A)):
            if i & (1 << j):
                subset.append(A[j])
        if N == len(subset) and K == my_sum(subset):
            cnt += 1
    print('#', test_case, ' ', cnt, sep='')