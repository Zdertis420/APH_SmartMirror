import pygame
from parser import getWeather, getTime



if __name__ == '__main__':
    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    runnig = True
    firstCycle = True
    counetr = 0


    while runnig:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnig = False

        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 75)

        time = getTime()

        textTime = font.render(time, True, (255, 255, 255))
        text_x = 100
        text_y = 75
        screen.blit(textTime, (text_x, text_y))

        if firstCycle:
            temp, feelsLike, windSpeed, conditions = getWeather()
            firstCycle = False

        if counetr == 432000:
            temp, feelsLike, windSpeed, conditions = getWeather()
            counetr = 0

        textTemp = font.render(f'{str(round(temp, 1))} {chr(8451)}', True, (255, 255, 255))
        text_x = 100
        text_y = 225
        screen.blit(textTemp, (text_x, text_y))

        textFeelsLike = font.render(f'{str(round(feelsLike, 1))} {chr(8451)}', True, (255, 255, 255))
        text_x = 100
        text_y = 325
        screen.blit(textFeelsLike, (text_x, text_y))

        textWindSpeed = font.render(f'{str(round(windSpeed, 1))} m/s', True, (255, 255, 255))
        text_x = 100
        text_y = 425
        screen.blit(textWindSpeed, (text_x, text_y))

        textConditions = font.render(str(conditions).capitalize(), True, (255, 255, 255))
        text_x = 100
        text_y = 525
        screen.blit(textConditions, (text_x, text_y))

        counetr += 1
        pygame.display.flip()
        clock.tick(120)

    pygame.quit()
