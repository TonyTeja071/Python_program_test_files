class Details:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Fdetails(Details):
    def det(self):
        print("name:",self.name,"\nAge:",self.age)


class Destination:
    def __init__(self, pickup, to):
        self.pickup=pickup
        self.to = to


class Desti(Destination):
    def pick(self):
        print("pickup:",self.pickup)
        print("drop:",self.to)

class Date:
    def __init__(self, month, year, day):
        self.month = month
        self.year = year
        self.day = day

class Da(Date):
    def bookdate(self):
        print("DATE:",self.day,self.month,self.year)

class Allclasses:
    def __init__(self, classes):
        self.classes = classes

class All(Allclasses):
    def bookclass(self):
        print(self.classes)

ob = Fdetails("Teja", 18)
ob.det()
obje = Desti("Vijayawada","Tirupati")
obje.pick()
obj = Da(4, 2003, 18)
obj.bookdate()
object = All("ACclass")
object.bookclass