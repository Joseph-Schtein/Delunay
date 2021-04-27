from Point import Point


class Edge:

    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2

    def get_p1(self):
        return self.point1

    def get_p2(self):
        return self.point2

    def to_string(self):
        print(self.point1.to_string(), ",  ", self.point2.to_string())
