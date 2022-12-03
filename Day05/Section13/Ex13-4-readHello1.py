file = open('hello.txt', 'rt', encoding='UTF-8')

str = file.read()
print(str, end='')

file.close()
