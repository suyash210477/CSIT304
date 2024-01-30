import matplotlib.pyplot as plt

def draw_ellipse(a, b):
    x = 0
    y = b
    a_squared = a * a
    b_squared = b * b
    d1 = b_squared - (a_squared * b) + (0.25 * a_squared)
    
    plot_points(x, y)

    while a_squared * (y - 0.5) > b_squared * (x + 1):
        if d1 < 0:
            d1 += b_squared * (2 * x + 3)
        else:
            d1 += (b_squared * (2 * x + 3)) + (a_squared * (-2 * y + 2))
            y -= 1
        x += 1
        plot_points(x, y)

    d2 = (b_squared * (x + 0.5) * (x + 0.5)) + (a_squared * (y - 1) * (y - 1)) - (a_squared * b_squared)

    while y > 0:
        if d2 < 0:
            d2 += b_squared * (2 * x + 2) + a_squared * (-2 * y + 3)
            x += 1
        else:
            d2 += a_squared * (-2 * y + 3)
        y -= 1
        plot_points(x, y)

    plt.axis('equal')
    plt.show()

def plot_points(x, y):
    # Plot the points in all eight octants
    plt.scatter(x, y)
    plt.scatter(-x, y)
    plt.scatter(x, -y)
    plt.scatter(-x, -y)
    plt.scatter(y, x)
    plt.scatter(-y, x)
    plt.scatter(y, -x)
    plt.scatter(-y, -x)

a = 10  # Semi-major axis
b = 5   # Semi-minor axis
draw_ellipse(a, b)
