# import module
from pdf2image import convert_from_path
import math

# {<week>: [<base_num>, <#page>]}
# week_config = {1: [0, 60], 2: [30, 60], 3: [60, 58], 4: [89, 60]}
# week_config = {1: [0, 60, 1-70], 2: [30, 60, 79-138], 3: [60, 58, 147-206], 4: [89, 60, 215-274]}
# week_config = {'12': [30, 60, 60], '34': [89, 60, 58]}
week_config = {'34': [89, 60, 60]}

# Store Pdf with convert_from_path function
for key, value in week_config.items():
    images = convert_from_path(f'500q_n1_w{key}.pdf')
    base_num = value[0]
    for i in range(value[1]):
        print(f"i = {i}")
        # Save pages as images in the pdf
        prefix = 'q' if i % 2 == 0 else 'a'
        num = math.floor(i / 2) + 1 + base_num
        path = f'page_images_n1/{prefix}_{num:03}.jpg'
        images[value[2]+6+i].save(path, 'JPEG')
