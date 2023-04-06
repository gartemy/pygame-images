import pygame

WIDTH = 600
HEIGHT = 400
FPS = 60

game_sc = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Работа с изображениями')

image = pygame.image.load('images/car.bmp')
image.set_colorkey([255, 255, 255])

car_rect = image.get_rect()

car_down = pygame.transform.flip(image, False, True)
car_left = pygame.transform.rotate(image, 90)
car_right = pygame.transform.rotate(image, -90)

background = pygame.image.load('images/sand.jpg')

background = pygame.transform.scale(background, [640, 400])

finish = pygame.image.load('images/finish.png')
finish_rect = finish.get_rect(bottomright = [600, 400])

clock = pygame.time.Clock()

car = car_right
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        car_rect.y -= speed
        car = image
        if car_rect.y < 0:
            car_rect.y = 0
    elif keys[pygame.K_DOWN]:
        car_rect.y += speed
        car = car_down
        if car_rect.y > HEIGHT - car_rect.height:
            car_rect.y = HEIGHT - car_rect.height
    elif keys[pygame.K_LEFT]:
        car_rect.x -= speed
        car = car_left
        if car_rect.x < 0:
            car_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        car_rect.x += speed
        car = car_right
        if car_rect.x > WIDTH - car_rect.height:
            car_rect.x = WIDTH - car_rect.height
        
    print(finish_rect)
    if car_rect.colliderect(finish_rect):
        exit()

    game_sc.blit(background, [0, 0])
    game_sc.blit(car, car_rect)
    game_sc.blit(finish, finish_rect)

    pygame.display.update()
    clock.tick(FPS)