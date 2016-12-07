import math
import copy

class PointND:

    def __init__(self, *args):
        for val in args[0]:
            if type(val) is not float:
                raise ValueError("Cannot instantiate an object with non-float values.")
        self.t = args[0]
        self.n = len(args[0])

    def __str__(self):
        return str(self.t)

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):

        if len(other.t) != len(self.t):
            raise ValueError("Cannot calculate between points of different cardinality")

        return math.sqrt(sum((val1 - val2)**2 for val1,val2 in zip(self.t, other.t))) # This returns the Euclidean distance between two co-ordinates

    def nearestPoint(self, points):

        if not points:
            raise ValueError("Input cannot be empty.")

        pointND_small = points[0]

        distance_small = self.distanceFrom(points[0])

        for point in points:
            if self.distanceFrom(point) < distance_small:
                distance_small = self.distanceFrom(point)
                pointND_small = point

        return pointND_small

    def clone(self):
        return copy.deepcopy(self)

    def __add__(self, other):

        if isinstance(self,PointND) and isinstance(other, PointND):
            if len(self.t) != len(other.t):
                raise ValueError("Cannot operate on points with different cardinalities")

            values = [val1 + val2 for val1, val2 in zip(self.t,other.t)]
            return PointND(tuple(values))

        # PointND + float
        if isinstance(self,PointND) and isinstance(other, float):
            values = [val1 + other for val1 in self.t]
            return PointND(tuple(values))

    def __sub__(self, other):

        if isinstance(self,PointND) and isinstance(other,PointND):
            if len(self.t) != len(other.t):
                raise ValueError("Cannot operate on points with different cardinalities")

            values = [val1 - val2 for val1, val2 in zip(self.t,other.t)]
            return PointND(tuple(values))

        # PointND - float
        if isinstance(self,PointND) and isinstance(other, float):
            values = [val1 - other for val1 in self.t]
            return PointND(tuple(values))

    def __mul__(self, other):

        if isinstance(self,PointND) and isinstance(other, float):
            values = [val1 * other for val1 in self.t]
            return PointND(tuple(values))

    def __truediv__(self, other):

        if isinstance(self,PointND) and isinstance(other, float):
            values = [val1 / other for val1 in self.t]
            return PointND(tuple(values))

    # Negate a PointND
    def __neg__(self):

        if isinstance(self, PointND):
            values = [val1 * -1 for val1 in self.t]
            return PointND(tuple(values))

    # Indexing of PointND
    def __getitem__(self, item):

        if isinstance(self,PointND) and isinstance(item, int):
            return self.t[item]

    def __eq__(self, other):

        if len(self.t) != len(other.t):
            raise ValueError("Cannot compare points with different cardinalities.")

        if isinstance(self, PointND) and isinstance(other, PointND):
            if self.distanceFrom(other) == 0:
                return True

            return False

    def __ne__(self, other):

        if isinstance(self,PointND) and isinstance(other, PointND):
            return not self.__eq__(other)

    def __lt__(self,other):

        if len(self.t) != len(other.t):
            raise ValueError("Cannot compare points with different cardinalities.")

        origin = [0.00]*len(self.t)
        origin = tuple(origin)  # Co-Ordinates of Origin
        origin = PointND(origin)

        if isinstance(self, PointND) and isinstance(other, PointND):
            if self.distanceFrom(origin) < other.distanceFrom(origin):
                return True

            return False

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self,other):
        return not self.__lt__(other) and not self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

# Inheriting the PointND Class
class Point3D(PointND):

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        point3D = x,y,z
        PointND.__init__(point3D)

class PointGroup:

    def __init__(self, **kwargs):

        self._pointMap = {}
        self.n = 0

        if not kwargs:
            self._pointMap = {}
            self.n = 0

        elif "pointList" not in kwargs:
            raise KeyError("'pointList' input parameter not found.")

        elif len(kwargs["pointList"]) == 0:
            raise ValueError("'pointList' input parameter cannot be empty")

        else:
            # Adding all the PointNDs in 'pointList' to the PointGroup's _pointMap
            for val in kwargs["pointList"]:
                self.addPoint(val)

    def addPoint(self, point):

        if isinstance(point,PointND):

            # Adding the first PointND to the PointGroup
            if self.n == 0:
                self.n = point.n
                self._pointMap[hash(point)] = point  # Adding the point to the _pointMap

            # When Cardinality Matches add the pointND to PointGroup Map _pointMap
            elif(point.n == self.n):
                self._pointMap[hash(point)] = point
            else:
                raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(point,self.n))

    def count(self):
        return len(self._pointMap.keys())

    def computeBoundingHyperCube(self):

        minX = 0
        minY = 0
        minZ = 0
        maxX = 0
        maxY = 0
        maxZ = 0


        for pointND in self._pointMap.values():

            if(minX > pointND.t[0]): # With an Assumption that X-Co-Ordinate is at 0 index and viceversa
                minX = pointND.t[0]

            if(minY > pointND.t[1]): # With an Assumption that Y-Co-Ordinate is at 1 index and viceversa
                minY = pointND.t[1]

            if(minZ > pointND.t[2]): # With an Assumption that Z-Co-Ordinate is at 2 index and viceversa
                minZ = pointND.t[2]

            if(maxX < pointND.t[0]): # With an Assumption that X-Co-Ordinate is at 0 index and viceversa
                maxX = pointND.t[0]

            if(maxY < pointND.t[1]): # With an Assumption that Y-Co-Ordinate is at 1 index and viceversa
                maxY = pointND.t[1]

            if(maxZ > pointND.t[2]): # With an Assumption that Z-Co-Ordinate is at 2 index and viceversa
                maxZ = pointND.t[2]

            minPointND = minX,minY,minZ
            maxPointND = maxX,maxY,maxZ

            return (minPointND,maxPointND)

    def __iter__(self):
        return iter(self._pointMap.values())

    def computeNearestNeighbors(self, otherPointGroup):

        list_near = []

        for point in self._pointMap.values():
            iter_otherPG = iter(otherPointGroup)
            min_distance = 1000000000000
            min_point = None

            while True:
                try:
                    point_1 = next(iter_otherPG) # Iterating all the keys in otherPointGroup
                    distance = point.distanceFrom(point_1)

                    if(distance < min_distance):
                        min_distance = distance
                        min_point = point_1

                except StopIteration:
                    break

            list_near.append((point.t,min_point.t))

        return (list_near)

    def __add__(self, other):

        if isinstance(other,PointND):
            self.addPoint(other)

        return self

    def __sub__(self, other):

        if isinstance(other, PointND):

            if hash(other) not in self._pointMap:
                return self

            else:
                self._pointMap.pop(hash(other))
                return self

    def __contains__(self, item):
        return hash(item) in self._pointMap


def main():

    point = (1.00,2.00,3.00)

    point1 = (21.00,22.00,23.00)
    point2 = (5.00,6.00,7.00)
    point3 = (9.10,10.20,11.30)
    point4 = (13.00,14.50,15.00)
    point5 = (17.25,18.35,19.45)

    point_nd = PointND(point)
    point_nd_copy = point_nd.clone()

    pointND_1 = PointND(point1)
    pointND_2 = PointND(point2)
    pointND_3 = PointND(point3)
    pointND_4 = PointND(point4)
    pointND_5 = PointND(point5)

    print("Nearest point to "+ str(point_nd) + " is " + str(point_nd.nearestPoint([pointND_1,pointND_2,pointND_3,pointND_4,pointND_5])))

    # Addition
    print(pointND_1 + pointND_2)
    print(pointND_1 + 2.0)

    # Subtraction
    print(pointND_1 - pointND_2)
    print(pointND_1 - 2.0)

    # Multiplication
    print(pointND_1 * 2.0)

    # Division
    print(pointND_1 / 2.0)

    # Negation
    print(-pointND_1)

    # Indexing
    print(pointND_1[2])

    print("\n")

    # Comparison
    print("gt comparison")
    print(pointND_2 > pointND_3)
    print(pointND_1 > point_nd)
    print("\n")

    print("gte comparison")
    print(pointND_1 >= pointND_2)
    print(pointND_1 >= pointND_1)
    print("\n")

    print("lt comparison")
    print(pointND_1 < pointND_2)
    print(pointND_1 < point_nd)
    print("\n")

    print("lte comparison")
    print(pointND_1 <= pointND_2)
    print(pointND_1 <= pointND_1)
    print("\n")


    # Original pointND_1
    print("\n\nOriginal: " + str(pointND_1))


    # PointGroup

    faulty = PointND((1.0,2.0,3.0,4.0,5.0))

    pointList_vals = [pointND_1,pointND_2,pointND_3,pointND_4,pointND_5]
    pointGroup = PointGroup(pointList=pointList_vals)
    pointGroup_1 = PointGroup(pointList=pointList_vals)

    print(pointGroup.computeNearestNeighbors(pointGroup_1))

    print(pointGroup.computeBoundingHyperCube())

    pointGroup + PointND((1000.0,2000.0,3000.0))
    print(PointND((1000.0,2000.0,3000.0)) in pointGroup)
    pointGroup - PointND((1000.0,2000.0,3000.0))
    print(PointND((1000.0,2000.0,3000.0)) in pointGroup)

if __name__ == "__main__":
    main()
