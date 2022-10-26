T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_station = tuple(map(int, input().split()))
  
    now = 0
    charge_pass = now + K
    bus_charge = 0
    cnt = 0
  
    while (charge_pass < N):
        for i in bus_station:
            if now < i <= charge_pass:
                bus_charge = i
            elif charge_pass < i:
                break

        if bus_charge == -1:
            cnt = 0
            break

        now = bus_charge
        charge_pass = now+K
        cnt += 1
        bus_charge = -1
    
    print('#', test_case, ' ', cnt, sep='')