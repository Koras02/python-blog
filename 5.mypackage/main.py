# from mypackage import module1, module2
# from mypackage.subpackage import submodule
# from mypackage.subpackage.submodule import sub_thank
#
# print(module1.func1()) # Function 1 from Module 1
# print(module2.func2()) # Function 2 from Module 2
#
# print(submodule.sub_function()) # Hello from submodule!
# print(sub_thank()) # Thank you!
#
# import mypackage
#
# print(mypackage.submodule.sub_function()) # Hello from submodule!

from mypackage.subpackage.subsubpackage import subsubmodule

print(subsubmodule.sub_thank()) # Thank you
print(subsubmodule.sub_hello()) # Hello from subsubmodule