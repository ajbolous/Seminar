import numpy as np
import random


def generateWordVectors(words,dim):
    points = []
    for w in words:
        point = []
        for i in range(dim):
            if i < len(w):
                point.append(ord(w[i]))
            else:
                point.append(0)
        points.append(point)
    return points


def randomClusters(k):
    np.random.seed(4711)  # for repeatability of this tutorial
    points = []
    for i in range(k):
        arr = np.random.multivariate_normal([10 * random.randint(1, 3),random.randint(1, 15)], [[3, 1], [1, 4]], size=[50, ])
        [points.append(point) for point in arr]
        arrb = np.random.multivariate_normal([random.randint(1, 15), 20 * random.randint(1, 3)], [[3, 1], [1, 4]], size=[50, ])
        [points.append(point) for point in arrb]

    return points

def randomData(n, rang, dim):
    points = []
    for i in range(1,n):
        point = []
        for i in range(dim):
            point.append(random.randint(1,rang))
        points.append(point)
    return points


def randomChars(n):
    points = []
    for i in range(0,n):
        letter = ord('a') + random.randint(0, n)
        point = [letter,letter]
        points.append(point)
    return points