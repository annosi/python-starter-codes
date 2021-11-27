#simplelambdafunctions
squared = lambda x: x ** 2
print(squared(5))
add = lambda x,y: x+y
print(add(3,5))
mult = lambda x,y,z: x*y*z
print(mult(3,2,1))
power = lambda x,y=2:x**y
print(power(5,3))
print(power(5))

#lambda with sort function
#extending sort
names = ['Ann Osi','Victor Ejiogu','Lola Eniodunmo','Eddah Mauti','Titilayo Akinseye','Mark Essien','Beyonce Knowles','Patricia Cornwell']
print(names)
names.sort()
print(names)
#let's sort by surname
names.sort(key=lambda x:x.split()[-1])
print(names)
people = [('Juliet',22),('Ann',27),('Victor',28),('Gabriel',10)]
print(people)
people.sort()
print(people)
people.sort(key=lambda x: x[1])
print(people)
#with above we change the sort function to pick another object
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f'{self.name}:{self.age}'
alex = Person('Alex',16)
mabel = Person('Mabel',15)
eddie = Person('Eddie',12)
p = [alex, mabel, eddie]
print(p)
p.sort(key=lambda x:x.age)
print(p)

#lambda with filter
#filtering numbers
nums = list(range(1,21))
print(nums)
evens = list(filter(lambda x: x%2==0,nums))
odds = list(filter(lambda x: x%2!=0,nums))
print(odds)
print(evens)

from statistics import mean
para = list(range(1,21))
avg = mean(para)
above_avg = list(filter(lambda x: x>avg, para))
below_avg = list(filter(lambda x: x<avg,para))
print(para)
print(avg)
print(above_avg)
print(below_avg)

nicknames = ['Diamondbacks', 'Braves','Orioles','Red Sox',\
    'Cubs','White Sox','Reds','Indians','Rockies']
print(nicknames)
short = list(filter(lambda x: len(x)<6,nicknames))
print(short)

#lambda with map
#map applies a function to an iterable to create a new iterable
number = list(range(1,11))
print(number)
sq_number = list(map(lambda x: x**2,number))
print(sq_number)

numbr = list(range(1,11))
print(numbr)
even = list(map(lambda x:x%2==0,numbr))
print(even)

wc_teams =[('Brazil',21),('Germany',19),('Italy',18),\
    ('Argentina',17),('France',15),('England',15)]
print(wc_teams)
new = list(map(lambda team: (team[0],team[1]+1),wc_teams))
print(new)

#lambda with reduce
#reduce applies function of two arguments to every element of an iterable cumulatively from left to right, reducing the sequence to a single value
from functools import reduce
numb = list(range(1,11))
total = reduce(lambda x,y: x+y,numb)
print(total) #this is a reconstruction of the sum function LOL

alias = ['dan','darren','joanna','jackie','chris']
conc = reduce(lambda x,y: x+y[:2],alias,'')
print(conc)

