import random
import numpy as np

# Used to generate a 'random'(seeded) binary image
# given a shape and size
class Generator:
    def __init__(self, seed, shape):
        self.seed = seed
        self.rows = shape[1]
        self.cols = shape[0]
        random.seed(self.seed)

    def random_bin(self):
        rand_bin = random.random()
        return round(rand_bin)

    # Return the seeded image
    def generate_image(self):
        image = []

        for row in range(self.rows):
            for col in range(self.cols):
                image.append(self.random_bin())
        np_image = np.array(image).reshape((self.rows,self.cols))

        return np_image