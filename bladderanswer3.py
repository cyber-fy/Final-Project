import pygame
import bladderquiz
import Button
import sys
import game
import rules

def bladderanswer3():
    pygame.init()
    screen_width = 1150
    screen_height = 700
    screen = pygame.display.set_mode([screen_width, screen_height])
    background = pygame.image.load('Images/bladder slide 2.png').convert()
    backgroundsize = pygame.transform.scale(background, (1150, 700))
    pygame.display.set_caption("Bladder Answer 3")

    running = True

    while running:
        mouse = pygame.mouse.get_pos()
        quit_button = Button.Button("Quit", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 400, 650,
                                    pygame.image.load("Images/button.png"))
        backtogame_button = Button.Button("Back to Game", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 600,
                                          650, pygame.image.load("Images/button.png"))
        backtobladder_button = Button.Button("Back to Bladder", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 800,
                                           650, pygame.image.load("Images/button.png"))
        buttons = [quit_button, backtogame_button, backtobladder_button]


        screen.blit(backgroundsize, (0, 0))
        for b in buttons:
            screen.blit(b.image, b.rect)
            screen.blit(b.text, b.text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.button_position(pygame.mouse.get_pos()):
                    running = False
                    pygame.quit()
                    sys.exit()
                if backtogame_button.button_position(mouse):
                    game.main()
                if backtobladder_button.button_position(mouse):
                    bladderquiz.quiz3()
        pygame.display.update()


if __name__ == "__main__":
    bladderanswer3()