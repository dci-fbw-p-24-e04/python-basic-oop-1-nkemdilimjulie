import math

class Point:
   
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y
             
    def reset(self):
        #self.pointer = (0,0)
        self.x = 0
        self.y = 0

    def calc_distance(self, other):
        ''' self = p1 --> holds the current object or instance; other = p2 --> holds the other  or 2nd instance'''
        x1 = self.x
        x2 = other.x
        y1 = self.y
        y2 = other.y
        ''' calculates the square roots of the difference of the two points or two instances'''
        self.distance = math.sqrt(((x1- x2)**2) + ((y1- y2)**2))
        return self.distance


if __name__ == "__main__":
    p1 = Point(3, 2)
    p2 = Point(3, 7)   

    print()

    p1.reset()
    p2.reset()

    p1.move(4, 7)
    p2.move(6, 2)

    print("After moving")
    print(p1.x, p1.y) # 4 7
    print(p2.x, p2.y) # 6 2

    print("find difference")
    print(p1.calc_distance(p2)) #5.385164807134504
