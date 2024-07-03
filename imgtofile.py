from PIL import Image

def convert(image_path):
    im = Image.open(image_path)  # Can be many different formats.
    pix = im.load()
    RVal = []
    GVal = []
    BVal = []
    AVal = []
    XVal, YVal = im.size  # Get the width and height of the image for iterating over
    print(im.size)
    for y in range(YVal):
        for x in range(XVal):
            r, g, b, a = pix[x, y]
            RVal.append(f"{r:02X}")
            GVal.append(f"{g:02X}")
            BVal.append(f"{b:02X}")
            AVal.append(f"{a:02X}")

    # Check if all values in each channel are the same and handle accordingly
    if len(set(RVal)) == 1:
        RVal = RVal[0]
    else:
        RVal = "".join(RVal)
    if len(set(GVal)) == 1:
        GVal = GVal[0]
    else:
        GVal = "".join(GVal)
    if len(set(BVal)) == 1:
        BVal = BVal[0]
    else:
        BVal = "".join(BVal)
    if len(set(AVal)) == 1:
        AVal = AVal[0]
    else:
        AVal = "".join(AVal)

    with open('output.imgc', 'w') as f:
        f.write(f"{image_path.split('/')[-1]}\n")
        f.write(f"{XVal:02X}\n{YVal:02X}\n")
        f.write(f"{RVal}\n")
        f.write(f"{GVal}\n")
        f.write(f"{BVal}\n")
        f.write(f"{AVal}\n")

# Specify the image path
image_path = './redyellow.png'
convert(image_path)
