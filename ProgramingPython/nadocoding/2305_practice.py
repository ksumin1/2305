# 숫자형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

# 문자형
# print('풍선')
# print("나비")
# print("ㅁㄴㅇㄹ")
# print("ㅋ"*9)

# boolean
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5>10))

# 변수
# 애완동물을 소개해 주세요
# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3
#
# print("우리집 " + animal + "의 이름은 " + name + "예요")
# hobby = "공놀이"
# print( name + "는"+ str(age) + "살이며," + hobby + "을 아주 좋아해요")
# print( name + "는 어른일까요? " + str(is_adult))
# +가 아닌 ,로 할수 있다 단 ,는 str()없이 그냥 출력할 수 있다
''' 여러문장 주석 이당!!! '''

# 연산자
# print(1 + 1)
# print(3 - 2)
# print(5 * 2)
# print(6 / 3)
#
# print(2 ** 3)
# 2의 3승 = 8
# print(5 % 3)
# 나누고 난 나머지
# print(10 % 3)
# print(5 // 3)
# 몫
# print(10 // 3)
#
# print(10 > 3)
# print(4 >= 7)
# print(10 < 3)
# print(5 <= 5)
#
# print(3 == 3)
# print(4 == 2)
# print(3 + 4 == 7)
#
# print(1 != 3)
# print(not (1 != 3))
#
# print((3 > 0) and (3 < 5))
# print((3 > 0) & (3 < 5))
# 앞뒤 모두 True 여야 True
# print((3 > 0) or (3 > 5))
# print((3 > 0) | (3 > 5))
# 앞뒤 하나만 True 여도 True
# print(5 > 4 > 3)
# print(5 > 4 > 7)

# 수식어
# print(2 + 3 * 4)
# print((2 + 3) * 4)
# number = 2 + 3 * 4
# print(number)
# number = number + 2 # number += 2
# print(number)
# number *= 2
# print(number)
# number /= 2
# print(number)
# number -= 2
# print(number)
# number %= 2
# print(number)

# 숫자처리 함수
# print(abs(-5)) # 5의 절댓값
# print(pow(4, 2)) # 4의 2승
# print(max(5, 12)) # 값중 큰값
# print(min(5, 12)) # 값중 작은 값
# print(round(3.14)) # 반올림
# print(round(4.99))
#
# from math import * # math 안에있는 함수를 이용
# print(floor(4.99)) # 내림
# print(ceil(3.14)) # 올림
# print(sqrt(16)) # 제곱근

# 랜덤 함수
# from random import *
# print(random()) # 0.0이상 1.0미만의 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0
# print(int(random() * 10)) # 0~10
# print(int(random() * 10) + 1) # 1~10이하의 임의의 값 생성
#
# print(randrange(1, 45)) # 1~45 미만의 임의의 값 생성
# print(randint(1, 45)) # 1~45 이하의 임의의 값 생성

# 문자열
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2= "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# 슬라이싱
# jumin = "990120-1234567"
#
# print("성별: " + jumin[7])
# print("연: " + jumin[0:2]) # 0번째부터 2번째 값 전까지
# print("월: " + jumin[2:4])
# print("일: " + jumin[4:6])
#
# print("생년월일: " + jumin[:6]) # 첨부터 6직전까지
# print("뒤 7자리: " + jumin[7:]) # 7번째부터 끝까지
# print("뒤 7자리 (뒤에서 부터): " + jumin[-7:])

# 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower()) # 전부 소문자
# print(python.upper()) # 전부 대문자
# print(python[0].isupper()) # 첫번째가 대문자인지
# print(len(python)) # 문자열 길이
# print(python.replace("Python", "Java")) # 문자열중 원하는곳 바꾸기
#
# index = python.index("n") # 문자열 중 어디에 n이 있는지
# print(index)
# index = python.index("n", index + 1) # 2번째 n찾기
# print(index)
#
# print(python.find("n"))
# print(python.find("Java")) # 원하는 값이 없으면 -1출력
# print(python.index("Java")) # 원하는 값이 없으면 오류, 뒤에있는 코드 출력x
#
# print(python.count("n"))

# 문자열 포맷
# print("a" + "b")
# print("a", "b")

# 방법 1
# print("나는 %d살입니다." % 20) # c와 비슷.
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요" % "A")
#
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간")) #순서가 달라져도 상관없다

# 방법 4(v3.6이상)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

# 탈출 문자
# print("백문이 불여일견\n백견이 불여일타")
# print('저는 "나도 코딩" 입니다.')
# print("저는 \"나도 코딩\" 입니다.")

# \\ : 문장 내에서 하나의\로
# \r : 커서를 맨 앞으로 이동
# print("Red Apple \rPine")
# \b : 백스페이스(한글자 삭제)
# print("Redd\bApple")
# \t :탭
# print("Red\tApple")

# 리스트[] : 순서를 가지는 객체의 집합
# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# print(subway.index("조세호"))
# 몇번째 칸에 있는지!
# subway.append("하하") # 맨뒤에추가
# print(subway)

# subway.insert(1, "정형돈") #사이에 넣기
# print(subway)

# print(subway.pop()) #맨뒤를 빼기
# print(subway)

# 같은 이름의 사람이 몇명 있는지
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)

# 순서 뒤집기
# num_list.reverse()
# print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
# num_list = [5, 2, 4, 3, 1]
# mix_list =["조세호", 20, True]
# print(mix_list)

# 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# 검사
# cabinet ={3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3)) # 만약 값이 없다면 none출력
# print(cabinet[5]) #오류로 프로그램 종료

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet ={"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# 간 손님
# del cabinet["A-3"]
# print(cabinet)

# 키 들만 출력
# print(cabinet.keys())

# 값만 출력
# print(cabinet.values())

# 함께 출력
# print(cabinet.items())

# 목욕탕 폐점
# cabinet.clear()

# 튜플 : 리스트와 다르게 수정,변경할수 없다
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스") # 오류

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age,hobby)

# 세트(집합) : 중복불가.순서없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# 교집합
# print(java & python)
# print(java.intersection(python))

# 합집합
# print(java | python)
# print(java.union(python))

# 차집합
# print(java - python)
# print(java.difference(python))

# python을 할수있는 사람이 늘어남
# python.add("김태호")
# print(python)

# java 를 잊었다!
# java.remove("김태호")
# print(java)

# 자료구조 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu)) #타입이 list형으로 바뀜

# menu = tuple(menu)
# print(menu, type(menu)) #타입이 tuple로 바뀜

# menu = set(menu)
# print(menu, type(menu)) # 타입 set로 원상복구

# 분기문
# weather = input("오늘 날씨는 어때요? ") # scanf같은 느낌
# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("너무 추워요. 나가지 마세요")

# 반복문(for)
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")

# for waiting_no in [0, 1, 2, 3, 4]:  # =range(5)
#     print("대기번호 : {0}".format(waiting_no))
#
# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# 반복문(while)
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다.".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"
#
# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# continue break
# absent = [2, 5] # 결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지.{0}는 교무실로 따라와",format(student))
#         break
#     print("{0}, 책을 읽어봐",format(student))

# 한줄 for
# studnets = [1,2,3,4,5]
# print(studnets)
# studnets = [i+100 for i in studnets]
# print(studnets)

# 1,2,3,4 -> 101,102,103,104
# studnets = ["Iron man", "Thor", "I am groot"]
# studnets = [len(i) for i in studnets]
# print(studnets)
# 문자열 길이 숫자로 출력

# studnets = ["Iron man", "Thor", "I am groot"]
# studnets = [i.upper() for i in studnets]
# print(studnets)
# 모든 문자 대문자로 변환

# 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.") # 호출하기 전까진 출력X
# open_account()

# 전달값, 변환값
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은{0} 원입니다.".format(balance + money))
#     return balance + money
#
# def whithdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은{0} 원입니다.".format(balance + money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다.잔액은{0} 원입니다.".format(balance))
#         return balance
#
# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission
#
# balance = 0
# balance = deposit(balance, 1000)
# print(balance)
#
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은{1}원 입니다.".format(commission, balance))

# 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#           .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#           .format(name, age, main_lang))
#
# profile("유재석")
# profile("김태호")

# 키워드 값
# def profile(name, age, main_lang):
#     print(name,age,main_lang)
#
# profile(name="유재석", main_lang="파이썬", age=20 )
# profile(main_lang="자바",age=25, name="김태호")

# 가변인자
# def profile(name, age,lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age,*language):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
#
# profile("유재석", 20, "python", "java", "C", "C++", "C#")
# profile("김태호", 25, "python", "java", "", "", "")

# 지역변수 전역변수
# gun = 10
#
# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers # 두번째 gun은 checkpoint안에있는 지역변수gun
#     print("[함수 내]남은 총 : {0}".format(gun))
#
#     def checkpoint_ret(gun, soldiers):
#         gun = gun - soldiers
#         print("[함수 내]남은 총 : {0}".format(gun))
#         return gun
#
#
# print("전체 총: {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총: {0}".format(gun))
# 클래스 + __init__
# name = "마린"
# hp = 40
# damage = 5
#
# print("{} 유닛이 생성되었습니다.".fomat(name))
# print("체력 {0},공격력 {1}\n".format(hp, damage))
#
# tank_name ="탱크"
# tank_hp = 150
# tank_damage = 35
# print("{} 유닛이 생성되었습니다.".fomat(tank_name))
# print("체력 {0},공격력 {1}\n".format(tank_hp, tank_damage))
#
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)
class Unit:
    def __init__(self, name, hp, damage,speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self,location):
        print("지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
#         self.damage = damage
#         print("{0}유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
#
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
#
# 멤버변수
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름:{0}, 공격력: {1}".format(wraith1.name,wraith1.damage)) # 멤버변수를 외부에서 사용가능
#
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True
#
# if wraith2.clocking == True:
#    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
# 객체의 변수를 외부에서 추가할수있음

# 메소드 + 상속
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage,speed):
#         Unit.__init__(self, name, hp,speed)
#        self.damage = damage

#    def attack(self, location):
#        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

#    def damaged(self, damage):
#        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#        self.hp ==damage
#        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#        if self.hp <= 0:
#            print("{0}: 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# 다중상속
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#     def fly(selfself, name, location):
#         print("{0} : {1}방향으로 날아갑니다. [속도 {2]".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage ,flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self,flying_speed)

#     def move(self,location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 연산자 오버라이딩
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# pass
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         Unit.__init__(self, name, hp ,0)
#         super().__init__(name, hp, 0)
#    self.location = location

# supply_depot = BuildingUnit("서플라이 디풋", 500, "7시")

# def game_start():
    # print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
    # pass
# game_start()
# game_over()

# super
# class Unit:
    # def __init__(self):
        # print("Unit생성자")

# class Flyable:
    # def __init__(self):
        # print("Flyable 생성자")

# class FlyableUnit(Flyable, Unit):
    # def __init__(self):
        # super().__init__()
        # Unit.__init__(self)
        # Flyable.__init__(self)

# dropship = FlyableUnit()

from random import *

class Unit:
    def __init__(self, name, hp, damage,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self,location):
        print("지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage,speed):
        Unit.__init__(self, name, hp,speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

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
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.set_seize_mode = False
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. [속도 {2} ]".format(name, location, self.flying_speed))

 class FlyableAttackUnit(AttackUnit, Flyable):
     def __init__(self, name, hp, damage ,flying_speed):
         AttackUnit.__init__(self, name, hp, 0, damage)
         Flyable.__init__(self,flying_speed)

     def move(self,location):
         print("[공중 유닛 이동]")
         self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 2, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,20))

game_over()

# theater_module.py
# 일반가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))
# 조조할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))
# 군인할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))

# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *   theater_module안에 있는 모든것을 사용
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_moring 원하는 함수만 가져다 사용가능
# from theater_module import price_soldier as price
# price(5) 군사할인 가격으로 나옴


# 패키지
# __init__.py
__all__ = ["Vietnam"]
# thailand.py
class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행.....")

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 ㅁ듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
# vietnam.py
class VietnamPackage:
    def detail(self):
        print("[베트남 패키지 3박 5일] 다냥 효도 여행 60만원")

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()
#
# from travel import vietnam
# trip_to = vietnam.VietnamPackage()

# all_
# from travel import *  # 공개범위를 설정해줘야 한다.
# trip_to= vietnam.VietnamPackage()
# trip_to.detail() # 오류!

# 패키치, 모듈 위치
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))