import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
YELLOW= (255,255,0)
GREEN= (0,255,0)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH =53
HEIGHT =62
 
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
width = 20
height = 20
class Player(pygame.sprite.Sprite):
   

    # Constructor function

    def __init__(self, x_point, y_point,last_move):
        # Make our top-left corner the passed-in location.
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.Surface([width,height])
        self.image.fill(BLUE)
        self.rect=self.image.get_rect()
        self.rect.x=x_point
        self.rect.y=y_point
        self.last_move=last_move
    def draw(self):
        pygame.draw.circle(screen,BLUE,(self.rect.x,self.rect.y),10)
        # print(self.rect.x, self.rect.y)
        # print("draw")
        # print(self.rect.x)
        # print(self.rect.y)
    
    

    def moveup(self) :
        #moves up when up arrow key is pressed
        self.rect.y=self.rect.y - HEIGHT
        self.last_move="up"
    def movedown(self):
        self.rect.y=self.rect.y + HEIGHT
        self.last_move="down"
    def moveleft(self):
        self.rect.x=self.rect.x - WIDTH
        self.last_move="left"
    def moveright(self):
        self.rect.x=self.rect.x + WIDTH
        self.last_move="right"
        
    def reset_player(self):
        self.circle.x = 680
        self.circle.y = 480

    # Find a new position for the player
    def update(self):
        self.circle.x += self.change_y
        self.circle.y += self.change_x

    def move(self,x_point,y_point):
        self.rect.x=x_point
        self.rect.y=y_point
        # print("move")
        # print(self.rect.x)
        # print(self.rect.y)
        







class Coins(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, color):
        super().__init__()
        self.color=color 
        self.image=pygame.Surface([width,height])
        self.image.fill(self.color)
        self.rect=self.image.get_rect()
        self.rect.x=x_pos
        self.rect.y=y_pos
    def returnx_pos():
        return x_pos 
    def returny_pos():
        return y_pos 
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.rect.x, self.rect.y), 10, 0)



  

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x_point, y_point, width, height, color):
        super().__init__()
        self.width=width
        self.height=height
        self.color=color
        self.image=pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x=x_point
        self.rect.y=y_point

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.rect.x, self.rect.y, self.width, self.height])





player1=Player(670,470,"none")




Coin1=Coins(34, 36, GREEN)
Coin2=Coins(20, 600, GREEN)
Coin3=Coins(405, 222, GREEN)
Coin4= Coins(193, 284, GREEN)
Coin5=Coins(511,36, GREEN)
Coin6=Coins(299,36, YELLOW)
Coin7=Coins (193, 408, GREEN)
Coin8=Coins(670,222, GREEN)
Coin9=Coins(600,600, GREEN)
Coin10=Coins(511, 284, GREEN)
Coin11=Coins(34, 408, GREEN)
Coin12=Coins(670,36, GREEN)

wall1=Obstacle(595, 380, 106, 60,BLACK)
wall2=Obstacle(488, 380, 106, 60,BLACK)
wall3=Obstacle(272, 379, 106, 60,BLACK)
wall4=Obstacle(325, 438, 53, 60,BLACK)
wall5=Obstacle(272, 318, 106, 60,BLACK)
wall6=Obstacle(542, 191, 106, 124,BLACK)
wall7=Obstacle(542, 65, 106, 60,BLACK)
wall8=Obstacle(380, 2, 106, 124,BLACK)
wall9=Obstacle(433, 127, 53, 63,BLACK)
wall10=Obstacle(164, 65, 216, 61,BLACK)
wall11=Obstacle(2, 65, 106, 124,BLACK)
wall12=Obstacle(161, 190, 216, 63,BLACK)
wall13=Obstacle(55, 318, 106, 124,BLACK)
wall14=Obstacle(0,0, 10, 500, BLACK)
wall15=Obstacle(690, 0, 40, 500, BLACK)
wall16=Obstacle(0, (10-20), 700, 20, BLACK)
wall17=Obstacle(0, 490, 700, 50, BLACK)

group_Coins=pygame.sprite.Group(Coin1, Coin2, Coin3, Coin4, Coin5, Coin6, Coin7, Coin8, Coin9, Coin10, Coin11, Coin12)
group_obstacles=pygame.sprite.Group(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14, wall15,wall16,wall17)






# Loop until the user clicks the close button.
done = False

 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
x_pos=670
y_pos=470

# -------- Main Program Loop -----------
while not done:
    
    for event in pygame.event.get():  # User did something
        x_player=player1.rect.x
        y_player=player1.rect.y
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    
    # for event in pygame.event.get():
    #     print (event.type)
        
        # elif event.type == pygame.KEYDOWN:

            
        collision = pygame.sprite.spritecollide(player1,group_obstacles,False)
        

            
        if event.type == pygame.KEYDOWN:
                
                if len(collision) == 0: 
                    # print(len(collision))

                    if event.key == pygame.K_UP:
                        player1.moveup()
                    elif event.key == pygame.K_DOWN:
                        player1.movedown()
                    elif event.key == pygame.K_LEFT:
                        player1.moveleft()
                    elif event.key == pygame.K_RIGHT:
                        player1.moveright()
 
                
        if len(collision) == 1:
            # print(len(collision))
                if player1.last_move == "up":
                    player1.movedown()
                elif player1.last_move == "down":
                    player1.moveup()
                elif player1.last_move == "right":
                    player1.moveleft()
                elif player1.last_move == "left":
                    player1.moveright()


        collision_coin = pygame.sprite.spritecollide(player1,group_Coins,True)
        print(collision_coin)

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
    
    
    group_Coins.draw(screen)


    player1.draw()

    wall1.draw()   
    wall2.draw()
    wall3.draw()
    wall4.draw()
    wall5.draw()
    wall6.draw()
    wall7.draw()
    wall8.draw()
    wall9.draw()
    wall10.draw()
    wall11.draw()
    wall12.draw()
    wall13.draw()
    wall14.draw()
    wall15.draw()
    wall16.draw()
    wall17.draw()
    
    
   # Limit to 60 frames per second
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
