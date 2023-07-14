import display_handler, pygame, os
from object import *
from config import *

screen = display_handler.DisplayHandler((width_tiles * tile_size * screen_modifier, height_tiles * tile_size * screen_modifier), 'Legacy game')

game_clock = pygame.time.Clock()

def get_image(img_name):
    return pygame.image.load(os.path.join('assets', img_name + '.png'))

def handle_events(events_list):
    for event in events_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

ground_texture = get_image('grass')

ground = Object(ground_texture)

screen.add_object(ground, (1, 0))
screen.add_object(ground, (0, 0))

while True:
    game_clock.tick(30)
    screen.tick()
    events = screen.get_event_queue()
    handle_events(events)