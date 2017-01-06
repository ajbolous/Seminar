#!/usr/bin/env python 
from algorithms.kmean import KmeanSolver
from utils.visualization import ClusterPlot
from utils.data_generator import generateWordVectors, getArgs
from utils.distances import manhattanDistance

args = getArgs()

words = ['word','work','store','goal','bore','star','guitar','get','set',
	'more','sore','ward','good','golf','bad','ace','ban','ran','ham',
	'hello','was','apple','ate','meet','war','jello','bat','hat','rat']
points = generateWordVectors(words,5)

from algorithms.elbow_method import findBestK

if not args.k:
    args.k = findBestK(points,10)

solver = KmeanSolver(points, args.k, manhattanDistance)
solver.solve()

pl = ClusterPlot()
pl.plot(points, solver, labels=words, proj='3d' if args.d3 else None)

if args.dendo:
    pl.plotDendo(points, words)
