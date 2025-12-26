import numpy as np
import matplotlib.pyplot as plt


def sierpinski_points(n_points=5000, vertices=None):
    if vertices is None:
        vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    pts = np.zeros((n_points, 2))
    # start at a random point
    pts[0] = np.random.rand(2)
    for i in range(1, n_points):
        v = vertices[np.random.randint(0, len(vertices))]
        pts[i] = (pts[i-1] + v) / 2.0
    return pts


def plot_sierpinski(n=5000, cmap='viridis'):
    pts = sierpinski_points(n)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(pts[:, 0], pts[:, 1], s=0.6, c=pts[:, 0], cmap=cmap)
    ax.set_aspect('equal')
    ax.set_axis_off()
    plt.show()


def main():
    plot_sierpinski(n=10000)


if __name__ == '__main__':
    main()
