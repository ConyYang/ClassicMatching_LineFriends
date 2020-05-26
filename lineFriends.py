import os
import random

import game_config as gc

from pygame import image, transform

friend_count = dict((picture, 0) for picture in gc.asset_files)


# print(animal_count)

def available_friends():
    return [friend_name for friend_name, available_friend in friend_count.items() if available_friend < 2]


class Animal(object):
    def __init__(self, index):
        self.index = index
        self.row = index // gc.Num_Pic_Side
        self.col = index % gc.Num_Pic_Side
        self.name = random.choice(available_friends())
        friend_count[self.name] += 1

        self.image_path = os.path.join(gc.asset_dir, self.name)
        self.friend_image = image.load(self.image_path)
        self.friend_image_scale = transform.scale(self.friend_image, (gc.Image_Size - 2*gc.Margin,
                                                                      gc.Image_Size - 2*gc.Margin))

        self.box = self.friend_image_scale.copy()
        self.box.fill((230, 230, 230))

        self.skip =False




