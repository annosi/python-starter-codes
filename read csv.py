import csv
with open("C:\\Users\\osian\\Desktop\\Python Learner Files\\employee_birthday.txt") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    #csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
    #above places everything inside " under one column
    #csv_reader = csv.DictReader(csv_file, delimiter=',', escapechar='|')
    #escapechar ignores quotes after the escape parameter |
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count +=1
  
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}')
        line_count+=1
