#!/usr/bin/env python 
from algorithms.kmean import KmeanSolver
import random
from utils.visualization import ClusterPlot


points = []
for i in  range(1,115):
    points.append([random.randrange(1,2222), random.randrange(1,2222)])

solver = KmeanSolver(points,10)
solver.solve()

pl = ClusterPlot(2)
pl.plot(solver)

