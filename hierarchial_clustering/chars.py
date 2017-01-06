#!/usr/bin/env python 
from algorithms.kmean import KmeanSolver
from utils.visualization import ClusterPlot
from utils.data_generator import randomChars, getArgs
from utils.distances import manhattanDistance

args = getArgs()

points = randomChars(args.size)
pl = ClusterPlot()

from algorithms.elbow_method import findBestK

if not args.k:
    args.k = findBestK(points,10)

solver = KmeanSolver(points, args.k, manhattanDistance)
solver.solve()
pl.plot(points, solver, labels=[str(unichr(point[0])) for point in points], proj='3d' if args.d3 else None )

if args.dendo:
    pl.plotDendo(points, [str(unichr(point[0])) for point in points])