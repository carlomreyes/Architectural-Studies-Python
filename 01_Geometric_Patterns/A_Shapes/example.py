import numpy as np
import matplotlib.pyplot as plt


def draw_circle(ax, center=(0, 0), r=1, **kwargs):
    t = np.linspace(0, 2 * np.pi, 200)
    x = center[0] + r * np.cos(t)
    y = center[1] + r * np.sin(t)
    ax.plot(x, y, **kwargs)


def draw_square(ax, center=(0, 0), size=1, **kwargs):
    s = size / 2
    xs = [center[0] - s, center[0] + s, center[0] + s, center[0] - s, center[0] - s]
    ys = [center[1] - s, center[1] - s, center[1] + s, center[1] + s, center[1] - s]
    ax.plot(xs, ys, **kwargs)


def main():
    fig, ax = plt.subplots(figsize=(5, 5))
    draw_circle(ax, r=1.0, color="#1f77b4")
    draw_square(ax, size=1.6, color="#ff7f0e")
    ax.set_aspect("equal")
    ax.set_axis_off()
    plt.show()


if __name__ == "__main__":
    main()
