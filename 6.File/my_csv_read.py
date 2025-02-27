import csv

# CSV 파일 읽기
with open('datas.csv', 'r', encoding="utf-8-sig") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
          print(row)