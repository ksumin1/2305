import pickle
from Person import Person

# 객체 하나 가져오자
with open('object.bin', 'rb') as f:
    data = pickle.load(f)   #AttributeError: Can't get attribute 'Person'
print(data)

# 리스트 객체 가져오자
with open('objects.bin', 'rb') as f:
    data = pickle.load(f)
for d in data:
    print(d)
