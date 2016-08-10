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
width = 50
height = 50
class Player(pygame.sprite.Sprite):
   

    # Constructor function

    def __init__(self, x_point, y_point):
        # Make our top-left corner the passed-in location.
        pygame.sprite.Sprite.__init__(self)

        self.x_point=x_point
        self.y_point=y_point
        self.image=pygame.Surface([width,height])
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()

    def draw(self):
        pygame.draw.circle(screen,BLUE,(self.x_point,self.y_point),20)
    

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
        self.circle.x = 680
        self.circle.y = 480

    # Find a new position for the player
    def update(self):
        self.circle.x += self.change_y
        self.circle.y += self.change_x








class Coins():
        def __init__(self, x_pos, y_pos):
            self.x_pos= x_pos
            self.y_pos= y_pos
    # self.value= value 
        def returnx_pos():
            return x_pos 
        def returny_pos():
            return y_pos 
    #def returnvalue ():
        #return value

        def disappear (self):
            return True
            
        def draw(self):
            pygame.draw.circle(screen, GREEN, (300, 50), 20, width=30)
            


class Obstacle(pygame.sprite.Sprite):
   
    
    def __init__(self, x_point, y_point, width, height, color):
        super().__init__()
        self.x_point=x_point
        self.y_point=y_point
        self.width=width
        self.height=height
        self.color=color

    def draw(self):
           
       
        pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])
# <<<<<<< HEAD
player1=Player(670,470)
# =======
# >>>>>>> 77d5fb4ce766851c53aa100af8168880c2327e71

# collision = pygame.sprite.collide_rect(Player,Obstacle):

# if pygame.sprite.collide_rect 

#print(pygame.sprite.collide_rect(Player,Obstacle))
 
wall1=Obstacle(595, 380, 106, 60,BLACK)
wall2=Obstacle(488, 380, 106, 60,BLACK)
wall3=Obstacle(272, 379, 106, 60,BLACK)
wall4=Obstacle(325, 438, 53, 60,BLACK)
wall5=Obstacle(272, 318, 106, 60,BLACK)
wall6=Obstacle(542, 191, 106, 124,BLACK)
wall7=Obstacle(542, 65, 106, 60,BLACK)
wall8=Obstacle(380, 2, 106, 124,BLACK)

wall9=Obstacle(433, 127, 53, 63,BLACK)
wall10=Obstacle(379, 2, 106, 124,BLACK)
wall11=Obstacle(379, 2, 106, 124,BLACK)
wall12=Obstacle(379, 2, 106, 124,BLACK)

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
# <<<<<<< HEAD
    player1.draw()
   
# =======

    wall1.draw()   
    wall2.draw()
    wall3.draw()
    wall4.draw()
    wall5.draw()
    wall6.draw()
    wall7.draw()
    wall8.draw()
# >>>>>>> 77d5fb4ce766851c53aa100af8168880c2327e71

    wall9.draw()
    wall10.draw()
    wall11.draw()
    wall12.draw()

   # Limit to 60 frames per second
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
