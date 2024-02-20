from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

def DrawCube():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10.0)
    
    A = [1,1,2] 
    B = [2,1,2]  
    C = [2,2,2]
    D = [1,2,2]
    E = [1,1,1]  
    F = [2,1,1]
    G = [2,2,1]
    H = [1,2,1]
    
    glBegin(GL_QUADS)
    glVertex3fv(A)
    glVertex3fv(B) 
    glVertex3fv(C)
    glVertex3fv(D)
    
    glVertex3fv(E)
    glVertex3fv(F)
    glVertex3fv(G) 
    glVertex3fv(H)
    
    glVertex3fv(E)
    glVertex3fv(A)
    glVertex3fv(D)
    glVertex3fv(H)   
    
    glVertex3fv(B)
    glVertex3fv(F)
    glVertex3fv(G)
    glVertex3fv(C)
    
    glVertex3fv(E) 
    glVertex3fv(F)
    glVertex3fv(B)
    glVertex3fv(A)
    
    glVertex3fv(H)
    glVertex3fv(G)
    glVertex3fv(C)
    glVertex3fv(D)
    glEnd()
    
    glFlush()
    
def initialize():
    glClearColor(0.0, 0.0, 0.0, 0.0)   
    gluOrtho2D(-100, 100, -100, 100)
    
def main():
    glutInit(sys.argv)
    
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)

    glutCreateWindow("OpenGL Cube Drawing")

    initialize()

    glutDisplayFunc(DrawCube)

    glutMainLoop()


if __name__ == "__main__":
    main()
