import math


class shape:
    def rectangle(self, length, breadth):
        print('perimeter is: ', 2 * (length + breadth))
        print('Area is: ', length * breadth)

    def circle(self, radius):
        pie = math.pi
        print('perimeter is: ', pie * radius * 2)
        print('Area is:', pie * radius * radius)

    def triangle(self, a, b, c):
        print('perimeter is:', a + b + c)
        s = (a + b + c) / 2
        val = s * (s - a) * (s - b) * (s - c)
        print('Area is:', math.sqrt(val))


obj = shape()
print('enter the l,b values')
obj.rectangle(int(input()), int(input()))
print('enter the radius')
obj.circle(int(input()))
print('enter the all sides of triangle')
obj.triangle(float(input()), float(input()), float(input()))