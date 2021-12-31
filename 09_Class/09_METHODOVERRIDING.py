class Unit:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self,location):
        print('[지상유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))
        
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): # self는 자기 자신을 뜻하고 메소드에서는 항상 적어준다 생각하면 됨
        Unit.__init__(self,name,hp,speed) # 위의 클래스에서 이름과 체력을 상속받음
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))
        
    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))
        # location은 self가 없다 -> 그러므로 전달받은 매개변수 location을 쓰겠다는것
    
    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1}입니다'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))        

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다 [속도{2}]'.format(name, location, self.flying_speed))
            
class FlyableAttackUnit(AttackUnit, Flyable): # AttackUnit과 Flyable클래스 두개를 상속받아 공격능력이 있는 공중유닛 생성 가능
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name,hp,0,damage) # 날라다니는 유닛이라 지상 스피드 필요X 그래서 0값 넣어줌
        Flyable.__init__(self,flying_speed)
        
    def move(self,location):
        print('[공중 유닛이동]')
        self.fly(self.name, location) # self가 있으면 이름을 궂이 떤져 줄 필요사 없음
        
# 75 : 지상유닛, 기동성이 좋음
vulture = AttackUnit('75',80,10,20)

# 배틀크루저 : 공중유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit('배틀크루저',500,25,3)

vulture.move('11시')
battlecruiser.fly(battlecruiser.name,'9시')
battlecruiser.move('9시') # self가 있어서 이름을 궂이 떤져 줄 필요가 없음