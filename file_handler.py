import pygame, os

def get_texture(img_name : str):
    '''
    Get the contents of the specified image from the assets folder

    Args:
        img_name: the name (no extension) for the texture or image you want
        
    Returns:
        pygame.Surface object
    '''
    return pygame.image.load(os.path.join('assets', img_name + '.png'))