#####################
# Author: Mikhaielh #
#####################


import random
from string import digits
from captcha.image import ImageCaptcha

# create a number
char = "".join(random.choice(digits) for i in range(4))

# create Obj
image = ImageCaptcha()

# create captcha and save it
image.write(char, "captcha.png")
