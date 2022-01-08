import random

n = random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
list1 = ["hello","how","are","you"]
set1 = {"hello","john","how are you"}
dict1 = { 1:"sushma",2:"reshma",3:"cindrella"}
print(random.choice(list1))
#print(random.choice(set1))
random.shuffle(list1)
