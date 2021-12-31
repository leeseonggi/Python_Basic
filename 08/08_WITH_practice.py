import pickle

with open('profile.pickle','rb') as profile_file: # proflie이란 pickle에 있는 내용을 profile_file이란 변수에 옮김
    print(pickle.load(profile_file))    # 출력하고 닫을필요가 없이 with문을 빠져나갈때 닫힘
    
with open('study.txt','w',encoding='utf8') as study_file:
    study_file.write('파이썬을 열심히 공부하고 있어요')
    
with  open('study.txt','r',encoding='utf8') as study_file:
    print(study_file.read())
# with 사용시 두문장 만으로 파일을 생성 할 수 있고
# 닫거나 하는거 없이 쉽게 쓰거나 읽을 수 있다
