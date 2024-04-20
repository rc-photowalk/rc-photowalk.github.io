import glob
from PIL import Image, ImageOps
from tqdm import tqdm
from os.path import join as pj

thumb_fs = glob.glob(pj('images', '*', 'thumbs', '*'))
for thumb_f in tqdm(thumb_fs):
    img = Image.open(thumb_f)
    img = ImageOps.exif_transpose(img)

    if min(img.size) > 360:
        (w, h) = img.size

        if w < h:
            h = round(h / w * 360)
            w = 360
        else:
            w = round(w / h * 360)
            h = 360

        img = img.resize((w, h))
        img.save(thumb_f)


full_fs = glob.glob(pj('images', '*', 'fulls', '*'))
for full_f in tqdm(full_fs):
    img = Image.open(full_f)
    img = ImageOps.exif_transpose(img)

    if min(img.size) > 1200:
        (w, h) = img.size

        if w < h:
            h = round(h / w * 1200)
            w = 1200
        else:
            w = round(w / h * 1200)
            h = 1200

        img = img.resize((w, h))
        img.save(full_f)