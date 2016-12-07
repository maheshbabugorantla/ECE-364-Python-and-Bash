from prelab08addon import performProcessing
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

def createPoint(dataString):
	datas = dataString.split(",")

	try:
		datas = [float(data) for data in datas]

	except:
		return("Input string should contain only a string of all floats")

	return PointND(tuple(datas))

def distanceBetween(point1, point2):

	try:
		return round(point1.distanceFrom(point2),2)

	except:
		return ("Unable to compute the distance between point1 and point2")

def checkVicinity(point, pointList, radius):

	inradius = 0
	outRadius = 0
	falseComputation = 0

	assert isinstance(point,PointND), "'point' should be of type 'PointND'"

	for point_val in pointList:
		assert isinstance(point_val, PointND), "Each item in the 'pointList' should be of type 'PointND'"

	assert type(radius) is float, "'radius' should be a 'float'"

	for point_val in pointList:

		if type(distanceBetween(point,point_val)) is str:
			falseComputation += 1
		else:
			if(distanceBetween(point,point_val) <= radius):
				inradius += 1

			else:
				outRadius += 1


	assert sum([inradius,outRadius,falseComputation]) == len(pointList), "Make sure 'inRadius' + 'outRadius' + 'falseCardinality' is equal to the length of 'pointList'"

	return (inradius,outRadius,falseComputation)


def checkOperation(*args):

	try:
		performProcessing(*args)

	except BlockingIOError:
		return "The Following Error occurred: BlockingIOError"

	except ChildProcessError:
		return "The Following Error occurred: ChildProcessError"

	except BrokenPipeError:
		return "The Following Error occurred: BrokenPipeError"

	except ConnectionAbortedError:
		return "The Following Error occurred: ConnectionAbortedError"

	except ConnectionRefusedError:
		raise ConnectionRefusedError

	except ConnectionResetError:
		return "The Following Error occurred: ConnectionResetError"

	except ConnectionError:
		return "The Following Error occurred: ConnectionError"

	except FileExistsError:
		return "The Following Error occurred: FileExistsError"

	except FileNotFoundError:
		return "The Following Error occurred: FileNotFoundError"

	except InterruptedError:
		return "The Following Error occurred: InterruptedError"

	except IsADirectoryError:
		return "The Following Error occurred: IsADirectoryError"

	except NotADirectoryError:
		return "The Following Error occurred: NotADirectoryError"

	except PermissionError:
		return "The Following Error occurred: PermissionError"

	except ProcessLookupError:
		return "The Following Error occurred: ProcessLookupError"

	except TimeoutError:
		return "The Following Error occurred: TimeoutError"

	except Exception:
		return False

	return True

def main():

	'''	print(createPoint("3.14,2.701,19.77"))
	print(createPoint("4.98,3FA2,None"))
	'''

	point = createPoint("3.14,2.701,19.77")
	point1 = createPoint("3.14,2.701,19.77")
	point2 = createPoint("6.28,5.402,39.54")
	point4 = createPoint("9.52,8.103,59.31")
	point5 = createPoint("9.52,8.103,59.31,12.34")
	point3 = createPoint("4.98,3FA2,None")

	pointList = [point1,point2,point4,point5]

	print("Distance between " + str(point1) + " and " + str(point2) + " is {0:2.2f}".format(distanceBetween(point1,point2)))

	print(checkVicinity(point,pointList,2.0))

	return

if __name__=='__main__':
	main()
