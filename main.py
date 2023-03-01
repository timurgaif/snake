import random
import pygame
import time

if __name__ == '__main__':
    pygame.init()
    running = True
    pygame.display.set_caption("snake")
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    move = 10
    g = (0, 255, 0)
    col = (100, 150, 126)
    x = 100
    y = 200
    x1 = 0
    y1 = 0
    fcol = (210, 123, 187)
    lostcol = (100, 50, 173)
    scorecol = (255, 102, 0)
    xf, yf = round(random.randrange(0, width - move) / 10) * 10, round(
        random.randrange(0, height - move) / 10) * 10
    f = pygame.font.SysFont('Impact', 40)
    num_of_food = 0
    length = 1
    direction = ''


    def lose():
        a = f.render('Поражение', True, lostcol)
        screen.blit(a, [width / 3, height / 3])


    def score(point):
        a = f.render('Набрано очков: ' + str(point), True, scorecol)
        screen.blit(a, [0, 0])


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1 = -move
                    y1 = 0
                    direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    x1 = move
                    y1 = 0
                    direction = 'right'
                elif event.key == pygame.K_UP:
                    x1 = 0
                    y1 = -move
                    direction = 'up'
                elif event.key == pygame.K_DOWN:
                    x1 = 0
                    y1 = move
                    direction = 'down'

        if x > width or y > height or x < 0 or y < 0:
            running = False
        x += x1
        y += y1
        if x == xf and y == yf:
            xf, yf = round(random.randrange(0, width - move) / 10) * 10, round(
                random.randrange(0, height - move) / 10) * 10
            num_of_food += 1
            length += 1
        screen.fill(col)
        if direction == 'left':
            pygame.draw.rect(screen, g, [x, y, 10 + move * length, 10])
        elif direction == 'right':
            pygame.draw.rect(screen, g, [x, y, 10 + move * length, 10])
        elif direction == 'up':
            pygame.draw.rect(screen, g, [x, y, 10, 10 + move * length])
        elif direction == 'down':
            pygame.draw.rect(screen, g, [x, y, 10, 10 + move * length])

        pygame.draw.rect(screen, fcol, [xf, yf, 10, 10])
        score(num_of_food)
        pygame.display.update()
        clock.tick(20)
    lose()
    pygame.display.update()
    time.sleep(3)

    pygame.quit()