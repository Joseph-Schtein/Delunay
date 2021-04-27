from copy import deepcopy

import numpy as np
import matplotlib.pyplot as plt

from Edge import Edge
from Point import Point
from triangle import Triangle


def count_lines(file):
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1

    file.close()
    return line_count


def load_point_list(file):
    file_pointer = open(file, 'r')
    number_lines = count_lines(file_pointer)
    file_pointer = open(file, 'r')
    line = file_pointer.readline().split()
    number_of_points = int(line[0])
    list_of_points = [Point for i in range(number_of_points)]
    counter = 0
    x = 0
    y = 0
    for index in range(1, len(line) - 1):
        if index % 2 == 1:
            x = int(line[index])

        else:
            y = int(line[index])
            tmp_point = Point(x, y)
            list_of_points[counter] = deepcopy(tmp_point)
            counter += 1

    for i in range(1, number_lines):
        x = line[len(line) - 1]
        line = file_pointer.readline().split()
        for j in range(len(line)):
            if j % 2 == 0:
                y = int(line[j])
                tmp_point = Point(x, y)
                list_of_points[counter] = deepcopy(tmp_point)
                counter += 1

            else:
                x = int(line[j])

    return list_of_points


def orientation(p1, p2, p3):
    val = (p2.get_y() - p1.get_y()) * (p3.get_x() - p2.get_x()) - \
          (p2.get_x() - p1.get_x()) * (p3.get_y() - p2.get_y())

    if val < 0:
        return [p1, p2, p3]

    if val > 0:
        return [p2, p1, p3]


def inside_triangle(p1, p2, p3, q):
    order = orientation(p1, p2, p3)

    mat = np.array([[1, order[0].get_x(), order[0].get_y(),
                     (order[0].get_x() * order[0].get_x()) + (order[0].get_y() * order[0].get_y())],
                    [1, order[1].get_x(), order[1].get_y(),
                     (order[1].get_x() * order[1].get_x()) + (order[1].get_y() * order[1].get_y())],
                    [1, order[2].get_x(), order[2].get_y(),
                     (order[2].get_x() * order[2].get_x()) + (order[2].get_y() * order[2].get_y())],
                    [1, int(q.get_x()), int(q.get_y()), int((q.get_x() * q.get_x())) + int((q.get_y() * q.get_y()))]])

    deter = np.linalg.det(mat)

    return deter < 0


def algorithm(list_points):
    p_2 = Point(0, 0)
    p_1 = Point(10000, 0)
    p0 = Point(5000, 8660)
    counter = 0
    triangle_list = []
    tmpTriangle = Triangle(p_2, p_1, p0)
    triangle_list.append(tmpTriangle)
    for i in range(len(list_points)):
        badTriangles = []
        for j in range(len(triangle_list)):
            if inside_triangle(triangle_list[j].get_p1(), triangle_list[j].get_p2(),
                               triangle_list[j].get_p3(), list_points[i]):
                badTriangles.append(triangle_list[j])

        polygon = []
        for k in range(len(badTriangles)):
            k_edges = badTriangles[k].get_edges()
            k_points = badTriangles[k].get_points()
            to_insert = [True, True, True]
            for t in range(len(badTriangles)):
                t_edges = badTriangles[t].get_edges()
                t_points = badTriangles[t].get_points()
                if not same_triangle(k_points, t_points):
                    for e in range(len(k_edges)):
                        if contain_edge(k_edges[e], t_edges):
                            to_insert[e] = False

            for index in range(3):
                if to_insert[index]:
                    polygon.append(k_edges[index])

        for k in range(len(badTriangles)):
            triangle_list.remove(badTriangles[k])

        for p in range(len(polygon)):
            tmp_edge = polygon[p]
            new_triangle = Triangle(tmp_edge.get_p1(), tmp_edge.get_p2(), list_points[i])
            triangle_list.append(new_triangle)

    triangle_list_without = []
    insert_triangle = True
    for t in triangle_list:
        if equal_points(t.get_p1()):
            insert_triangle = False

        if equal_points(t.get_p2()) and insert_triangle:
            insert_triangle = False

        if equal_points(t.get_p3()) and insert_triangle:
            insert_triangle = False

        if insert_triangle:
            triangle_list_without.append(t)
        insert_triangle = True

    return triangle_list, triangle_list_without


def equal_points(p):
    if (p.get_x() == 0 and p.get_y() == 0) or (p.get_x() == 10000 and p.get_y() == 0) or (
            p.get_x() == 5000 and p.get_y() == 8660):
        return True

    else:
        return False


def contain_edge(e, edge_list):
    p1 = e.get_p1()
    p2 = e.get_p2()
    for i in range(len(edge_list)):
        tmp1 = edge_list[i].get_p1()
        tmp2 = edge_list[i].get_p2()
        if p1.get_x() == tmp1.get_x() and p1.get_y() == tmp1.get_y() and \
                p2.get_x() == tmp2.get_x() and p2.get_y() == tmp2.get_y():
            return True

    return False


def same_triangle(t1, t2):
    same_p1 = t1[0].get_x() == t2[0].get_x() and t1[0].get_y() == t2[0].get_y()
    same_p2 = t1[1].get_x() == t2[1].get_x() and t1[1].get_y() == t2[1].get_y()
    same_p3 = t1[2].get_x() == t2[2].get_x() and t1[2].get_y() == t2[2].get_y()

    return same_p1 and same_p2 and same_p3


def GUI(triangle_list):
    for index in range(len(triangle_list)):
        points = triangle_list[index].get_points()
        coordinate_x_list = [points[0].get_x(), points[1].get_x(), points[2].get_x(), points[0].get_x()]
        coordinate_y_list = [points[0].get_y(), points[1].get_y(), points[2].get_y(), points[0].get_y()]
        plt.plot(coordinate_x_list, coordinate_y_list, color="black")

    plt.show()


def main():
    path = r"C:\Users\yossi\OneDrive\Documents\discrete-geometric\input-data.txt"
    list_of_points = load_point_list(path)
    triangle_list, triangle_list_without = algorithm(list_of_points)
    GUI(triangle_list)
    GUI(triangle_list_without)



if __name__ == '__main__':
    main()
