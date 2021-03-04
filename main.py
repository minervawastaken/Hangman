import pygame
from hangman.constants import WIDTH, HEIGHT
from hangman.drawing import Drawing

pygame.init()
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")


def main():
    global message
    global playing
    clock = pygame.time.Clock()
    graphic = Drawing()
    run = True
    
    while run:   
        run, message = graphic.win_lose() 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                graphic.collision()
              
        graphic.draw(WIN)
        pygame.display.update()

restart_graphic = Drawing()
playing = True
play = True
phase = 0

while playing:
    if play:
        main()

    play = False
    if phase % 2 == 1:
        restart_graphic.display_message(WIN, "Do you want to play again?")
    else:    
        restart_graphic.display_message(WIN, message)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            phase += 1 
            if (phase - 1) % 2 == 1:
                play = True

pygame.quit()


