myfile = open("poem.txt")
for line in myfile:
    print(line)

yourfile = open("sample.txt",'w')
yourfile.write("Hello there!")
#any data already int he file is lost when new data is written
#if the file doesn't exist, python creates a new file
#new file is located in the same directory where your python file is
theirfile = open("happy.txt",'w')
theirfile.writelines(["My brother had a daughter","The beauty that she brings", "Illumination", "Don't back down", "Concentrate on seeing the breakers in the bar"])
#writelines helps you write multiple lines
#you can do this using string characters
herfile = open("song.txt",'w')
text = "My brother had a daughter.\nThe beauty that she brings\n\tIllumination.\nDon\'t back down;\nConcentrate on seeing the breakers in the bar."
herfile.write(text)
#if you write to a filename that already exists, existing data is wiped out to add new data
afile = open("song.txt",'a')
afile.write("\nNo reason to live")
#above i just added an additional line without overwriting data
#r: read mode
#w: write mode
#r+: read and write
#a+: append and read
#x: create new file
#...b: for binary files add b e.g. rb, wb
myfile.close()
yourfile.close()
theirfile.close()
herfile.close()

#using with automatically closes your file
#split the lines as list
with open("song.txt","r") as f:
    data = f.readlines()
    for line in data:
        words = line.split()
        print(words)

#writing csv
import csv
with open('employee_birthday.csv','w') as g:
    employee_writer = csv.writer(g,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['John Smith','Accounting','November'])
    employee_writer.writerow(['Erica Meyers','IT','March'])
#writerow adds rows. however it adds an additional line after each

#writing using dictionaries
with open('test.csv','w') as h:
    fieldnames = ['name','dept','birth_month']
    #use dictwriter. specify fieldnames as headers.
    writer = csv.DictWriter(h,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name':'John Dustin','dept':'Accounting','birth_month':'November'})
    writer.writerow({'name':'Erica Abeg','dept':'IT','birth_month':'March'})

#using pandas
import pandas as pd
df = pd.read_csv("hrdata.csv")
print(df)