import matplotlib.pyplot as plt


def bresenham3Q(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)

    xdata = []
    ydata = []

    if 0 < m <= 1:
        dx = x1 - x2
        dy = y1 - y2
        P = dx - (2 * dy)
        x = x1
        y = y1
        x_end = x2

        xdata.append(x)
        ydata.append(y)

        while x > x_end:
            x -= 1
            if P < 0:
                P += 2 * dy
            else:
                y -= 1
                P += 2 * (dy - dx)

            xdata.append(x)
            ydata.append(y)

    elif m > 1:
        dx = x1 - x2
        dy = y1 - y2
        P = dy - (2 * dx)
        x = x1
        y = y1
        y_end = y2

        xdata.append(x)
        ydata.append(y)

        while y > y_end:
            y -= 1
            if P < 0:
                P += 2 * dx
            else:
                x -= 1
                P += 2 * (dx - dy)

            xdata.append(x)
            ydata.append(y)

    plt.plot(xdata, ydata)
    plt.show()
