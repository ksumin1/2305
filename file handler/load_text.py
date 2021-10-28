print('한꺼번에 전체 읽기')
# f = open('text.txt', 'r', encoding = 'utf-8')
# data = f.read()
# f.close()
# print(data)

with open('text.txt','r',encoding='utf-8') as f:
    data = f.read()
print(data)

print('한 줄씩 읽기')    # 제일 많이 씀
with open('text.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline() # line: 'hello\n'
        if line == '':
            break
        print(line.rstrip())

print('한꺼번에 전체 읽어서, 한 줄씩 리스트')
with open('text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
for line in lines:
    print(line.rstrip())












