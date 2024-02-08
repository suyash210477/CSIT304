from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-100, -100, -100, 100)
    
def 







# def draw_boundary(left_bottom, right_top):
#     left_x, left_y = left_bottom # creating points from a single variable
#     right_x, right_y = right_top
#     plt.plot([left_x, right_x], [left_y, left_y], color='blue') # Bottom line
#     plt.plot([left_x, right_x], [right_y, right_y], color='blue') # Top line
#     plt.plot([left_x, left_x], [left_y, right_y], color='blue') # Left line
#     plt.plot([right_x, right_x], [left_y, right_y], color='blue') # Right line

# # LeftBottom(-3,1)
# # RightTop(2,6)
# draw_boundary((-3, 1), (2, 6))
# plt.show()

# def Line(first_endpt, second_endpt):
#     x1,y1 = first_endpt
#     x2,y2 = second_endpt
    