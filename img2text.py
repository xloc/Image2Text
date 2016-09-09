import Image
from char import CHAR_HEIGHT, CHAR_WIDTH
from brightness import CHAR_TABLE


def if_just_fit(image):
    width, height = image.size

    return (width % CHAR_WIDTH == 0) and \
           (height % CHAR_HEIGHT == 0)


def make_a_proper_pic(image, row_num):
    width, height = image.size

    h = row_num * CHAR_HEIGHT
    w = h * width / height

    image = image.resize((w,h))
    # image.resize(size, Image.ANTIALIAS)

    col_num = w / CHAR_WIDTH

    return image.crop((0, 0, CHAR_WIDTH*col_num, h))


def gen_row_iterator(image):
    width, height = image.size
    for i in range(0, height, CHAR_HEIGHT):
        yield image.crop((0, i, width, i + CHAR_HEIGHT))


def gen_column_iterator(image):

    width, height = image.size
    for i in range(0, width, CHAR_WIDTH):
        yield image.crop((i, 0, i+CHAR_WIDTH, height))





# Prepare for picture
im = Image.open("img.jpg")
im = im.convert("L")

im = make_a_proper_pic(im, 40)


with open("output.txt", "w") as output:

    import itertools as it
    for ir in gen_row_iterator(im):
        for ich in gen_column_iterator(ir):
            eachPix = it.product(
                range(CHAR_WIDTH),
                range(CHAR_HEIGHT))
            grayPxs = [ich.getpixel(xy) for xy in eachPix]
            value = sum(grayPxs)/len(grayPxs)

            output.write(CHAR_TABLE[value])

        output.write("\n")





