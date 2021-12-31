# 4 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 4-2 슬라이싱

jumin = "991234-1234567"

print("성별 : " +jumin[7])
print("연 : "+jumin[0:2]) #직전값 까지이기 떄문에 0~2직전까지
print('월 : ' + jumin[2:4])
print('일 : ' +jumin[4:6])

print('생년월일 : ' + jumin[:6]) # 처음부터 6직전까지 
print('뒤 7자리 : ' + jumin[7:]) # 끝까지면 생략 가능
print('뒤 7자리 (뒤에부터) : ' + jumin[-7:])
# 맨 뒤에서 7번쨰 부터 끝까지

# 4-3 문자열 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # []번째 문자가 대문자인지 묻는거
print(len(python))
print(python.replace("Python","C"))

index = python.index("n") # 몇번째에 n이 나오는지 찾는거
print(index)
index = python.index("n", index + 1) # 찾은 n 다음에 어디서 n이 나오는가 찾는거
print(index)

print(python.find("n"))
print(python.find("C")) # 원하는 값이 없는 경우에는 -1을 반환
# print(python.index("C")) # 원하는 겂이 없는 경우에는 오류를 내고 프로그램 종료

print(python.count("n")) # 몇번 나오냐

# 4-4 문자열 포멧
# print('a'+'b')
# print('a','b')

# 방법 1
print('나는 %d살입니다' % 20)
print('나는 %s을 좋아해요'%'파이썬')
print("Apple은 %c로 시작해요." % 'A')
print("나는 %s색과 %s색을 좋아해요." % ('파란','빨간'))

# 방법 2
print('나는 {}살 입니다.'.format(30))
print('나는 {}색과 {}색을 좋아해요.'.format('노랑','초록'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('보라','검정'))

# 방법 3
print('나는 {age}살이며, {color}색을 좋아해요.'.format(age=30, color='파랑'))
print('나는 {age}살이며, {color}색을 좋아해요.'.format(color='노랑',age=29))

# 방법 4(v3.6 이상)
age = 30
color = "파랑"
print(f'나는 {age}살이며, {color}색을 좋아해요')

# 4-5 탈출문자
print('백문이 불여일견\n백견이 불여일타') # 줄바꿈
print("저는 '이성기'입니다.")
print('저는 "이성기"입니다.')
print("저는 \"이성기\"입니다.")
print('저는 \'이성기\'입니다.')

# 4-6 퀴즈
site = 'http://naver.com'
print(site.index('/')+1)
print(site.index('.')-1)
start = site.index('/')+1
end = site.index('.')-1
word_len = end-start
first_3 = site[start+1:start+4]
e_count = site.count('e')
print('생성된 비밀번호 : %s%s%s%c'%(first_3,word_len,e_count,'!'))
print('생성된 비밀번호 : {}{}{}{}'.format(first_3,word_len,e_count,'!'))

# 해설
# url = 'http://naver.com'
url = 'http://google.com'
my_str = url.replace('http://','') # 규칙 1
my_str = my_str[:my_str.index('.')] 
# 규칙 2 my_str[0:5] 이미 http:// 부분은 빈칸으로 변환 
# '.'이후 쓸데없는거 다 날리고 다시 저장 my_str에는 naver만 남김
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e'))+'!'
print('{0}의 비밀번호는 {1} 입니다.'.format(url, password))
