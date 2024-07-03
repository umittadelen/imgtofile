from PIL import Image

with open('output.imgc', 'r') as f:
    filename, x, y, r, g, b, a = [line.strip() for line in f.readlines()]
    print(len(r)/2)
ImgX = int(x)
ImgY = int(y)
RList = [r[i:i+2] for i in range(0, len(r), 2)]
GList = [g[i:i+2] for i in range(0, len(g), 2)]
BList = [b[i:i+2] for i in range(0, len(b), 2)]
AList = [a[i:i+2] for i in range(0, len(a), 2)]

print(len(BList))

if len(RList) == 1:
    i = 1
    while i < (ImgX*ImgY):
      RList.append(RList[0])
      i += 1

if len(GList) == 1:
    i = 1
    while i < (ImgX*ImgY):
      GList.append(GList[0])
      i += 1

if len(BList) == 1:
    i = 1
    while i < (ImgX*ImgY):
      BList.append(BList[0])
      i += 1

if len(AList) == 1:
    i = 1
    while i < (ImgX*ImgY):
      AList.append(AList[0])
      i += 1

img = Image.new('RGBA', (ImgX, ImgY), (0, 0, 0, 0))

counter = 0
for y in range(ImgY):
  for x in range(ImgX):
    img.putpixel((x, y), (int(RList[counter], 16), int(GList[counter], 16), int(BList[counter], 16), int(AList[counter], 16)))
    counter += 1  # Increment counter for the next pixel

img.save(filename)
