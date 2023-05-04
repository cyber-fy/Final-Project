# This is a sample Python script.
import pygame
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

## PUSH
## 1. git add .i
## 2. git commit -m "type whatever message you want along with this"
## 3. git push

## PULL
## 1. git pull

import pygame

pygame.init()
screen = pygame.display.set_mode((600, 900))
test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')
background = pygame.image.load('Images/backroundnew.jpeg').convert()
bread = pygame.image.load('Images/bread.png').convert_alpha()
##game_surface = pygame.image.convert(background)
pygame.display.flip()
screen.blit(background, (50, 50))
pygame.display.update()


##testing message
##game surface
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    screen.blit(background,(0,0))
    screen.blit(bread,(300,520))
    pygame.display.update()

