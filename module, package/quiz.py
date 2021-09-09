# 1. 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다. 62400원 청구. 59827원일 경우, 실제 청구 금액은?
import math
bill = 59827
print(math.floor(bill/100)*100)
# print(bill//100*100) or print(bill-bill%100)

# 2. 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?
score = 56
print((math.round(score / 10))*10)
# print(round(score,-1))

# 3. 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
import random
listNum = []
LottoNum = []
for i in range(1,46):
    listNum.append[i]
for i in range(7):
    LottoNum[i] = random.random(listNum)
    print(LottoNum)
# print(random.sample(range(1,46),6)


# 4. 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)
# list_r = random.sample(range(1,10), 3)
# print(**,join(Str(n)for n in list_r)
# print(**.join(str,list_r))
num = []
for i in range(1,10):
    num[i].append(i)
for i in range(3):
    print(random.random(num[i]))
    del num[i]

# 5. 내가 태어난 날로부터 며칠이 지났는지?
import datetime
now = datetime.datetime.now()
birth = datetime.datetime(2004, 9, 23)
print(now - birth)

# 6. 올해 크리스마스까지 며칠이 남았는지?
christmas = datetime.datetime(2021, 12, 24)
print(christmas - now)

# 7. 내 생일이 며칠 남았는지?
yj_birth = datetime.datetime(2021, 1, 4)
if yj_birth < now:
    yj_birth = yj_birth.replace(year=yj_birth.year + 1)
print(birth - now)

# 8. 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?

# 마지막 번호가 몇번인지
last_number = input("마지막 번호: ")
# 1~마지막번호까지 리스트만들기
list_class = list(range(1, int(last_number) + 1))
# 무한 반복
while True:
# 나간 친구 번호
    exclude_number = input("뺄 번호(enter치면 끝): ")
# 리스트 제외
    list_class.remove(int(exclude_number))
    print(list_class)
# 그냥 enter면 반복 끝
    if exclude_number == '':
        break

# 랜덤으로 섞기
random.shuffle(list_class)
# 출력
# print(list_class)
print('자리\t학생번호')
for index,n in enumerate(list_class):
    print(f'{index + 1}\t{n}')