import pygame, settings

class Object:
    '''
    The class for storing textures to display on screen
    '''
    def __init__(self, texture : pygame.Surface):
        '''
        Args:
            texture: A pygame.Surface object with the texture for the object. WARNING: TEXTURE WILL BE RESIZED TO SETTINGS.TILE_SIZE
        
        Returns:
            None
        '''
        self.texture = pygame.transform.scale(texture, (settings.tile_size, settings.tile_size))

class Sprite(Object):
    '''
    A class for storing textures for displaying on-screen. Use this class for textures that won't be background or static, like players or animated textures
    '''
    def __init__(self, textures):
        '''
        Args:
            textures: A list of pygame.Surface objects with the texture for the object. WARNING: TEXTURE WILL BE RESIZED TO SETTINGS.TILE_SIZE
        
        Returns:
            None
        '''
        self.textures = textures
        self.animation_frame = 0
        self.texture = textures[self.animation_frame]
    
    def set_animation_frame(self, index):
        if index < len(self.textures):
            self.animation_frame = index
            self.texture = self.textures[self.animation_frame]
            return True
        return False