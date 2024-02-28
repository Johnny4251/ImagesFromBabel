import cv2
import numpy as np
from generator import Generator

# compute string->integer use ord()
def text_to_seed(text):
    seed = 0
    for i,c in enumerate(text): seed += ord(c)
    return seed

# returns list of the decimal values
# on each binary row in image.
def get_bit_pattern(img):
    bit_pattern = []
    for row in range(len(img[0])):
        decimal_number = 0
        row_bin = img[row]
        for i in range(len(row_bin)):
            decimal_number += row_bin[i] * 2 ** (len(row_bin) - i - 1)
        bit_pattern.append(decimal_number)
    return bit_pattern

# Example usage
def main():
    text = input("seed: ")
    seed = text_to_seed(text)
    print(f"Seed is {seed}")
    
    size = (900,900)

    gen = Generator(seed, size)
    img = gen.generate_image()
    print("Img shape: ", img.shape)

    # Could be used as an image label
    pattern = get_bit_pattern(img)
    print(f"Bit pattern: {pattern}")

    img = img.astype(np.float32)

    cv2.imshow('Generated Image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()