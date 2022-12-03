file = open('hello.txt', 'rt', encoding='UTF-8')

while True:
    str = file.read(5)
    if not str:
        break
    print(str, end='')

file.close()