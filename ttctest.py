import struct
import skia


fileName = "MutatorSans.ttc"
for i in range(4):
    tf = skia.Typeface.MakeFromFile(fileName, i)
    print(i, tf)
