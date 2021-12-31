#__init__ 함수
# self가 붙은 변수만큼 무조건 다 선언해 주어야만 함

# 일반유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
       
    
# 메소드
# 공격유닛
class AttackUnit:
    def __init__(self, name, hp, damage): # self는 자기 자신을 뜻하고 메소드에서는 항상 적어준다 생각하면 됨
        self.name = name
        self.hp = hp
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

marine1 = AttackUnit('마린', 40, 5)
marine2 = AttackUnit('마린', 40, 5)
# marine3 = Unit('마린')
# marine4 = Unit('마린',40) # 클래스 안에 설계된 내용이 전부 다 들어가야함 아니면 불가능
tank = Unit('탱크',150,30)

# 멤버변수
# 레이스 : 공중유닛, 비행기. 클로킹 (상대에게 보이지 않음)
wraith1 = AttackUnit('레이스',125,8)
print('유닛 이름: {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는것
wraith2 = AttackUnit('레이스',125,8)
wraith2.clocking = True # 파이썬에서는 추가 변수를 만들어서 사용 가능
                        # wraith1에는 클로킹이 없음 wraith2에만 클로킹이 적용 된거

if wraith2.clocking == True:
    print('{0}는 현재 클로킹 상태 입니다.'.format(wraith2.name))
    
# 파이어뱃 : 공격유닛, 화염방사기
firebat1 = AttackUnit('파이어뱃',75,16)
firebat1.attack('5시')
# 공격 2번 받는다고 가정
firebat1.damaged(40)
firebat1.damaged(40)

# 메딕: 의무병

# 상속

        