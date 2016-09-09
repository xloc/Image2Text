import char
import Image, ImageDraw

brightnessMap = {}

for ich in char.charset:
    im = Image.new("RGB", char.CHAR_SIZE, "white")
    draw = ImageDraw.Draw(im)

    draw.text((0, 0, 0, 0), ich, fill="black", font=char.font)

    import itertools as it
    eachpix = it.product(\
        range(char.CHAR_WIDTH),\
        range(char.CHAR_HEIGHT))
    grayPxs = [sum(im.getpixel(xy))/3 for xy in eachpix]
    # for xy in eachpix:
    #     print im.getpixel(xy)
    avgBrightness = sum(grayPxs)/len(grayPxs)
    brightnessMap[avgBrightness] = ich

maxbri = max(brightnessMap.keys())
minbri = min(brightnessMap.keys())
# print "Max '%s'=%s" % (brightnessMap[maxbri], maxbri)
# print "Min '%s'=%s" % (brightnessMap[minbri], minbri)

brightnessMapList = list(brightnessMap.items())
brightnessMapList.sort(key=lambda a: a[0])

# Print all brightness as a sorted array
# for ln in brightnessArray:
#     print "'{}' - {}".format(ln[0],ln[1])

blist = map(lambda a: (int(float(a[0]-minbri)/(maxbri-minbri+3)*255),a[1]),\
            brightnessMapList)
blist.append((256,' '))

charBrightnessTable = []
for i in range(len(blist)-1):
    for b in range(blist[i][0],blist[i+1][0]):
        charBrightnessTable.append(blist[i][1])

CHAR_TABLE = "".join(charBrightnessTable)

# for ln in enumerate(charBrightnessTable):
#     print "'{}'\t- {}".format(ln[1],ln[0])




#im.show()