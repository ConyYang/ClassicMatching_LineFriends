import pygame
from pygame import display, event, image
from PIL import Image
import game_config as gc
from lineFriends import Animal

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

# screen.blit(matched, ((0.5 * screen_width) - (0.5 *image_width), (0.5 * screen_height) - (0.5 *image_heigt)))
# display.flip()

running = True
friends = [Animal(i) for i in range(0, gc.Num_Pic_Total)]
print(friends)

while running:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

    screen.fill((197, 199, 196))

    for friend in friends:
        screen.blit(friend.friend_image,
                    (friend.col * gc.Image_Size,
                     friend.row * gc.Image_Size))
    display.flip()
print("You quit the game")
