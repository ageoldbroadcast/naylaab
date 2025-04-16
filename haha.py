import pygame
import sys

pygame.init()

# Screen setup
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Cute Game - Start Screenn")

# Colors
YELLOW = (255, 255, 150)

# Load button sprite
button_image = pygame.image.load("assets/start.png").convert_alpha()
button_rect = button_image.get_rect(center=(500, 450))

# Function to show the start screen
def start_screen():
    while True:
        screen.fill(YELLOW)  # Keep yellow for start screen
        screen.blit(button_image, button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Start button clicked!")
                    return

        pygame.display.flip()

# Game loop (after the start screen)
def game_loop():
    # Load sprites
    char_a = pygame.image.load("assets/char_a.png").convert_alpha()
    char_b = pygame.image.load("assets/char_b.png").convert_alpha()
    char_hug = pygame.image.load("assets/char_hug.png").convert_alpha()
    background = pygame.image.load("assets/gamebackground.png").convert()

    # Character positions
    start_x = 200
    end_x = 750
    char_a_x = start_x
    char_y = 500  # Ground level for characters (used as bottom alignment)

    # Scrollbar setup
    scrollbar_rect = pygame.Rect(200, 550, 600, 10)
    handle_rect = pygame.Rect(200, 545, 30, 20)
    dragging = False

    running = True
    hugged = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if handle_rect.collidepoint(event.pos):
                    dragging = True

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False

            elif event.type == pygame.MOUSEMOTION and dragging:
                handle_rect.x = max(scrollbar_rect.left, min(event.pos[0] - handle_rect.width // 2, scrollbar_rect.right - handle_rect.width))
                percent = (handle_rect.x - scrollbar_rect.x) / (scrollbar_rect.width - handle_rect.width)
                char_a_x = start_x + percent * (end_x - start_x)

        screen.blit(background, (0, 0))  # Draw background image

        if not hugged and char_a_x >= end_x - 50:
            hugged = True

        if hugged:
            hug_x = (start_x + end_x) // 2
            hug_rect = char_hug.get_rect(midbottom=(hug_x, char_y))
            screen.blit(char_hug, hug_rect)
        else:
            char_a_rect = char_a.get_rect(midbottom=(char_a_x, char_y))
            char_b_rect = char_b.get_rect(midbottom=(end_x, char_y))
            screen.blit(char_a, char_a_rect)
            screen.blit(char_b, char_b_rect)

        # Scrollbar
        pygame.draw.rect(screen, (220, 220, 220), scrollbar_rect)
        pygame.draw.rect(screen, (100, 200, 255), handle_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Run the game
start_screen()
game_loop()
