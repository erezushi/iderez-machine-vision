import Image

im = Image.open("orange.jpg")
x = 0
y = 0
width, height = im.size


# draw a short line
x=10; y=10; im.putpixel( (x,y), (255,255,255) )
x=11; y=10; im.putpixel( (x,y), (255,255,255) )
x=12; y=10; im.putpixel( (x,y), (255,255,255) )

# print values of pixels
for y in range(0,height):
    for x in range(0,width):
        r,g,b = im.getpixel((x,y))
        if ((r >= 250 and g < r and b < r) or (r > g + 60 and g > b + 60) or (r > 240 and r > g + 30 and b < g - 90)) :
            im.putpixel( (x,y), (255,255,255) )

# show the image
im.show()
