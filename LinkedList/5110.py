 # 삽입정렬
def my_insert():
    for i in range(m - 1):
        check = len(lst)
        stack = list(map(int, input().split()))
        for j in range(len(lst)):
            if lst[j] > stack[0]:
                lst[j:0] = stack
                break
        if len(lst) == check:
            lst.extend(stack)
        print(lst)
    return lst[::-1]
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    res = my_insert()  
    #print(res[-1:-11:-1])
    print('#', test_case, sep='', end=' ')
    print(' '.join(str(res[n]) for n in range(10)))


# 제한 시간 초과
# 대소비교
# def my_max(i):
#     print('대소비교 seq : ',seq, len(seq))
#     for s in range(len(seq)):
#         print(s)
#         if seq[s] > lst[i][0]:
#             print('대소비교 : ',s)
#             return s
#         elif not seq[s] > lst[i][0]:
#             continue
#     return len(seq)
#  # 삽입정렬
# def my_insert():
#     stack = []
#     print('xhdrhk')
#     for i in range(1, m):
#         ind = my_max(i)
#         print('인덱스 : ',ind)
#         if not len(seq) == ind:           
#             for _ in range(len(seq) - ind):
#                 v = seq.pop()
#                 stack.append(v)
#             for j in lst[i]:
#                 seq.append(j)
#             for j in range(len(stack)):
#                 v = stack.pop()
#                 seq.append(v)
#         else:
#             for j in lst[i]:
#                 seq.append(j)
#         print(seq)
#     #stack = seq[::-1]
#     for i in range(10):
#         stack.append(str(seq.pop()))
#     print('asdfdf ',stack)
#     return stack
# T = int(input())
# for test_case in range(1, T + 1):
#     n, m = map(int, input().split())
#     lst = [list(map(int, input().split())) for _ in range(m)]
#     seq = lst[0]
#     print(seq)
#     #print('#', test_case, sep='', end=' ')
#     print(' '.join(my_insert()))