largest=None
smallest=None
list1=[]
while True:
    x=input()
    if x == "done":
        break
    try:
        if int(x)==-1:
            break
        list1.append(int(x))
    except:
        print("Invalid Number")
for i in list1:
    if largest is None:
        largest=i
    elif i>largest:
        largest = i
    if smallest is None:
        smallest=i
    elif i<smallest:
        smallest=i 
print("Maximum is", largest)
print("Minimum is", smallest)