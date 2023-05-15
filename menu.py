import pygame
import sys
import Button
import game
import rules


pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill((0,160,255))
pygame.display.set_caption("Operation")

pygame.font.init()
font = pygame.font.Font(None, 54)
text = font.render("Operations Game", True, (255, 255, 255))


def menu():
    running = True

    while running:
        mouse = pygame.mouse.get_pos()
        #text, color, font, x, y, image#
        start_button = Button.Button("Start", (255,255,255), pygame.font.SysFont("Helvetica", 20), 390, 370, pygame.image.load("Images/button.png"))
        instruction_button = Button.Button("Rules", (255,255,255), pygame.font.SysFont("Helvetica", 20), 390, 435, pygame.image.load("Images/button.png"))
        quit_button = Button.Button("Quit", (255,255,255), pygame.font.SysFont("Helvetica", 20), 390, 495, pygame.image.load("Images/button.png"))
        buttons = [start_button, instruction_button, quit_button]

        for b in buttons:
            screen.blit(b.image, b.rect)
            screen.blit(b.text, b.text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.button_position(mouse):
                    game.main()
                if instruction_button.button_position(mouse):
                    rules.rules()
                if quit_button.button_position(mouse):
                    ##note: I want to try to do something so that the text disappears when quit button pressed b
                    running = False
                    pygame.quit()
                    sys.exit()

        screen.blit(text, (240, 275))
        pygame.display.update()


if __name__ == "__main__":
    menu()