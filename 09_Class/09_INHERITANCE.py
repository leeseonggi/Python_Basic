# 일반유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
       

# 공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage): # self는 자기 자신을 뜻하고 메소드에서는 항상 적어준다 생각하면 됨
        Unit.__init__(self,name,hp) # 위의 클래스에서 이름과 체력을 상속받음
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
        
# 다중상속

# 드랍쉽 : 공중유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격X
# 공중 유닛 클래스 
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다 [속도{2}]'.format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # AttackUnit과 Flyable클래스 두개를 상속받아 공격능력이 있는 공중유닛 생성 가능
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name,hp,damage)
        Flyable.__init__(self,flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit('발키리',200,6,5)
valkyrie.fly(valkyrie.name, '3시') # 속도만 있어서 별도로 이름 추가


        
        
    