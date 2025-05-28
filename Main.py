import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Image Display')
# Load and scale images
bg = pygame.transform.scale(pygame.image.load('Background Pic.png'), (500, 500))
penguin = pygame.transform.scale(pygame.image.load('Character.png').convert_alpha(), (200, 200))
penguin_rect = penguin.get_rect(center=(250, 220))
# Create text
font = pygame.font.Font(None, 36)
text = font.render('Hello World', True, (0, 0, 0))
text_rect = text.get_rect(center=(250, 360))
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg, (0, 0))
    screen.blit(penguin, penguin_rect)
    screen.blit(text, text_rect)
    pygame.display.flip()
pygame.quit()