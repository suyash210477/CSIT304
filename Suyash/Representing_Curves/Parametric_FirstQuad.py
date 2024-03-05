from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Circle parameters
radius = 0.5
num_segments = 50

def compute_circle_points(cx, cy, r, num_segments):
    points = []
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        points.append((x, y))
    return points

def draw_points(points):
    glPointSize(5)
    glBegin(GL_POINTS)
    for point in points:
        glVertex2f(point[0], point[1])
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0, 1.0, 1.0)
    circle_points = compute_circle_points(0, 0, radius, num_segments)
    first_quadrant_points = [(x, y) for (x, y) in circle_points if x >= 0 and y >= 0]
    draw_points(first_quadrant_points)
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"OpenGL Circle")
    glutDisplayFunc(draw)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()