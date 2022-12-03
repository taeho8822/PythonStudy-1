'''
readline
  파일에서 1줄을 읽고 그 결과를 리턴해줍니다.

'''

file = open('hello.txt', 'rt', encoding='UTF-8')

while True:
    str = file.readline()
    if str == '':
        break
    print(str, end='')

file.close()