class Person: # 슈퍼 클래스

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + '가 ' + food + '를 먹습니다.')


class Student(Person): # 서브 클래스

    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def study(self):
        print(self.name + '는 ' + self.school + '에서 공부를 합니다.')


potter = Student('해리포터', '호그와트')
potter.eat('감자')
potter.study()

print(isinstance(potter, Student))
print(isinstance(potter, Person))
