import Image

im = Image.open("img.jpg")

im = im.convert("1")
im.show()
# im.show()


def get_region_iter(height_div, width_div):
    w,h = im.size

    for iy in range(0, h, h/height_div):
        for ix in range(0, w, w / width_div):
            yield im.crop((ix, iy, ix+w/width_div, iy+h/height_div))

ite = get_region_iter(5, 5)
for i in range(5):
    ite.next().show()
