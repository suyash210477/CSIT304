from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

# Initialize global variables
car_pos_x = 0.0 # car position on x-axis
car_pos_y = -0.9 # car position on y-axis
car_speed = 0.01  # Initial speed of the car
light_state = "green"  # Initial state of the traffic light
light_timer = 0  # Timer to change traffic light state
green_duration = 20  # Duration of green light in terms of update cycles
yellow_duration = 10  # Duration of yellow light
red_duration = 20  # Duration of red light

def draw_circle(x, y, radius, color):
    glBegin(GL_POLYGON)
    glColor3f(*color)
    for i in range(100):
        theta = 2.0 * pi * i / 100
        glVertex2f(x + cos(theta) * radius, y + sin(theta) * radius)
    glEnd()

def car():
    global car_pos_x, car_pos_y
    car_width = 0.05
    car_length = 0.1
    
    glColor3f(0.0, 0.0, 1.0)  # Car body color
    glBegin(GL_QUADS)
    glVertex2f(car_pos_x - car_width, car_pos_y - car_length)
    glVertex2f(car_pos_x + car_width, car_pos_y - car_length)
    glVertex2f(car_pos_x + car_width, car_pos_y + car_length)
    glVertex2f(car_pos_x - car_width, car_pos_y + car_length)
    glEnd()

    wheel_radius = 0.015
    glColor3f(0.0, 0.0, 0.0)  # Wheels color
    # Wheels
    draw_circle(car_pos_x - 0.03, car_pos_y - 0.08, wheel_radius, (0, 0, 0))
    draw_circle(car_pos_x + 0.03, car_pos_y - 0.08, wheel_radius, (0, 0, 0))
    draw_circle(car_pos_x - 0.03, car_pos_y + 0.08, wheel_radius, (0, 0, 0))
    draw_circle(car_pos_x + 0.03, car_pos_y + 0.08, wheel_radius, (0, 0, 0))

# update function for setting animations
def update(value):
    global car_pos_y, light_state, light_timer, green_duration, yellow_duration, red_duration, car_speed
    
    # Increment the timer
    light_timer += 1

    # Check the state of the traffic light and adjust car speed
    if light_state == "green":
        car_speed = 0.01  # Normal speed
    elif light_state == "yellow":
        car_speed = 0.005  # Slower speed
    else:  # light_state is "red"
        car_speed = 0  # Stop

    # Transition from green to yellow
    if light_state == "green" and light_timer > green_duration:
        light_state = "yellow"
        light_timer = 0  # Reset timer for the yellow state

    # Transition from yellow to red
    elif light_state == "yellow" and light_timer > yellow_duration:
        light_state = "red"
        light_timer = 0  # Reset timer for the red state

    # Transition from red back to green
    elif light_state == "red" and light_timer > red_duration:
        light_state = "green"
        light_timer = 0  # Reset timer for the green state

    # Move the car based on the current speed
    car_pos_y += car_speed
    if car_pos_y > 1.0:
        car_pos_y = -0.9  # Reset car position after it moves off the screen
    
    glutPostRedisplay()
    glutTimerFunc(100, update, 0)

def traffic_light():
    global light_state
    glPushMatrix()
    glTranslatef(0.7, 0.0, 0.0)  # Move the traffic light to the right side
    
    glColor3f(0.0, 0.0, 0.0)  # Pole color
    glBegin(GL_QUADS)
    glVertex2f(-0.05, -0.3)
    glVertex2f(0.05, -0.3)
    glVertex2f(0.05, 0.6)
    glVertex2f(-0.05, 0.6)
    glEnd()
    
    # Lights color based on state
    red_light = (1, 0, 0) if light_state == "red" else (0.3, 0, 0)
    yellow_light = (1, 1, 0) if light_state == "yellow" else (0.3, 0.3, 0)
    green_light = (0, 1, 0) if light_state == "green" else (0, 0.3, 0)

    draw_circle(0.0, 0.4, 0.04, red_light)
    draw_circle(0.0, 0.3, 0.04, yellow_light)
    draw_circle(0.0, 0.2, 0.04, green_light)
    
    glPopMatrix()

def road():
    glColor3f(0.3, 0.3, 0.3)  # Road color
    glBegin(GL_QUADS)
    glVertex2f(-0.8, -1.0)
    glVertex2f(-0.8, 1.0)
    glVertex2f(0.8, 1.0)
    glVertex2f(0.8, -1.0)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)  # Lines color
    glLineWidth(2)
    glBegin(GL_LINES)
    for i in range(-10, 11, 2):
        glVertex2f(0, i / 10.0)
        glVertex2f(0, (i + 1) / 10.0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    road()
    traffic_light()
    car()
    glFlush()

def main():
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
