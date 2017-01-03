import matplotlib.pyplot as plot
from matplotlib.patches import Ellipse
from itertools import cycle
from utils.distances import calculateEllipse
from matplotlib.colors import cnames
from scipy.cluster.hierarchy import dendrogram,linkage
from mpl_toolkits.mplot3d import axes3d, Axes3D

class ClusterPlot():
    def __init__(self):
        self._colors = cycle(cnames)

    def plot(self, solver, proj=None):
        print proj
        self.fig = plot.figure(0)
        self.ax = self.fig.add_subplot(111, aspect='equal', projection=proj)
        for cluster in solver.getClusters():
            self.plotCluster(cluster, proj)
        self.showPlot()

    def plotDendo(self, points, labels=None):
        Z = linkage(points)
        plot.figure(figsize=(25, 10))
        plot.title('Hierarchical Clustering Dendrogram')
        plot.xlabel('sample index')
        plot.ylabel('distance')
        dendrogram(
            Z,
            leaf_rotation=90.,  # rotates the x axis labels
            leaf_font_size=8.,  # font size for the x axis labels
            labels=labels
        )
        plot.show()


    def plotPoints(self, points,proj=None):
        self.fig = plot.figure(0)
        self.ax = self.fig.add_subplot(111, aspect='equal', projection=proj)
        if proj == '3d':
            self.plotPoints3d(points,'black')
        else:
            self.plotPoints2d(points,'black')

        self.showPlot()

    def plotCluster(self, cluster, proj):
        color = self._colors.next()

        if proj == '3d':
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
            z.append(point[2])
        self.ax.scatter(x, y,z, color = color)

    def plotEllipse(self, cluster, color):
        ellipse = calculateEllipse(cluster.getPoints(), cluster.getCentroid())
        el = Ellipse(xy=ellipse[0], width=ellipse[1]*2, height=ellipse[2]*2, angle= ellipse[3], color=color)
        el.set_alpha(0.25)
        self.ax.add_artist(el)

    def clear(self):
        plot.clf()

    def showPlot(self):
        plot.show()
