class Circle:

    def __init__(self, radius):
        self.radius = radius

# class Area(self):  
#     pass

    def __mul__(self, area):
        area = 2 *( 22/7) * self.radius
        return Circle(area)

area = Circle(2)     
area.Area()