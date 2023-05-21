#########################################
# 예외처리
#########################################
'''
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError: # ValueError가 발생하였을때 해당 구문을 탄다.
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 에러 메세지를 안에 넣고싶은 경우
    print(err)
except Exception as err:# 명시되지 않은 에러는 아래 구문을 무조건 탄다(메세지를 받고싶을 경우 Exception as err 추가)
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
'''
#########################################
# 예외발생시키기
#########################################
# 의도적으로 발생시키기
'''
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError # 에러를 강제로 발생시키는 구문 (해당 에러로 바로 빠진다.)
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
'''
#########################################
# 사용자 정의 에러 처리
#########################################
'''
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0} , {1}".format(num1, num2)) # 에러를 강제로 발생시키는 구문 (해당 에러로 바로 빠진다.)
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
'''
#########################################
# finally
#########################################
# 예외처리시 무조건적으로 사용되어지는 부분
'''
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0} , {1}".format(num1, num2)) # 에러를 강제로 발생시키는 구문 (해당 에러로 바로 빠진다.)
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
'''
#########################################
# 퀴즈
#########################################
# 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
# 출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
# 치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
# 출력 메세지 :"재고가 소진되어 더이상 주문을 받지 않습니다."

# [코드]
'''
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작.

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        if chicken == 0:
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        order = int(input("치킨 몇마리 주문하시겠습니까? : "))
        if order <= 0:
            raise ValueError
        if order > chicken: 
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError as err:
        print(err)
        break
'''
#########################################
# 모듈
#########################################
'''
# 기본 사용 방법
import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을때 가격
theater_module.price_morning(4)
theater_module.price_soldier(2)
# 별명을 지정 가능
import theater_module as tm 
tm.price(3) # 3명이서 영화 보러 갔을때 가격
tm.price_morning(4)
tm.price_soldier(2)
# 바로 상수로 호출해서 쓰는 방법
from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

# 필요한 함수만 쓸 경우
from theater_module import price, price_morning
price(3)
price_morning(4)
#price_soldier(5)
# 필요한 함수를 줄여쓰는 방법(별명 붙히기)
from theater_module import price_soldier as price
price(5)
'''
#########################################
# 패키지
#########################################
# 모듈을 모아놓은 집합
# 패키지 사용
'''
import travel.thailand # 맨 뒤엔 모듈이나 패키지만 가능 (클래스는 불가능)
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
# 대신 from으로 부를땐 클래스로 바로 사용 가능하다
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()
from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()
'''
#########################################
# __all__
#########################################
# *로 선언했을 경우 공개 범위를 설정해주지 않으면 에러가 발생
'''
from travel import * # 위와같이 정의하기만 하면 에러가 뜸(공개 범위를 설정 해 주어야 함)
trip_to = vietnam.VietnamPackage() 
trip_to.detail()
trip_to = thailand.ThailandPackage() 
trip_to.detail()
'''
#########################################
# 모듈 직접 실행
#########################################
# 모듈에서 직접 실행한건지 / 외부에서 실행한건지 구분해주는 기능
'''
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()
'''
#########################################
# 패키지, 모듈 위치
#########################################
# 패키지 경로를 확인 할 수 있다.
'''
from travel import *
import inspect # 패키지 모듈 경로를 확인하게 해주는 모듈
import random
trip_to = thailand.ThailandPackage()
trip_to.detail()
print(inspect.getfile(random))
print(inspect.getfile(thailand))
'''
#########################################
# pip install
#########################################
# https://pypi.org/project/beautifulsoup4/에 접속
# 터미널창에 다운로드 링크 복사 
# pip install beautifulsoup4
# 실제 사용 예제
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
'''
# pip 설치 현황 확인
# 터미널 창에 pip list
# pip 정보 확인
# pip show beautifulsoup4 
# pip 업그레이드
# pip install --upgrade beautifulsoup4
# pip 삭제
# pip uninstall beautifulsoup4
#########################################
# 내장함수
#########################################
# 파이썬에 기본적으로 내장되어있는 함수
# input : 사용자 입력을 받는 함수
#language = input("무슨 언어를 좋아하세요? :")
#print("{0}은 아주 좋은 언어입니다!".format(language))
# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
'''
print(dir())
import random # 외장 함수
print(dir())
print(dir(random)) # 랜덤 안에 있는 함수들
lst = [1,2,3]
print(dir(lst)) # lst로 쓸 수 있는 함수들이 표시가 됨
name = "Jim"
print(dir(name))
'''
# 내장함수 확인 주소
# https://docs.python.org/ko/3/library/functions.html
#########################################
# 외장함수
#########################################
# 직접적으로 import를 사용해서 써야하는 함수
# 외장함수 확인 주소
# https://docs.python.org/ko/3/py-modindex.html
# 예제
# glob : 경로 내의 폴더 / 파일 목록 조회( 윈도우 cmd = dir)
'''
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일 확인
# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리
folder = "sample_dir"
if os.path.exists(folder): # 폴더 존재 유무 확인
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")
print(os.listdir()) # 해당 폴더의 모든 폴더/파일 표시

# time : 시간 관련 함수
import time
print(time.localtime()) # 시간정보 출력
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 시간 정보 포멧 변경

# datetime : 날짜시간 관련 간편 함수
import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격 , 경과 날짜
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은" , today + td) # 오늘부터 100일 후
'''
#########################################
# 퀴즈
#########################################
# 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
# 조건 : 모듈 파일명은 byme.py 로 작성
# (모듈 사용 예제)
# import byme
# byme.sign()
# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어졌습니다.
# 유튜브 : http://youtube.com
# 이메일 : nadocoding@gmail.com
'''
import byme
byme.sign()
'''
#########################################
# enumerate
#########################################
# 인덱스와 벨류값까지도 가져올 수 있다.
'''
lst = ["가", "나", "다"]
for lst_idx, list_val in enumerate(lst):
    print(lst_idx, list_val)
'''
#########################################
# 2중 for문 탈출하기
#########################################
balls = [1,2,3,4]
weapons = [11,22,3,44]

for ball_idx, ball_val in enumerate(balls):
    print("ball : ", ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapon : ", weapon_val)
        if ball_val == weapon_val:
            print("공과 무기가 충돌")
            break # 안쪽 for문 종료(이 조건을 안타면 else문을 계속 탄다 break를 타면 바깥쪽 break를 탄다.)
    else: # 안쪽 for문을 if문처럼 쓸 수 있다
        continue
    print("바깥 for문 break")
    break