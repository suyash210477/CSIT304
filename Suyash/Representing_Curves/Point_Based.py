from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Function to draw the curve
def draw_curve():
    glLineWidth(2)
    glColor3f(1.0, 0.0, 0.0)  # Set color to red
    
    glBegin(GL_LINE_STRIP)  # Begin drawing line strip
    for i in range(0, 10):  # Draw points for the curve
        t = i / 10.0
        x = t * 2 - 1  # X coordinate of the point
        y = t ** 2  # Y coordinate of the point
        glVertex2f(x, y)  # Add point to the curve
    glEnd()  # End drawing line strip
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set clear color to black
    gluOrtho2D(-2.0, 2.0, -0.5, 2.0)  # Set the orthogonal view

def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the buffer
    draw_curve()  # Draw the curve
    glutSwapBuffers()  # Swap buffers

def main():
    glutInit(sys.argv)  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set display mode
    glutInitWindowSize(800, 600)  # Set window size
    glutInitWindowPosition(100, 100)  # Set window position
    glutCreateWindow(b"Curve using OpenGL")  # Create window with a title

    init()  # Initialize OpenGL parameters
    glutDisplayFunc(display)  # Set the display callback function
    glutMainLoop()  # Enter the GLUT main loop

if __name__ == "__main__":
    main()
