#!/usr/bin/env python 
from algorithms.kmean import KmeanSolver
from utils.visualization import ClusterPlot
from utils.data_generator import randomData, getArgs
from algorithms.elbow_method import findBestK

args = getArgs()

points = randomData(args.size,50,args.dim)

from algorithms.elbow_method import findBestK

if not args.k:
    args.k = findBestK(points,10)

solver = KmeanSolver(points, args.k)
solver.solve()

pl = ClusterPlot()
pl.plot(points, solver, proj='3d' if args.d3 else None)

if args.dendo:
    pl.plotDendo(points)