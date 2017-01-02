import math
from algorithms.kmeans import KmeansSolver
import random

points = []
for i in  range(1,2222):
    points.append([random.randrange(1,2222), random.randrange(1,2222)])

solver = KmeansSolver(points,15)
solver.solve()

from utils.visualization import ClusterPlot

pl = ClusterPlot(2)

for cluster in solver.getClusters():
    pl.plotCluster(cluster)

pl.showPlot()
