class Point:

    def __init__(self, new_x, new_y):
        self.x = int(new_x)
        self.y = int(new_y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def to_string(self):
        print("X: ", self.x, ", Y: ", self.y)
