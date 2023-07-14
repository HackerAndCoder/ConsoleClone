import pygame, config

class Object:
    def __init__(self, texture : pygame.Surface):
        self.texture = pygame.transform.scale(texture, (config.tile_size, config.tile_size))