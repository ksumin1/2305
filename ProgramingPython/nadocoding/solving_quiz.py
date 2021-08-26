# quiz 1-1
id_number = "123456"
year = id_number[0:2] # [:2], [-6:-4]
month_day = id_number[2:6] # [2:], [-4:]
print(year)
print(month_day)
print("둘의 곱은: " +str(int(year)) * int(month_day))

# quiz 1-2
phone_number = "02-1234-5678"
x = phone_number.find('-')
print(phone_number[0:x])
print(phone_number[-4:])

phone_number2 = "032-9876-4321"
x = phone_number2.index('-')
print(phone_number2[0:x])
print(phone_number2[-4:])

# 전화번호 입력시 -가잇든읎든 출력
phone_number1 = '010-1234-5678'
phone_number2 = '10198765432'
phone_number3 = '010 1111 2222'

phone_number = phone_number3
result = phone_number.replace('-', '').replace(' ', '')
print(result)

# result = phone_number3.replace('', '')
# print(result)

# quiz 2-1
student_number = "2100"
number = student_number[1]
number = int(number)
if number == 1 or number ==2:
    print(f"{number}반 뉴미디어 소프트웨어과")
elif number == 3 or number == 4:
    print(f"{number}반 뉴미디어 웹솔루션과")
elif number == 5 or number == 6:
    print(f"{number}반 뉴미디어 디자인과")
else:
    print("잘못 입력했습니다.")

majors = ['뉴미디어소프트웨어과', '뉴미디어웹솔루션과', '뉴미디어디자인과']
if 1 <= number <= 6:
    print(f"{number}반 {majors[(number - 1) // 2]}")
else:
    print("잘못입력했습니다.")

# quiz 2-2
def get_major(student_number):
    if student_number[1] == "1" or student_number[1] == "2":
        return "뉴미디어소프트웨어과", student_number[0]
    elif student_number[1] == "3" or student_number[1] == "4":
        return "뉴미디어웹솔루션과", student_number[0]
    elif student_number[1] == "5" or student_number[1] == "6":
        return "뉴미디어디자인과", student_number[0]
    else:
        return "잘못입력했습니다."
grade, major = get_major('2100')
print(major, grade)

# # 구구단 2~9단 출력
# for dan in range(2, 10):
#     for i in range(1, 9 + 1):
#         print(f'{dan} x {i} = {dan * i}')
#     print('-' * 10)
# # 구구단 2~7단 출력
# for dan in range(2, 9+1):
#     for i in range(1, 9 + 1):
#         print(f'{dan} x {i} = {dan * i}')
#     print('-' * 10)
#     if dan == 7:
#         break
# # 구구단 2 ~7단 출력, 홀수만 출력
# for dan in range(2, 9+1):
#     for i in range(1, 9 + 1, 2):
#         if i % 2 == 0:
#             continue
#         print(f'{dan} x {i} = {dan * i}')
#     print('-' * 10)
#     if dan == 7:
#         break
# 변수와 자료형
# 숫자형 - 정수형: int 실수형: float 복소수: complex 진수
# 문자열'',""
# 인덱싱,슬라이싱