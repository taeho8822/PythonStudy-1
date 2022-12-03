'''
 read(인자)
    인자값 수 만큼 읽어온다

'''

file = open('hello.txt', 'rt', encoding='UTF-8')

while True:
    str = file.read(5)
    if not str:
        break
    # print(str, end='')

file.close()