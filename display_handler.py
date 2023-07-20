import pygame
from settings import *
import objects

pygame.init()

class DisplayHandler:
    def __init__(self, dimensions, caption):
        self.display = pygame.display.set_mode(dimensions)
        pygame.display.set_caption(str(caption))
        self.objects = []
        self.events = []
        self.sprites = {}

    def add_sprite(self, sprite : objects.Sprite, local_name : str, pos = (0, 0)):
        '''
        Adds a sprite to the screen
        
        A sprite is like an object but it can be positioned per pixel instead of grid row/column and is easily moved around
        
        Args:
            sprite: the sprite object to be added
            local_name: the name of the sprite that will be used to access the sprite later. Will overide other sprites with the same local name
            pos: the initial position of the sprite
        '''
        self.sprites[local_name] = [sprite, pos]
    
    def get_sprites(self):
        '''
        Returns a list of all the screen's sprites
        '''
        return self.sprites
    
    def get_sprite(self, local_name):
        if self.sprites[local_name]:
            return self.sprites[local_name][0]
        return None
    
    def set_sprite(self, local_name, sprite : objects.Sprite):
        self.sprites[local_name][0] = objects

    def set_sprite_pos(self, local_name, pos = (0, 0)):
        self.sprites[local_name][1] = pos

    def set_sprite_animation_frame(self, local_name, frame):
        self.sprites[local_name][0].set_animation_frame(frame)
    
    def add_object(self, object, pos):
        '''
        Adds an object to the screen
        
        Args:
            object: the object to be added
            pos: where you want to render the object
        '''
        self.objects.append((object, pos))
    
    def remove_object(self, object):
        '''
        If the list of screen objects contains object, remove it from the list and return True. Otherwise return False
        Args:
            object: the object you want to remove
        
        Returns:
            bool: whether the object was found and removed
        '''
        for i in range(len(self.objects)):
            if object in self.objects[i]:
                del self.objects[i]
                return True
        return False
    
    def get_objects(self):
        '''
        Returns the list of objects the screen is to display.
        '''
        return self.objects

    def clear_objects(self):
        self.objects.clear()
    
    def get_event_queue(self):
        '''
        Returns a queue of the unhandled events
        '''
        events = self.events.copy()
        self.events.clear()
        return events
    
    def tick(self):
        '''
        Calls a game tick for the screen renderer. Updates the screen and updates the event queue.
        '''
        self.display.fill((255, 255, 255))
        for object in self.objects:
            self.display.blit(pygame.transform.scale(object[0].texture, translate_point(object[0].texture.get_size(), screen_modifier)), translate_point(object[1], tile_size * screen_modifier))
        for key in self.sprites.keys():
            sprite = self.sprites[key]
            self.display.blit(pygame.transform.scale(sprite[0].texture, translate_point(object[0].texture.get_size(), screen_modifier)), (sprite[1][0] * screen_modifier, sprite[1][1] * screen_modifier))
        pygame.display.flip()

        for event in pygame.event.get():
            self.events.append(event)

def translate_pos(num, mod = 8):
    '''
    It functions like the translate_point function, but takes and returns only one number. Useful when you don't want to have to strip a tuple for one digit
    
    Args:
        num: A number that you want to be translated
        mod: The amount you want to translate the num argument
    Returns:
        num x mod
    '''
    return num * mod

def translate_point(pos = (0, 0), mod = 2):
    '''
    Translates the specified pos by the modifier argument
    
    Args:
        pos: a tuple or list of numbers of any length
    
    Returns:
        A tuple of the same length as the pos argument, with every value translated by the modifier
    
    
    For example, if pos is 13, 5 the function would return 13 x modifier and 5 x modifier as a tuple
        
    '''
    final = []
    for num in pos:
        final.append(num * mod)
    return tuple(final)