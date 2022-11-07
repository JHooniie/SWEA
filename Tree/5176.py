def binary_tree(s):
    global cnt
    if s <= n:
        binary_tree(s*2)
        cnt += 1
        tree[s] = cnt
        binary_tree((s*2)+1)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    tree = [0] * (n+1)
    cnt = 0
    binary_tree(1)
        
    print('#', test_case, ' ', tree[1],' ', tree[n//2], sep='')