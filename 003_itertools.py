from itertools import *

list_1 = [1,2,3,'a','b','c']
list_2 = [101,102,103,'X','Y']

for i in chain(list_1, list_2):
    print(i)

list_of_chain = list(chain(list_1, list_2))

print('*'*10)

for i in count(10, 2.5):
    # start value, incrementation value
    if i <= 25:
        print(i)
    else:
        break

print('*'*10)

# iterable sequence on a function
print(list(filterfalse(lambda x: x < 5, [1,2,3,4,5,6,7])))

print('*'*10)

print(list(range(10))[2:9:2])
print(list(islice(range(10),2,9,2)))