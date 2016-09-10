import char
import Image, ImageDraw

SAMPLE_SIZE = (3, 3)


def cell_feature(img):
    reduced = img.resize(SAMPLE_SIZE, Image.ANTIALIAS)

    return list(reduced.getdata())


def char_img(c):
    img = Image.new("L", char.CHAR_SIZE, "white")
    draw = ImageDraw.Draw(img)

    draw.text((0, 0, 0, 0), c, fill="black", font=char.font)

    return img


FEATURE_TABLE = []
CHAR_INDEX_MAP = []

for ich in char.charset:
    iimg = char_img(ich)

    feature = cell_feature(iimg)

    FEATURE_TABLE.append(feature)
    CHAR_INDEX_MAP.append(ich)

import numpy

MAT_FEATURE_TABLE = numpy.mat(FEATURE_TABLE)




def find_most_fit(img):
    ftr = cell_feature(img)

    repeated_feature = numpy.mat(ftr).repeat(len(FEATURE_TABLE), axis=0)
    numpy.savetxt("feature_table.txt",repeated_feature,fmt="%d",delimiter='\t')
    criterias = numpy.absolute(MAT_FEATURE_TABLE - repeated_feature).mean(axis=1, dtype=numpy.float32)
    best_idx = criterias.argmin()

    # print best_idx, '->', CHAR_INDEX_MAP[best_idx]

    return CHAR_INDEX_MAP[best_idx]

find_most_fit(char_img("}"))