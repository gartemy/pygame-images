import pygame

WIDTH = 600
HEIGHT = 400
FPS = 60

game_sc = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Работа с изображениями')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)