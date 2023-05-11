import pygame


class Item(pygame.sprite.Sprite):
    def __init__(self, image, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.click = False
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        if self.click:
            self.rect.x, self.rect.y = pygame.mouse.get_pos()

    def draw(self,screen):
        screen.blit(self.image, self.rect.topleft)