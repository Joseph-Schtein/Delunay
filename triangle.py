from Edge import Edge
from Point import Point


class Triangle:

    def __init__(self, new_p1, new_p2, new_p3):
        self.points = [Point for i in range(3)]
        self.points[0] = new_p1
        self.points[1] = new_p2
        self.points[2] = new_p3
        e1 = Edge(new_p1, new_p2)
        e2 = Edge(new_p1, new_p3)
        e3 = Edge(new_p2, new_p3)
        self.edges = [Edge for i in range(3)]
        self.edges[0] = e1
        self.edges[1] = e2
        self.edges[2] = e3

    def get_p1(self):
        return self.points[0]

    def get_p2(self):
        return self.points[1]

    def get_p3(self):
        return self.points[2]

    def get_points(self):
        return self.points

    def get_edges(self):
        return self.edges

    def to_string(self):
        print(self.points[0].get_x(), " ", self.points[0].get_y(), " ", self.points[1].get_x(), " ",
              self.points[1].get_y(), " ",self.points[2].get_x(), " ",self.points[2].get_y())
