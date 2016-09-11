import Image

import char
from char import draw_char

SAMPLE_SIZE = (3, 3)


def cell_feature(img):
    reduced = img.resize(SAMPLE_SIZE, Image.ANTIALIAS)

    return list(reduced.getdata())


FEATURE_TABLE = []
CHAR_INDEX_MAP = []

for ich in char.charset:
    iimg = draw_char(ich)

    feature = cell_feature(iimg)

    FEATURE_TABLE.append(feature)
    CHAR_INDEX_MAP.append(ich)

import numpy

MAT_FEATURE_TABLE = numpy.mat(FEATURE_TABLE)




def find_most_fit(img):
    ftr = cell_feature(img)

    repeated_feature = numpy.mat(ftr).repeat(len(FEATURE_TABLE), axis=0)
    # numpy.savetxt("feature_table.txt",repeated_feature,fmt="%d",delimiter='\t')
    criterias = numpy.absolute(MAT_FEATURE_TABLE - repeated_feature).mean(axis=1, dtype=numpy.float32)
    best_idx = criterias.argmin()

    # print best_idx, '->', CHAR_INDEX_MAP[best_idx]

    return CHAR_INDEX_MAP[best_idx]

find_most_fit(draw_char("}"))