class Cluster():
    def __init__(self, points, centroid):
        self._points = points
        self._dim = len(points[0])
        self._N = len(points)
        self._centroid = centroid

    def calcCentroid(self):
        if self._N <=0:
            return None

        cent = [0] * self._dim

        for point in self._points:
            for i in range(self._dim):
                cent[i] += point[i]

        for i in range(self._dim):
            cent[i] /= self._N

        self._centroid = cent
        return cent

    def clear(self):
        self._N = 0
        self._points = []

    def getCentroid(self):
        return self._centroid

    def addPoint(self,point):
        self._points.append(point)
        self._N = len(self._points)

    def getPoints(self):
        return self._points

    def __repr__(self):
        return "<points:{} centroid:{}>".format(self._N, self._centroid)