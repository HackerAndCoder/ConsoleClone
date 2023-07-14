import pygame, settings

class Object:
    def __init__(self, texture : pygame.Surface):
        self.texture = pygame.transform.scale(texture, (settings.tile_size, settings.tile_size))

class Sprite:
    def __init__(self, texture : pygame.Surface):
        self.texture = pygame.transform.scale(texture, (settings.tile_size, settings.tile_size))