import pygame
import heartquiz
import stomachquiz
import bladderquiz
import throatquiz
import ribquiz
import lungquiz
import Button
import key
from items import Item
from pygame import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION

def main():
    pygame.init()
    list_items = []
    screen = pygame.display.set_mode((600, 900))
    background = pygame.image.load('Images/backroundnew.jpeg').convert()
    bin = pygame.image.load('Images/bin image.png').convert_alpha()
    binsize = pygame.transform.scale(bin, (180, 190))
    ping_sound = pygame.mixer.Sound("Images/Ping sound effect.mp3")
    collision_status = {}

    #step 1: load the image
    bread = pygame.image.load('Images/bread.png').convert_alpha()
    butterfly = pygame.image.load('Images/butterfly.png').convert_alpha()
    apple = pygame.image.load('Images/apple.png').convert_alpha()
    heart = pygame.image.load('Images/heart icon.png').convert_alpha()
    bone = pygame.image.load('Images/crayon.png').convert_alpha()
    rib = pygame.image.load('Images/bone icon.png').convert_alpha()
    ankle = pygame.image.load('Images/rubber band icon.png').convert_alpha()
    wishbone = pygame.image.load('Images/wish bone.png').convert_alpha()
    horse = pygame.image.load('Images/charlie horse.png').convert_alpha()
    funnybone = pygame.image.load('Images/funny bone icon.png').convert_alpha()
    pail = pygame.image.load('Images/bucket.png').convert_alpha()
    wrench = pygame.image.load('Images/wrench.png').convert_alpha()

    #Step 2: scale the image as needed
    smallbread= pygame.transform.scale(bread, (50, 50))
    smallbutterfly = pygame.transform.scale(butterfly, (50, 50))
    smallbutterflyrotate= pygame.transform.rotate(smallbutterfly, 20)
    smallapple = pygame.transform.scale(apple, (35, 35))
    smallheart = pygame.transform.scale(heart, (60, 40))
    smallheartrotate= pygame.transform.rotate(smallheart, -20)
    smallbone = pygame.transform.scale(bone, (25, 65))
    smallbonerotate= pygame.transform.rotate(smallbone, -155)
    smallrib = pygame.transform.scale(rib, (50, 70))
    smallribrotate= pygame.transform.rotate(smallrib, 95)
    smallankle = pygame.transform.scale(ankle, (50, 135))
    smallanklerotate= pygame.transform.rotate(smallankle, 0)
    smallwishbone = pygame.transform.scale(wishbone, (65, 65))
    smallwhishrotate= pygame.transform.rotate(smallwishbone, 30)
    smallhorse = pygame.transform.scale(horse, (55, 55))
    smallhorserotate= pygame.transform.rotate(smallhorse, 15)
    smallfunny = pygame.transform.scale(funnybone, (40, 40))
    smallfunnyrotate= pygame.transform.rotate(smallfunny, 10)
    smallpail = pygame.transform.scale(pail, (80, 80))
    smallpailrotate= pygame.transform.rotate(smallpail, -10)
    smallwrench = pygame.transform.scale(wrench, (95, 25))
    smallwrenchrotate= pygame.transform.rotate(smallwrench, -50)


    #Step 3: initialize the object as item in a certain position
    smallbread_item = Item(smallbread,355,540)
    smallbutterfly_item = Item(smallbutterflyrotate,365,448)
    smallapple_item = Item(smallapple, 355, 265)
    smallheart_item = Item(smallheartrotate, 400, 345)
    smallbone_item = Item(smallbonerotate, 505, 467)
    smallrib_item = Item(smallribrotate, 313, 402)
    smallankle_item = Item(smallanklerotate, 310, 715)
    smallwishbone_item = Item(smallwhishrotate, 340, 330)
    smallhorse_item = Item(smallhorserotate, 293, 615)
    smallfunny_item = Item(smallfunnyrotate, 240, 385)
    smallpail_item = Item(smallpailrotate, 385, 670)
    smallwrench_item = Item(smallwrenchrotate, 390, 775)


    #Step 4: Append the item into list of items
    list_items.append(smallbread_item)
    list_items.append(smallbutterfly_item)
    list_items.append(smallapple_item)
    list_items.append(smallheart_item)
    list_items.append(smallbone_item)
    list_items.append(smallrib_item)
    list_items.append(smallankle_item)
    list_items.append(smallwishbone_item)
    list_items.append(smallhorse_item)
    list_items.append(smallfunny_item)
    list_items.append(smallpail_item)
    list_items.append(smallwrench_item)
    pygame.display.flip()

    #Initialize coordinates of area
    bin_rect = pygame.Rect(40, 40, 100, 100)

    ##Button for key
    button_image = pygame.image.load("Images/quizbutton.png").convert_alpha()
    resized_button_image = pygame.transform.scale(button_image, (100, 100))

    running = True
    while running:
        mouse = pygame.mouse.get_pos()

        screen.blit(background, (0, 0))
        screen.blit(binsize, (50, 40))

        keybutton = Button.Button("KEY", (255, 255, 255), pygame.font.SysFont("Helvetica", 20), 500,
                                  100, resized_button_image)
        buttons = [keybutton]

        for b in buttons:
            screen.blit(b.image, b.rect)
            screen.blit(b.text, b.text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONUP:
                for item in list_items:
                    item.click = False
            elif event.type == MOUSEBUTTONDOWN:
                for item in list_items:
                    item.click = item.rect.collidepoint(event.pos)
                if keybutton.button_position(mouse):
                    key.key()

        for item in list_items:
            item.draw(screen)
            item.update()
            if bin_rect.colliderect(item.rect) and not collision_status.get(item, False):
                pygame.mixer.Sound.play(ping_sound)
                collision_status[item] = True
            if bin_rect.colliderect(smallbread_item):
                pygame.mixer.Sound.play(ping_sound)
                score = 1
                running = False
                bladderquiz.quiz3()
            if bin_rect.colliderect(smallbutterfly_item):
                pygame.mixer.Sound.play(ping_sound)
                score = 1
                running = False
                stomachquiz.quiz2()
            if bin_rect.colliderect(smallapple_item):
                pygame.mixer.Sound.play(ping_sound)
                score = 1
                running = False
                throatquiz.quiz4()
            if bin_rect.colliderect(smallheart_item):
                pygame.mixer.Sound.play(ping_sound)
                score = 1
                running = False
                heartquiz.quiz1()
            if bin_rect.colliderect(smallrib_item):
                pygame.mixer.Sound.play(ping_sound)
                score = 1
                running = False
                ribquiz.quiz6()
            if bin_rect.colliderect(smallwishbone_item):
                pygame.mixer.Sound.play(ping_sound)
                score = 1
                running = False
                lungquiz.quiz5()
        pygame.display.update()


if __name__ == "__main__":
    main()