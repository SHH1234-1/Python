from math import factorial #factorial 함수 호출
n = int(input()) #첫째줄에 n 이 주어진다
cnt = 0 #끝에 있는 0의 개수를 세기 위한 카운터 cnt
for x in str(factorial(n))[::-1]:#n의 factorial을 구한후 문자열을 뒤집고 그 문자열 하나씩 꺼내서
    if x !='0': #뒤집은 문자열열이 0이 아니면
        break
    cnt+=1
    print(cnt)




