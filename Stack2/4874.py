# 오답
# def cal(stack, v):
#     stack.append(v)
#     while stack:
#         v = stack.pop()
#         if not v.isdigit():
            
#             print('not int v1 : ', v)
#             print('not int stack', stack)
#             print('not int token', token)
#             if len(stack) == 1 and v == '.':
#                 v = stack.pop()
#                 return v
            
#             elif not len(stack) == 1 and v == '.':
#                 v = 'error'
#                 return v
#             y = stack.pop()
#             x = stack.pop()
#             print('not int x y : ', x, y)
#             if x.isdecimal() and y.isdecimal():
#                 if v == '+':
#                     v = x + y
#                 elif v == '-':
#                     v = x - y
#                 elif v == '*':
#                     v = x * y
#                 elif v == '/':
#                     v = x // y
                
#                 stack.append(v)
#                 v = token.pop()
#                 print('stack : ', stack)
#                 print('token : ', token)
#                 print('int v : ', v)
#                 return cal(token, v)
                
#             else:
#                 v = 'error'
#                 return v
#         else:
#             print('origin v : ', v)
#             stack.append(v)
#             v = token.pop()
#             print('pop v : ', v)
#             print('pop stack : ', stack)
#             return cal(stack, v)

# T = int(input())

# for test_case in range(1, T + 1):
#     lst = list(map(str, input().split()))
#     token = lst[::-1]
#     stack = []
#     v = token.pop()
#     print('#', test_case, ' ', cal(stack, v), sep='')


# 오답1
# def cal(stack, v):
#     if stack:
#         while stack:
#             print('stack : ', stack)
#             print('token : ', token)
#             if v == '.' or v == '+' or v == '-' or v == '*' or v == '/':
#                 x =int(token.pop())
#                 y = int(token.pop())
#                 if v == '+':
#                     v = x + y
#                 elif v == '-':
#                     v = x - y
#                 elif v == '*':
#                     v = x * y
#                 elif v == '/':
#                     v = x / y
#                 print('stack in : ',v)
#                 token.append(v)
#                 print('stack in : ',token)
#                 v = stack.pop()
#                 print('stack after :',v)
#                 cal(stack, v)
#                 return v
#             else:
#                 token.append(int(v))
#                 print('int token: ', token)
                
#                 v = stack.pop()
#                 cal(stack, v)
#                 return v
#     else:
#         print(v)
#         if v == '.':
#             print(v)
#             v = token.pop()    
#             print(v)
#     print('final token : ', token)
#     return v
            

# T = int(input())

# for test_case in range(1, T + 1):
#     lst = list(map(str, input().split()))
#     stack = lst[::-1]
#     token = []
#     v = stack.pop()
#     print('#', test_case, ' ', cal(stack, v), sep='')

#오답2
# def cal(stack, v):
#     while stack:
#         print('stack : ', stack)
#         print('token : ', token)
#         if not v.isdigit():
#             x =int(token.pop())
#             y = int(token.pop())
#             if v == '+':
#                 v = x + y
#             elif v == '-':
#                 v = x - y
#             elif v == '*':
#                 v = x * y
#             elif v == '/':
#                 v = x // y
#             print('stack in : ',v)
#             token.append(v)
#             print('stack in : ',token)
#             v = stack.pop()
#             print('stack after :',v)
#             if len(token) == 1 and not v.isdigit():
#                 if v == '.':
#                     print('final stack : ', stack)
#                     print('final token : ', token)
#                     v = token.pop()
#                     return v
#                 else:
#                     v = 'error'
#                     return v
#             elif len(token) >= 2 and not v.isdigit():
#                 if v == '.':
#                     v = 'error'
#                     return v
#             return cal(stack, v)
#         else:
#             token.append(int(v))
#             print('int token: ', token)
            
#             v = stack.pop()
#             return cal(stack, v)
#     print('cal token : ',token)    
#     return 
            

# T = int(input())

# for test_case in range(1, T + 1):
#     lst = list(map(str, input().split()))
#     stack = lst[::-1]
#     token = []
#     v = stack.pop()
#     print('#', test_case, ' ', cal(stack, v), sep='')