chicken = 10
waiting = 1 #홀 안에는 만석. 대기번호 1부터 시작


class SoldOutError(Exception):
    pass

try:
    while(True):
        print('[남은 치킨 : {0}]'.format(chicken))
        order = int(input('치킨을 몇마리 주문 하시겠습니까?'))

        if order<1: # 시작부터 걸러 버리면은 그대로 반복문을 빠져 나감 그래서 밑에서 elif로 해주는게 나음
            raise ValueError
        else:
            if order > chicken: # 남은 재료보다 주문량이 많을때
                print('닭이 부족합니다.')
            else:
                print('[대기번호 {0}] {1} 마리 주문이 완료되었습니다'.format(waiting, order))
                waiting += 1
                chicken -= order
                if chicken ==0:
                    raise SoldOutError
                    break
                        
except ValueError:
    print('잘못된 값을 입력하셨습니다')
except SoldOutError as err:
    print('닭이 다 떨어지쓰')
    print(err)