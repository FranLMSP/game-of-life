import pygame
import numpy as np

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))

# Background
bg = 25, 25, 25
screen.fill(bg)

# Number of cells
nxC, nyC = 25, 25

# Size of cells
dimCW = width / nxC
dimCH = height / nyC

# States of cells. 1 = Alive, 0 = Death
gameState = np.zeros((nxC, nyC))

while True:


    for x in range(0, nxC):
        for y in range(0, nyC):

            # Calculate tne neighbors
            n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x)     % nxC, (y - 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x - 1) % nxC, (y)     % nyC] + \
                      gameState[(x)     % nxC, (y)     % nyC] + \
                      gameState[(x + 1) % nxC, (y)     % nyC] + \
                      gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                      gameState[(x)     % nxC, (y + 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y + 1) % nyC]


            # The square to draw
            polygon = [((x)   * dimCW, y * dimCH),
                       ((x+1) * dimCW, y * dimCH),
                       ((x+1) * dimCW, (y+1) * dimCH),
                       ((x)   * dimCW, (y+1) * dimCH)]

            # Draw a square with 1 pixel of width
            pygame.draw.polygon(screen, (128, 128, 128), polygon, 1)

    pygame.display.flip()
