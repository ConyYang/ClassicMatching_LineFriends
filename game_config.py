import os

Image_Size = 128
Screen_Size = 512
Num_Pic_Side = 4
Num_Pic_Total = 16
Margin = 4

asset_dir = 'assets'
asset_files = [pictures for pictures in os.listdir(asset_dir)
               if pictures[-3:].lower() == 'png']
# print(asset_files)
