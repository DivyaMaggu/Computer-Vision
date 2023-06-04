import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle",circle)

# Bitwise-AND --> returns intersecting region
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("BITWISE-AND",bitwise_and)

# Bitwise-OR --> returns both the intersecting and non-intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("BITWISE-OR",bitwise_or)

# BItwise-XOR --> returns only the non-intersecting region
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("BITWISE-XOR",bitwise_xor)

# Bitwise-NOT --> inverts the binary pixels (1(white) if 0(black) and 0(black) if 1(white))
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("BITWISE-NOT",bitwise_not)

cv.waitKey(0)