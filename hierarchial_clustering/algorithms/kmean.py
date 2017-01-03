from utils.cluster import Cluster
from utils.distances import *
import random
from sys import maxsize

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
        points = []
        indexes = len(self._points)
        for i in range(self._k):
            points.append(self._points[random.randint(0,indexes-1)])
        return points

    def getClusters(self):
        return self._clusters

    def findMinimalCluster(self, point):
        minimal = (maxsize,None)
        for cluster in self._clusters:
            dist = self._df(cluster.getCentroid(), point)
            if dist < minimal[0]:
                minimal = (dist, cluster)
        return minimal

    def solve(self):
        #Initialize the random clusters
        self._clusters = [Cluster([point],point) for point in self.randPoints()]

        for i in range(1,50):

            for cluster in self._clusters:
                cluster.calcCentroid()
                cluster.clear()

            for point in self._points:
                distance, cluster = self.findMinimalCluster(point)
                cluster.addPoint(point)
