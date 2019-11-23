import numpy as np
import cv2
import os
from edge_pixels import find_edge_pixels
from fft import to_complex_number, fft, complex_to_number

for img in os.listdir('./inputs'):
    print(f"Processando: {img}")

    x = cv2.imread('./inputs/' + img, 0)
    hei, wid = x.shape[:2]
    output_shape = np.zeros(x.shape[:2])

    list_edge, output_img = find_edge_pixels(x)

    complex_list = to_complex_number(list_edge)
    list_fourier = fft(complex_list, 20)
    output_list = complex_to_number(list_fourier)

    output_shape[output_list] = 255

    cv2.imwrite('./outputs/border_' + img, output_img)
    cv2.imwrite('./outputs/shape_' + img, output_shape)
    print(list_edge)
