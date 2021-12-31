# 리스트 []

# 지하철 칸별로 10명, 20명, 30명

subway = [10, 20, 30]
print(subway)

subway = ['유재석','조세호','박명수']
print(subway)

# 조세호씨가 몇번째 칸에 타고있는가?
print(subway.index('조세호'))

# 다음 정류장에서 다음칸에 류진이 탐
subway.append('류진')
print(subway)
# 유나를 유재석 / 조세호 사이에 태워봄
subway.insert(1,'유나')
print(subway)

# 지하철 타고있는 사람이 뒤에서부터 한명씩 내림
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명 있는지 확인

subway.append('유재석')
print(subway)
print(subway.count('유재석'))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기도 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 리스트는 자료형에 구애받지 않음(파이썬)
num_list = [3,4,5,6,78,1]
mix_list = ['아이린',30,True]
print(mix_list)
num_list.extend(mix_list) # 배열을 뒤에다 같다붙임
print(num_list)

# 사전 (Dictionary)
cabinet = {3:'신유나', 100:"신류진"} # key : value
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5)) # NONE 이라 출력하고 그냥 프로그램 지속
print(cabinet.get(5, '사용가능'))
# print(cabinet[5]) 없는 키의 값을 가져오려 할때 []는 오류 출력하고 프로그램 종료
print(3 in cabinet) # 있으면 True
print(5 in cabinet) # 없으면 False

cabinet_01 = {'A-3':'슬기','B-100':'아이린'}
print(cabinet_01['A-3'])
print(cabinet_01['B-100'])

# 새 손님
print(cabinet_01)
cabinet_01['A-3'] = '은하'
cabinet_01['C-10'] = "예린"
print(cabinet_01)

# 간 손님
del cabinet_01['A-3']
print(cabinet_01)

# key 들만 출력
print(cabinet_01.keys())

# value 들만 출력
print(cabinet_01.values())

# key, value 쌍으로 출력
print(cabinet_01.items())

# 목욕탕 마감
cabinet_01.clear()
print(cabinet_01)


# Tuple 
# 리스트보다 빠르나 변경이나 수정 불가
menu = ("돈까스", "치즈까쓰")
print(menu[0])
print(menu[1])
# menu.add("생선까쓰") 추가나 변경 불가

name = '은비'
age = 25
hobby = '노래'
print(name, age, hobby)

(name_01, age_01, hobby_01) = ("은비",25,'노래')
print(name_01,age_01,hobby_01)

# SET 집합
# 중복이 안됨, 순서가 없음
my_set = {1,2,3,4,3,3} # Dictionary와 형태는 같지만 key와 value로 나누지는 않음
print(my_set)   # 중복된 값들 다 무시함

java = {'예린','신비','은하'}
python = set(['예린','소원'])

# 교집합 출력 java와 python 모두 가능한사람 출력
print(java & python)
print(java.intersection(python))

# 합집합 (java 나 python 둘중 하나만 해도 된다)
print(java | python)
print(java.union(python)) # 순서에 없이 출력

# 차집합 (java는 할줄알지만 python 못하는 개발자들에게 교육하겠다)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는사람이 늘어남
python.add('유주')
print(python)

# java를 까먹었다!
java.remove('신비')
print(java)

# 자료구조의 변경
# 커피숍
menu = {'커피','우유','주스'}
print(menu,type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu,type(menu))

menu = set(menu)
print(menu,type(menu))

# random 모듈의 shuffle과 sample을 활용
from random import * # 문제풀이 위한 랜덤 선언
first = [1,2,3,4,5]
print(first)
shuffle(first) # 셔플로 섞음
print(first)

#퀴즈 random 끌어와서 shuffle과 sample활용
commentors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(commentors)
print(commentors)
print('---당첨자 발표---')
print('치킨 당첨자 : ',commentors.pop())
print('커피 당첨자 : [' ,commentors.pop(),',',commentors.pop(),',',commentors.pop(),']')
print('---축하합니다---')

# 풀이
users = range(1,21) # 1부터 20까지 숫자 생성
print(type(users)) # type이 range로 나옴 그래서 
users = list(users) # 자료구조 변환 list로
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명을 우선 뽑아서 1명은 치킨 3명을 커피

print('---당첨자 발표---')
print('치킨 당첨자 : {0}'.format(winners[0]))
print('커피 당첨자 : {0}' .format(winners[1:]))
print('---축하합니다---')






