__author__ = 'Zachary'

import pyglet.window
from pyglet.window import key, mouse, gl
from math import pi, sin, cos

class StartingBranch:
    pass

root = StartingBranch()
root.x = 500
root.y = 0
root.length = 500
root.direction = pi/4
root.percent = .75
root.start_angle = pi/2
root.num_children = 1
root.offset_angle = pi/2
root.levels = 4

window = pyglet.window.Window(resizable=True)

def generate_branch(x, y, direction, length, percent, start_angle, num_children, offset_angle, levels, points):
    if levels == 0:
        return
    x2 = x + cos(direction)*length
    y2 = y + sin(direction)*length
    points.append(x)
    points.append(y)
    points.append(x2)
    points.append(y2)
    angle_step = offset_angle/(num_children - 1) if num_children > 1 else 0
    for child in range(0, num_children):
        generate_branch(x2, y2, direction + start_angle - child*angle_step,
                    length*percent, percent, start_angle, num_children, offset_angle, levels - 1, points)

@window.event
def on_draw():
    window.clear()
    pyglet.gl.glColor4f(1.0, 0.0, 1.0, 1.0)
    points = []
    generate_branch(window.width/2, root.y, pi/2, root.length*root.percent, root.percent,
                root.start_angle, root.num_children, root.offset_angle, root.levels, points)
    pyglet.graphics.draw(len(points)//2, pyglet.gl.GL_LINES, ('v2f', points))

@window.event
def on_mouse_motion(x, y, dx, dy):
    root.direction= pi - x/window.width * pi
    root.start_angle = -x/window.width * pi*2 + pi
    root.offset_angle = y/window.height * 2*pi

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    if buttons & mouse.LEFT:
        root.length += dy
        root.percent += dx/window.width
    else:
        on_mouse_motion(x, y, dx, dy)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        root.levels += 1
    elif symbol == key.DOWN:
        root.levels -= 1

    if symbol == key.LEFT:
        root.num_children -= 1
    elif symbol == key.RIGHT:
        root.num_children += 1

@window.event
def on_resize(width, height):
    root.length = height/2

pyglet.app.run()