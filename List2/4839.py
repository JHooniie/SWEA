def binary_search(l, r, p, res):
    global cnt
    c = int((l + r) / 2)
    print(c)
    res += 1
    if c == p:
        return res
    if c > p:
        res = binary_search(l, c, p, res)
    else:
        res = binary_search(c, r, p, res)
    return res


T = int(input())

for test_case in range(1, T + 1):
    r, Pa, Pb = map(int, input().split())
    res = 0
    cnt = 0
    res_pa = 0
    res_pb = 0
    res_pa = binary_search(1, r, Pa, res_pa)
    res_pb = binary_search(1, r, Pb, res_pb)
    print('pa : ', res_pa)
    print('pb : ', res_pb)
    if res_pa == res_pb:
        res = '0'
    elif res_pa < res_pb:
        res = 'A'
    else:
        res = 'B'
    print('#', test_case, ' ', res, sep='')
