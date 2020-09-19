import struct
import skia


def intToTag(intTag):
    return struct.pack(">i", intTag)


for fileName in ["MutatorSans.ttf", "IBMPlexSansVar-Roman.ttf"]:
    print(fileName)
    tf = skia.Typeface.MakeFromFile(fileName)
    pos = tf.getVariationDesignPosition()
    loc = {intToTag(p.axis): p.value for p in pos}
    print(loc)
