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
    def __init__(self, x_point, y_point):
        # Make our top-left corner the passed-in location.
        self.x_point=x_point
        self.y_point=y_point

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x_point,self.y_point), 30)
    

    def moveup(self) :
        #moves up when up arrow key is pressed
        self.y_point=self.y_point - HEIGHT
    def movedown(self):
        self.y_point=self.y_point + HEIGHT
    def moveleft(self):
        self.x_point=self.x_point - WIDTH
    def moveright(self):
        self.x_point=self.x_point + WIDTH
        
        
    


    def reset_player(self):
        self.circle.x = 670
        self.circle.y = 470

    # Find a new position for the player
    def update(self):
        self.circle.x += self.change_y
        self.circle.y += self.change_x









class Obstacle():
   
    
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point=x_point
        self.y_point=y_point
        self.width=width
        self.height=height
        self.color=color
    def draw(self):
       
        
       
        pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])
player1=Player(670,470)

 
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
                player1.moveup()
            elif event.key == pygame.K_DOWN:
                player1.movedown()
            elif event.key == pygame.K_LEFT:
                player1.moveleft()
            elif event.key == pygame.K_RIGHT:
                player1.moveright() 
         
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
    player1.draw()
   

    # Limit to 60 frames per second
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
