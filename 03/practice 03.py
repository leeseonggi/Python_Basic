print(1+1)
print(3-1)

print(2**3) # 2^3
print(5 % 3) # 나머지 계신
print(10 % 3)
print(5//3) # 몫
print(10//3)

print(10>3)
print(4 >= 7)
print(5 <= 5)

print(3==3) # 등호 앞과 뒤가 똑같은지 확인

print(1 != 3) # True
print(not(1 != 3)) #False

print((3>0)and(3<5)) 
print((3>0) & (3<5)) # AND 연산

print((3>0) or (3>5)) # OR 연산
print((3>0) | (3>0))

print(5>4>7)

print(2+3*4)
print((2+3)*4)
number = 2+3*4
number = number + 2
print(number)
number += 2
print(number)
number *=2
print(number)
number /= 2
print(number)
number -= 2
print(number)

number %= 5
print(number)

print(abs(-5)) # 절대값 반환
print(pow(4, 2)) # 4^2 
print(max(5, 12)) # 최대값
print(min(5,12)) # 최소값
print(round(3.14)) # 반올림
print(round(4.99))

from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근

from random import *
print(random()) # 0.0 ~ 1.0 사이의 임의의 값 생성
print(random()*10)  # 0.0 ~ 10.0 사이의 임의의 값 생성
print(int(random()))    # 0.0 ~ 1.0 사이의 정수부분만
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)

print(randrange(1, 46)) # 1 ~ 46미만의 임의의 값 생성

print(randint(1, 45)) # 1과 45 포함
print(randint(1, 45)) # 1과 45 포함

offline_date = randrange(3,29)
print('오프라인 스터디 모임 날짜는 매월'+str(offline_date)+'일로 선정되었습니다')
