import char
import Image, ImageDraw

brightnessMap = {}

for ich in char.charset:
    im = char.draw_char(ich)

    avgBrightness = im.resize((1, 1), resample=Image.ANTIALIAS).getdata()[0]
    brightnessMap[avgBrightness] = ich

maxv = max(brightnessMap.keys())
minv = min(brightnessMap.keys())
# print "Max '%s'=%s" % (brightnessMap[maxbri], maxbri)
# print "Min '%s'=%s" % (brightnessMap[minbri], minbri)

valueList = list(brightnessMap.items())
valueList.sort(key=lambda a: a[0])

# Print all brightness as a sorted array
# for ln in brightnessArray:
#     print "'{}' - {}".format(ln[0],ln[1])

valueList = map(
    lambda a: (int(float(a[0] - minv) / (maxv - minv + 3) * 255), a[1]),
    valueList
)
valueList.append((256, ' '))

charLookupTable = []
for i in range(len(valueList)-1):
    for b in range(valueList[i][0], valueList[i+1][0]):
        charLookupTable.append(valueList[i][1])


def find_most_fit(img):
    value = img.resize((1, 1), resample=Image.ANTIALIAS).getdata()[0]

    return charLookupTable[value]