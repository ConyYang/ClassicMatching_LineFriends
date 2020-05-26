import game_config as gc


def find_index(x_pos, y_pos):
    row = y_pos // gc.Image_Size
    col = x_pos // gc.Image_Size
    index = row * gc.Num_Pic_Side + col
    return index
