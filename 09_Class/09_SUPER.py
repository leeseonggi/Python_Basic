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
        # Unit.__init__(self, name,hp, 0) # 건물을 이동 못하니까 0 넣어줌 (일단 띄우는거 제외)
        super().__init__(name,hp,0) 
        # Unit.__init__과 같은 역할 다만 super(). 형태
        # self를 받지 않음
        self.location = location
