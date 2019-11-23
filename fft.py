import numpy as np

def complex_to_number(list_ifft):
    return np.array([(int(num.real), int(num.imag)) for num in list_ifft])

def to_complex_number(list_edge):
    return np.array([complex(pixel[0], pixel[1]) for pixel in list_edge])

def fft(complex_list, freq_max):
    fft_list = np.fft.fft(complex_list)
    fft_shift = np.fft.fftshift(fft_list)
    # Passa-baixa
    fft_shift[fft_shift > freq_max] = 0
    fft_ishift = np.fft.ifftshift(fft_shift)
    return np.fft.ifft(fft_ishift)
    
    