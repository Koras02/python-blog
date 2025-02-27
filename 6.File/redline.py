with open('example.txt', 'r') as file:
     line = file.readline() # 첫 번째 줄 읽기
     while line:
         print(line, end= '') # 줄바꿈 없이 출력
         line = file.readline() # 다음 줄 읽기