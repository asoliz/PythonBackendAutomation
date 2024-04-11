import csv
import pandas as pd


# with open('files/books.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         print(f'\t{row["name"]} works in the {row["isbn"]} department, and was born in {row["aisle"]}.')
#         line_count += 1
#     print(f'Processed {line_count} lines.')


# 'files/books.csv'
# df = pd.read_csv('files/books.csv')

def getCsv(fileName, key, index):
    df = pd.read_csv(fileName)
    value = df.get("name")[2]
    return value


print(getCsv('files/books.csv', "name", 2))

def another(file):
    df = pd.read_csv(file)
    return df

print(another('files/books.csv').to_string())
print(another('files/books.csv').get("name")[2])
