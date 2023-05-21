from random import *

# 일반유닛
class Unit:
    def __init__(self, name, hp, speed) -> None:
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0}유닛 : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}유닛 : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}유닛이 파괴되었습니다.".format(self.name))

# 공격유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage) -> None:
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0}유닛 : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage))

# 공중유닛
class Flyable:
    def __init__(self, flying_speed) -> None:
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도:{2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed) -> None:
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

class Tank(AttackUnit):
    sieze_developed = False # 시즈모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
    
    def set_seize_mode(self):
        if Tank.sieze_developed == False:
            return
        
        # 시즈모드아닐때(시즈모드)
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 시즈모드일때(해제)
        else:
            print("{0} : 시즈모드를 해제합니다".format(self.name))
            self.damage /= 2
            self.seize_mode = False

class Wraith(FlyableAttackUnit):
        def __init__(self):
            FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
            self.clocked = False
        
        def clocking(self):
            # 클로킹모드 해제
            if self.clocked == True:
                print("{0} : 클로킹 모드를 해제합니다".format(self.name))
                self.clocked = False
            # 클로킹모드
            else:
                print("{0} : 클로킹 모드로 전환합니다".format(self.name))
                self.clocked = True

def game_start():
    print("[알림]새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 시작
game_start()

# 유닛 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.sieze_developed = True
print("[알림]탱크 시즈모드 개발이 완료되었습니다.")

# 공격 모드 준비(탱크 : 시즈모드, 레이스 : 클로킹, 마린 : 스팀팩)
for unit in attack_units:
    if isinstance(unit, Marine): # isinstance 클래스 안에 어떤 인스턴스인지 확인하는 처리
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21)) # 5 ~ 20까지의 랜덤으로 데미지를 받음
    
# 게임 종료
game_over()