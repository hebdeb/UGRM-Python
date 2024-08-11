import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x=x
        self.__y=y
        #
        # Escribir el código aquí.
        #

    def getx(self):
        return self.__x
        #
        # Escribir el código aquí.
        #

    def gety(self):
        return self.__y
        #
        # Escribir el código aquí.
        #

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x-x),abs(self.__y-y))
        #
        # Escribir el código aquí.
        #

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(),point.gety())
        #
        # Escribir el código aquí.
        #


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__p1=vertice1
        self.__p2=vertice2
        self.__p3=vertice3
        #
        # Escribir el código aquí.
        #

    def perimeter(self):
        return self.__p1.distance_from_point(self.__p2)+self.__p1.distance_from_point(self.__p3)+self.__p2.distance_from_point(self.__p3)
        #
        # Escribir el código aquí.
        #


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
