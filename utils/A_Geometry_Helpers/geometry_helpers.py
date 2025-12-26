"""Simple geometry helper utilities for examples.
"""

def grid_points(rows, cols, spacing=1.0):
    """Return a list of (x, y) coordinates on a grid."""
    pts = []
    for i in range(rows):
        for j in range(cols):
            pts.append((j * spacing, i * spacing))
    return pts


def bbox(points):
    """Return bounding box (minx, miny, maxx, maxy) for a list of points."""
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return (min(xs), min(ys), max(xs), max(ys))


if __name__ == "__main__":
    pts = grid_points(3, 4)
    print("Grid points:\n", pts)
    print("BBox:", bbox(pts))
