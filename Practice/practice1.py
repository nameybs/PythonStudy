#########################################
# 자료형(숫자)
#########################################
'''
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
'''
#########################################
# 자료형(문자)
#########################################
'''
print('풍선')
print("나비")
print('ㅋ'*9)
print("ㅋ"*9)
'''
#########################################
# 자료형 Boolean
#########################################
'''
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))
'''
#########################################
# 변수
#########################################
'''
애완동물 소개
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "이에요")
hobby = "공놀이"
print(name + "는" + str(age) +"살이며, " + hobby +"을(를) 아주 좋아해요")
#print(name , "는" , age ,"살이며," , hobby ,"을 아주 좋아해요")
print(name +"는 어른일까요? " + str(is_adult))
'''
#########################################
# 퀴즈
#########################################
'''
#퀴즈) 변수를 이용하여 다음 문장을 출력하시오
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")
'''
#########################################
# 연산자
#########################################
'''
# 산술 연산
print(1+1)
print(3-2)
print(5*2)
print(6/3)
print(2**3) # 2 ^ 3 = 8 3재곱
print(5%3) # 나머지 구하기 2
print(5//3) # 몫 구하기 1
print(10%3) # 나머지 구하기 1
print(10//3) # 몫 구하기 3

# 비교 연산
print(10>3) # True
print(4 >= 7) # False
print(3 == 3) # True
print(3+4 == 7) # True
print(3 != 3) # False
print(not (3 != 3)) # True

# AND
print((3 > 0) and ( 3 < 5)) # True
print((3 > 0) & ( 3 < 5)) # True

# OR
print((3 > 0) or ( 3 < 5)) # True
print((3 > 0) | ( 3 < 5)) # True

# 3개값 비교
print(5 > 4 > 3)
print(5 > 4 > 7)
'''
#########################################
# 간단한 수식
#########################################
'''
print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 5
print(number)
'''
#########################################
# 숫자처리 함수
#########################################
'''
print(abs(-5)) #절대값 반환 5
print(pow(4,2)) # 제곱 16
print(max(5,12)) # 최대값 반환
print(min(5,12)) # 최소값 반환
print(round(3.14)) # 반올림/반내림
print(round(3.51)) # 반올림/반내림

from math import * # math함수 라이브러리
print(floor(4.99)) # 반내림
print(ceil(3.14)) # 반올림
print(sqrt(16)) # 제곱근
'''
#########################################
# 랜덤 함수
#########################################
'''
from random import * # 랜덤함수 라이브러리
print(random()) # 0.0 ~ 1.0 사이의 임의의 소수 생성
print(random() * 10) # 0.0 ~ 10.0 사이의 임의의 소수 생성
print(int(random() * 10)) # 정수값만 뽑고 싶은 경우
print(int(random() * 10) + 1) # 1부터 뽑고 싶은 경우

# 로또값
print(int(random() * 45) + 1)
print(randrange(1,46)) # 1 ~ 46 미만의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 값 생성
'''
#########################################
# 퀴즈
#########################################
# 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오
# 조건1 랜덤으로 날짜를 뽑아야 함
# 조건2 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 매월 1~3일은 스터디 준비를 해야 하므로 제외
# 예제) 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.
'''
from random import * # 랜덤함수 라이브러리
day = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" + str(day) + "일로 선정되었습니다.")
'''
#########################################
# 문자열
#########################################
'''
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)
'''
#########################################
# 슬라이싱 (substring)
#########################################
'''
jumin = "990120-1234567"
print("성별 : " + jumin[7]) # 7번쩨 인덱스만
print("연 : " + jumin[0:2]) # 0~2 인덱스 다 가져오기
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리(뒤에부터) : " + jumin[-7:]) # 맨 뒤부터 -7자리 전부터 끝까지
'''
#########################################
# 문자열 처리함수
#########################################
'''
python = "Python is Amazing"
print(python.lower()) # 소문자 출력
print(python.upper()) # 대문자 출력
print(python[0].isupper()) # n번째 인덱스 문자열이 대문자인지 체크 True
print(len(python)) # 문자열 길이 출력
print(python.replace("Python", "Java")) # 문자열 치환

index = python.index("n") # 문자열 인덱스 취득
print(index)
index = python.index("n" , index + 1) # 두번째 n을 찾게 됨
print(index)

print(python.find("n")) # index랑 비슷
index = python.find("n" , index + 1) # find는 두번째 인덱스 찾을시 -1 리턴
print(index)
print(python.find("Java")) # 문자열이 없을경우 -1 리턴
#print(python.index("Java")) # index로 할 시에 에러를 리턴해버린다.
print(python.count("n")) # 해당 문자열이 몇번 나오는지 확인
'''
#########################################
# 문자열 포맷
#########################################
'''
# +, ,이외의 출력 방법
# 방법 1 
print("나는 %d살입니다." % 20) # %d 는 정수만 가능
print("나는 %s을 좋아해요." % "파이썬") # %s 는 문자열
print("Apple은 %c로 시작해요." % 'A') # %c 는 캐릭터형
# %s로 쓰면 왠만한건 다 가능하다
print("나는 %s살입니다." % 20) # %d 는 정수만 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 2개 이상 문자열을 나열하고 싶을 때
# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) # 괄호에 숫자를 넣지 않으면 순서대로 출력
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # 순서를 바꿀 수 있음
# 방법 3
print("나는 {age}살이며 {color}색을 좋아해요.".format(age = 20,color = "빨간")) # 변수명을 추가하는거이므로 순서에 상관이 없어진다.
# 방법 4 (v3.6이상 부터 가능)
age = 20
color = "빨간"
print(f"나는 {age}살이며 {color}색을 좋아해요.") # 앞에 f를 붙히면 위에 선언한 변수를 그대로 사용 할 수 있게 된다.
'''
#########################################
# 탈출(이스케이프) 문자
#########################################
'''
print("백문이 불여일견\n백견이 불여일타") # \n 을 쓰면 개행 처리를 해줌
# 저는 "코딩"입니다.
print("저는 '코딩' 입니다.") #작은 따옴표도 1차 방법
print('저는 "코딩" 입니다.') # 작은따옴표로 최상단을 감쌀 수 있음
print("저는 \"코딩\" 입니다.") # 탈출문자 처리
# \\ 는 문장 내에서는 \로 인식
print("F:\\python\\workspace")
# \r 커서를 맨앞으로 이동(커서 맨 앞으로 이동해서 뒤에 문자열만큼 새로 씀)
print("Red Apple\rPine") # PineApple
# \b 한글자 삭제
print("Redd\bApple") # RedApple
# \t 탭처리
print("Red\tApple") #Red    Apple
'''
#########################################
# 퀴즈
#########################################
# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 갯수 + "!" 로 구성
# 예) 생성된 비밀번호 : nav51!
'''
url = "http://naver.com"
#url = "http://daum.com"
temp = url.replace("http://", "") # 규칙1
temp = temp[:temp.index(".")] # 규칙2
password = temp[:3] + str(len(temp)) + str(temp.count("e")) + "!" #규칙3
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
'''
#########################################
# 리스트(배열)
#########################################
'''
subway = [10,20,30]
print(subway)
# 20은 몇번째 배열에 있는가
print(subway.index(20)) # 1번째 인덱스에 위치
subway.append(40) # 배열 맨뒤에 값을 새로 추가
print(subway)
subway.insert(1, 15) # 배열 1번째 인덱스에 추가
print(subway)
# 배열 내용 빼기
subway.pop() # 맨뒤에 한명을 뺌
print(subway)
# 배열 값이 몇개 있는지 확인
subway.append(10)
print(subway.count(10))
#정렬하기
num = [5,2,4,3,1]
num.sort() # 오름차순 정렬
print(num) 
num.reverse() # 내림차순 정렬
print(num)
#값을 모두 지우기
num.clear() 
print(num)
# 다양한 자료형을 함께 사용
num = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)
# 두개의 배열 합치기
num.extend(mix_list)
print(num)
'''
#########################################
# 사전(Dictionary)
#########################################
# 자바의 Map같은 것
# key value 로 이루어져 있다.
# key는 중복이 허용되지 않는다.
'''
# 초기화
cabinet = {3:"유재석", 100:"김태호"} # 2개의 key,value가 있음
print(cabinet[3]) # 값 취득 방법 1 
print(cabinet.get(100)) # 값 취득 방법 2
#print(cabinet[5]) # 값 취득방법1의 에러 -> 에러처리 되어서 프로그램이 종료
#print(cabinet.get(5)) # 값 취득 방법2의 에러 -> None라는 값으로 출력
print(cabinet.get(5, "사용 가능")) # 키값이 없을 경우에 우측의 문장을 출력 시켜준다. 
print("hi!")
# 사전 자료안에 값 확인
print(3 in cabinet) # 3이라는 key가 있으면 True리턴
print(5 in cabinet) # 5이라는 key가 없으면 False리턴
# 문자열 key
cabinet = {"A-3":"유재석", "B-100":"김태호"} # 2개의 key,value가 있음
print(cabinet["A-3"])
print(cabinet["B-100"])
# 사전에 값 추가
cabinet["C-20"] = "조세호" # key가 없으면 key와 value을 추가한다
print(cabinet)
cabinet["C-20"] = "조세호2" # key가 있으면 value를 변경함
print(cabinet)
# 사전에 값을 빼기
del cabinet["C-20"] # 해당 key를 삭제
print(cabinet)
# key만 출력하기
print(cabinet.keys())
# value만 출력하기
print(cabinet.values())
# 양쪽 다 출력
print(cabinet.items())
# 모든 data클리어
cabinet.clear()
print(cabinet)
'''
#########################################
# 튜플
#########################################
# 리스트와는 다르게 내용 변경 추가가 안됨
# 속도는 더 빠름
'''
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
name = "김종국"
age = 20
hobby = "코딩"
print(name,age,hobby)
(name,age,hobby) = ("유재석", 30 , "자바")
print(name,age,hobby)
'''
#########################################
# 세트 (집합)
#########################################
# 중복 안됨, 순서 없음
'''
my_set = {1,2,3,3,3}
print(my_set) # 중복 값은 출력 안됨 1,2,3만 출력됨
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
php = {"유재석", "김종국", "박명수"}
# 교집합 (Java와 Python을 모두 할 수 있는 사람)
print(java & python) # 방법 1
print(java.intersection(python)) # 방법 2
#합집합(둘중 하나만 가능한 개발자)
print(java | python)
print(java.union(python))
#차집합(Java가능 , Python불가능)
print(java - python)
print(java.difference(python))
# 집합에 값 추가하기
python.add("김태호")
print(python)
# 집합에 값 제외하기
java.remove("김태호")
print(java)
'''
#########################################
# 자료구조의 변경
#########################################
'''
menu = {"커피", "우유", "주스"} # 타입을 set으로 선언
print(menu, type(menu)) # 괄호는 {}
menu = list(menu) # type을 list로 변경
print(menu, type(menu)) # 괄호는 []
menu = tuple(menu) # type을 tuple로 변경
print(menu, type(menu)) # 괄호는 ()
menu = set(menu)
print(menu, type(menu))
'''
#########################################
# 퀴즈
#########################################
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 suffle과 sample을 활용
# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --
# (활용 예제)
'''
from random import *
#lst = [1,2,3,4,5]
#print(lst)
#shuffle(lst)
#print(lst)
#print(sample(lst,1))
#users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
users = range(1,21) # 1부터 20까지의 숫자를 생성
print(type(users)) # 위처럼 선언하면 type이 range로 생성
users = list(users) # list타입으로 변환
print(users)
shuffle(users)
print(users)
winners = sample(users, 4) # 4명중 1명은 치킨 3명은 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("-- 축하합니다. --")
'''