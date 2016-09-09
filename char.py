import ImageFont,ImageDraw,Image

font = ImageFont.truetype(r'/Library/Fonts/Andale Mono.ttf', 10)
# font = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc',10)

charset = " !\"#$%&'()*+,-./0123456789:;<=>?@" \
          "ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`" \
          "abcdefghijklmnopqrstuvwxyz{|}~"

brightnessMap = {}


elementaryCharSize = font.getsize(charset[0])

for ich in charset:
    im = Image.new("RGB", elementaryCharSize, "white")
    draw = ImageDraw.Draw(im)

    draw.text((0, 0, 0, 0), ich, fill="black", font=font)

    import itertools as it
    eachpix = it.product(\
        range(elementaryCharSize[0]),\
        range(elementaryCharSize[1]))
    grayPxs = [sum(im.getpixel(xy))/3 for xy in eachpix]
    # for xy in eachpix:
    #     print im.getpixel(xy)
    avgBrightness = sum(grayPxs)/len(grayPxs)
    brightnessMap[avgBrightness] = ich

maxbri = max(brightnessMap.keys())
minbri = min(brightnessMap.keys())
print "Max '%s'=%s" % (brightnessMap[maxbri], maxbri)
print "Min '%s'=%s" % (brightnessMap[minbri], minbri)

# print "'%s'=%s" % (brightnessMap[maxbri], maxbri)



# draw.text((0, 0, 0, 0), "ijklmn", fill="black", font=font)

#im.show()
