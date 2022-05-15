# Importing Image class from PIL module
from PIL import Image

cut_line12_config = {'q': [0.35, 0.65], 'a': [0.35, 0.65]}
quality = 20


def reduce_compress(img: Image):
    w, h = img.size
    resize_ratio = 0.8
    img_out = img.resize((int(w * resize_ratio), int(h * resize_ratio)), Image.ANTIALIAS)
    return img_out


for prefix in ['q', 'a']:
    index = 1
    for num in range(1, 120):  # MAX_PAGE=119
        im = Image.open(f"page_images/{prefix}_{num:03}.jpg")
        width, height = im.size

        left = 0
        right = width
        line1 = height * cut_line12_config[prefix][0]
        line2 = height * cut_line12_config[prefix][1]

        im1 = reduce_compress(im.crop((left, 0, right, line1)))
        im2 = reduce_compress(im.crop((left, line1, right, line2)))
        im3 = reduce_compress(im.crop((left, line2, right, height)))

        im1.save(f"single_images/n2_q500_{prefix}{index:03}.jpg", optimize=True, quality=quality)
        index += 1
        im2.save(f"single_images/n2_q500_{prefix}{index:03}.jpg", optimize=True, quality=quality)
        index += 1
        im3.save(f"single_images/n2_q500_{prefix}{index:03}.jpg", optimize=True, quality=quality)
        index += 1
