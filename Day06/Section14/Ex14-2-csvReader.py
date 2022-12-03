'''
파일명 : Ex14-2-csvReader.py

CSV(comma-separated values)
    몇 가지 필드를 쉼표(,)로 구분한
    텍스트 데이터 및 텍스트 파일이다.
'''
student_list = []
with open('학생명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline()     # 첫줄 제거
    while True:
        line = file.readline()
        if not line:
            break
        student = line.split(',')
        student_list.append(student)
print(student_list)






