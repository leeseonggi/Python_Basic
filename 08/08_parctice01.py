# 표준입출력
print('Python','Java','JavaScript',sep=', ',end='? ') 
# end 부분을 명시적으로 적어주면서 문장의 끝부분을 ?로 바꿔달다 -> 줄바꿈 대신
# 뒤의 문장을 한문장으로
print('무엇이 더 재밌을까요?')

import sys
print('Python','Java',file=sys.stdout) # 표준 출력으로 처리
print('Python','Java',file=sys.stderr) # 표준 에러로 처리(필요하면 따로 에러처리라는데 모르겠음)

# 시험 성적
scores = {'수학':0,'영어':50,'코딩':100}
for subject, score in scores.items(): # subject, score 두개의 변수에서 딕셔너리의 키와 벨류를 튜플로 받아오겠다
    # print(subject,score)
    # print(subject.ljust(8),score) # 왼쪽정렬을 하는데 8칸을 만들어서 한다
    # print(subject,str(score).rjust(4)) # 4칸 공간확보 오른쪽 정렬
    print(subject.ljust(8),str(score).rjust(4), sep=':') # 둘 다하고 sep 써서 사이에 : 넣어줌 
    
# 은행 대기순번표
# 001, 002, 003, ....
for num in range(1,21):
    # print('대기번호 : ' + str(num))
    print('대기번호 : ' + str(num).zfill(3)) 
    # 3크기 만큼의 공간을 확보하고 값을 넣을 수 있는 함수 
    # zfill(3)이면 3크기 앞에 빈공간은 0으로 채움
    
answer = input('아무값이나 입력 하세요 : ')
# 사용자 입력을 통해서 값을 받으면은 항상 문자열 형식으로 저장
print(type(answer))
print('입력하신 값은 '+answer+'입니다')
