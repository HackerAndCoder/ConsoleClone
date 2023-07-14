import display_handler, pygame

screen = display_handler.DisplayHandler((600, 600), 'Legacy game')

game_clock = pygame.time.Clock()

def get_image(path):
    return pygame.image.load(path)

def handle_events(events_list):
    for event in events_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

while True:
    game_clock.tick(30)
    screen.tick()
    events = screen.get_event_queue()
    handle_events(events)