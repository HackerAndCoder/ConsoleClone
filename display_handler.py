import pygame

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
        if object in self.objects:
            self.objects.remove(object)
    
    def get_objects(self):
        return self.objects
    
    def get_event_queue(self):
        events = self.events.copy()
        self.events.clear()
        return events
    
    def tick(self):
        self.display.fill((255, 255, 255))
        for object in self.objects:
            self.display.blit(object[0].texture, object[1])
        pygame.display.flip()

        for event in pygame.event.get():
            self.events.append(event)