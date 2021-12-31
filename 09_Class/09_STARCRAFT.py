from random import *

class Unit:
    def __init__(self, name, hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{0} 유닛이 생성되었습니다.'.format(name))
        
    def move(self,location):
        print('[지상유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1}입니다'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))        

        
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): # self는 자기 자신을 뜻하고 메소드에서는 항상 적어준다 생각하면 됨
        Unit.__init__(self,name,hp,speed) # 위의 클래스에서 이름과 체력을 상속받음
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))
        
    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))
        # location은 self가 없다 -> 그러므로 전달받은 매개변수 location을 쓰겠다는것
    
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
        
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '마린',40,1,5)
    # 스팀팩 : 일정 시간동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print('{0} : 스팀팩을 사용합니다. (HP 10감소)'.format(self.name))
        else:
            print('{0} : 체력이 부족하여 스팀팩을 사용하지 못합니다.'.format(self.name))
            
# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜 더 높은 파워로 공격 가능. 이동 불가
    seize_developed = False # 시즈모드 개발여부
    
    def __init__(self):
        AttackUnit.__init__(self,'탱크',150 ,1, 30)
        self.seize_mode = False
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        # 현재 시즈모드가 아닐 때 -> 시즈모드 하면 됨
        if self.seize_mode == False:
            print('{0} : 시즈모드로 전환 합니다.'.format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print('{0} : 시즈모드를 해제합니다'.format(self.name))
            self.damage /= 2
            self.seize_mode = False

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,'레이스',125,20,5)
        self.clocked = False # 클로킹 모드 (해제 상태)
    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해제
            print('{0} : 클로킹 모드 해제합니다.'.format(self.name))
            self.clocked = False
        else: # 클로킹 모드 해제 -> 모드 설정
            print('{0} : 클로킹 모드 설정합니다.'.format(self.name))
            self.clocked = True
            
def game_start():
    print('[알림] 새로운 게임을 시작합니다.')
def game_over():
    print('player : gg') # good game
    print('[player] 님이 게임에서 퇴장하셨습니다.')
    
# 게임 시작
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄 관리(생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move('1시')
    
# 탱크 시즈모드 개발
Tank.seize_developed = True
print('[알림] 탱크 시즈모드 개발이 완료되었습니다.')

# 공격모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit,Marine): # unit이 Marin클래스이 인스텐스이면 스팀팩(refine하는 작업)
        unit.stimpack()
    elif isinstance(unit,Tank): 
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack('1시')

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) # 공격은 랜덤으로 받음 (5 ~ 20)
    
# 게임 종료
game_over()
    
        