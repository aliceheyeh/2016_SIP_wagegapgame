import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 53
HEIGHT = 62
 
MARGIN = 1
grid = []
for row in range(8):
    grid.append([])
    for column in range(13):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [700, 500]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Women")
class Player():
    def __init__(self, coins):
        self.coins=coins
        

    def move(self, speed):
        #moves with each arrow key
        self.x_point = self.x_point + speed

class Obstacle():
    def __init__(self, width, color):
        self.width=width
        self.color=color

 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
x_pos=670
y_pos=470
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                x_pos = x_pos-5
            elif event.type == pygame.K_RIGHT:
                x_pos = x_pos + 5
        
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(8):
        for column in range(13):
            color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(60)
    pygame.draw.circle(screen, BLUE, (x_pos,y_pos), 30)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()