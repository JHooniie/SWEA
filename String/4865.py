#카운트 리스트 비교 함수
def my_max(max_lst):
    str_max = 0
    for i in max_lst:
        if str_max < i:
            str_max = i
    return str_max

T = int(input())

for test_case in range(1, T + 1):
    N = list(map(str, input()))
    M = list(map(str, input()))

    # 딕셔너리(키:값) 사용
    # str1의 원소가 M(str2)에 몇 개 포함되어 있는지 저장할 리스트
    str1 = dict()
    max_lst = []

    # N리스트에 있는 원소들을 str1 딕셔너리에 키, 값 설정
    for i in N:
        str1[i] = i
    
    # str1의 원소를 하나씩 추출한 뒤 M(str2)의 리스트 원소들과 전체 비교 후 같은 값이 존재하면 카운트
    # 카운트된 값을 리스트에 삽입 후 대소비교 함수를 사용하여 바로 출력
    for i in str1:
        cnt = 0
        for j in range(len(M)):
            
            if str1[i] == M[j]:
                cnt += 1
            else:
                continue
            
        max_lst.append(cnt)
        print(max_lst)
            
    print('#', test_case, ' ', my_max(max_lst), sep='')
