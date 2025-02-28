class Animal:
      def speak(self):
           return "Animal speaks"
class Cat(Animal): # Animal 클래스를 상속
    def speak(self):
         return "Cat says Meow"
class Dog(Animal): # Animal 클래스를 상속
    def speak(self):
        return "Dog says Woof"

# 객체 생성
my_cat = Cat()
my_dog = Dog()

# 메서드 호출
print(my_cat.speak()) # result: Cats say Meow
print(my_dog.speak()) # result: Dog says Woof