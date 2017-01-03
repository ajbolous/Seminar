#!/usr/bin/env python 
from algorithms.kmean import KmeanSolver
from utils.visualization import ClusterPlot
from utils.data_generator import randomChars
from utils.distances import manhattanDistance
k = 5

points = randomChars(25)
pl = ClusterPlot()
pl.plotPoints(points)

solver = KmeanSolver(points, k, manhattanDistance)
solver.solve()

pl.plot(solver)
pl.plotDendo(points, [str(unichr(point[0])) for point in points])