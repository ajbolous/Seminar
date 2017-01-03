import math

def manhattanDistance(v,u):
    dist = 0
    for a,b in zip(v,u):
        dist += math.fabs(a-b)
    return dist

def euclidianDistance(v,u):
    s = 0
    for a,b in zip(v,u):
        s += math.pow(a-b,2)
    return math.sqrt(s)


def calculateEllipse(points, centroid):
    maxx = maxy = 0
    angle = 0
    for point in points:
        xdis = math.fabs(point[0] - centroid[0])
        ydis = math.fabs(point[1] - centroid[1])
        if  xdis > maxx:
            maxx = xdis
        if ydis > maxy:
            maxy = ydis

    return centroid, maxx,maxy, angle/math.pi * 180

