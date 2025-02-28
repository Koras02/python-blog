class Person:
     def __init__(self, name, age):
         self.name = name # 인스턴스 변수
         self.age = age

     def bark(self): # 메서드
          return f"{self.name} says Human!"
# 객체 생성
my_person = Person("James", 27)

# 객체 사용
print(my_person.bark()) # result: James says Human!;