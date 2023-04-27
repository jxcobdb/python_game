import pygame

WIDTH , HEIGHT = 1280, 720
FPS= 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BG = pygame.image.load("textures/mapa.jpeg")
pygame.display.set_caption("Dupa")

def draw():
    WIN.blit(BG, (0, 0))
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()
    pygame.quit()



if __name__ == "__main__":
    main()
