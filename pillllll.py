from PIL import Image, ImageDraw


def drow(width, height, sky_color='#3F72AF', snow_color='white', trunk_color='#A45A52', sun_color='#FFDC70',
         needls_color='#01796F'):
    im = Image.new("RGB", (width, height), sky_color)
    draw = ImageDraw.Draw(im)

    x, y = 0, height * 0.8
    xx, yy = width, height
    draw.rectangle(((x, y), (xx, yy)), snow_color)

    x, y = width * 0.8, -(height * 0.2)
    xx, yy = width + width * 0.2, height * 0.2
    draw.ellipse(((x, y), (xx, yy)), sun_color)

    x, y = width * 6.45, height * 0.7
    xx, yy = width * 6.55, height * 0.9
    draw.rectangle(((x, y), (xx, yy)), trunk_color)

    x1, x2, x3 = width * 0.5, width * 0.6, width * 0.4
    y1, y2, y3 = height * 0.1, height * 0.3, height * 0.3
    draw.polygon(((x1, y1), (x2, y2), (x3, y3)), needls_color)

    x1, x2, x3, x4 = width * 0.45, width * 0.55, width * 0.65, width * 0.35
    y1, y2, y3, y4 = height * 0.3, height * 0.3, height * 0.5, height * 0.5
    draw.polygon(((x1, y1), (x2, y2), (x3, y3), (x4, y4)), needls_color)

    x1, x2, x3, x4 = width * 0.4, width * 0.6, width * 0.7, width * 0.3
    y1, y2, y3, y4 = height * 0.5, height * 0.5, height * 0.7, height * 0.7
    draw.polygon(((x1, y1), (x2, y2), (x3, y3), (x4, y4)), needls_color)

    im.save('res.bmp')


drow(1000, 800)
