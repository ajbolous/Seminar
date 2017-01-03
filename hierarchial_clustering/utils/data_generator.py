import numpy as np
import random

def getArgs():
    import argparse
    parser = argparse.ArgumentParser(description='Cluster data using KMeans and dendogram')
    parser.add_argument('--k', metavar='K', default=3, type=int, help='The number of clusters to produce')
    parser.add_argument('--dim', metavar='D', default=2, type=int, help='the dimension of the data')
    parser.add_argument('--size', metavar='N', default=100, type=int, help='the size of the data')
    parser.add_argument('--dendo',action='store_true', help='show dendograph')
    parser.add_argument('--d3',action='store_true', help='show dendograph')

    args = parser.parse_args()
    return args


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

def randomClusters(k,size):
    np.random.seed(0)  # for repeatability of this tutorial
    points = []
    for i in range(k):
        arr = np.random.multivariate_normal([random.randint(1, 45),random.randint(1, 45)], [[4, 1], [1, 4]], size=[size, ])
        [points.append(point) for point in arr]

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
    n = min(66,n)
    print n
    points = []
    done = {}
    for i in range(0,n):
        letter = ord('0') + random.randint(0, n)
        if letter in done:
            continue
        done[letter] = True
        point = [letter,letter]
        points.append(point)
    return points