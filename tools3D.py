import math
class Obj3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norm(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))
    
    def normalize(self):
        l = self.norm()
        return Obj3D(self.x / l, self.y / l, self.z / l)
    
    def __add__(self, o): 
        return Obj3D(self.x + o.x, self.y + o.y, self.z + o.z)

    def __sub__(self, o):
        return Obj3D(self.x - o.x, self.y - o.y, self.z - o.z)

    def __str__(self):
        return f"Obj3D({self.x}, {self.y}, {self.z})"

class Vector3D(Obj3D):
    @classmethod
    def cross_product(cls, p0, p1):
        n = Obj3D(0,0,0)
        n.x = p0.y * p1.z - p0.z * p1.y
        n.y = p0.z * p1.x - p0.x * p1.z
        n.z = p0.x * p1.y - p0.y * p1.x
        return n

class Point3D(Obj3D):
    pass
        

if __name__ == '__main__':
    x0, y0, z0 = 3322.091064, 604.751282, 963.947876
    x1, y1, z1 = 3296.091064, 838.303528, 888.062134
    x2, y2, z2 = 3296.091064, 604.751282, 963.947876 
    
    p0 = Point3D(x0, y0, z0)
    p1 = Point3D(x1, y1, z1)
    p2 = Point3D(x2, y2, z2)

    vec0 = p1 - p0
    vec1 = p2 - p0

    N = Vector3D.cross_product(vec0, vec1)

    print("N             :", N)
    print("N (normalize) :", N.normalize())



