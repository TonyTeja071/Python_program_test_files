class Person:
	def __init__(self, fname,lname):#main method or constructor and self is compulsary
		self.firstName = fname
		self.lastName=lname
	def printname(self):#Method print name
		print(self.firstName,self.lastName)

#Creating object and executing methods
x=Person("Tony","Teja")
x.printname()
del x #to delete the object

class student(Person): #Child class of person class
	pass #used to create empty class
x=student("Tony","Stark") #can use parent class methods
x.printname()


class boss(Person): #another child class
	def __init__(self,fname,lname,graduationYear):
		super().__init__(fname,lname) #using super keyword to inherit parent class
		self.graduationYear=graduationYear

	def print12(self):
		print("Welcome", self.firstName, self.lastName, "to the class of", self.graduationYear)
x = boss("Tony", "Stark", 2003)
x.print12()


#trying inheritance classes
class booking:
	def __init__(self,name,age):
		self.name=name 
		self.age=age 

class dest(booking):
	def __init__(self,name,age,destination):
		super().__init__(name,age)
		self.destination=destination
	def printTicket(self):
		print("Thanks "+self.name+" for using our services.Your age is "+str(self.age)+" and your destination is "+self.destination)
obj=dest("Teja",19,"Tirupati")
obj.printTicket()

# import random
import random

# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

r1 = random.randint(5, 15)
print("Random number between 5 and 15 is % s" % (r1))

random.seed(10)
print(random.random())

random.seed(10)	
print(random.random())

import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=["jadeja","ashwin","virat","Dhoni","Bumrah","Rohit"]
print(random.choice(mylist))
random.shuffle(mylist)
print(mylist)

import re 
txt="Use of python in Machine Learning"
x=re.search("^Use.*Learning$", txt)
if(x):
	print("We Found a Match")
else:
	print("No Match")

y=re.findall("in",txt)
print(y)
obj= re.search("\s",txt)
print(obj)


x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')

x=2.0
if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')





astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1

print(istr)