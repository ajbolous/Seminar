#!/usr/bin/env python 
from algorithms.kmean import KmeanSolver
from utils.visualization import ClusterPlot
from utils.data_generator import generateWordVectors
from utils.distances import manhattanDistance
k = 5

words = ['word','work','ward','good','golf','bad','ace','hello','was','apple','ate','meet','war','jello','bat','hat','rat']
points = generateWordVectors(words,5)
pl = ClusterPlot()
pl.plotPoints(points)

solver = KmeanSolver(points, k, manhattanDistance)
solver.solve()
pl.plot(solver)

print(solver.getClusters())

pl.plotDendo(points, words)