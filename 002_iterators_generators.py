
def my_gen(x, y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y


my_list = [1,2,3,4,5,6,7,8,9]

my_iter = iter(my_list)
print(next(my_iter))

my_object1 = my_gen(10, 5)
print(next(my_object1))
print(next(my_object1))
print("*****")

my_object2 = my_gen(4, 2)
for k in range(4):
    print(next(my_object2))

print("*****")
gen_exp = (x * 2 for x in range(4,8))
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))