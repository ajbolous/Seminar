import matplotlib.pyplot as plot
from matplotlib.patches import Ellipse
from itertools import cycle
from distances import calculateEllipse
from matplotlib.colors import cnames

class ClusterPlot():
    def __init__(self, dim):
        print cnames
        self._colors = cycle(cnames)
        self.fig = plot.figure(0)
        self.dim = dim
        if dim > 2:
            self.ax = self.fig.add_subplot(111, aspect='equal', projection='3d')
        else:
            self.ax = self.fig.add_subplot(111, aspect='equal')


    def plotCluster(self, cluster):
        color = self._colors.next()

        if self.dim > 2:
            self.plotPoints3d(cluster.getPoints(), color)
        else:
            self.plotPoints2d(cluster.getPoints(), color)
            self.plotEllipse(cluster, color)


    def plotPoints2d(self, points, color):
        x, y = [], []
        for point in points:
            x.append(point[0])
            y.append(point[1])
        plot.scatter(x, y, color=color)


    def plotPoints3d(self, points, color):
        x, y, z = [], [], []
        for point in points:
            x.append(point[0])
            y.append(point[1])
            if len(point)>2:
                z.append(point[2])
            else:
                z.append(0)
        self.ax.scatter(x, y,z, color = color)

    def plotEllipse(self, cluster, color):
        ellipse = calculateEllipse(cluster.getPoints(), cluster.getCentroid())
        print(ellipse)
        el = Ellipse(xy=ellipse[0], width=ellipse[1]*2, height=ellipse[2]*2, angle= ellipse[3], color=color)
        el.set_alpha(0.25)
        self.ax.add_artist(el)

    def clear(self):
        plot.clf()

    def showPlot(self):
        plot.show()
