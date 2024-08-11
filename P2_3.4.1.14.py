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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
