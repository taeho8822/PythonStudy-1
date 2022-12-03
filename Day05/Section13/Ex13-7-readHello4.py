file = open('hello.txt', 'rt', encoding='UTF-8')

line_list = file.readlines()
for line in line_list:
    print(line, end='')

file.close()