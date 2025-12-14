words = ["lkjlkjlkj", "lkjlkjlkjl5757"]
sent = " ".join(words)
print(sent)

my_list = [1, 2, 3, 'hello', True]
print(my_list)

empty = []
print (empty)

my_str = "Python"
char_list = list(my_str)
print(char_list)

num = [1, 5, 2, 8, 3]
print(len(num))
print(sum(num))
print(min(num))
print(max(num))

num = [1, 5, 2, 8, 3]
print(5 in num)
print(10 in num)

num = [1, 5, 2, 8, 3]
print(num[0])
print(num[1:3])

num = [1, 5, 2, 8, 3]
num[0] = -1
print(num[0])
print(num[1:3])

l1 = [1, 2]
l2 = [3, 4]
print(l1 + l2)
print(l1 * 3)

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)

my_list = [1, 2, 3]
my_list.insert(1, "hello")
print(my_list)

my_list = [1, 2, 2, 3]
pop_val = my_list.pop(1)
print(my_list)
print(pop_val)

my_list = [1, 2, 3, 2]
print(my_list.index(3))

my_list = [1, 2, 3, 2]
print(my_list.count(2))

my_list = [1, 2, 3, 5, 8, 2]
my_list.sort()
print(my_list)

my_list = [1, 2, 3, 5, 8, 2]
my_list.reverse()
print(my_list)

my_list = [1, 2, 3, 5, 8, 2]
del my_list[1]
print(my_list)

my_list = [1, 2, 3, 5, 8, 2]
my_list.clear()
print(my_list)

my_list = [1, 2, 3, 5, 8, 2]
new_list =  my_list.copy()
new_list.append(10)
print(new_list)
print(my_list)

my_list = [1, 2, 3, 5, 8, 2]
for item in my_list:
    print(item)

my_list = [3, 1, 4]
a, b, c = my_list
print(a, b, c)

stroka = input()
num = stroka.split()
a, b, c = num
print(a, b, c)