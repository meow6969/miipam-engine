import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import standard


pygame.display.set_caption("Rika-chan Engine")
pygame.display.set_icon(pygame.image.load('content/icon.png'))
w = pygame.display.set_mode([640, 480])

# sound
pygame.mixer.init()
pygame.mixer.music.load("content/msysri.ogg")
pygame.mixer.music.set_volume(.2)
pygame.mixer.music.play(-1)

pygame.font.init()
# pygame.mixer.pause()
standard.main_menu(w)

