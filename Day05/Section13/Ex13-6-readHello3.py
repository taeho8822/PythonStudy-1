file = open('hello.txt', 'rt', encoding='UTF-8')

while True:
    str = file.readline()
    if str == '':
        break
    print(str, end='')

file.close()