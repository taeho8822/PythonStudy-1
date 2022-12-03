'''
readlines
    Line 단위로 텍스트를 읽고 List로 리턴해 줍니다.
'''

file = open('hello.txt', 'rt', encoding='UTF-8')

line_list = file.readlines()
for line in line_list:
    print(line, end='')

file.close()