class Unit:
    def __init__(self):
        print('Unit 생성자')
class Flyable:
    def __init__(self):
        print('Flyable 생성자')
        
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__() 
        # 다중상속시에 super함수를 사용한다면
        # 맨 첫번째 상속받는 클래스에 대해서만 호출이 된다
        # 다중상속시에 모든 부모클래스로부터 상속이 필요하다 하면은
        # Unit.__init__(self)
        # Flyable.__init__(self)
        # 형식으로 명시적으로 초기화를 해야 한다
        
# 드랍쉽 
dropship = FlyableUnit()
