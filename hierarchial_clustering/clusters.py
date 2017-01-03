#!/usr/bin/env python 
from algorithms.kmean import KmeanSolver
from utils.visualization import ClusterPlot
from utils.data_generator import randomClusters

k = 5

points = randomClusters(10)
pl = ClusterPlot()
pl.plotPoints(points)

solver = KmeanSolver(points, k)
solver.solve()

pl.plot(solver)

#pl.plotDendo(points)