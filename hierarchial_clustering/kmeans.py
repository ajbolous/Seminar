import math
import random
from sys import maxsize

def distFunc(v,u):
    s = 0
    for a,b in zip(v,u):
        s += math.pow(a-b,2)
    return math.sqrt(s)


class Cluster():
    def __init__(self, points, centroid):
        self._points = points
        self._dim = len(points[0])
        self._N = len(points)
        self._centroid = centroid

    def calcCentroid(self):
        if self._N <=0:
            return None

        cent = [0] * self._dim

        for point in self._points:
            for i in range(self._dim):
                cent[i] += point[i]

        for i in range(self._dim):
            cent[i] /= self._N

        self._centroid = cent
        return cent

    def clear(self):
        self._N = 0
        self._points = []

    def getCentroid(self):
        return self._centroid

    def getDiam(self):
        return max([distFunc(self._centroid, point) for point in self._points])

    def addPoint(self,point):
        self._points.append(point)
        self._N = len(self._points)

    def __repr__(self):
        return "<points:{} centroid:{}>".format(self._N, self._centroid)


class KmeansSolver():
    def __init__(self, data, k, dfunc=None):
        self._data = data
        self._k = k
        self._clusters = []
        if dfunc == None:
            self._df = distFunc
        else:
            self._df = dfunc

    def randPoints(self):
        points = []
        indexes = len(self._data)
        for i in range(self._k):
            points.append(self._data[random.randint(0,indexes)])
        return points

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

        for i in range(1,100):

            for cluster in self._clusters:
                cluster.calcCentroid()
                cluster.clear()

            for point in points:
                distance, cluster = self.findMinimalCluster(point)
                cluster.addPoint(point)

points = []
for i in  range(1,100):
    points.append([random.randrange(1,1000), random.randrange(1,1000)])


print (points)

solver = KmeansSolver(points,8)
solver.solve()






import matplotlib.pyplot as plot

colors = ['red','blue','black','green','yellow','magenta','purple','orange']
i= 0

fig = plot.figure(0)
ax = fig.add_subplot(111, aspect='equal')
from matplotlib.patches import Ellipse


for cluster in solver._clusters:
    plot.scatter([p[0] for p in cluster._points],[p[1] for p in cluster._points], color=colors[i])
    diam = cluster.getDiam()
    el = Ellipse(xy= cluster.getCentroid(), width= diam, height=diam, angle=0, color=colors[i])
    el.set_alpha(0.25)
    ax.add_artist(el)
    i+=1

plot.show()