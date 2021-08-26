# quiz 1-1
# id_number = "020316"
# year = id_number[:2]
# day = id_number[2:]
# sum = str(int(year) * int(day))
# print(year + "\n" + day + "\n" + sum)

# quiz 1-2
# phone_number = "02-1234-5678"
# index = phone_number.index("-")
# first = phone_number[0:index]
# last = phone_number[8:]
# print(first + "\n" + last)

# result = phone_number.replace('-','').replcace(' ','')


# quiz 2-1
# student_number = "2100"
# if student_number[1] == "1" or student_number[1] == "2":
#     department = "뉴미디어소프트웨어과"
#     print(student_number[1] + "반" + department)
# elif student_number[1] == "3" or student_number[1] == "4":
#     department = "뉴미디어웹솔루션과"
#     print(student_number[1] + "반" + department)
# elif student_number[1] == "5" or student_number[1] == "6":
#     department = "뉴미디어디자인과"
#     print(student_number[1] + "반" + department)
# else:
#     print("잘못 입력했습니다.")
#
#
# # quiz 2-2
# def get_major(student_number):
#     global major
#     grade = student_number[0]
#
#     if student_number[1] == "1" or student_number[1] == "2":
#         major = "뉴미디어소프트웨어과"
#     elif student_number[1] == "3" or student_number[1] == "4":
#         major = "뉴미디어웹솔루션과"
#     elif student_number[1] == "5" or student_number[1] == "6":
#         major = "뉴미디어디자인과"
#
#     return major, grade
#
# grade, major = get_major("2100")
# print(major, grade)
#
# # quiz 2-3
# # def average(*number):
# #     sum = 0
# #     for i in number:
# #         sum += number
# #     avg = round(sum / i, 3)
# #
# #     return avg
# #
# # print(average(10, 20, 30))
# # print(average(4, 23))
#
# def average(*numbers):
# 	sum_value = 0
# 	count = 0
# 	for number in numbers:
# 		sum_value += number
# 		count += 1
# 	return sum_value + number
#
# print(average(10, 20, 30))
# print(average(4, 23))
#
#
#
# def average2(*numbers):
# 	return sum(numbers) / len(numbers)
#
# print(average(10, 20, 30))
# print(average(4, 23))
#
# # quiz 2-4
# def get_bmi(height, weight):
#     height /= 100
#     bmi = weight / (height * height)
#     if bmi < 18.5:
#         print("저체중")
#     elif 18.5 <= bmi < 23:
#         print("보통")
#     elif 23 <= bmi < 25:
#         print("과체중")
#     elif 25 <= bmi:
#         print("비만")
#     return round(bmi, -1)
# bmi = get_bmi(176, 69)
# print(bmi)
#
# 3-1
# def n_sum(argument):
#     x = len(str(argument))
#     sum = 0
#     if x < 10:
#         for i in range(0, x + 1):
#             sum += argument % 10
#             argument //= 10
#         return sum
#     else:
#         return -1
# result = n_sum(10)
# print(result)
# 3-2
# def get_subway_fare(km):
#     if km < 10:
#         money = 720
#     elif km < 50:
#         money = 720 + (km - 10) // 5 * 100 + 100
#     elif km > 50:
#         x = km - 50
#         y = km - x - 10
#         money = 720 + (y // 5 * 100) + (x // 8 * 100) + 100
#     return money
# fare = get_subway_fare(5)
# print(fare)
# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(61)
# print(fare)        #1720

# 3-3
# def get_three_six_nine(num):
#     a = str(num)
#     cnt = a.count("3") + a.count("6") + a.count("9")
#     if cnt == 0:
#         return num
#     else:
#         return "짝" * cnt
# result = get_three_six_nine(1)
# print(result)
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝

# quiz 3-4
# n4함수에 넣은 인수들중 4의 배수의 숫자들 개수 리턴하기

def multipleOfFour(*numbers):
    # *number 에서 숫자들 받기 - > if문으로 4의배수인지 판별 - > cnt ++ -> cnt return
    cnt = 0
    list(numbers)
    for i in range(0, len(numbers)):
        if numbers[i] % 4 == 0:
            cnt += 1
    return cnt

result = multipleOfFour(10, 12, 14, 100)
print(result) # 2

'''
Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
is_prime() 함수를 만든다.
인수로 1개의 숫자를 받는다.
인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
'''
def is_prime(number):
        for i in range(2, number + 1):
            if (number == 1) or (number == 2):
                return "소수"
            elif (number % i == 0):
                return "소수아님"
            else:
                return "소수"


result = is_prime(2)
print(result)     #소수
result = is_prime(13)
print(result)     #소수
result = is_prime(36)
print(result)     #소수 아님


'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다. 
'''
def get_compliment(comment):
        if comment.find("고구마") != -1:
            return "왓쇼이!"
        elif comment.find("맛있는") != -1:
            return "우마이!"
        elif (comment.find("놀랄 만한") != -1) or (comment.find("황당한") != -1) or (comment.find("굉장한") != -1):
            return "요모야..!"
        else:
            return "으무!"


result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황')
print(result) # 요모야..!
result = get_compliment('좋은 마음가짐이다!')
print(result) # 으무!


'''
Quiz5-1. 모듈이란?


Quiz5-2. 패키지란?



Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요



Quiz5-4. __all__의 역할은?
import하여 불러올때 사용범위를 지정해준다.

Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?

Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 VietnamPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
import travel.vietnam
< 가 > 


from travel import vietnam
< 나 > 


from travel.vietnam import VietnamPackage

< 다 > 
'''