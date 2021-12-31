#input : 사용자 입력을 받는 함수
# language = input('무슨 언어를 좋아하세요? ')
# print('{0}은 아주 좋은 언어입니다!'.format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

print(dir(random)) 
# random 안에서 쓸 수 있는것들 보여줌
# random. 찍었을때 나오는거량 유사함

lst = [1,2,3]
print(dir(lst))

name = 'jim'
print(dir(name))

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob('*.py')) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리

folder = 'sample_dir'

if os.path.exists(folder): # sample_dir 이란 폴더가 있으면은 구문을 타라
    print('이미 존재하는 폴더입니다')
    os.rmdir(folder) # 존재하는 폴더를 제거하는 함수
    print(folder, '폴더를 삭제하였습니다.')
else:
    os.makedirs(folder) # 폴더를 직접 만듬
    print(folder,'폴더를 생성하였습니다.')
    
print(os.listdir()) # 글롭과 비슷하게 사용

# time : 시간 관련 함수
import time
print(time.localtime()) # 현재 날짜와 시간 등등 나옴
print(time.strftime('%y-%m-%d %H:%M:%S')) # 원하는 형태로 년-월-일 시-분-초

import datetime
print('오늘 날짜는 ',datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜를 저장
td = datetime.timedelta(days=100) # 100일 저장
print('우리가 만난지 100일은',today+td) # 오늘부터 100일 후
