import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship_pic.bmp')
        self.offset = 141   #image offset 
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        #storing a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        

        #Movement flag

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right -self.offset < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left +self.offset > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x


    def blitme(self):
        self.screen.blit(self.image, self.rect)