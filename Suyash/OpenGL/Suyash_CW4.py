from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Coordinates of the clicked point
clicked_point = False

# Define vertices of the color picker triangle
color_picker_vertices = np.array([
    [100.0, 100.0],
    [300.0, 400.0],
    [500.0, 200.0]
])

# Define colors at each vertex of the color picker triangle
color_picker_colors = np.array([
    [1.0, 0.0, 0.0],  # Red
    [0.0, 1.0, 0.0],  # Green
    [0.0, 0.0, 1.0]   # Blue
])

# Define vertices of the outline triangle
outline_vertices = np.array([
    [700.0, 100.0],
    [900.0, 400.0],
    [1100.0, 100.0]
])

# Initialize the selected color to white
selected_color = [1.0, 1.0, 1.0]

# Function to draw a triangle
def draw_triangle(vertices, colors=None, fill=False):
    glBegin(GL_TRIANGLES if fill else GL_LINE_LOOP)
    for i in range(len(vertices)):
        if colors is not None:
            glColor3fv(colors[i])
        glVertex2fv(vertices[i])
    glEnd()

# Function to interpolate color based on barycentric coordinates
def interpolate_color(alpha, beta, gamma, colors):
    R = alpha * colors[0][0] + beta * colors[1][0] + gamma * colors[2][0]
    G = alpha * colors[0][1] + beta * colors[1][1] + gamma * colors[2][1]
    B = alpha * colors[0][2] + beta * colors[1][2] + gamma * colors[2][2]
    return [R, G, B]

# Function to calculate barycentric coordinates
def barycentric_coordinates(px, py, vertices):
    ax, ay = vertices[0]
    bx, by = vertices[1]
    cx, cy = vertices[2]

    v0 = (bx - ax, by - ay)
    v1 = (cx - ax, cy - ay)
    v2 = (px - ax, py - ay)

    d00 = np.dot(v0, v0)
    d01 = np.dot(v0, v1)
    d11 = np.dot(v1, v1)
    d20 = np.dot(v2, v0)
    d21 = np.dot(v2, v1)

    denom = d00 * d11 - d01 * d01
    v = (d11 * d20 - d01 * d21) / denom
    w = (d00 * d21 - d01 * d20) / denom
    u = 1 - v - w

    return u, v, w

# OpenGL display function
def display():
    global selected_color
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw the color picker triangle
    draw_triangle(color_picker_vertices, color_picker_colors, fill=True)

    # Draw the Target triangle
    if clicked_point:
        draw_triangle(outline_vertices, [selected_color]*3, fill=True)
    else:
        draw_triangle(outline_vertices, None, fill=False)

    glFlush()

# OpenGL initialization function
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 1200.0, 0.0, 500.0)

# Mouse click event handler
def mouse_click(button, state, x, y):
    global selected_color
    global clicked_point
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        alpha, beta, gamma = barycentric_coordinates(x, 500 - y, color_picker_vertices)
        
        if 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1:
            selected_color = interpolate_color(alpha, beta, gamma, color_picker_colors)
            clicked_point = True
        else:
            clicked_point = False

        glutPostRedisplay() # Recall Display Function

# Main function
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1200, 500)
    glutCreateWindow("Color Picker Application")
    glutDisplayFunc(display)
    glutMouseFunc(mouse_click)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
