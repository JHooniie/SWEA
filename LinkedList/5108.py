T = int(input())

for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    lst = list(map(int, input().split()))
    for i in range(m):
        stack = []
        ind, num = map(int, input().split())
        for j in range(len(lst) - ind):
            v = lst.pop()
            stack.append(v)
        lst.append(num)
        for j in range(len(stack)):
            v = stack.pop()
            lst.append(v)
    print('#', test_case, ' ', lst[l], sep='')
