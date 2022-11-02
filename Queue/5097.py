def enQueue(item):
    queue.append(item)

def isEmpty():
    return len(queue) == 0

def deQueue():
    if isEmpty():
        print('empty')
    else:
        v = queue.pop(0)
        return v
    
T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    queue = list(input().split())
    for _ in range(m):
        enQueue(deQueue())
    print('#',test_case, ' ', queue[0], sep='')