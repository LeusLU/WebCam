#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cv2

classfier = cv2.CascadeClassifier("/root/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml")

def overlay_image_alpha(img, img_overlay, pos, alpha_mask):
    """Overlay img_overlay on top of img at the position specified by
    pos and blend using alpha_mask.

    Alpha mask must contain values within the range [0, 1] and be the
    same size as img_overlay.
    """

    x, y = pos

    # Image ranges
    y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
    x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

    # Overlay ranges
    y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
    x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

    # Exit if nothing to do
    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return

    channels = img.shape[2]

    alpha = alpha_mask[y1o:y2o, x1o:x2o]
    alpha_inv = 1.0 - alpha

    for c in range(channels):
        img[y1:y2, x1:x2, c] = (alpha * img_overlay[y1o:y2o, x1o:x2o, c] +
                                alpha_inv * img[y1:y2, x1:x2, c])

while True:
    mark = cv2.imread("/root/camera-01/mark.png", -1)
    if mark == None: continue
    if mark.shape == None: continue
    frame = cv2.imread("/root/camera-01/update-capture.jpg")
    if frame == None: continue
    if frame.shape == None: continue
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
    if len(faceRects) > 0:
        for faceRect in faceRects:
            x, y, w, h = faceRect

            x_offset = x - 20
            y_offset = y - 20

            if w > h:
                mark = cv2.resize(mark, (w + 40, w + 40))
            else:
                mark = cv2.resize(mark, (h + 40, h + 40))

            overlay_image_alpha(frame,
                mark[:, :, 0:3],
                (x_offset, y_offset),
                mark[:, :, 3] / 255.0)
    cv2.imwrite("/root/camera-01/opencv.jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

cap.release()
