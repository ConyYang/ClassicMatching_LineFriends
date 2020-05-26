import pygame
from pygame import display, event, image
from PIL import Image

pygame.init()
display.set_caption('Line Friends Classical Matching')


screen_width = 512
screen_height = 512
screen = display.set_mode((screen_width, screen_height))

matched = image.load('otherAssets/matched.png')
image_info = Image.open('otherAssets/matched.png')
image_width = image_info.size[0]
image_heigt = image_info.size[1]
# print(image_width, image_heigt)

screen.blit(matched, ((0.5 * screen_width) - (0.5 *image_width), (0.5 * screen_height) - (0.5 *image_heigt)))
display.flip()

runnig = True

while runnig:
    current_events = event.get()

    for e in current_events:
       if e.type == pygame.QUIT:
            runnig = False

print("You quit the game")