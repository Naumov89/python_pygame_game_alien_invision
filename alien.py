
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Класс, представляющий одного пришельца.'''

    def __init__(self, ai_game):
        '''Инициализирует пришельца и задает его начальную позицию.'''
        super().__init__()
        self.screen = ai_game.screen
        self.setings = ai_game.settings

        # Загрузка изображения пришельца и назнаение атрибута rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect() 

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранения точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)

    def check_edges(self):
        '''Возвращает True, если пришелец находиться у края экрана.'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True
    
    def update(self):
        '''Перемещает прешельцев вправо.'''
        self.x += (self.setings.alien_speed * self.setings.fleet_direction)
        self.rect.x = self.x
