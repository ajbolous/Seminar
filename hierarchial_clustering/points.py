#!/usr/bin/env python 
from algorithms.kmean import KmeanSolver
from utils.visualization import ClusterPlot
from utils.data_generator import randomData

k = 3

points = randomData(100,100,3)
pl = ClusterPlot()
pl.plotPoints(points,'3d')

solver = KmeanSolver(points, k)
solver.solve()

pl.plot(solver,'3d')

#pl.plotDendo(points)