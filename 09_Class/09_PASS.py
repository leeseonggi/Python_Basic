class Unit:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self,location):
        print('[지상유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))
# 건물 
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        pass # 아무것도 안하고 일단은 넘어간다 -> beak처럼 종료시키거나 하지 않는다
             # 일단은 완성된거처럼 오류는 안내게 된다

# 서플라이 디폿 : 건물, 1개 건물 = 8개 유닛 인수
supply_depot = BuildingUnit('서플라이 디폿',500,'7시')

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')
def game_over():
    pass

game_start()
game_over()

