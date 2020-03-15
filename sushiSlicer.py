import pygame

pygame.init()
display_width = 700
display_height = 300
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Sushi slicer")
white = (255, 255, 255)
green = (200, 225, 200)
rice_color = (220, 220, 200)
black = (0, 0, 0)


def gameLoop():
    gameOver = False
    sushi_width = 250
    sushi_height = 50
    knife = pygame.image.load('knife.png')
    sushi1 = pygame.image.load('sushi1.png')
    sushi1_head = pygame.image.load('sushi1head.png')
    board = pygame.image.load('board.png')
    while not gameOver:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameOver = True
        gameDisplay.fill(green)
        mouse_pos = pygame.mouse.get_pos()
        gameDisplay.blit(knife, (mouse_pos[0] - 80, 20))
        # outline of sushi

        # gameDisplay.blit(board, (display_width / 2 - 135, display_height / 2))
        gameDisplay.blit(sushi1, (display_width/2 - 135, display_height/2 - 31))
        # gameDisplay.blit(sushi1_head, (display_width / 2 - 135, display_height / 2 - 31))
        get_pressed = pygame.mouse.get_pressed()
        if get_pressed[0] == 1:
            if mouse_pos[0] > 50:
                print("hi")
        # print(pygame.mouse.get_pos())
        pygame.display.update()
    pygame.quit()
    quit()


gameLoop()
