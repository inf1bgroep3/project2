import pygame
import time

pygame.init()

white = (255,255,250)
black = (0,0,0)
turquoise = (174,243,227)
coral = (255,127,80)
light_coral = (250,127,80)

gameDisplay = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Euromast')


cloudimg = pygame.image.load('background.png').convert()
gameDisplay.blit(cloudimg, (0, 0))
pygame.display.update()

pygame.draw.rect(gameDisplay, black, pygame.Rect (320, 195, 200, 40), 5)
pygame.draw.rect(gameDisplay, black, pygame.Rect (320, 295, 200, 40), 5)
pygame.draw.rect(gameDisplay, black, pygame.Rect (320, 395, 200, 40), 5)
pygame.draw.rect(gameDisplay, black, pygame.Rect (320, 495, 200, 40), 5)
pygame.display.update()

font1 = pygame.font.SysFont(None, 70)
font2 = pygame.font.SysFont(None, 50)

def message_to_screen1(msg, color):
    screen_text = font1.render(msg, True, color)
    gameDisplay.blit(screen_text, [65, 80])

def message_to_screen2(msg, color):
    screen_text = font2.render(msg, True, color)
    gameDisplay.blit(screen_text, [320, 500])

def message_to_screen3(msg, color):
    screen_text = font2.render(msg, True, color)
    gameDisplay.blit(screen_text, [320, 400])

def message_to_screen4(msg, color):
    screen_text = font2.render(msg, True, color)
    gameDisplay.blit(screen_text, [320, 300])

def message_to_screen5(msg, color):
    screen_text = font2.render(msg, True, color)
    gameDisplay.blit(screen_text, [320, 200])


message_to_screen1("HOW MANY PLAYERS?", coral)
message_to_screen2("4 PLAYERS", black)
message_to_screen3("3 PLAYERS", black)
message_to_screen4("2 PLAYERS", black)
message_to_screen5("1 PLAYER", black)
pygame.display.update()
time.sleep(2)



gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True


pygame.quit()
quit()

