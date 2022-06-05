# -*- encoding: utf-8 -*-
# Date: 05/Jun/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: Image operations
"""

import cv2


def loadImg(file, mode=cv2.IMREAD_COLOR, toRgb=True):
    return cv2.imread(file, mode)


def writeImg(img, filePath):
    cv2.imwrite(filePath, img)


def showImg(img, str='image', autoSize=False):
    flag = cv2.WINDOW_NORMAL
    if autoSize:
        flag = cv2.WINDOW_AUTOSIZE

    cv2.namedWindow(str, flag)
    cv2.imshow(str, img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getImgHW(img):
    return img.shape[0], img.shape[1]


def textImg(img, str, loc=None, color=(255, 0, 0), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, thickness=1):
    H, W = getImgHW(img)
    newImg = img.copy()
    textSize = cv2.getTextSize(str, fontFace, fontScale, thickness)
    if loc is None:
        loc = ((W - textSize[0][0]) // 2, (H + textSize[0][1]) // 2)
    return cv2.putText(newImg, str, loc, fontFace, fontScale, color, thickness, cv2.LINE_AA)


def rectangleImg(img, startPt, stopPt, color=(255, 0, 0), thickness=2):
    return cv2.rectangle(img, startPt, stopPt, color=color, thickness=thickness)


def main():
    pass


if __name__ == "__main__":
    main()
