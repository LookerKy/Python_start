# section 11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME = test/csv

# 예제 1
import csv
import pandas as pd

with open("./src/resource/sample3.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader)

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

with open("./src/resource/sample2.csv", 'r') as f:
    reader = csv.reader(f, delimiter='|')
    next(reader)

    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

with open("./src/resource/sample2.csv", 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        print(c)

# 예제 4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
with open('./src/resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# 예제 5
with open('./src/resource/sample5.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    wt.writerows(w)

# XSL, XLSX
# openpyx1, xlsxwriter, xlrd, xlwt, xlutils
# pandas 를 주로 사용
# pip install xlrd
# pip install openpyxl
# pip install pandas


# sheetname = "시트명" 또는 숫자 header=숫자, skiprow=숫자
xlsx = pd.read_excel("./src/resource/sample.xlsx")
print(type(xlsx))

print(xlsx.head())  # 상위 5개 데이터

print(xlsx.tail())

print(xlsx.shape)

# 쓰기

xlsx.to_excel('./src/resource/result.xlsx', index=False)
xlsx.to_csv('./src/resource/result.csv', index=False)
