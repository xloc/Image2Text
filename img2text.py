import Image
from char import CHAR_SIZE,CHAR_TABLE


def if_just_fit(image):
    width, height = image.size

    return (width % CHAR_SIZE[0] == 0) and \
           (height % CHAR_SIZE[1] == 0)


def make_a_proper_pic(image, row_num):
    width, height = image.size

    h = row_num * CHAR_SIZE[1]
    w = h * width / height

    image = image.resize((w,h))
    # image.resize(size, Image.ANTIALIAS)

    col_num = w / CHAR_SIZE[0]

    return image.crop((0, 0, CHAR_SIZE[0]*col_num, h))


def gen_row_iterator(image):
    width, height = image.size
    for i in range(0, height, CHAR_SIZE[1]):
        yield image.crop((0, i, width, i + CHAR_SIZE[1]))


def gen_column_iterator(image):

    width, height = image.size
    for i in range(0, width, CHAR_SIZE[0]):
        yield image.crop((i, 0, i+CHAR_SIZE[0], height))





# Prepare for picture
im = Image.open("img.jpg")
im = im.convert("L")

im = make_a_proper_pic(im, 40)


with open("output.txt", "w") as output:

    import itertools as it
    for ir in gen_row_iterator(im):
        for ich in gen_column_iterator(ir):
            eachPix = it.product(
                range(CHAR_SIZE[0]),
                range(CHAR_SIZE[1]))
            grayPxs = [ich.getpixel(xy) for xy in eachPix]
            value = sum(grayPxs)/len(grayPxs)

            output.write(CHAR_TABLE[value])

        output.write("\n")





