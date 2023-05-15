##TESTING WORK

import pygame
import pygame_gui

import game

import pygame_gui.data

from pygame.color import Color
from pygame.surface import Surface

from pygame_gui.elements.ui_text_box import UITextBox



def rules():
    pygame.init()

    display_surface = pygame.display.set_mode((800, 600))

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
                  "<b>Step 1:</b> Click on any body part."
                  "<br><br>"
                  "<b>Step 2:</b> Drag the body part into the red disposal bin."
                  "<br><br>"
                  "<b>Step 3:</b> Learn about some of the real world explanations as to why you may have to perform "
                  "surgery on this body part!"
                  "<br><br>"
                  "Now press the red quit button for the start button so you can begin!"
                  "</font>",
        relative_rect=pygame.Rect(0, 0, 800, 800),
        manager=ui_manager)

    text_box.update(5.0)

    is_running = True

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        display_surface.blit(background, (0, 0))
        ui_manager.update(0.01)
        ui_manager.draw_ui(window_surface=display_surface)
        pygame.display.update()

if __name__ == "__main__":
    rules()
