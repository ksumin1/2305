import os

data = os.listdir('.')  # 현재 디렉터리
data = os.listdir('..')  # 상위 디렉터리
data = os.listdir('my_directory')  # 하위 디렉터리
data = os.listdir('C:\\Users\\User\\PycharmProjects\\Programming-Python-\\2300\\file handler')  #절대경로
data = os.listdir('C:/Users/User/PycharmProjects/Programming-Python-/2300/file handler')  #절대경로

# print(data)
for d in data:
    print(d)
    print(f'is directory? : {os.path.isdir(d)}')
    print(f'is file? : {os.path.isfile(d)}')