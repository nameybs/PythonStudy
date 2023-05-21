#########################################
# if (분기)
#########################################
'''
#weather = "비"
#weather = "미세먼지"
weather = ""
# 입력값 설정
#weather = input("오늘 날씨는 어때요? ")
if weather == "비" or "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else :
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? ")) # 숫자 자료형만 입력하고 싶을 경우(다른 자료형을 넣으면 에러 발생)
if 30 <= temp :
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30 :
    print("괜찮은 날씨에요")
elif 0 <= temp < 10 :
    print("외투를 챙기세요")
else :
    print("너무 추워요. 나가지 마세요")
'''
#########################################
# for (반복문)
#########################################
'''
#for waiting_nu in [0,1,2,3,4] :
#    print("대기번호 : {0}".format(waiting_nu))
#for waiting_nu in range(1,6) :
#    print("대기번호 : {0}".format(waiting_nu))
starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks :
    print("{}, 커피가 준비되었습니다.".format(customer))
'''
#########################################
# while (반복문)
#########################################
'''
customer = "토르"
index = 5
while index >= 1 :
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0 :
        print("커피는 폐기처분 되었습니다.")
#무한루프
#customer = "아이언맨"
#index = 1
#while True :
#    print("{0}, 커피가 준비되었습니다. 호출{1}회".format(customer, index))
#    index += 1
customer = "토르"
person = "Unknown"
while person != customer :
    print("{0}, 커피가 준비되었습니다. .".format(customer))
    person = input("이름이 어떻게 되세요? ")
'''
#########################################
# continue, break
#########################################
'''
absent = [2,5] #결석
nobook = [7] # 책안가져옴
for student in range(1,11) :
    if student in absent : # 리스트에 항목이 있으면 Continue
        continue
    elif student in nobook :
        print("오늘수업 여기까지. {0}는 교무실로 따라와.".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))
'''
#########################################
# 한줄 for
#########################################
'''
# 출석번호가 1 2 3 4, 앞에 100을 붙임 -> 101 102 103 104
students = [1,2,3,4,5]
print(students)
students = [i + 100 for i in students] # 100을 붙히고 길이만큼 반복함 [수식,값대입,조건 for 변수 in 배열]
print(students)
# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)
# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)
'''
#########################################
# 퀴즈
#########################################
# 당신은 cocoa서비스를 이용하는 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
# 조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
#(출력문 예제)
#[0] 1번째 손님 (소요시간 : 15분)
#[ ] 2번째 손님 (소요시간 : 50분)
#...
# 총 탑승 승객 : 2분
'''
from random import *
idx = 0
for customer in range(1,51): # 1 ~ 50 이라는 수
    time = randrange(5,51) # 5~50분 사이의 소요시간
    if 5 <= time <= 15 :
        print("[O]{0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        idx += 1
    else :
        print("[]{0}번째 손님 (소요시간 : {1}분)".format(customer, time))

print("총 탑승 승객 : {0}분".format(idx))
'''
#########################################
# 함수
#########################################
'''
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()
'''
#########################################
# 전달값과 반환값
#########################################
'''
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은{0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은{0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 1000)
print(balance) 

commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))
'''
#########################################
# 기본값
#########################################
'''
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2} "\
        .format(name,age,main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2} "\
         .format(name,age,main_lang))

profile("유재석")
profile("김태호")

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(name="김태호", age=25, main_lang="파이썬")
'''
#########################################
# 가변 인자
#########################################
'''
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ") # end=" " 끝날때 줄바꿈을 사용하지 않고 끝낸다는 의미
     print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#") # 추가될 경우 함수를 바꿔야 하게 됨
profile("김태호", 25, "Kotlin", "Swift", "", "", "") # 빈값을 일부러 넣어줘야하는 경우가 생김

def profile2(name, age, *language): # *language 라고 적으면 가변으로 인자값을 받는다.
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ") # end=" " 끝날때 줄바꿈을 사용하지 않고 끝낸다는 의미
    for lang in language:
        print(lang, end=" ")
    print()

profile2("유재석", 20, "Python", "Java", "C", "C++", "C#") # 추가될 경우 함수를 바꿔야 하게 됨
profile2("김태호", 25, "Kotlin", "Swift", "", "", "") # 빈값을 일부러 넣어줘야하는 경우가 생김
'''
#########################################
# 지역변수와 전역변수
#########################################
'''
gun = 10
def checkpoint(soldiers):
    global gun # 지역변수 내 전역변수 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[리턴 함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2) 
print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("전체 총 : {0}".format(gun))
'''
#########################################
# 퀴즈
#########################################
# 표준 체중을 구하는 프로그램을 작성하시오
# 표준 체중 : 각 개인의 키에 적당한 체중
# 성별에 따른 공식
# 남자 : 키 X 키 X 22
# 여자 : 키 X 키 X 21
# 조건1 : 표준 체중은 별도의 함수 내에서 계산 (함수명 : std_weight, 전달값 : 키, 성별)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
# (출력예제)
# 키 175CM 남자의 표준 체중은 67.38kg 입니다.

#man = 175
#woman = 165
# def std_weight(height, gender):
#     if gender == "남자":
#         print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, round((height/100) * (height/100) * 22, 2)))
#     else :
#         print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, round((height/100) * (height/100) * 21, 2)))
#std_weight(man, "남자")
#std_weight(woman, "여자")
'''
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else :
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height/100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
'''
#########################################
# 표준입출력
#########################################
'''
print("Python", "Java", "Javascript", sep=", ", end="?") # sep은 구분점 #end는 문장 끝부분을 설정하는 것(디폴트는 줄바꿈)
print("무엇이 더 재밌을까요?")
import sys
print("Python", "Java", file=sys.stdout) # stdout는 표준 출력
print("Python", "Java", file=sys.stderr) # stderr는 표준 에러
scores = {"수학":0,"영어":50, "코딩":100}
for subject, score in scores.items():
    # subject = key, score = value
    #print(subject, score)
    print(subject.ljust(4), str(score).rjust(4), sep=":") #ljust(8) 8개의 공간을 확보하고 왼쪽정렬 , rjust(4) 오른쪽 정렬 후 4칸 확보
#은행 대기순번표
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) #zfill(3) 3자리수로 체우고 빈공간은 0으로 체움 
#표준입력
answer = input("아무값이나 입력하세요 : ") # 사용자입력으로 값을 받으면 항상 문자로 받는다.
print(type(answer))
print("입력하신값은 " + answer + "입니다.") # str없이도 잘 출력된다.
'''
#########################################
# 다양한 출력 포멧
#########################################
# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
'''
print("{0: >10}".format(500)) # 부호가 없을때 양수일경우엔 500만 찍힘
# 양수일땐 +로 표시 음수일땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽정렬하고, 10자리 확보를 하고 빈칸을 밑줄로 채움
print("{0:_<10}".format(500))
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(10000000000000))
# 3자리마다 콤마찍기 , +-부호
print("{0:+,}".format(10000000000000))
print("{0:+,}".format(-10000000000000))
# 3자리마다 콤마찍기, 부호붙이기, 자릿수 확보
# 빈자리는 ^표시
print("{0:^<+30,}".format(10000000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수
print("{0:.2f}".format(5/3))
'''
#########################################
# 파일 입출력
#########################################
'''
# 파일 생성 및 쓰기
score_file = open("score.txt", "w", encoding="utf=8") # w은 쓰기전용, encoding처리를 안하면 문자가 깨질수도있음
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()
# 파일 덮어쓰기 및 이어쓰기
score_file = open("score.txt", "a", encoding="utf=8") # a는 덮어쓰기, 이어쓰기
score_file.write("과학 : 80") # write는 줄바꿈이 없으니 명시적으로 추가해야함
score_file.write("\n코딩 : 100")
score_file.close()
# 파일 읽기
score_file = open("score.txt", "r", encoding="utf=8") # r은 읽기
# 한번에 다 읽기
print(score_file.read())
score_file.close()
# 한줄씩 읽기
score_file = open("score.txt", "r", encoding="utf=8") # r은 읽기
print(score_file.readline(), end="") # 한줄을 읽고 커서를 다음줄로 이동함
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
# 몇줄일지 모를때 처리
score_file = open("score.txt", "r", encoding="utf=8") # r은 읽기
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()
# 리스트에 담아서 넣기
score_file = open("score.txt", "r", encoding="utf=8") # r은 읽기
lines = score_file.readlines() # list형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
'''
#########################################
# 피클
#########################################
# 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장해줌
'''
import pickle
# 파일 쓰기 
profile_file = open("profile.pickle", "wb") # wb = 쓰기 + 바이너리 (피클때는 필수)
profile = {"이름" : "박명수", "나이" : 30, "취미":{"축구","골프","코딩"}}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()
# 파일 읽기 
profile_file = open("profile.pickle", "rb") # 읽을때도 바이너리
profile = pickle.load(profile_file) # file에 있는 정보를 변수로 불러오기
print(profile)
profile_file.close()
'''
#########################################
# with
#########################################
'''
import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
# with를 쓰면 close처리를 안해도 된다.
# with 쓰기
with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
# with 읽기
with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())
'''
#########################################
# 퀴즈
#########################################
# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
# - X주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 : 
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.
'''
import pickle
for report in range(1,51) :
    with open("fileTest/" + str(report) + "주차.txt", "w", encoding="utf-8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(report))
        report_file.write("\n부서 : 영업부")
        report_file.write("\n이름 : 홍길동")
        report_file.write("\n업무 요약 : {0}주차 업무 보고입니다.".format(report))
'''