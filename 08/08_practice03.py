score_file = open('score.txt','w',encoding='utf8') # w로 열면은 쓰기용도로 덮어쓰기가 됨
print('수학 : 0',file=score_file)
print('영어 : 100',file=score_file)
score_file.close()

score_file = open('score.txt','a', encoding='utf8') # 내용이 존재하는 파일에 이어서 쓰겠다 -> a 
score_file.write('과학 : 80')
score_file.write('\n코딩 : 100') # print가 아니라 스코어파일에 직접 쓰면은 자동 줄바꿈이 안됨
score_file.close()

score_file = open('score.txt','r', encoding='utf8')# 한번에 모든 내용을 불러올 수 있음
print(score_file.read())
score_file.close()

score_file = open('score.txt','r', encoding='utf8')
print(score_file.readline()) # 줄별로 읽기동작, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline()) 
print(score_file.readline()) 
print(score_file.readline()) 
score_file.close()

score_file = open('score.txt','r', encoding='utf8')
print(score_file.readline(),end='') # 줄바꿈 없이 붙여서 뽑겠다
print(score_file.readline(),end='') 
print(score_file.readline(),end='') 
print(score_file.readline(),end='') 
score_file.close()

score_file = open('score.txt','r', encoding='utf8') # 파일이 몇줄인지는 모를때 반복문으로 불러 올 수 있음
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open('score.txt','r', encoding='utf8')
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end='')
    
score_file.close()