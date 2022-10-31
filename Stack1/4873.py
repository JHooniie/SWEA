def overlap(lst, v):
    if lst:
        while lst:
            x = lst.pop()
            if v == x:
                if not stack and not lst:
                    print('동일한 if의 stack: ', stack)
                    print('동일한 if의 lst: ', lst)
                    return
                elif not stack:
                    v = lst.pop()
                    print('동일한 elif의 stack: ', stack)
                    print('동일한 elif의 lst: ', lst)
                    
                    overlap(lst, v)
                else:
                    v = stack.pop()
                    print('동일한 else의 stack: ', stack)
                    print('동일한 else의 lst: ', lst)
                    
                    overlap(lst, v)
            else:
                stack.append(v)
                print('동일하지 않을 때 stack: ', stack)
                print('동일하지 않을 때 lst: ', lst)
                print(x)
                overlap(lst, x)
    else:
        stack.append(v)
    
    print('최종 lst :', lst)
    print('최종 stack :', stack)
    return len(stack)

T = int(input())
for test_case in range(1, T + 1):
    str = list(input())
    lst = str[::-1]
    v = lst.pop()
    stack = []
    print('#', test_case, ' ', overlap(lst, v), sep='')

#오답
# def overlap(lst):
#     while lst:
#         if len(lst) == 1:
#             x = lst.pop()
#             y = stack.pop()
#             if not x == y:
#                 stack.append(y)
#                 stack.append(x)
#                 overlap(lst)
#         if len(lst) >= 2:
#             x = lst.pop()
#             y = lst.pop()
#             print('x : ', x, 'y : ', y)
#             if not x == y:
#                 stack.append(x)
#                 lst.append(y)
#                 overlap(lst)
#         if x == y:
#             print('동일문자 삭제 후 lst :', lst)
#             print('동일문자 삭제 후 stack :', stack)
            
#             overlap(lst)
#     print('최종 lst :', lst)
#     print('최종 stack :', stack)
#     return len(stack)