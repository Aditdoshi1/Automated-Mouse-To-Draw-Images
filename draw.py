import cv2
import pyautogui
import time
import numpy as np

image = cv2.imread('C:\\Users\\aditd\\Desktop\\Draw\\12.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

pyautogui.FAILSAFE = True

# Set threshold level
threshold_level = 50

# Find coordinates of all pixels below threshold
coords = np.column_stack(np.where(gray < threshold_level))
print(coords)
##x = 67

time.sleep(3)
c = 0
for i in coords:
	co = str(coords[c])
	a = co.split(" ")
	b = len(a)
	if b == 2:
		p = a[0]
		x1 = int(p[1:])
		q = a[1].rsplit(']')
		y1 = int(q[0])
		print(x1)
		print(y1)
		pyautogui.click(x=x1, y=y1) 
	elif b == 3:
		x = int(a[1])
		y = a[2].rsplit(']')
		y1 = int(y[0])
		print(x)
		print(y1)
		pyautogui.click(x, y=y1)
	c = c+5