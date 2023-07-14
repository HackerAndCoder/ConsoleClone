import pygame
from settings import *

pygame.init()

class DisplayHandler:
    def __init__(self, dimensions, caption):
        self.display = pygame.display.set_mode(dimensions)
        pygame.display.set_caption(str(caption))
        self.objects = []
        self.events = []
    
    def add_object(self, object, pos):
        self.objects.append((object, pos))
    
    def remove_object(self, object):
        for i in range(len(self.objects)):
            if object in self.objects[i]:
                del self.objects[i]
    
    def get_objects(self):
        return self.objects

    def clear_objects(self):
        self.objects.clear()
    
    def get_event_queue(self):
        events = self.events.copy()
        self.events.clear()
        return events
    
    def tick(self):
        self.display.fill((255, 255, 255))
        for object in self.objects:
            self.display.blit(pygame.transform.scale(object[0].texture, translate_point(object[0].texture.get_size(), screen_modifier)), translate_point(object[1], tile_size * screen_modifier))
        pygame.display.flip()

        for event in pygame.event.get():
            self.events.append(event)

def translate_pos(pos1, mod = 8):
    return pos1 * mod

def translate_point(pos = (0, 0), mod = 2):
    final = []
    for num in pos:
        final.append(num * mod)
    return tuple(final)