def orientation(p, q, r):
    """Find the orientation of the triplet (p, q, r)."""
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0 # collinear
    elif val > 0:
        return 1 # clockwise
    else:
        return 2 # counterclockwise

def convex_hull(points):
    """Find the convex hull of a set of points."""
    n = len(points)
    if n < 3:
        return points

    hull = []
    for i in range(n):
        for j in range(i+1, n):
            # check if (i, j) makes up an edge of the convex hull
            left = []
            right = []
            for k in range(n):
                if k != i and k != j:
                    if orientation(points[i], points[j], points[k]) == 2:
                        left.append(k)
                    else:
                        right.append(k)
            if not left or not right:
                hull.append((points[i], points[j]))

    # construct the convex hull from the edges
    ch = []
    for (p, q) in hull:
        if p not in ch:
            ch.append(p)
        if q not in ch:
            ch.append(q)
    ch.sort(key=lambda x: (x[0], x[1]))

    return ch