def tree_search(N):
    global cnt
    visited[N] = True
    cnt += 1
    print(N, ' cnt: ', cnt)
    for i in tree[N]:
        if i == 0:
            continue
        if not visited[i]:
            tree_search(i)

    return cnt


T = int(input())

for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    p_tree = lst[0::2]
    print(p_tree)
    c_tree = lst[1::2]
    print(c_tree)
    tree = [[0] for _ in range(E + 2)]
    print(tree)
    visited = [False] * (E + 2)
    cnt = 0
    for i in p_tree:
        tree[i].append(c_tree.pop(0))

    print('#', test_case, ' ', tree_search(N), sep='')
