import numpy as np
import matplotlib.pyplot as plt

from skimage import data, color
from skimage.transform import hough_circle
from skimage.feature import peak_local_max, canny
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte
from PIL import Image
from skimage.io import imread
from skimage.color import rgb2gray

pic = imread("images/Image 8-2.jpg")

image = rgb2gray(pic) > 0.07
# image = np.invert(image)
fig2, ax2 = plt.subplots()

ax2.imshow(image, cmap=plt.cm.gray)

image = img_as_ubyte(image)

edges = canny(image, sigma=5, low_threshold=60, high_threshold=80)

fig2, ax2 = plt.subplots()

ax2.imshow(edges, cmap=plt.cm.gray)
# fig2, ax2 = plt.subplots()
#
# ax2.imshow(edges, cmap=plt.cm.gray)
plt.show()