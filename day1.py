import numpy as np
a=10
b=12
print(a+b)
sum=a+b
print(sum)
b=7.25
print(a+b)

#min and max functions
print(max(a,b))
print(min(a,b))

#print length of list
Names = ['Jon', 'Bill', 'Maria', 'Jenny', 'Jack']
print(len(Names))


#normal method of multiply in list
Age = [22,34,42,27,57]
num=[10,11,12,14,65]
res_list = [Age[i] * num[i] for i in range(len(Age))]
print(res_list)


#using numpy
product = np.multiply(Age,num)
print(product)