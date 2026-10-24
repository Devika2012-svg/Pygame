import pygame
import random

# Initialize pygame
pygame.init()

# Custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

#Define basic colours using pygame.Color()
# BG colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

# sprite colors
YELLOW= pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

# sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):

    # constructor method
    def __init__(self, color, height, width):
        # Call to the parent class (Sprite) constructor
        super().__init__()
        # create the sprite's surface with dimensions and color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Get the sprite's rect defining its position and size
        self.rect = self.image.get_rect()
        # set initial velocity with random direction
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    # Method to update the sprite's position
    def update(self):
        # move the sprite by it's velocuty
        self.rect.move_ip(self.velocity)
        # Flag to track if the sprite hits a boundary
        boundary_hit = False
        # Check for collision with left or right boundaries and reverse direction
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        # check for collision with top or bottom boundaries and reverse direction
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1]= -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

# Function to change the bg color
def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])

# Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()
# Instantiate the sprite
sp1 = Sprite(WHITE, 20, 30)
# randomly position the sprite
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
# add the sprite to the group
all_sprites_list.add(sp1)

# Instantiate the sprite
sp2 = Sprite(WHITE, 20, 30)
# randomly position the sprite
sp2.rect.x = random.randint(0, 480)
sp2.rect.y = random.randint(0, 370)
# add the sprite to the group
all_sprites_list.add(sp2)

# create the game window
screen = pygame.display.set_mode((500, 400))
# set window title
pygame.display.set_caption("Boundary Sprite")
# set the initial bg color
bg_color = BLUE
# Apply the bg color
screen.fill(bg_color)

# Game loop control flag
exit = False
clock = pygame.time.Clock()

# main game loop
while not exit:
    #Event handling loop
    for event in pygame.event.get():
        # if the window'a close button is clicked, exit the game
        if event.type == pygame.QUIT:
            exit = True
        # if the sprite color change event is triggered, change the sprites color
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
            sp2.change_color()
        # if the bg color change event is triggered change the bg color
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    all_sprites_list.update()
    # fill the screen with the current bg color
    screen.fill(bg_color)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(240)

pygame.quit()