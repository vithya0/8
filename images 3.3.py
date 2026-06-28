import pygame
pygame.init()

SCREEN_WIDTH=500
SCREEN_HEIGHT=500

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first game")
white=(255,255,255)

image = pygame.image.load("assets/universe.jpg")

def main():
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        window.fill(white)
        window.blit(image, (0, 0))
        pygame.display.flip()
        
    pygame.quit()

if __name__=="__main__":
    main()