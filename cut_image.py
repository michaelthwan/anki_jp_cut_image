# Importing Image class from PIL module
from PIL import Image

#n2
# cut_line12_config = {'q': [0.35, 0.65], 'a': [0.35, 0.65]}
#n1
cut_line12_config = {'q': [0.42, 0.622], 'a': [0.42, 0.622]}
right_ratio = 0.61
quality = 20


def reduce_compress(img: Image):
    w, h = img.size
    resize_ratio = 0.8
    img_out = img.resize((int(w * resize_ratio), int(h * resize_ratio)), Image.ANTIALIAS)
    return img_out


for prefix in ['q', 'a']:
    index = 1
    MAX_PAGE = 119
    # MAX_PAGE = 2
    for num in range(1, MAX_PAGE+1):  #
        im = Image.open(f"page_images_n1/{prefix}_{num:03}.jpg")
        width, height = im.size

        left = 0
        right = width * right_ratio
        line1 = height * cut_line12_config[prefix][0]
        line2 = height * cut_line12_config[prefix][1]

        im1 = reduce_compress(im.crop((left, height*0.217, right, line1)))
        im2 = reduce_compress(im.crop((left, line1, right, line2)))
        im3 = reduce_compress(im.crop((left, line2, right, height*0.82)))

        im1.save(f"single_images_n1/n1_q500_{prefix}{index:03}.jpg", optimize=True, quality=quality)
        index += 1
        im2.save(f"single_images_n1/n1_q500_{prefix}{index:03}.jpg", optimize=True, quality=quality)
        index += 1
        im3.save(f"single_images_n1/n1_q500_{prefix}{index:03}.jpg", optimize=True, quality=quality)
        index += 1
