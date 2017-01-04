from utils.cluster import Cluster
from utils.distances import *
import random
from sys import maxint

class KmeanSolver():
    def __init__(self, data, k, dfunc=None):
        self._points = data
        self._k = k
        self._clusters = []
        if dfunc == None:
            self._df = euclidianDistance
        else:
            self._df = dfunc

    def randPoints(self):
        indexes = len(self._points)
        points = [self._points[random.randint(0,indexes-1)]]
        maxdist = maxint

        while len(points) < self._k:
            maxp = self._points[random.randint(0,indexes-1)]
            dist = 0
            for point in self._points:
                for p in points:
                    dist += self._df(point,p)
                if dist<maxdist:
                    maxp = point
                    maxdist = dist

            points.append(maxp)
        return points

    def getClusters(self):
        return self._clusters

    def findMinimalCluster(self, point):
        minimal = (maxint, None)
        for cluster in self._clusters:
            dist = self._df(cluster.getCentroid(), point)
            if dist < minimal[0]:
                minimal = (dist, cluster)
        return minimal

    def solve(self):
        #todo dynamically choose k
        #Initialize the random clusters
        self._clusters = [Cluster([point],point) for point in self.randPoints()]
        #todo find a dynamic stop threshold
        for i in range(1,20):

            for cluster in self._clusters:
                cluster.calcCentroid()
                cluster.clear()

            for point in self._points:
                distance, cluster = self.findMinimalCluster(point)
                cluster.addPoint(point)
