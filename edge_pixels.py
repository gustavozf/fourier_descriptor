import numpy as np
import cv2

MAX_VALUE = 255

def get_8_neighbors_clockwise(img, pixel):
    i, j = pixel
    max_hei, max_wid = img.shape[:2]

    return [z for z in [
        (i-1, j),   # up
        (i-1, j+1), # top-right
        (i, j+1),   # right
        (i+1, j+1), # bottom-right
        (i+1, j),   # bottom
        (i+1, j-1), # bottom-left
        (i, j-1),   # left
        (i-1, j-1), # top-left
    ]
        if not False in [z[0] >= 0,
                         z[0] < max_hei,
                         z[1] >= 0,
                         z[1] < max_wid]
    ]


def is_edge_pixel(img, pixel):
    if img[pixel] <= 0:
        return False

    neighbors = get_8_neighbors_clockwise(img, pixel)

    # verifica quantos vizinhos de fundo existem
    return len([z for z in neighbors if img[z] == 0]) > 0


def get_neighbors(img, out_img, pixel):
    neighbors = get_8_neighbors_clockwise(img, pixel)

    # seleciona todos os vizinhos que nao foram vizitados ainda
    # e que sao pixeis de borda
    return [z for z in neighbors if (out_img[z] == 0 and is_edge_pixel(img, z))]


def find_first_white_pixel(img):
    hei, wid = img.shape[:2]

    for i in range(hei):
        for j in range(wid):
            if img[i, j] > 0:
                return (i, j)


def find_edge_pixels(img):
    global MAX_VALUE
    output_img = np.zeros(img.shape[:2], dtype=np.int32)
    output_list = []

    first_pixel = find_first_white_pixel(img)
    print(first_pixel)
    output_img[first_pixel] = MAX_VALUE
    output_list.append(first_pixel)

    neighbors = get_neighbors(img, output_img, first_pixel)

    #i = 0
    while neighbors:
        #print(neighbors)
        output_img[neighbors[0]] = MAX_VALUE
        #cv2.imwrite(f'out_{i}.png', output_img)
        output_list.append(neighbors[0])
        neighbors = get_neighbors(img, output_img, neighbors[0])

        #i += 1

    return np.array(output_list), output_img

