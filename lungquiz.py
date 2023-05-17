import pygame
import sys
import game
import Button
import lunganswer1
import lunganswer2
import lunganswer3


def quiz5():
    pygame.init()
    screen_width = 1150
    screen_height = 700
    screen = pygame.display.set_mode([screen_width, screen_height])
    background = pygame.image.load('Images/lung slide 1.png').convert()
    backgroundsize = pygame.transform.scale(background, (1150, 700))
    pygame.display.set_caption("Lungs Quiz")

    button_image = pygame.image.load("Images/quizbutton.png").convert_alpha()
    resized_button_image = pygame.transform.scale(button_image, (50, 50))


    running = True

    while running:
        mouse = pygame.mouse.get_pos()
        #text, color, font, x, y, image#

        option1_button = Button.Button("", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 210,
                                       310, resized_button_image)

        option2_button = Button.Button("", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 210,
                                       410, resized_button_image)

        option3_button = Button.Button("", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 210,
                                       510, resized_button_image)
        quit_button = Button.Button("Quit", (255,255,255), pygame.font.SysFont("Helvetica", 20), 450, 600, pygame.image.load("Images/button.png"))
        backtogame_button = Button.Button("Back to Game", (255,255,255), pygame.font.SysFont("Helvetica", 20), 650, 600, pygame.image.load("Images/button.png"))
        buttons = [quit_button, option1_button, option2_button, option3_button, backtogame_button]

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
                if option1_button.button_position(mouse):
                    lunganswer1.lunganswer1()
                if option2_button.button_position(mouse):
                    lunganswer2.lunganswer2()
                if option3_button.button_position(mouse):
                    lunganswer3.lunganswer3()
                if backtogame_button.button_position(mouse):
                    game.main()
        pygame.display.update()


if __name__ == "__main__":
    quiz5()