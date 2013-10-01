__author__ = 'Zachary'

import pyglet
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
root.num_children = 2
root.offset_angle = pi/2
root.levels = 4

window = pyglet.window.Window(resizable=True)

def draw_branch(x, y, direction, length, percent, start_angle, num_children, offset_angle, levels):
    if levels == 0:
        return
    x2 = x + cos(direction)*length
    y2 = y + sin(direction)*length
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', (x, y, x2, y2)))
    for child in range(0, num_children):
        pyglet.gl.glColor4f(1.0, 1.0, 0.0, 1.0)
        draw_branch(x2, y2, direction + start_angle - (offset_angle*child/(num_children - 1)),
                    length*percent, percent, start_angle, num_children, offset_angle, levels - 1)

@window.event
def on_draw():
    window.clear()
    pyglet.gl.glColor4f(1.0, 0.0, 0.0, 1.0)
    draw_branch(root.x, root.y, root.direction, root.length, root.percent,
                root.start_angle, root.num_children, root.offset_angle, root.levels)

@window.event
def on_mouse_motion(x, y, dx, dy):
    root.direction= pi - x/window.width * pi
    root.start_angle = root.direction * 2
    root.offset_angle = y/window.height * 2*pi

pyglet.app.run()