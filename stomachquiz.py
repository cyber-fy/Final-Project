import pygame
import Button
import game
import rules



def quiz2():
    pygame.init()
    screen_width = 1150
    screen_height = 700
    screen = pygame.display.set_mode([screen_width, screen_height])
    background = pygame.image.load('Images/stomach slide 1.png').convert()
    backgroundsize = pygame.transform.scale(background, (1150, 700))
    pygame.display.set_caption("Stomach Quiz")
    running = True

    while running:
        mouse = pygame.mouse.get_pos()
        #text, color, font, x, y, image#
        quit_button = Button.Button("Quit", (255,255,255), pygame.font.SysFont("Helvetica", 20), 600, 600, pygame.image.load("Images/button.png"))
        buttons = [quit_button]

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
        pygame.display.update()


if __name__ == "__main__":
    quiz2()