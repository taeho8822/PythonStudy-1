'''
매직 메소드 (Magic Method)란?
    매직 메소드 혹은 스페셜 메소드라고 불리며, 메소드의 양쪽을 두 개의 언더스코어(__)로 감싼 메소드를 말한다.
'''

'''
__init__()
해당 메소드는 파이썬 클래스의 인스턴스를 생성할 때 자동으로 호출되며, 일반적으로 인스턴스 생성과 함께 인스턴스 변수를 선언하기 위해 사용된다.
'''

class Person1:

    def __init__(self):
        print("인스턴스 생성")


p1 = Person1()

'''
__str__()
해당 메소드는 객체를 우리가 이해할 수 있는 문자열로 만들 수 있도록 해준다.
'''
# __str__ 오버라이딩 전
class Person2:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person2("SeongEon", 27)
print(p1)  # <__main__.Person object at 0x7f78a0036df0>


# __str__ 오버라이딩 후
class Person3:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}"


p1 = Person3("SeongEon", 27)
print(p1)  # Person SeongEon


'''
__len__()
두 가지 이외에도, 특정 객체의 길이를 구하는 len() 또한 매직 메소드로, 새로 만드는 객체에 대하여 오버라이딩이 가능하다.
'''


class Person4:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}"

    def __len__(self):
        return self.age


p1 = Person4("SeongEon", 27)
print(len(p1))  # 27




'''
__add__: 더하기 연산
__mul__: 곱하기 연산
__doc__: 객체의 DocString을 리턴하는 연산자
__gt__: ~보다 크다 (greater than)
__ge__: ~보다 크거나 같다 (greater than or equal to)
__lt__: ~보다 작다 (less than)
__le__: ~보다 작거나 같다 (less than or equal to) 
__del__: 객체가 삭제될 때 호출되는 메소드
__eq__: == 연산 (equals)
__ne__: != 연산 (not equals)
'''


