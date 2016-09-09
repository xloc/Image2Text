import ImageFont,ImageDraw,Image

font = ImageFont.truetype(r'/Library/Fonts/Andale Mono.ttf', 10)
# font = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc',10)
for ch in "ijklmn":
    print "ch:'%s' - %s" % (ch, font.getsize(ch))

width, height = 120, 60
im = Image.new("RGB", (width,height), "white")

draw = ImageDraw.Draw(im)

draw.text((0, 0, 0, 0), "ijklmn", fill="black", font=font)

im.show()
