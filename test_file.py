file = open('example.txt', 'r')
content = file.read()
print(content)
file.close

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

with open('example.txt', 'r') as file:
    content = file.readline()
    print(content)

with open('example.txt', 'r') as file:
    content = file.readlines()
    print(content)

with open('example.txt', 'w') as file:
    content = file.write("six\n")
    content = file.write("seven")

with open('example.txt', 'a') as file:
    content = file.write("six\n")
    content = file.write("seven\n")