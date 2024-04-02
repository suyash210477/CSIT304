from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

# Initialize global variables
# control the position of the car
car_pos_x = -0.7
car_pos_y = -0.9
light_state = "green"  # Initial state of the traffic light
light_timer = 0  # Timer to change traffic light state

def draw_circle(x, y, radius, color):
    """Draws a filled circle with the given specifications."""
    glBegin(GL_POLYGON)
    glColor3f(*color)
    for i in range(100):
        theta = 2.0 * pi * i / 100
        glVertex2f(x + cos(theta) * radius, y + sin(theta) * radius)
    glEnd()

def car():
    """Draws the car at its current position."""
    global car_pos_x, car_pos_y
    car_width = 0.05
    car_length = 0.1

    # Car body
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(car_pos_x - car_width, car_pos_y - car_length)
    glVertex2f(car_pos_x + car_width, car_pos_y - car_length)
    glVertex2f(car_pos_x + car_width, car_pos_y + car_length)
    glVertex2f(car_pos_x - car_width, car_pos_y + car_length)
    glEnd()

    # Car wheels
    wheel_radius = 0.015
    for wx, wy in [(-0.8, -0.9), (0.8, -0.9), (-0.8, 0.9), (0.8, 0.9)]:
        draw_circle(car_pos_x + wx * car_width, car_pos_y + wy * car_length, wheel_radius, (0, 0, 0))

    # Windshield
    glColor4f(0.7, 0.9, 1.0, 0.5)
    glBegin(GL_QUADS)
    glVertex2f(car_pos_x - car_width * 0.5, car_pos_y + car_length * 0.5)
    glVertex2f(car_pos_x + car_width * 0.5, car_pos_y + car_length * 0.5)
    glVertex2f(car_pos_x + car_width * 0.3, car_pos_y + car_length * 0.8)
    glVertex2f(car_pos_x - car_width * 0.3, car_pos_y + car_length * 0.8)
    glEnd()

def update(value):
    """Updates the scene state."""
    global car_pos_y, light_state, light_timer
    light_timer += 1

    # Change the light state based on the timer
    if light_timer >= 100:
        if light_state == "green":
            light_state = "yellow"
        elif light_state == "yellow":
            light_state = "red"
        elif light_state == "red":
            light_state = "green"
        light_timer = 0  # Reset timer

    # Move the car only if the light is green
    if light_state == "green":
        car_pos_y += 0.01
        if car_pos_y > 1.0:
            car_pos_y = -0.9  # Reset car position

    glutPostRedisplay()
    glutTimerFunc(100, update, 0)

def traffic_light():
    """Draws the traffic light, changing colors based on its state."""
    global light_state
    colors = {
        "red": ((1, 0, 0), (0.3, 0.3, 0), (0, 0.3, 0)),
        "yellow": ((0.3, 0, 0), (1, 1, 0), (0, 0.3, 0)),
        "green": ((0.3, 0, 0), (0.3, 0.3, 0), (0, 1, 0)),
    }
    red, yellow, green = colors[light_state]
    glPushMatrix() # save the state of the matrix
    glTranslatef(0.7, 0.0, 0.0) # translate the traffic light 

    # Draw the pole
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(-0.05, -0.3)
    glVertex2f(0.05, -0.3)
    glVertex2f(0.05, 0.6)
    glVertex2f(-0.05, 0.6)
    
    glEnd()

    # Draw lights
    draw_circle(0.0, 0.4, 0.04, red)
    draw_circle(0.0, 0.3, 0.04, yellow)
    draw_circle(0.0, 0.2, 0.04, green)

def road():
    """Draws the road and the lane markings."""
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_QUADS)
    glVertex2f(-0.8, -1.0)
    glVertex2f(-0.8, 1.0)
    glVertex2f(0.8, 1.0)
    glVertex2f(0.8, -1.0)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(2)
    glBegin(GL_LINES)
    for i in range(-10, 11, 2):
        glVertex2f(0, i / 10.0)
        glVertex2f(0, (i + 1) / 10.0)
    glEnd()

def display():
    """Display callback for drawing the scene."""
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    road()
    traffic_light()
    car()
    glFlush()

def main():
    """Main function to set up OpenGL."""
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"OpenGL Traffic Simulation")
    glutDisplayFunc(display)
    glutTimerFunc(100, update, 0)
    glClearColor(1.0, 1.0, 1.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glutMainLoop()

if __name__ == "__main__":
    main()
