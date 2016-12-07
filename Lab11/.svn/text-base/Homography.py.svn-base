from enum import Enum
import numpy as np
import scipy as sp
from pyparsing import col
from scipy import interpolate
import copy

import os
from os.path import join
from glob import glob
import unittest
from random import uniform
from inspect import isclass
from enum import Enum
from scipy.misc import *
import numpy as np
from Homography import *

testFolder = "TestImages"

class Effect(Enum):
    rotate90 = 90
    rotate180 = 180
    rotate270 = 270
    flipHorizontally = 1
    flipVertically = 2
    transpose = 3

class Homography:

    forwardMatrix = np.zeros((3,3),dtype=np.float64)
    inverseMatrix = np.zeros((3,3),dtype=np.float64)

    def __init__(self, **kwargs):

        memberOptions = kwargs.keys()

        if "homographyMatrix" in memberOptions:

            homographyMatrix = kwargs.get("homographyMatrix")

            if "sourcePoints" in memberOptions or "targetPoints" in memberOptions or "effect" in memberOptions:
                raise ValueError("kwargs cannot contain 'sourcePoints' or 'targetPoints' or 'effect' when 'homographyMatrix' is present")

            # Checking for the Datatype
            if not isinstance(homographyMatrix,np.ndarray):
                raise ValueError("'homographyMatrix' should be of type numpy Array")

            # Checking for the Dimensions of np.array
            if not homographyMatrix.shape == (3,3):
                raise ValueError("'homographyMatrix' dimensions should be 3 x 3 ")

            # Checking for DataType of np.array
            if not homographyMatrix.dtype == np.dtype('float64'):
                raise ValueError("Data type of 'homographyMatrix' should be 'float64'")

            self.forwardMatrix = homographyMatrix
            self.inverseMatrix = np.linalg.inv(homographyMatrix)

        elif "sourcePoints" not in memberOptions:
            raise ValueError("Expected 'sourcePoints' matrix, but not available")

        elif "targetPoints" not in memberOptions:
            raise ValueError("Expected 'targetPoints' matrix, but not available")

        else: # make this elif later on

            sourcePoints = kwargs.get("sourcePoints")
            targetPoints = kwargs.get("targetPoints")

            # Checking the Datatype of Source and TargetPoints
            if not isinstance(sourcePoints,np.ndarray) and not isinstance(targetPoints,np.ndarray):
                raise ValueError("'sourcePoints' and 'targetPoints' have to of type np.array")

            if "effect" in memberOptions:
                if kwargs.get("effect") != None and not isinstance(kwargs.get("effect"),Effect):
                    raise TypeError("Datatype of 'effect' has to be 'enum.Enum'")

            # Dimension Check
            if  sourcePoints.shape != (4,2) or targetPoints.shape != (4,2):
                raise ValueError("Dimensions of 'sourcePoints' and 'targetPoints' have to (4,2)")

            # DataType of ndArray check
            if not sourcePoints.dtype == np.dtype('float64') and not targetPoints.dtype == np.dtype('float64'):
                raise TypeError("The DataType of 'sourcePoints' and 'targetPoints' should be np.dtype('float64')")

            if "effect" not in memberOptions:
                self.computeHomography(sourcePoints=sourcePoints,targetPoints=targetPoints)
            else:
                self.computeHomography(sourcePoints=sourcePoints,targetPoints=targetPoints,effect=kwargs.get("effect"))

    def computeHomography(self, sourcePoints, targetPoints,effect=None):

        VStack = list()
        VStack2 = list()

        if(effect != None):

            if(effect == Effect.rotate90):
                sourcePoints = np.array([sourcePoints[2], sourcePoints[0], sourcePoints[3], sourcePoints[1]])

            elif(effect == Effect.rotate180):
                sourcePoints = np.array([sourcePoints[3], sourcePoints[2], sourcePoints[1], sourcePoints[0]])

            elif(effect == Effect.rotate270):
                sourcePoints = np.array([sourcePoints[1], sourcePoints[3], sourcePoints[0], sourcePoints[2]])

            elif(effect == Effect.flipHorizontally):
                sourcePoints = np.array([sourcePoints[2], sourcePoints[3], sourcePoints[0], sourcePoints[1]])

            elif(effect == Effect.flipVertically):
                sourcePoints = np.array([sourcePoints[1], sourcePoints[0], sourcePoints[3], sourcePoints[2]])

            elif(effect == Effect.transpose):
                sourcePoints = np.array([sourcePoints[0], sourcePoints[2], sourcePoints[1], sourcePoints[3]])

        for val in range(0, sourcePoints.shape[0]):
            newArray = np.array([[sourcePoints[val][0],sourcePoints[val][1],1,0,0,0,-1*targetPoints[val][0]*sourcePoints[val][0],-1*targetPoints[val][0]*sourcePoints[val][1]],[0,0,0,sourcePoints[val][0],sourcePoints[val][1],1,-1*targetPoints[val][1]*sourcePoints[val][0],-1*targetPoints[val][1]*sourcePoints[val][1]]],dtype=np.float64)
            VStack2.append(targetPoints[val][0])
            VStack2.append(targetPoints[val][1])
            VStack.append(newArray)

        VStack = np.vstack(tuple(VStack))
        VStack2 = np.hstack(tuple(VStack2))

        self.forwardMatrix = np.linalg.solve(VStack,VStack2)
        self.forwardMatrix = np.append(self.forwardMatrix,1)
        self.forwardMatrix = np.array(self.forwardMatrix,dtype=np.float64).reshape((3,3))
        self.inverseMatrix = np.linalg.inv(self.forwardMatrix)

def rotate90(sourcePoints, no_rotations):

    print(sourcePoints)

    for val in range(0,no_rotations):
        row1 = copy.deepcopy(sourcePoints[3])
        sourcePoints[3] = sourcePoints[2]
        sourcePoints[2] = sourcePoints[1]
        sourcePoints[1] = sourcePoints[0]
        sourcePoints[0] = row1

    print(sourcePoints)

    return sourcePoints

class Transformation:

    def __init__(self, sourceImage, homography=None):

        if not isinstance(sourceImage,np.ndarray):
            raise TypeError("'sourceImage' should be of type <numpy.ndarray>")

        self.sourceImage = sourceImage

        if homography is not None and not isinstance(homography,Homography):
            raise TypeError("'homography' should be of type <Homography>")

        self.homography = homography # homography is an instance of Class 'Homography'

    def setupTransformation(self, targetPoints, effect=None):

        # Computing Homography when not instantiated
        if self.homography is None:
            # Getting the new SourcePoints bounds
            sourcePoints = np.array([[0,0],[self.sourceImage.shape[1] - 1, 0],[0, self.sourceImage.shape[0] - 1],[self.sourceImage.shape[1] -1, self.sourceImage.shape[0] - 1]],dtype=np.float64)
            self.homography = Homography(sourcePoints=sourcePoints,targetPoints=targetPoints,effect=effect)

        # calculating the Target Bounding Box
        XCoOrds, YCoOrds = zip(targetPoints[0], targetPoints[1], targetPoints[2], targetPoints[3])
        self.minX = min(XCoOrds)
        self.minY = min(YCoOrds)
        self.maxX = max(XCoOrds)
        self.maxY = max(YCoOrds)

    def transformImageOnto(self, containerImage):

        if not isinstance(containerImage, np.ndarray):
            raise TypeError("'containerImage' is Invalid should be of type <numpy.ndarray>")

        # Using RectBiVariateSpline will allows us get the 2D Interpolation which is used in the second Step
        # kx = 1 and ky = 1 are the degrees of interpolation polynomial.
        twoDim_Interpolation = sp.interpolate.RectBivariateSpline(np.arange(0, self.sourceImage.shape[0], 1),
                                                                  np.arange(0, self.sourceImage.shape[1], 1),
                                                                  self.sourceImage, kx=1, ky=1)

        rows = np.arange(self.minX, self.maxX + 1, 1, dtype=np.uint16)
        columns = np.arange(self.minY, self.maxY + 1, 1, dtype=np.uint16)

        for row in rows:
            for col in columns:
                # Step 2: Performing the Inverse projection of Co-Ordinates using inverseMatrix
                dotProduct = np.dot(self.homography.inverseMatrix, np.array([[row],[col],[1]],dtype=np.float64))
                twoDimMatrix = np.array([[dotProduct[0,0] / dotProduct[2,0]], [dotProduct[1,0] / dotProduct[2,0]], [1]])
                twoDimMatrix = np.round(twoDimMatrix, 3)

                # Step 3: Checking if the result is within the bounds of the Source Image
                if (twoDimMatrix[0,0] >= 0 and twoDimMatrix[0,0] <= self.sourceImage.shape[1] - 1) and (twoDimMatrix[1,0] >= 0 and twoDimMatrix[1,0] <= self.sourceImage.shape[0] - 1):

                    # Step 4
                    pixelVal = np.round(twoDim_Interpolation(twoDimMatrix[1,0], twoDimMatrix[0,0]))
                    containerImage[col,row] = pixelVal

        return containerImage

class ColorTransformation(Transformation):

    def __init__(self, sourceImage, homography=None):
        Transformation.__init__(self, sourceImage, homography)

        # Dimension Check
        if len(sourceImage.shape) is not 3:
            raise ValueError("'sourceImage' shape should be as follow [x,y,z]")

    def transformImageOnto(self, containerImage):

        if not isinstance(containerImage, np.ndarray):
            raise TypeError("'containerImage' is Invalid should be of type <numpy.ndarray>")

        redValues = self.sourceImage[:,:,0]
        greenValues = self.sourceImage[:,:,1]
        blueValues = self.sourceImage[:,:,2]

        colors = [redValues, greenValues, blueValues]

        colorIndex = 0

        for color in colors:

            twoDim_Interpolation = sp.interpolate.RectBivariateSpline(np.arange(0, color.shape[0], 1),
                                                                      np.arange(0, color.shape[1], 1),
                                                                      color, kx=1, ky=1)

            rows = np.arange(self.minX, self.maxX + 1, 1)
            columns = np.arange(self.minY, self.maxY + 1, 1)

            for row in rows:
                for col in columns:
                    # Step 2: Performing the Inverse projection of Co-Ordinates using inverseMatrix
                    dotProduct = np.dot(self.homography.inverseMatrix, np.array([[row],[col],[1]], dtype=np.float64))
                    twoDimMatrix = np.array([[dotProduct[0,0] / dotProduct[2,0]], [dotProduct[1,0] / dotProduct[2,0]], [1]])
                    twoDimMatrix = np.round(twoDimMatrix, 3)

                    # Step 3: Checking if the result is within the bounds of the Source Image
                    if (twoDimMatrix[0,0] >= 0 and twoDimMatrix[0,0] <= self.sourceImage.shape[1] - 1) and (twoDimMatrix[1,0] >= 0 and twoDimMatrix[1,0] <= self.sourceImage.shape[0] - 1):

                        # Step 4
                        pixelVal = np.round(twoDim_Interpolation(twoDimMatrix[1,0], twoDimMatrix[0,0]))
                        containerImage[col,row, colorIndex] = pixelVal

            colorIndex += 1

        return containerImage

def main():

    #sourcePoints = np.array([[0, 0], [1919, 0], [0, 1079], [1919,  1079.0]])
    targetPoints = np.array([[600, 50], [1550, 500], [50, 400], [800, 1150.0]])

    sourceImage = imread(join(testFolder, "knight.png"))

    '''transform = Transformation(sourceImage)
    transform.setupTransformation(targetPoints)

    containerImage = imread(join(testFolder, "WhiteGray.png"))
    actualValue = transform.transformImageOnto(containerImage)
    expectedValue = imread(join(testFolder, "Target_knight.png"))

    imsave('test.png',actualValue) '''

    transform = Transformation(sourceImage)
    transform.setupTransformation(targetPoints, Effect.rotate180)

    containerImage = imread(join(testFolder, "WhiteGray.png"))
    actualValue = transform.transformImageOnto(containerImage)
    expectedValue = imread(join(testFolder, "Target_knight_{}.png".format("rotate180")))

    print(actualValue)
    print(expectedValue)


'''    diff = np.absolute(expectedValue, actualValue)
    #print(diff)
    bool_diff = np.logical_and(diff, np.ones(expectedValue.shape, dtype=np.uint8))
    diffImage = 255 * bool_diff
    imsave('test_diff.png',diffImage)
'''

if __name__ == '__main__':
    main()