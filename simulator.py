import pygame
import math
from parameters import ParamManager


def draw_circle(surface, center_x, center_y, radius, color):
    """Draw a circle using the midpoint circle algorithm."""
    x = radius - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (radius << 1)

    while x >= y:
        surface.set_at((center_x + x, center_y + y), color)
        surface.set_at((center_x + y, center_y + x), color)
        surface.set_at((center_x - y, center_y + x), color)
        surface.set_at((center_x - x, center_y + y), color)
        surface.set_at((center_x - x, center_y - y), color)
        surface.set_at((center_x - y, center_y - x), color)
        surface.set_at((center_x + y, center_y - x), color)
        surface.set_at((center_x + x, center_y - y), color)

        if err <= 0:
            y += 1
            err += dy
            dy += 2

        if err > 0:
            x -= 1
            dx += 2
            err += dx - (radius << 1)


def draw_smiley(renderer):
    width, height = renderer.get_size()

    # Create a surface to draw on
    surface = pygame.Surface((width, height))

    # Draw the face
    draw_circle(surface, width // 2, height // 2, 40,
                pygame.Color(255, 255, 0))  # Yellow face

    # Draw the eyes
    draw_circle(surface, height // 2 - 20, width // 2 - 20, 5,
                pygame.Color(0, 0, 0))  # Left eye
    draw_circle(surface, height // 2 + 20, width // 2 - 20, 5,
                pygame.Color(0, 0, 0))  # Right eye

    # Draw the smile
    for angle in range(-45, 45):
        x = int(20 * math.cos(math.radians(angle)))
        y = int(20 * math.sin(math.radians(angle)))
        surface.set_at((width // 2 + x, height // 2 + 20 + y),
                       pygame.Color(0, 0, 0))

    # Copy the surface to the renderer
    renderer.blit(surface, (0, 0))
    pygame.display.flip()


def main():
    width, height = 300, 300
    scale = 2
    window_width, window_height = width * scale, height * scale
    pygame.init()

    window = pygame.display.set_mode((window_width, window_height))
    surface = pygame.Surface((width, height))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill(pygame.Color(255, 255, 255))
        draw_smiley(surface)
        window.blit(pygame.transform.scale(surface, (window_width, window_height)),
                    (0, 0))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()