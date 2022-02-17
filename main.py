#!/usr/bin/python3

import cv2
import os
import sys
from os import walk
import numpy as np

# Function to get mean square error
def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err


# Verify the input format
if len(sys.argv) != 2 and len(sys.argv) != 5:
    print("Error!! ")
    print("Usage: python3 main.py videoinput.mp4 [hour minutes seconds]")
    sys.exit()

print("Starting.......")

files = []
for d in os.walk("."):
    files = d[1]
    break

if "material" in files:
    os.system("rm -r material")

# extract images from the video input file in regular intervals
os.system("mkdir material")
ext_cmd = "ffmpeg -i {} -r 0.033 material/image-%3d.jpeg".format(sys.argv[1])
if len(sys.argv) > 2:
    ext_cmd = "ffmpeg -i {} -r 0.033 -t {}:{}:{}.0 material/image-%3d.jpeg".format(
        sys.argv[1], sys.argv[2].zfill(2), sys.argv[3].zfill(2), sys.argv[4].zfill(2)
    )
os.system(ext_cmd)

for i in walk("material"):
    files = i[2]
    break
files.sort()

# crop the extracted images
for f in files:
    newf = "n" + f.split(".")[0]
    os.system(
        "convert material/{} -crop 581x434+153+186 material/{}.jpeg".format(f, newf)
    )
    os.system("rm material/{}".format(f))

for i in walk("material"):
    files = i[2]
    break
files.sort()

deleted = [0] * len(files)

# idea is that, if mse of 2 images is more than 100, then the 2 images are different
for j in range(1, len(files)):
    valid = 1
    for i in range(0, j):
        if deleted[i] == 1:
            continue
        img1 = cv2.imread("material/" + files[i], -1)
        img2 = cv2.imread("material/" + files[j], -1)
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        m = mse(img1, img2)
        if m < 100:
            valid = 0
            break
    if valid == 0:
        os.system("rm material/{}".format(files[j]))
        deleted[j] = 1


os.system("convert material/*jpeg material/mypdf.pdf")

print("Pdf generated: material/mypdf.pdf")
