class Teja:
    def areaRectangle(a, b):
        return (a * b)

    def perimeterRectangle(a, b):
        return (2 * (a + b))

    a = float(input('enter a:'))
    b = float(input('enter b:'))

    print("Area = ", areaRectangle(a, b))
    print("Perimeter = ", perimeterRectangle(a, b))

    def areaCircle(r):
        return (3.14*r*r)

    def perimeterCircle(r):
        return (2*3.14*r)

    r = float(input('enter r:'))

    print("Area = ", areaCircle(r))
    print("Perimeter = ", perimeterCircle(r))

    def areaTriangle(c, d, e):
        return ( 0.5*q*e)

    def perimeterTriangle(c, d, e):
        return (c+d+e)

    c = float(input('enter q:'))
    d = float(input('enter w:'))
    e = float(input('enter e:'))

    print("Area = ", areaTriangle(c, d, e))
    print("Perimeter = ", perimeterTriangle(c, d, e))