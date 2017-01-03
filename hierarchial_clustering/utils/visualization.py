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

    def plot(self,points, solver, proj=None, labels=None):
        fig = plot.figure(0)

        ax = plot.subplot(121, aspect='equal', projection=proj)

        if proj == '3d':
            self.plotPoints3d(points,'black',ax, labels)
        else:
            self.plotPoints2d(points,'black',ax, labels)


        ax = plot.subplot(122, aspect='equal', projection=proj)
        for cluster in solver.getClusters():
            self.plotCluster(cluster, proj, ax, labels)

        self.showPlot()

    def plotDendo(self, points, labels=None):
        Z = linkage(points)
        plot.figure(figsize=(25, 10))
        plot.title('Hierarchical Clustering Dendrogram')
        plot.xlabel('sample index')
        plot.ylabel('distance')
        dendrogram(
            Z,
            leaf_rotation=90,  # rotates the x axis labels
            leaf_font_size=16,  # font size for the x axis labels
            labels=labels,
        )
        plot.show()


    def plotPoints(self, points,proj=None):
        fig = plot.figure(0)
        ax = fig.add_subplot(111, aspect='equal', projection=proj)
        if proj == '3d':
            self.plotPoints3d(points,'black', ax)
        else:
            self.plotPoints2d(points,'black', ax)

        self.showPlot()

    def plotCluster(self, cluster, proj, axis, labels=None):
        color = self._colors.next()

        if proj == '3d':
            self.plotPoints3d(cluster.getPoints(), color, axis, labels)
        else:
            self.plotPoints2d(cluster.getPoints(), color, axis, labels)
            self.plotEllipse(cluster, color, axis)


    def plotPoints2d(self, points, color, axis,labels=None):
        x, y = [], []
        i = 0

        for point in points:
            x.append(point[0])
            y.append(point[1])
            if labels:
                plot.annotate(labels[i],xy=point[0:2],xytext=point[0:2],fontsize=12)
            i+=1
        axis.scatter(x, y, color=color)


    def plotPoints3d(self, points, color, axis, labels=None):
        x, y, z = [], [], []
        i = 0
        for point in points:
            x.append(point[0])
            y.append(point[1])
            if len(point) > 2:
                z.append(point[2])
            else:
                z.append(0)
            if labels:
                plot.annotate(labels[i],xy=point[0:2],xytext=point[0:2],fontsize=12)
            i+=1
        axis.scatter(x, y,z, color = color)

    def plotEllipse(self, cluster, color, axis):
        ellipse = calculateEllipse(cluster.getPoints(), cluster.getCentroid())
        el = Ellipse(xy=ellipse[0], width=ellipse[1]*2, height=ellipse[2]*2, angle= ellipse[3], color=color)
        el.set_alpha(0.25)
        axis.add_artist(el)

    def clear(self):
        plot.clf()

    def showPlot(self):
        plot.show()
