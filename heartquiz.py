import pygame
import Button
import game
import rules


pygame.init()
pygame.init()
screen_width = 1150
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])
background = pygame.image.load('Images/heart slide 1.png').convert()
backgroundsize = pygame.transform.scale(background, (1150, 700))
pygame.display.set_caption("Operation")



def main():
    running = True

    while running:
        mouse = pygame.mouse.get_pos()
        #text, color, font, x, y, image#
        start_button = Button.Button("Start", (255,255,255), pygame.font.SysFont("Helvetica", 20), 390, 370, pygame.image.load("Images/button.png"))
        instruction_button = Button.Button("Rules", (255,255,255), pygame.font.SysFont("Helvetica", 20), 390, 435, pygame.image.load("Images/button.png"))
        quit_button = Button.Button("Quit", (255,255,255), pygame.font.SysFont("Helvetica", 20), 390, 495, pygame.image.load("Images/button.png"))
        buttons = [start_button, instruction_button, quit_button]

        for b in buttons:
            screen.blit(backgroundsize, (0, 0))
            screen.blit(b.image, b.rect)
            screen.blit(b.text, b.text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.button_position(mouse):
                   pass
                if instruction_button.button_position(mouse):
                   pass
                if quit_button.button_position(mouse):

                    running = False
        pygame.display.update()


if __name__ == "__main__":
    main()