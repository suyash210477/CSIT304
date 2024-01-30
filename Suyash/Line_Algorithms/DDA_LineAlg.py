# MY CODE
# import matplotlib.pyplot as plt
# import numpy as np

# x1 = 1
# y1 = 1
# x2 = 8
# y2 = 5

# def line(x1,x2,y1,y2):
#     m = (y2-y1)/(x2-x1)
#     c = y1-m*(x1)
    
#     for i in range(x1,x2+1):
#         y = round(m*i) + c
#         y = round(y)
#         print(i, "=", i,",",y)
    
# line(1,8,1,5)

# xpoint = np.array([1,8])
# ypoint = np.array([1,5])

# plt.plot(xpoint,ypoint)
# plt.show()

# DDA (digital differential analyser)
import matplotlib.pyplot as plt
import numpy as np

x1 = 1
y1 = 1
x2 = 8
y2 = 5

def line(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * (x1)

    x_values = list(range(x1, x2 + 1))
    y_values = [round(m * x + c) for x in x_values]

    for i, y in zip(x_values, y_values):
        print(i, "=", i, ",", y)

    return x_values, y_values

x_points, y_points = line(1, 8, 1, 5)

plt.plot(x_points, y_points, marker='o')
plt.show()
