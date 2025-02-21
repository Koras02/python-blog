def outer_function(x):
    def inner_function(y):
         return x * y
    return inner_function

add_25 = outer_function(25)
print(add_25(5)) # 125
