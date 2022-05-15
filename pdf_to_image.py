# import module
from pdf2image import convert_from_path
import math

# {<week>: [<base_num>, <#page>]}
week_config = {1: [0, 60], 2: [30, 60], 3: [60, 58], 4: [89, 60]}

# Store Pdf with convert_from_path function
for key, value in week_config.items():
    images = convert_from_path(f'500q_n2_w{key}.pdf')
    base_num = value[0]

    for i in range(value[1]):
        # Save pages as images in the pdf
        prefix = 'q' if i % 2 == 0 else 'a'
        num = math.floor(i / 2) + 1 + base_num
        path = f'page_images/{prefix}_{num:03}.jpg'
        images[i].save(path, 'JPEG')
