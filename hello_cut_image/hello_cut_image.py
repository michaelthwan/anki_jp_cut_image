# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"test_cut.png")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
left = 0
right = width
line1 = height * 0.4
line2 = height * 0.7

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, 0, right, line1))
im2 = im.crop((left, line1, right, line2))
im3 = im.crop((left, line2, right, height))

# Shows the image in image viewer
# im1.show()
# im2.show()
# im3.show()

im1.save("cut_q1.png")
im2.save("cut_q2.png")
im3.save("cut_q3.png")
