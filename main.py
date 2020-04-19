import pygame
import numpy as np
import time

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
newGameState = np.zeros((nxC, nyC))

pause = False

gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

while True:

    screen.fill(bg)
    time.sleep(0.1) # Don't burning up the CPU

    newGameState = np.copy(gameState)


    # Register the event and mouse events
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pause = not pause

    for x in range(0, nxC):
        for y in range(0, nyC):

            # Don't update the game if it's paused
            if not pause:

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


                # Rule 1: If a death cell has exacly 3 neighbors, the cell revives
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # Rule 2: If an alive cell has less than 2 neighbors and more than 3, the cell dies
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            # The square to draw
            polygon = [((x)   * dimCW, y * dimCH),
                       ((x+1) * dimCW, y * dimCH),
                       ((x+1) * dimCW, (y+1) * dimCH),
                       ((x)   * dimCW, (y+1) * dimCH)]

            # Draw a square with 1 pixel of width
            if newGameState[x, y] == 0:
                # Black (dead) cell
                pygame.draw.polygon(screen, (128, 128, 128), polygon, 1)
            else:
                # White (alive) cell
                pygame.draw.polygon(screen, (255, 255, 255), polygon, 0)

    # Update the game state
    gameState = np.copy(newGameState)

    pygame.display.flip()
