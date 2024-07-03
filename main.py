from PIL import Image

def convert(image_path):
    im = Image.open(image_path) # Can be many different formats.
    pix = im.load()
    RVal = []
    GVal = []
    BVal = []
    AVal = []
    XVal,YVal = im.size  # Get the width and hight of the image for iterating over
    for y in range(YVal):
        for x in range(XVal):
            r, g, b, a = pix[x, y]
            RVal.append(f"{r:02X}")
            GVal.append(f"{g:02X}")
            BVal.append(f"{b:02X}")
            AVal.append(f"{a:02X}")
    if len(set(RVal)) == 1:
        RVal = RVal[0]
    if len(set(GVal)) == 1:
        GVal = GVal[0]
    if len(set(BVal)) == 1:
        BVal = BVal[0]
    if len(set(AVal)) == 1:
        AVal = AVal[0]
    f = open('output.imgc', 'w')
    f.write(f"{image_path.split("/")[-1]}\n")
    f.write(f"{XVal:02X}\n{YVal:02X}\n")
    f.write(f"{"".join(RVal)}\n")
    f.write(f"{"".join(GVal)}\n")
    f.write(f"{"".join(BVal)}\n")
    f.write(f"{"".join(AVal)}\n")

# Specify the image path
image_path = './img.png'
convert(image_path)
