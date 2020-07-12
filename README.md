# Automated-Mouse-To-Draw-Images
Automated Mouse Bot will draw any image passed to the function in MS-Paint.

The logic behind this is, any image that is passed to the python function should be converted to Greyscale image, this greyscale image will be used to detect borders and black pixels below the threshold value 50. And the cordinates of each pixel will be stored in an array. This Cordinate Array will then be passed to the PYAUTOGUI.click function will click each on cordinates present in the array list and will create an image.
Works best with images with only black, white and grey colours as the greyscale convertion is not so accurate with coloured Images.
You can find video explaination here - https://www.linkedin.com/feed/update/urn:li:activity:6688217034670637057/
