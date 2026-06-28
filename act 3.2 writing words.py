import pygame
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first game")

white = (255, 255, 255)
green = (0, 255, 0)

font = pygame.font.Font(None, 36)
text_surface = font.render("This is shapes!", True, (255, 0, 0))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(white)
        window.blit(text_surface, (10, 10))
        pygame.draw.rect(window, (255, 255, 0), (100, 100, 30, 30))
        pygame.draw.circle(window, green, (250, 250), 50)
        pygame.draw.line(window, (0, 0, 255), (300, 300), (400, 400), 5)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
