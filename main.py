# Basic Note - Python (edited.03.30.2022)  
# Data
a = 1    #Int 정수
b = -7
c = 0
aa = 1.5  #RealNum 실수
bb = -1.5
cc = 5.
dd = -.5
aaa = 1e9 #지수 표현 , 숫자e지수 = 숫자*10지수, 1e9 == 10억
bbb = 75.25e1 # 752.5
ccc = 3954e-3 # 3.954
aaa= int(1e9)  # 표현할 시 정수형으로 출력하고 싶으면 지정해주기


#Round 함수 / round(number,자리수지정)
round(123.456,2)  # 123.46

#산술연산자
division = a / b # 나누기는 지정 없을시 실수형으로 반환함
remainder = a % b # 나머지
Quotient = a // b # 몫
2 ** 3 == 8 # 제곱

#비교연산자
a == 2 and b == 3 # 두 조건 모두 참일시
a == 2 or b == 3 # 두 조건 중 하나라도 참일시
not b == 3  # 조건 자체가 거짓일 시 True

# 비트를 아끼고 싶다면... 비트 연산자를 쓰세요...

#항등연산자
L1 = [1,2,3]
L2 = [1,2,3]
L1 == L2 #True
L1 is L2 #False
L1 is not L2 #True

#List
n=5        #ex-1
L3 = [0]*n
#print(L3) : [0,0,0,0,0]

L4 = [3,4,6,9]  #ex-2
L4[4] = 4
#print (L4) : [3,4,6,4]
