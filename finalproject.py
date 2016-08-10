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
   

    # Constructor function
    def __init__(self, color, x, y, points):
        # Make our top-left corner the passed-in location.
        self.sprite = self.circle
        self.circle.x = 670
        self.circle.y = 470
        self.points=points


    def reset_player(self):
        self.circle.x = 670
        self.circle.y = 470

    # Find a new position for the player
    def update(self):
        self.circle.x += self.change_y
        self.circle.y += self.change_x

        

    def move(self, x_point):
        #moves with each arrow key
        self.x_point = self.x_point + speed
        

    def move(self, speed):
        #moves with each arrow key
        self.x_point = self.x_point + speed


class Obstacle():
   
    
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point=x_point
        self.y_point=y_point
        self.width=width
        self.height=height
        self.color=color
    def draw(self):
           
       
        pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])

 
wall1=Obstacle(595, 380, 106, 60,BLACK)
wall2=Obstacle(488, 380, 106, 60,BLACK)
wall3=Obstacle(272, 379, 106, 60,BLACK)
wall4=Obstacle(325, 438, 53, 60,BLACK)
wall5=Obstacle(272, 318, 106, 60,BLACK)

wall6=Obstacle(542, 254, 106, 60,BLACK)
wall7=Obstacle(272, 318, 106, 60,BLACK)
wall8=Obstacle(272, 318, 106, 60,BLACK)

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
    
    # for event in pygame.event.get():
    #     print (event.type)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_pos=y_pos- HEIGHT
            elif event.key == pygame.K_DOWN:
                y_pos=y_pos+HEIGHT
            elif event.key == pygame.K_LEFT:
                x_pos=x_pos- WIDTH
            elif event.key == pygame.K_RIGHT:
                x_pos = x_pos+WIDTH 
         
            # Something similar for the up & down keys
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

    wall1.draw()   
    wall2.draw()
    wall3.draw()
    wall4.draw()
    wall5.draw()
    
    wall6.draw()
    wall7.draw()
    wall8.draw()

   # Limit to 60 frames per second
    clock.tick(60)
    circle = pygame.draw.circle(screen, BLUE, (x_pos,y_pos), 30)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
