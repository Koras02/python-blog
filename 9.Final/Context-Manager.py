class MyContextManager:
    def __enter__(self):
        print("Context In.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
         print("Context Exit")

with MyContextManager() as manager:
    print("Context interior")