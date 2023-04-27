import pygame
import time
import random
pygame.font.init()

WIDTH , HEIGHT = 1280, 720
FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BG = pygame.image.load("textures/mapa.jpeg")
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
PLAYER_VEL = 10
FONT = pygame.font.SysFont("comicsans", 30)

pygame.display.set_caption("Dupa")


def draw(player, elapsed_time):
    
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)} s", 1, "white")
    time_table_width = time_text.get_width()
    WIN.blit(time_text, (WIDTH/2 - time_table_width/2 , 10))
    pygame.draw.rect(WIN, "blue", player)
    pygame.display.update()

def main():
    
    run = True
    player = pygame.Rect(WIDTH/2 - PLAYER_WIDTH/2, HEIGHT/2 - PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0;

    while run:
        elapsed_time = time.time() - start_time

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL    
        if keys[pygame.K_s] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL
        if keys[pygame.K_w] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL    
        
        draw(player, elapsed_time)
    pygame.quit()

if __name__ == "__main__":
    main()
