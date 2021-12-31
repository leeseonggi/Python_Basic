chicken = 10
waiting = 1

class SoldOutError(Exception):
    pass

while(True):
    try:
        print('[남은 치킨 : {0}]'.format(chicken))
        order = int(input('치킨 몇 마리 주문하는교?'))
        if order > chicken: 
            print('재료 부족')
        elif order <= 0:
            raise ValueError
        else:
            print('[대기번호 {0}] {1} 마리 주문이 완료되었습니다'.format(waiting, order))
            waiting +=1
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError
        
    except ValueError:
        print('잘못된 값을 입력함')
    except SoldOutError as err:
        print('닭이 다 떠어지쓰')
        print(err)
        break