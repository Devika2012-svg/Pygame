import pygame
pygame.init()
# Create the display surface object of specific dimension
window = pygame.display.set_mode((400, 400))
# Fill the screen with white colour
window.fill((255, 255, 255))
# define colours
Blue = (0, 0, 255)
# draw a solid circle
pygame.draw.circle(window, Blue, (300, 300), 50)
# draw outlined circle
pygame.draw.circle(window, Blue, (100, 100), 50, 5)
# draw the durface object to the screen
pygame.display.update()
# game loop
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()