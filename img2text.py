import Image
from char import CHAR_HEIGHT, CHAR_WIDTH


def trim_pic(image, row_num):
    width, height = image.size

    h = row_num * CHAR_HEIGHT
    w = h * width / height

    image = image.resize((w, h))
    # image.resize(size, Image.ANTIALIAS)

    col_num = w / CHAR_WIDTH

    return image.crop((0, 0, CHAR_WIDTH*col_num, h))


def row_iterator(image):
    width, height = image.size
    for i in range(0, height, CHAR_HEIGHT):
        yield image.crop((0, i, width, i + CHAR_HEIGHT))


def column_iterator(image):
    width, height = image.size
    for i in range(0, width, CHAR_WIDTH):
        yield image.crop((i, 0, i+CHAR_WIDTH, height))


def main():
    # Prepare for picture
    img = Image.open("img.jpg").convert("L")
    # Trim the picture to a proper size
    img = trim_pic(img, 20)
    # Import criteria
    import finepattern as fp
    with open("output.txt", "w") as output:

        for ir in row_iterator(img):
            for cell in column_iterator(ir):
                ch = fp.find_most_fit(cell)

                output.write(ch)

            output.write("\n")


if __name__ == '__main__':
    main()
