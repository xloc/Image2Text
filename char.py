import ImageFont,ImageDraw,Image

# font = ImageFont.truetype(r'/Library/Fonts/Andale Mono.ttf', 10)
font = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc',12)

charset = " !\"#$%&'()*+,-./0123456789:;<=>?@" \
          "ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`" \
          "abcdefghijklmnopqrstuvwxyz{|}~"



CHAR_SIZE = font.getsize(charset[0])
CHAR_WIDTH = CHAR_SIZE[0]
CHAR_HEIGHT = CHAR_SIZE[1]


