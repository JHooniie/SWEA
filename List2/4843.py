def asc_sort(list):
    for n in range(len(list) - 1):
        for m in range(n + 1, len(list)):
            if list[n] > list[m]:
                list[n], list[m] = list[m], list[n]


def my_sort(list):
    subset = []
    for i in range(5):
        subset.append(list[-(i + 1)])
        subset.append(list[i])

    return subset


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    M = list(map(int, input().split()))
    asc_sort(M)

    print('#', test_case, sep='', end=' ')
    print(*my_sort(M), end=' ')
    print()
