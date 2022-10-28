# 회문(펠린드롬) 찾는 함수
def search_palindrome(lst, N, M):
    for i in range(N):
        for j in range(N):

            # 세로줄 탐색

            # N*N 범위 안에서만 탐색할 수 있게 설정
            # 처음에는 i + M > N으로 if문을 작성한 뒤 continue를 걸었지만 
            # 가로 범위를 탐색하지 않는걸 발견 함
            # continue의 경우 해당 반복문을 더 이상 실행하지 않고 넘길 때 필요함
            # 밑의 가로 범위 하나에만 설정하는 것은 괜찮을 것 같음
            if i + M <= N:
                comp = []
                comp_lst = []
                #세로의 경우 [:]범위 지정이 안되기에 원래 값을 담아둘 리스트와 회문 함수를 같이 설정
                for k in range(i, i+M):
                    #print('k : ',k)
                    comp.append(lst[k][j])
                    comp_lst.append(lst[k][j])
                
                make_palindrome(comp)
                #print(i,'-', j, '세로 회문 만들기 : ', comp)
                #테스트 10개 중 9개에서 실패가 떠서 직접 확인한 코드
                if comp == comp_lst:
                    return listToString(comp)
            # 가로줄 탐색

            # 가로 범위탐색 초과 시
            if j + M <= N:
                comp = lst[i][j:j+M]
                
                make_palindrome(comp)
                #print(i,'-', j,  '가로 회문 만들기 : ', comp)
                if comp == lst[i][j:j+M]:
                    return listToString(comp)
              
#[::-1]을 사용하지 않고 회문을 만들기 위한 함수(아마 다음에는 [::-1]을 사용할 듯)
def make_palindrome(comp):
    for i in range(M//2):
        comp[i], comp[-(i+1)] = comp[-(i+1)], comp[i]
        #print('회문 변경 중 : ', comp)

# 리스트의 문자를 문자열로 합쳐주는 함수
def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + ""
    return result.strip()
  
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = []
    for i in range(N):
        lst.append(list(map(str, input())))
    #print(lst)
    print('#', test_case, ' ', str(search_palindrome(lst, N, M)), sep='')
