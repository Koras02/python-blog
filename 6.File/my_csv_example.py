import csv

# csv파일을 쓰기모드 'w'로 열기(인코딩 'cp949', 라인 종료 문자 설정 'newline = '')
with open('datas.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile) # 파일 객체를 csv.writer의 인자로 전달해 새로운 writer 객체를 생성

    writer.writerow(['이름', '나이'])
    writer.writerow(['홍길동', 30])
    writer.writerow(['김철수', 25])
    writer.writerow(['이영희', 22])

    print("CSV 파일 작성 완료.")


