a=5
b=2.57
c=1+5j
print(a)
print(b)
print(c)


k=True
j=False
print(k)
print(j)
print(k+j)

Names = ['Jon', 'Bill', 'Maria', 'Jenny', 'Jack']
Age = [22,34,42,27,57]
print(Names)
print (Age)
print(type(Names))
print (type(Age))
print(Age.sort())


# Python3 Program to Create list
# with integers within given range

def createList(r1, r2):
	return list(range(r1, r2+1))
	
# Driver Code
r1, r2 = -5, 1
print(createList(r1, r2))
list2=[]


#dir to get commands
print(dir(list))
age=Names.copy()
print(age)

#help to get help
for i in Age:
	print(i)
print(help(list))


#del used to delete items
del Age[3]
print(Age)


#concating lists
print(Names+Age)


#multipling lists
print(Names*2)


#check in the list
print(22 in Age)
print(22 not in Age)

#checks max and min 
print(max(Age))
print(max(Names))
print(min(Names))

#Nested lists
a = [[1, 2],[3,4],[5,6]]
print   (a[1])
print   (a[2][1])
for i in a[2]:
	print  (i)

#list comprehensions can give statements inside list for iteration
squares=[x**2 for x in range(1,11)]
print(squares)

#normal way
squares=[ ]
for i in range(1,11):
	squares.append(i**2)
print(squares)

#tuples are immunable
tuple1=(10,12,14)
print(tuple1)
print(type(tuple1))


#convert tuple to list
list1=list(tuple1)
print(type(list1))


#convert list to tuple
nam=tuple(Names)
print(type(nam))


#multi line comments
'''3 singel quotes'''



