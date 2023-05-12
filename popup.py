import pygame
import Button
pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill((0,0,255))
pygame.display.set_caption("Operation")

def main ():
    running = True
    while running:
        #text, color, font, x, y, image#
        start_button = Button.Button("Start", (255,255,255), pygame.font.SysFont("Helvetica", 20), 390, 395, pygame.image.load("Images/button.png"))
        instruction_button = Button.Button("Rules", (255,255,255), pygame.font.SysFont("Helvetica", 20), 390, 435, pygame.image.load("Images/button.png"))
        quit_button = Button.Button("Quit", (255,255,255), pygame.font.SysFont("Helvetica", 20), 390, 475, pygame.image.load("Images/button.png"))
        buttons = [start_button, instruction_button, quit_button]

        for b in buttons:
            screen.blit(b.image, b.rect)
            screen.blit(b.text, b.text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
        pygame.display.update()


if __name__ == "__main__":
    main()