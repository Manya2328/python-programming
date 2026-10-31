# Image Processing Using NumPy
import numpy as np
img = np.array([[10, 50, 100, 150],
                [20, 60, 110, 160],
                [30, 70, 120, 170],
                [40, 80, 130, 180]])
print("Original image:\n", img)
print("\nReshaped to 2x8:\n", img.reshape(2, 8))
print("\nFlattened to 1D:\n", img.flatten())

print("\nCentre 2x2 region:\n", img[1:3, 1:3])
print("\nFirst row:", img[0])
print("Last column:", img[:, -1])

bright = np.clip(img + 100, 0, 255)
dark = np.clip(img - 50, 0, 255)
print("\nBrighter (+100):\n", bright)
print("\nDarker (-50):\n", dark)

flip = np.fliplr(np.eye(4, dtype=int))  
print("\nHorizontal flip (img @ flip):\n", img @ flip)
print("\nVertical flip (flip @ img):\n", flip @ img)
