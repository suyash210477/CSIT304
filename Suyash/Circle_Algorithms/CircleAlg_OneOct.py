import matplotlib.pyplot as plt

def draw_circle(radius):
    x = radius
    y = 0
    p = 1 - radius

    # Plot the initial point in the first octant
    plot_point(x, y)

    while x >= y:
        y += 1

        # Mid-point is inside or on the perimeter of the circle
        if p <= 0:
            p = p + 2 * y + 1
        else:
            x -= 1
            p = p + 2 * y - 2 * x + 1

        # Plot the generated point in the first octant
        plot_point(x, y)

    plt.axis('equal')
    plt.show()

def plot_point(x, y):
    # Plot the point in the first octant
    plt.scatter(x, y)

radius = 10
draw_circle(radius)
