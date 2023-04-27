import pygame

WIDTH , HEIGHT = 1280, 720
FPS= 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Dupa")


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()

if __name__ == "__main__":
    main()
