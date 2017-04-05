import numpy as np
import matplotlib.pyplot as plt


from skimage.io import imread

# Load picture and detect edges
pic = imread("images/Image 8-1.jpg")

px_size = 7.3395    #px/um
n = [23,23] #[nx,ny]

burst = []
intact = []

for xs in np.linspace(30, 1500, 23):
    for ys in np.linspace(8, 1510, 14):
        mean = np.mean(pic[int(ys):int(ys+10),int(xs):int(xs+10),1])

        if mean > 90:
            burst.append(mean)
        else:
            intact.append(mean)

for xs in np.linspace(66, 1535, 23):
    for ys in np.linspace(66, 1455, 13):
        mean = np.mean(pic[int(ys):int(ys + 10), int(xs):int(xs + 10),1])

        if mean > 90:
            burst.append(mean)
        else:
            intact.append(mean)


# fig, ax = plt.subplots()
# ax.imshow(pic, cmap=plt.cm.gray)
#
# plt.show()

print(len(burst), len(intact))