#########################################
# 클래스
#########################################
'''
name = "마린"
hp = 40
damage = 5
print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 : {0}, 공격력 : {1}".format(hp,damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35
print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 : {0}, 공격력 : {1}".format(tank_hp,tank_damage))

tank2_name = "탱크2"
tank2_hp = 150
tank2_damage = 35
print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 : {0}, 공격력 : {1}".format(tank2_hp,tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(\
        name,location,damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 이렇게 하면 많은 데이터를 처리하는데 힘들다.
# 클래스는 하나의 틀
# 클래스 화 시킨 부분
class Unit:
    # 기본 생성자
    def __init__(self, name, hp, damage) -> None:
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp,self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
'''
#########################################
# __init__
#########################################
# 생성자(자동호출부분)
'''
class Unit:
    # 기본 생성자(생성자 갯수가 틀리면 에러가 뜬다.)
    def __init__(self, name, hp, damage) -> None:
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp,self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
''' 
#########################################
# 멤버 변수
#########################################
'''
class Unit:
    # 기본 생성자(생성자 갯수가 틀리면 에러가 뜬다.)
    def __init__(self, name, hp, damage) -> None:
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp,self.damage))

wraith1 = Unit("레이스", 80, 5)
# 멤버 변수를 외부에서 쓸 수 있다.
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 외부에서 객체에 추가로 변수를 넣을 수 있다.
# 추가하지 않은 변수는 에러가 뜸

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
'''
#########################################
# 메소드
#########################################
'''
class AttackUnit:
    # 기본 생성자(생성자 갯수가 틀리면 에러가 뜬다.)
    def __init__(self, name, hp, damage) -> None:
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}".format(self.hp,self.damage))
    
    def attack(self, location):
        print("{0}유닛 : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage)) # self는 전역변수

    def damaged(self, damage):
        print("{0}유닛 : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}유닛 : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}유닛이 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어벳", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)
'''
#########################################
# 상속
#########################################
'''
# 일반유닛
class Unit:
    # 기본 생성자(생성자 갯수가 틀리면 에러가 뜬다.)
    def __init__(self, name, hp) -> None:
        self.name = name
        self.hp = hp

# 공격유닛
class AttackUnit(Unit): # Unit을 상속받음
    def __init__(self, name, hp, damage) -> None:
        # 상속받은 내용을 호출한다.
        Unit.__init__(self, name, hp)
        self.damage = damage
    
    def attack(self, location):
        print("{0}유닛 : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage)) # self는 전역변수

    def damaged(self, damage):
        print("{0}유닛 : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}유닛 : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}유닛이 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어벳", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)
'''
#########################################
# 다중 상속
#########################################
'''
# 일반유닛
class Unit:
    # 기본 생성자(생성자 갯수가 틀리면 에러가 뜬다.)
    def __init__(self, name, hp) -> None:
        self.name = name
        self.hp = hp

# 공격유닛
class AttackUnit(Unit): # Unit을 상속받음
    def __init__(self, name, hp, damage) -> None:
        # 상속받은 내용을 호출한다.
        Unit.__init__(self, name, hp)
        self.damage = damage
    
    def attack(self, location):
        print("{0}유닛 : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage)) # self는 전역변수

    def damaged(self, damage):
        print("{0}유닛 : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}유닛 : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}유닛이 파괴되었습니다.".format(self.name))

# 공중유닛
class Flyable:
    def __init__(self, flying_speed) -> None:
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도:{2}]".format(name, location, self.flying_speed))

# 두 클레스로부터 상속을 받음
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed) -> None:
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
    
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
valkyrie.attack("5시")
'''
#########################################
# 연산자 오버로딩
#########################################
'''
# 일반유닛
class Unit:
    # 기본 생성자(생성자 갯수가 틀리면 에러가 뜬다.)
    def __init__(self, name, hp, speed) -> None:
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

# 공격유닛
class AttackUnit(Unit): # Unit을 상속받음
    def __init__(self, name, hp, speed, damage) -> None:
        # 상속받은 내용을 호출한다.
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0}유닛 : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage)) # self는 전역변수

    def damaged(self, damage):
        print("{0}유닛 : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}유닛 : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}유닛이 파괴되었습니다.".format(self.name))

# 공중유닛
class Flyable:
    def __init__(self, flying_speed) -> None:
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도:{2}]".format(name, location, self.flying_speed))

# 두 클레스로부터 상속을 받음
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed) -> None:
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 Speed 0
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = AttackUnit("벌쳐", 80, 10 , 20)
battlecruiser = FlyableAttackUnit("배틀쿠르저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("3시")
# move 함수로 통일시키도록 한다.
'''
#########################################
# pass
#########################################
# pass는 일단 완성된 것처럼 쓸 수 있음.
'''
# 일반유닛
class Unit:
    # 기본 생성자(생성자 갯수가 틀리면 에러가 뜬다.)
    def __init__(self, name, hp, speed) -> None:
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

# 공격유닛
class AttackUnit(Unit): # Unit을 상속받음
    def __init__(self, name, hp, speed, damage) -> None:
        # 상속받은 내용을 호출한다.
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0}유닛 : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage)) # self는 전역변수

    def damaged(self, damage):
        print("{0}유닛 : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}유닛 : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}유닛이 파괴되었습니다.".format(self.name))

# 공중유닛
class Flyable:
    def __init__(self, flying_speed) -> None:
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도:{2}]".format(name, location, self.flying_speed))

# 두 클레스로부터 상속을 받음
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed) -> None:
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location) -> None:
        pass

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass
game_start()
game_over()
'''
#########################################
# super
#########################################
'''
class Unit:
    def __init__(self):
        print("Unit생성자")

class Flyable:
    def __init__(self):
        print("Flyable생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 2개 이상의 클래스를 다중상속받을때 super를 쓰면 맨앞에 있는 클래스만 초기화를 시켜준다.
# 그러므로 다중상속할때는 super()를 사용하면 안됨. 
dropship = FlyableUnit()
'''
#########################################
# 퀴즈
#########################################
# 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

#[코드]
'''
class House:
    # 매물 초기화 (위치, 집형태, 거래형태, 가격, 준공연도)
    def __init__(self, location, house_type, deal_type, price, completion_year) -> None:
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

house_list = []
house_list.append(house1)
house_list.append(house2)
house_list.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(house_list)))
for house in house_list:
    house.show_detail()
'''