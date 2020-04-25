import cv2
import math
import numpy as np


class Filter:
    """
    The Filter class describes the construction, members, and functions of the 2d gaussian convolution filter
    vars: self.elements - 2d list containing the values of the filter
    functions:
    __init__(size,sigma)
    displayFilter()
    applyFilter(image)
    """

    def __init__(self,size,sigma):
        """

        :param size: The desired window size of the filter Ex. 5 would result in a 5x5 window
        NOTE: Size must be an odd positive integer
        :param sigma: The variance of the gaussian distribution
        """
        self.size = size
        self.sigma = sigma
        self.elements = [[0] * size for i in range(size)]

        for i in range(self.size):
            for j in range(self.size):
                self.y = i - self.size//2
                self.x = j - self.size//2
                self.elements[i][j] = (1/(2*np.pi*np.power(self.sigma,2))) * np.power((math.e),(-1*((self.x**2 + self.y**2)/(2*(self.sigma**2)))))
        topLeft = self.elements[0][0]
        print(topLeft)
        for i in range(self.size):
            for j in range(self.size):

                self.elements[i][j] *= (1/topLeft)


    def displayFilter(self):
        """
        Displays the filter matrix in an easy to read string format
        :return: null
        """
        for i in range(self.size):
            res = ""
            for j in range(self.size):
                res += str(self.elements[i][j]) + " "

            print(res)

    def applyFilter(self,image):
        """
        Applies the gaussian filter to the image
        :param image: 2d list containing grey scale image values.
        :return:
        """
        filteredImage = np.zeros((image.shape[0],image.shape[1]),np.float32)
        for i in range((self.size//2),image.shape[0]-((self.size//2)+1)):
            for j in range((self.size//2),image.shape[1]-((self.size//2)+1)):
                sumproduct = 0
                filtersum = 0
                for a in range(-self.size//2,self.size//2+1):
                    for b in range(-self.size//2,self.size//2+1):
                        sumproduct += self.elements[self.size//2 + a][self.size//2 + b]*image[i+a][j+b]
                        filtersum += self.elements[self.size//2 + a][self.size//2 + b]
                filteredImage[i][j] = int(sumproduct/filtersum)


        return filteredImage




def main():
    testImage = cv2.imread("dale.jpg")
    testG = cv2.cvtColor(testImage,cv2.COLOR_BGR2GRAY)

    convo = Filter(5,5)
    convo2 = Filter(5,.5)
    convo3 = Filter(5, .1)

    convo.displayFilter()

    finalIm = convo.applyFilter(testG)
    finalIm2 = convo2.applyFilter(testG)
    finalIm3 = convo3.applyFilter(testG)
    cv2.imshow("first", testG)
    cv2.imshow("s5/sigma 5", finalIm / 255)
    cv2.imshow("s5/sigma .5", finalIm2 / 255)
    cv2.imshow("s5/sigma .1", finalIm3 / 255)
    cv2.waitKey()

    cv2.waitKey()

    cv2.waitKey()




if __name__ == "__main__":
    main()