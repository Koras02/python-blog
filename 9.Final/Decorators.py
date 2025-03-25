def my_decorator(func):
    def wrapper():
        print("Function Before Call")
        func()
        print("Function After Call")
    return wrapper

@my_decorator
def say_py():
    print("Hello!, Python World")

say_py()