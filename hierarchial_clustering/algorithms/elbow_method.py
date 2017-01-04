from algorithms.kmean import KmeanSolver
from math import fabs
def findBestK(points, maxk):

    histo = []
    lastError = 0
    bestk = maxk
    for i in range(1,maxk,2):
        solver = KmeanSolver(points,i)
        solver.solve()
        error = 0
        for cluster in solver.getClusters():
            if len(cluster.getPoints())== 0:
                continue
            error += cluster.getSse() / len(cluster.getPoints())
        histo.append([i, error])

        diff = fabs(lastError - error)

        if diff < 0.05:
            bestk = i
            break

        lastError = error

    from utils.visualization import ClusterPlot

    pl = ClusterPlot()

    pl.plotPoints(histo)
    print("Choose best k as :{}".format(bestk))
    return bestk


