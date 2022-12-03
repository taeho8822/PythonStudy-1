'''
print 대신
sys.stdout.writelines()
'''

import sys

file = open('hello.txt', 'rt', encoding='UTF-8')

line_list = file.readlines()
sys.stdout.writelines(line_list)

file.close()