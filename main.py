import numpy as np
import cv2
from edge_pixels import find_edge_pixels
from fft import to_complex_number, fft, complex_to_number

x = cv2.imread('1_binary.png', 0)
hei, wid = x.shape[:2]
output_shape = np.zeros(x.shape[:2])

list_edge, output_img = find_edge_pixels(x)
complex_list = to_complex_number(list_edge)
list_fourier = fft(complex_list, 20)
output_list = complex_to_number(list_fourier)

output_shape[output_list] = 255

cv2.imwrite('out.png', output_img)
cv2.imwrite('out_shape.png', output_shape)
print(list_edge)
