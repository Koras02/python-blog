def my_generator():
    for i in range(5):
        yield i * 2

for value in my_generator():
    print(value) # 0,2,4,6,8