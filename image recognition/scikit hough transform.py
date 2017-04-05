import numpy as np
import matplotlib.pyplot as plt

from skimage import data, color
from skimage.transform import hough_circle
from skimage.feature import peak_local_max, canny
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte
from skimage.io import imread
from skimage.color import rgb2gray

# Load picture and detect edges
pic = imread("images/Image 8-1.jpg")

image = rgb2gray(pic) > 0.05
# image = np.invert(image)

image = img_as_ubyte(image)

edges = canny(image, sigma=5, low_threshold=80, high_threshold=100)


# fig2, ax2 = plt.subplots()
#
# ax2.imshow(edges, cmap=plt.cm.gray)

# Detect two radii
hough_radii = np.arange(20, 21, 1)
hough_res = hough_circle(edges, hough_radii)

centers = []
accums = []
radii = []

for radius, h in zip(hough_radii, hough_res):
    # For each radius, extract two circles
    num_peaks = 600
    peaks = peak_local_max(h, min_distance=10, num_peaks=num_peaks, threshold_rel=0.4)
    centers.extend(peaks)
    accums.extend(h[peaks[:, 0], peaks[:, 1]])
    radii.extend([radius] * num_peaks)

# Draw the most prominent 5 circles
image = color.gray2rgb(image)
for idx in np.argsort(accums)[::-1][:(len(accums)-1)]:
    center_x, center_y = centers[idx]
    radius = radii[idx]
    cx, cy = circle_perimeter(center_y, center_x, radius)
    # if max(cx)<1560 and max(cy)<1560:
    pic[cy, cx] = (220, 220, 20)

fig, ax = plt.subplots()
ax.imshow(pic, cmap=plt.cm.gray)

print(len(accums))

plt.show()
