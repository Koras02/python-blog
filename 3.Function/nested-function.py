def other_function():
    def inner_function():
         return "inner_function"
    return inner_function()

print(other_function()) # inner_function