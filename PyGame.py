import pygame

# Initialize PyGame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600

def render_text(text, font_size, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()





# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title
pygame.display.set_caption("Text Adventure")

# Main game loop
running = True
welcome_text, welcome_rect = render_text("Welcome to Text Adventure!", 48)
welcome_rect.center = (screen_width // 2, screen_height // 2)
screen.blit(welcome_text, welcome_rect)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()

# Quit PyGame
pygame.quit()