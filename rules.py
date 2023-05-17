##TESTING WORK

import pygame
import pygame_gui

import game
import Button

import pygame_gui.data

from pygame.color import Color
from pygame.surface import Surface

from pygame_gui.elements.ui_text_box import UITextBox



def rules():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    ui_manager = pygame_gui.UIManager((800, 600), 'data/themes/theme_1.json')

    background = Surface((800, 600), depth=32)
    background.fill(Color("#FFFFFF"))

    text_box = UITextBox(
        html_text="<br><br>"
                  "<body><font color=#E0E080><b>Welcome to the Operations Game!</b> In this game, you will have the"
                  " opportunity to try out your surgery skills by removing assorted body parts, including the 'broken heart,"
                  " 'Adam's apple,' 'spare rib,' or the 'butterflies in stomach,'"
                  "<br><br>"
                  "<a href=It's time to learn about the rules.>It's time to learn about the rules.</a>"
                  "<br><br>"
                  "<b>Step 1:</b> Click on any body part that you want to learn about."
                  "<br><br>"
                  "Note: click on the 'Key' to check what body part each icon represents! "
                  "<br><br>"
                  "<b>Step 2:</b> Drag the body part into the red disposal bin."
                  "<br><br>"
                  "<b>Step 3:</b> Learn about some of the real world explanations as to why you may have to 'perform "
                  "surgery on' (or really just provide treatment for) this body part!"
                  "<br><br>"
                  "<b>Step 4:</b> Now press the button below to start playing the game!"
                  "<br><br>"
                  "Have fun :)"
                  "</font>",
        relative_rect=pygame.Rect(0, 0, 800, 800),
        manager=ui_manager)

    text_box.update(5.0)

    is_running = True

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        screen.blit(background, (0, 0))
        ui_manager.update(0.01)
        ui_manager.draw_ui(window_surface=screen)

        mouse = pygame.mouse.get_pos()
        begingame_button = Button.Button("Begin the Game!", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 400,
                                         500, pygame.image.load("Images/button.png"))

        buttons = [begingame_button]

        for b in buttons:
            screen.blit(b.image, b.rect)
            screen.blit(b.text, b.text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if begingame_button.button_position(mouse):
                    game.main()

        pygame.display.update()


if __name__ == "__main__":
    rules()
