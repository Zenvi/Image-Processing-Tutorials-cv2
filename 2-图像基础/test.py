import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('./png_files/1.png', 0)

# def GetHist(image, normalize=False):
#     image = image.flatten()
#     image = image.tolist()
#     hist = []
#     for i in range(256):
#         current_bar = image.count(i)/len(image) if normalize else image.count(i)
#         hist.append(current_bar)
#
#     return hist
#
# hist = GetHist(image, normalize=True)

plt.figure()
# plt.subplot(121)
# plt.imshow(image, cmap='gray')
#
# plt.subplot(122)
hist = plt.hist(image.flatten(), bins=range(0,255))

plt.show()

