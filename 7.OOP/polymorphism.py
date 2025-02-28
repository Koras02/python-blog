class Animal:
    def speak(self):
        return "Animal speaks"


class Cat(Animal):  # Animal 클래스를 상속
    def speak(self):
        return "Cat says Meow"


class Dog(Animal):  # Animal 클래스를 상속
    def speak(self):
        return "Dog says Woof"


def animal_sound(animal):
    print(animal.speak())

# 객체 생성
my_cat = Cat()
my_dog = Dog()

animal_sound(my_cat) #출력: Cat says Meow
animal_sound(my_dog) #출력: Dog says Woof