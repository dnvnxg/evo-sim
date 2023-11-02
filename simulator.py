import sdl2.ext
import math
from parameters import ParamManager


def set_pixel(surface, x, y, color):
    """Set a single pixel on the surface."""
    surface[x][y] = color

def draw_circle(surface, center_x, center_y, radius, color):
    """Draw a circle using the midpoint circle algorithm."""
    x = radius - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (radius << 1)

    while x >= y:
        set_pixel(surface, center_x + x, center_y + y, color)
        set_pixel(surface, center_x + y, center_y + x, color)
        set_pixel(surface, center_x - y, center_y + x, color)
        set_pixel(surface, center_x - x, center_y + y, color)
        set_pixel(surface, center_x - x, center_y - y, color)
        set_pixel(surface, center_x - y, center_y - x, color)
        set_pixel(surface, center_x + y, center_y - x, color)
        set_pixel(surface, center_x + x, center_y - y, color)

        if err <= 0:
            y += 1
            err += dy
            dy += 2

        if err > 0:
            x -= 1
            dx += 2
            err += dx - (radius << 1)

def draw_smiley(renderer):
    width, height = renderer.logical_size

    # Create a surface to draw on
    surface = [[sdl2.ext.Color(255, 255, 255) for _ in range(width)] for _ in range(height)]

    # Draw the face
    draw_circle(surface, width // 2, height // 2, 40, sdl2.ext.Color(255, 255, 0))  # Yellow face

    # Draw the eyes
    draw_circle(surface, height // 2 - 20, width // 2 - 20, 5, sdl2.ext.Color(0, 0, 0))  # Left eye
    draw_circle(surface, height // 2 + 20, width // 2 - 20, 5, sdl2.ext.Color(0, 0, 0))  # Right eye

    # Draw the smile
    for angle in range(-45, 45):
        x = int(20 * math.cos(math.radians(angle)))
        y = int(20 * math.sin(math.radians(angle)))
        set_pixel(surface, width // 2 + x, height // 2 + 20 + y, sdl2.ext.Color(0, 0, 0))

    # Copy the surface to the renderer
    for x in range(width):
        for y in range(height):
            renderer.draw_point((x, y), surface[y][x])

def main():
    width, height = 300, 300
    sdl2.ext.init()

    window = sdl2.ext.Window("Smiley Face", size=(width*2, height*2))
    window.show()

    renderer = sdl2.ext.Renderer(window)
    renderer.logical_size = (width*1, height*1)

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False

        renderer.clear()
        draw_smiley(renderer)
        renderer.present()

    sdl2.ext.quit()

if __name__ == "__main__":
    main()



# class Simulator:
#     width, height = renderer.logical_size

#     def __init__(self, parameters: ParamManager=ParamManager()) -> None:
#         self.parameters = parameters