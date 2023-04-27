import pygame

WIDTH , HEIGHT = 1280, 720
FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BG = pygame.image.load("textures/mapa.jpeg")
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40

pygame.display.set_caption("Dupa")


def draw(player):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, "blue", player)
    pygame.display.update()

def main():
    run = True
    player = pygame.Rect(WIDTH/2, HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(player)
    pygame.quit()

if __name__ == "__main__":
    main()
