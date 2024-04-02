from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

# Function to draw a circle
def draw_circle(x, y, radius, color):
    glBegin(GL_POLYGON)
    glColor3f(*color)
    num_segments = 100
    for i in range(num_segments):
        theta = 2.0 * 3.1415926 * i / num_segments
        dx = radius * cos(theta)
        dy = radius * sin(theta)
        glVertex2f(x + dx, y + dy)
    glEnd()

# Function to draw the traffic light
def traffic_light():
    # Draw the pole
    glColor3f(0.0, 0.0, 0.0)  # Black color for the pole
    glBegin(GL_QUADS)
    glVertex2f(-0.05, -0.3)  # Slightly thicker pole
    glVertex2f(0.05, -0.3)
    glVertex2f(0.05, 0.6)
    glVertex2f(-0.05, 0.6)
    glEnd()

    # Colors with reduced intensity (darker)
    off_red = (0.3, 0, 0)
    off_yellow = (0.3, 0.3, 0)
    off_green = (0, 0.3, 0)

    # Reduced radius for the circles
    radius = 0.04  # Smaller circle size

    # Draw the red light
    draw_circle(0.0, 0.4, radius, off_red)
    # Draw the yellow light
    draw_circle(0.0, 0.3, radius, off_yellow)
    # Draw the green light
    draw_circle(0.0, 0.2, radius, off_green)
# Function to draw the road and the lines
def road():
    # Draw the road
    glColor3f(0.3, 0.3, 0.3)  # Dark grey color for the road
    glBegin(GL_QUADS)
    glVertex2f(-0.8, -1.0)
    glVertex2f(-0.8, 1.0)
    glVertex2f(0.8, 1.0)
    glVertex2f(0.8, -1.0)
    glEnd()

    # Draw the dashed center lines
    glColor3f(1.0, 1.0, 1.0)  # White color for the lines
    glLineWidth(2)
    glBegin(GL_LINES)
    for i in range(-10, 11, 2):  # Draw dashed lines
        glVertex2f(0, i / 10.0)
        glVertex2f(0, (i + 1) / 10.0)
    glEnd()

# The display callback function
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    road()
    glTranslatef(0.7,0.3,0.0)
    traffic_light()
    glFlush()

# Main function
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(0, 7)
    glutCreateWindow(b"OpenGL Traffic Light")
    glutDisplayFunc(display)
    glClearColor(1.0, 1.0, 1.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glutMainLoop()

if __name__ == "__main__":
    main()
