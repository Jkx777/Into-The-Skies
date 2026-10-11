import pygame
import sys

pygame.init()  # initialize all modules

# Create a window (800×600)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Window")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))  # draw something
    pygame.display.flip()      # update the full display