import display_handler, pygame, file_handler
from objects import *
from settings import *

screen = display_handler.DisplayHandler((width_tiles * tile_size * screen_modifier, height_tiles * tile_size * screen_modifier), 'Legacy game')

game_clock = pygame.time.Clock()


def handle_events(events_list : list):
    '''
    This isn't a mandatory function to use but it helps to structure and organize your code.
    This function is responsible for the handling of all events, like keypresses.

    Args:
        events_list: a list of pygame events
    
    Returns:
        None
    '''
    for event in events_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

grass_texture = file_handler.get_texture('example')

test_sprite = Sprite([grass_texture])

screen.add_object(Object(grass_texture), (0, 0))
screen.add_sprite(test_sprite, 'test_sprite', (0, 0))

while True:
    game_clock.tick(30)
    screen.tick()
    events = screen.get_event_queue()
    handle_events(events)