#정답코드
def pair(str):
    brac = []
    for i in str:
        if i == '(' or i == '{':
            brac.append(i)
        elif i == ')' or i == '}':
            if not brac:
                return 0
            elif i == ')' and brac.pop() != '(':
                return 0
            elif i == '}' and brac.pop() != '{':
                return 0

    if len(brac) == 0:
        return 1
    return 0


T = int(input())

for test_case in range(1, T + 1):
    str = list(input())
    print('#', test_case, ' ', pair(str), sep='')

#런타임 에러 코드
# def pair(str):
#     for i in str:
#         print(i)
#         if i == '(' or i == '{':
#             brac.append(i)
#             print(brac)
#         elif i == ')' or i == '}':
#             print('-1 :', brac[-1])
#             if brac[-1] == '(' and i == ')':
#                 brac.pop()
#             elif brac[-1] == '{' and i == '}':
#                 print('pop :', i)
#                 brac.pop()
#         else:
#           continue
#         print(brac)
#     if len(brac) == 0:
#         return 1
#     else:
#         return 0
# T = int(input())

# for test_case in range(1, T + 1):
#     str = list(map(str, input()))
#     print(str)
#     brac = []
#     print('#', test_case, ' ', pair(str), sep='')
