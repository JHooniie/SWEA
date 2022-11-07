def binary_tree(s):
    if s <= n:
        if tree[s//2] > tree[s]:
            tree[s//2], tree[s] = tree[s], tree[s//2]
            binary_tree(s//2)
    return
def p_node(n):
    sum = 0
    while n >= 1:
        n = n // 2
        sum += tree[n]
        
    return sum
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    tree = [0] + list(map(int, input().split()))
    for i in range(1, n+1):
        binary_tree(i)
    print('#', test_case, ' ', p_node(n), sep='')

# 런타임 에러
# 함수 실행 시 반복문을 활용하여 런타임에러 해결
# def binary_tree(s):
#     if s <= n:
#         print(s)
#         if tree[s//2] > tree[s]:
#             tree[s//2], tree[s] = tree[s], tree[s//2]
#             binary_tree(s//2)
#         binary_tree(s+1)
#     return
# def p_node(n):
#     sum = 0
#     while n >= 1:
#         print('조상 노드 : ',n)
#         n = n // 2
#         sum += tree[n]
        
#     return sum
# T = int(input())
# for test_case in range(1, T + 1):
#     n = int(input())
#     heap = list(map(int, input().split()))
#     tree = [0] * (n+1)
#     for i in range(n):
#         tree[i+1] = heap[i]
#     print(tree)
#     binary_tree(1)
#     print(tree)    
#     print('#', test_case, ' ', p_node(n), sep='')