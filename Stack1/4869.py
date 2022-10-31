def fibo(c):

    if c == 1:
        fibo_lst[1] = 1
    if c == 2:
        fibo_lst[2] = 3
    if c == 3:
        fibo_lst[3] = 3
    if c > 2:
        fibo_lst[c] = fibo(c - 1) + (fibo(c - 2) * 2)
    return fibo_lst[c]


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    c = N // 10
    fibo_lst = [0] * (c + 1)
    print('#', test_case, ' ', fibo(c))
