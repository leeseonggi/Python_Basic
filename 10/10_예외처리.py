try: # try 내부의 문장을 실하다가 오류가 났을때 except에 해당하는 에러면은 에러 구문을 출력함
    
    print('나누기 전용 계산기 입니다.')
    nums = []
    nums.append(int(input('첫 번째 숫자를 입력하세요 : ')))
    nums.append(int(input('두 번째 숫자를 입력하세요 : ')))
    # nums.append(int(nums[0]/nums[1]))
    print('{0} / {1} = {2}'.format(nums[0], nums[1], int(nums[2])))
    
except ValueError:
    print('에러! 잘못된 값을 입력하였습니다.')
except ZeroDivisionError as err: # division by zero란 에러 코드를 뜨게 만듬
    print(err)
except:
    print('알 수 없는 에러가 발생하였습니다.') 
'''
위의 두 에러가 아닌 나머지 에러에 대해서는 여기서 다 처리함
정확한 에러 명을 알고싶다?
except Exception as err:
print(err)
이 코드 실행
'''

    