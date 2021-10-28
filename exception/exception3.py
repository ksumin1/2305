list1 = [1, 5, 7]
try:
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[3])     # index error

except IndexError as e:
    print(e)            # list index out of range
except:
    pass
else:
    print('성공')
finally:
    print('꼭 실행해야하는 코드')
