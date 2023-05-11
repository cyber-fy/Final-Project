# This is a sample Python script.
import pygame
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pygame
from items import Item
from pygame import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION

pygame.init()
list_items = []
screen = pygame.display.set_mode((600, 900))
test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')
background = pygame.image.load('Images/backroundnew.jpeg').convert()
bin = pygame.image.load('Images/bin image.png').convert_alpha()
binsize = pygame.transform.scale(bin, (180, 190))


#Loop begins
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
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONUP:
            for item in list_items:
                item.click = False
        elif event.type == MOUSEBUTTONDOWN:
            for item in list_items:
                item.click = item.rect.collidepoint(event.pos)
    screen.blit(background, (0,0))
    screen.blit(binsize, (50, 40))
    for item in list_items:
        item.draw(screen)
        item.update()
    pygame.display.update()







