# -*- coding: utf-8 -*-
from PIL import Image


def main():
    im = Image.open('./westbrook.jpg')
    pixel_access = im.load()

    new_im = Image.new(im.mode, im.size)
    new_pixel_access = new_im.load()
    width, height = im.size
    for i in range(width):
        for j in range(height):
            rgb = pixel_access[i, j]
            new_rgb = tuple([color // 2 for color in rgb])
            new_pixel_access[i, j] = new_rgb
    new_im.save(f'Q2.jpg', im.format)


if __name__ == '__main__':
    main()
