from baseball_game_engine import make_quiz, check

answer = make_quiz()
# print(answer)
# 무한반복
count = 0


def save_history(player, count):
    with open('baseball_history.txt', 'a')as f:     # 'a' == append
        f.write(f'{player}\t{count}\n')


def load_history():
    count_list = []
    with open('baseball_history.txt','r')as f:
        while True:
            line = f.readLine()
            if line == '' or not line:
                break
            # print(line.rstrip())
            line_data= line.rstrip().split('\t')
            count_list.append(line_data[1])
        # 중복제거
        count_list = set(count_list)    # 집합은 중복x
        count_list = list(count_list)
        count_list.sort()
        return count_list[:3]

while True:
#  숫자3자리 중복없이 묻자
    player = input("숫자 세자리는?(t: top3)")
    if player == 't':
        try:
            history = load_history()
        except FileNotFoundError:
            print('history 파일이 없당')
            continue
        print(history)
        continue
#  strike, ball 확인하자
    count += 1
    strike, ball = check(answer, player)
#  출력하자
    print(f'{player}\tstrike: {strike}\tball: {ball}\t{count}try')
#  strike가 3일 때, 나가자
    if strike == 3:
        # 저장
        save_history(player, count)
        break

#축하해주자
print('축하합니다. 짝짝짝👏👏')