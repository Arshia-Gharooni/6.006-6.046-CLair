class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def merge(hull_a, hull_b):
    upper_tangent = find_upper_tangent(hull_a, hull_b)
    lower_tangent = find_lower_tangent(hull_a, hull_b)

    merged_hull = []
    ai_found = False
    bi_found = False

    for point in hull_a + hull_b:
        if point == upper_tangent:
            ai_found = True
        elif point == lower_tangent:
            bi_found = True

        if ai_found:
            merged_hull.append(point)
        if bi_found and not ai_found:
            merged_hull.append(point)

    return merged_hull

def find_upper_tangent(hull_a, hull_b):
    ai = max(hull_a, key=lambda point: point.x)
    bi = min(hull_b, key=lambda point: point.x)

    while True:
        j = hull_b.index(bi)
        next_j = (j + 1) % len(hull_b)

        if y_intersection(ai, hull_b[next_j]) > y_intersection(ai, bi) or y_intersection(hull_a[(hull_a.index(ai) - 1) % len(hull_a)], bi) > y_intersection(ai, bi):
            bi = hull_b[next_j]
        else:
            break

    return ai, bi

def find_lower_tangent(hull_a, hull_b):
    ak = min(hull_a, key=lambda point: point.x)
    bm = min(hull_b, key=lambda point: point.x)

    while True:
        i = hull_a.index(ak)
        prev_i = (i - 1) % len(hull_a)

        if y_intersection(ak, hull_b[(hull_b.index(bm) + 1) % len(hull_b)]) > y_intersection(ak, bm) or y_intersection(ak, hull_b[(hull_b.index(bm) - 1) % len(hull_b)]) > y_intersection(ak, bm):
            ak = hull_a[prev_i]
        else:
            break

    return ak, bm

def y_intersection(point1, point2):
    return (point1.y - point2.y) / (point1.x - point2.x)

def convex_hull_divide_and_conquer(points):
    if len(points) <= 1:
        return points

    sorted_points = sorted(points, key=lambda point: point.x)

    mid = len(sorted_points) // 2
    hull_left = convex_hull_divide_and_conquer(sorted_points[:mid])
    hull_right = convex_hull_divide_and_conquer(sorted_points[mid:])

    return merge(hull_left, hull_right)

# Example usage:
points = [Point(1, 2), Point(3, 4), Point(5, 6), Point(7, 8), Point(9, 10)]
convex_hull = convex_hull_divide_and_conquer(points)
print(convex_hull)
