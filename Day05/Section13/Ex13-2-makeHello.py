'''
파일명 : Ex13-2-makeHello.py
r (read mode) : 읽기 전용 모드
w (write mode) : 쓰기 전용 모드
a (append mode) : 추가 모드
t (text mode) : 해당 파일의 데이터를 텍스트 파일로 인식하고 입출력함.
b (binary mode) : 해당 파일의 데이터를 바이너리 파일로 인식하고 입출력함.
x (exclusive mode) : 열고자 하는 파일이 이미 존재하면 파일 개방에 실패함.
+ (update mode) : 파일을 읽을 수도 있고 쓸 수도 있는 모드
'''
file = open('hello.txt', 'wt', encoding='UTF-8')
file.write('안녕하세요.')
file.write('\n')
file.write('반갑습니다.')
file.write('\n')
print('hello.txt 파일이 생성되었습니다.')
file.close()