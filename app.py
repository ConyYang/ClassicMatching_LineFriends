import pygame
from pygame import display, event, image
from PIL import Image
import game_config as gc
from lineFriends import Animal
from findIndex import find_index
from time import sleep

pygame.init()
display.set_caption('Line Friends Classical Matching')

screen_width = 512
screen_height = 800
FPS = 30
screen = display.set_mode((screen_width, screen_height))

matched = image.load('transferedImage/otherAssets/matched.png')
congrats = image.load('transferedImage/otherAssets/finish.png')
image_info = Image.open('transferedImage/otherAssets/matched.png')
image_width = image_info.size[0]
image_heigt = image_info.size[1]
# print(image_width, image_heigt)
clock = pygame.time.Clock()

running = True
friends = [Animal(i) for i in range(0, gc.Num_Pic_Total)]
current_friends = []

while running:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            if index not in current_friends:
                current_friends.append(index)
            if len(current_friends) > 2:
                current_friends = current_friends[1:]

    screen.fill((255, 255, 255))
    total_skipped = 0

    for _, friend in enumerate(friends):
        image_i = friend.friend_image if friend.index in current_friends else friend.box

        if not friend.skip:
            screen.blit(image_i,
                        (friend.col * gc.Image_Size + gc.Margin,
                         friend.row * gc.Image_Size + gc.Margin))
        else:
            total_skipped += 1

        display.flip()
        if len(current_friends) == 2:
            friend_1, friend_2 = current_friends
            if friends[friend_1].name == friends[friend_2].name:
                friends[friend_1].skip = True
                friends[friend_2].skip = True
                screen.blit(matched, (0, 530))
                display.flip()
                sleep(1)
                current_friends = []

        if total_skipped == len(friends):
            screen.blit(congrats, (0, 400))
            display.update()
            sleep(5)
            running = False

    clock.tick(FPS)

print("You quit the game")
