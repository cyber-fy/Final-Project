import pygame
import ribquiz
import Button
import sys
import game


def ribanswer3():
    pygame.init()
    screen_width = 1150
    screen_height = 700
    screen = pygame.display.set_mode([screen_width, screen_height])
    background = pygame.image.load('Images/rib slide 4.png').convert()
    backgroundsize = pygame.transform.scale(background, (1150, 700))
    pygame.display.set_caption("Rib Answer 3")

    running = True

    while running:
        mouse = pygame.mouse.get_pos()
        quit_button = Button.Button("Quit", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 400, 600,
                                    pygame.image.load("Images/button.png"))
        backtogame_button = Button.Button("Back to Game", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 600,
                                          600, pygame.image.load("Images/button.png"))
        backtoheart_button = Button.Button("Back to Rib", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 800,
                                           600, pygame.image.load("Images/button.png"))
        buttons = [quit_button, backtogame_button, backtoheart_button]

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
                if backtoheart_button.button_position(mouse):
                    ribquiz.quiz6()
        pygame.display.update()


if __name__ == "__main__":
    ribanswer3()