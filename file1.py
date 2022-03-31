#문제 1000번 (백준)
#Q.두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오
#입력조건/ 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
#출력조건/ 첫째 줄에 A+B를 출력한다
#예제 입력 / 1 2
#예제 출력 / 3



a,b = map(int,input().split())
print(a+b)

#a,b는 콘솔 창에서 입력 받을 것이므로 input() 명령문을 사용한다
#input().split() -> 입력 될 값은 ('1 2') 이다, 이것을 각각
# a = 1 , b = 2 로 지정 해 주기 위해서는 ('1 2') 를
# 우선 1, 2 로 분리 해 주어야 한다.

# 이 때 .split() 을 사용하여 input() 값을 슬라이스한다
# (split 기능은 특정 인수를 기준으로 데이터를 슬라이스 함,
# 소괄호 안을 공백으로 둘 시, 스페이스 기준으로 슬라이스)

# 마지막으로 map () 기능으로 input().split() 리스트를
# int 형식으로 바꿔준다. ex)map (형식,리스트)
# map(int,input().split()) 은 매우 자주 사용되는 구조로
# 잘 이해 해 두는 것이 좋음