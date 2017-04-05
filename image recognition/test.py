import numpy as np
from numpy import sin,pi
import matplotlib.pyplot as plt
import math


x_0 = 0
y_0 = 0
n_x,n_y = 3,4
l = 50




x = np.linspace(x_0, x_0+(n_x-1)*l, n_x, dtype=int)
x1 = np.linspace(x_0+l/2, x_0+((n_x-1)+0.5)*l, n_x, dtype=int)

y = np.linspace(y_0, y_0+(math.ceil((n_y)/2)-1)*2*l*sin(pi/3), math.ceil(n_y/2), dtype=int)

if n_y%2==0:
    y1 = np.linspace(y_0+l*sin(pi/3), y_0+l*sin(pi/3)+(math.ceil(n_y/2)-1)*2*l*sin(pi/3), math.ceil(n_y/2), dtype=int)
else:
    y1 = np.linspace(y_0+l*sin(pi/3), y_0+l*sin(pi/3)+(int((n_y)/2)-1)*2*l*sin(pi/3), int(n_y/2), dtype=int)

xv, yv = np.meshgrid(x, y)
# xv1, yv1 = np.meshgrid(x1, y1)
# fig, ax = plt.subplots()
# # ax.imshow(pic, cmap=plt.cm.gray)
# ax.plot(xv,yv,'or')
# ax.plot(xv1,yv1,'og')
#
# plt.show()
#
# print(x,y,"\n - \n")
#
from skimage.io import imread

pic = imread("images/Image 8-1.jpg")
a = []

print([xv,yv])
# for i in range(3):
#     for j in range(3):
#         a.append([xv+i,yv+j])
print(pic[[xv,yv],[xv+1,yv+1],[xv+2,yv+2]],"\n - \n")

print(pic[[xv,yv],[xv+1,yv+1],[xv+2,yv+2]][:,:,:,1])