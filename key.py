import pygame
import Button
import sys
import game


def key():
    pygame.init()
    screen_width = 500
    screen_height = 400
    screen = pygame.display.set_mode([screen_width, screen_height])
    button_image = pygame.image.load("Images/quizbutton.png").convert_alpha()
    resized_button_image = pygame.transform.scale(button_image, (50, 50))
    background = pygame.image.load('Images/key slide.jpeg').convert()
    backgroundsize = pygame.transform.scale(background, (500, 400))
    pygame.display.set_caption("Stomach Answer 1")

    running = True

    while running:
        mouse = pygame.mouse.get_pos()
        quit_button = Button.Button("Quit", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 120, 40,
                                    pygame.image.load("Images/button.png"))
        backtogame_button = Button.Button("Back to Game", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 400,
                                          40, pygame.image.load("Images/button.png"))

        buttons = [quit_button, backtogame_button]

        screen.blit(backgroundsize, (0, 0))

        for b in buttons:
            screen.blit(b.image, b.rect)
            screen.blit(b.text, b.text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.button_position(mouse):
                    running = False
                    pygame.quit()
                    sys.exit()
                if backtogame_button.button_position(mouse):
                    game.main()
        pygame.display.update()



if __name__ == "__main__":
    key()