import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.dimensions = 1200, 700
        self.bg_color = pygame.Color('#404040')

    def dims(self):
        return self.dimensions
