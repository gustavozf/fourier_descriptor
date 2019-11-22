import numpy as np
import cv2

MAX_VALUE = 255


def is_edge_pixel(img, pixel):
    i, j = pixel
    max_hei, max_wid = img.shape[:2]

    neighbors = [z for z in [
        (i, j+1),  # right
        (i+1, j),  # down
        (i, j-1),  # left
        (i-1, j),  # up
    ]
        if not False in [z[0] >= 0,
                         z[0] < max_hei,
                         z[1] >= 0,
                         z[1] < max_wid]
    ]

    # verifica quantos vizinhos de fundo existem
    return len([z for z in neighbors if img[z] == 0]) > 0


def get_neighbors(img, out_img, pixel):
    i, j = pixel
    max_hei, max_wid = img.shape[:2]

    neighbors = [z for z in [
        (i, j+1),  # right
        (i+1, j),  # down
        (i, j-1),  # left
        (i-1, j),  # up
    ]
        if not False in [z[0] >= 0,
                         z[0] < max_hei,
                         z[1] >= 0,
                         z[1] < max_wid]
    ]

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

    while neighbors:
        print(neighbors)
        output_img[neighbors[0]] = MAX_VALUE
        output_list.append(neighbors[0])
        neighbors = get_neighbors(img, output_img, neighbors[0])

    cv2.imwrite('out.png', output_img)


x = cv2.imread('1.jpeg', 0)
x = MAX_VALUE - x
x = cv2.threshold(x, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
find_edge_pixels(x)
