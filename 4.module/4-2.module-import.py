# 전체 모듈 가져오기
# import module;


# print(module.greet("JackSon")) # Hello, JackSon
# print(module.PI) # 3.14159

# 모듈의 특정 함수 또는 변수 가져오기
from module import greet
print(greet("King")) # Hello, King!!

# 모듈의 이름 변경해 가져오기
import module as mm
print (mm.greet("Chain")) # Hello, Chain