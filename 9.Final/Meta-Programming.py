class Meta(type):
    def __new__(cls, name, bases, attrs):
         attrs['greet'] = lambda self: print("Meta's Hello!")
         return super().__new__(cls,name, bases, attrs)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
obj.greet() # Meta's Hello!