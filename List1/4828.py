def my_min(num, i):
    global num_min
    if i == 0:
        num_min = num[i]
    else:
        if num_min > num[i]:
            num_min = num[i]

def my_max(num, i):
    global num_max
    if i == 0:
        num_max = num[i]
    else:
        if num_max < num[i]:
            num_max = num[i]     

T = int(input())
num_min = 0
num_max = 0

for test_case in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    for i in range(n):
        my_min(num, i)
        my_max(num, i)
    print('#',test_case, " ", num_max - num_min, sep='')
    num = []
    num_min = 0
    num_max = 0
    