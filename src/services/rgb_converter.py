import requests
from PIL import Image
from io import BytesIO

def convert_int_to_rgb(color_int):
    """
    Конвертация из 24bit int в rgb
    :param: color_int - int цвет
    """
    blue = 0x0000ff & color_int
    green = 0x0000ff & (color_int >> 8)
    red = 0x0000ff & (color_int >> 16)
    alpha = 0x0000ff & (color_int >> 24)

    return (red, green, blue)



def url_to_pixel_matrix(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image_rgb = image.convert('RGB')

        width, height = image_rgb.size
        pixel_matrix = []

        for y in range(height):
            row = []
            for x in range(width):
                r, g, b = image_rgb.getpixel((x, y))
                row.append((r, g, b))
            pixel_matrix.append(row)

        return pixel_matrix
    else:
        raise Exception("GG")

def mix_rgb_colors(list_rgb_colors):
    """
    Смешать rgb цвета
    :param: list_rgb_colors - список rgb [(r,g,b), (r,g,b), (r,g,b)]
    """
    red, green, blue = 0,0,0
    for r,g,b in list_rgb_colors:
        red += r
        green += g
        blue += b
    red = round(red / len(list_rgb_colors))
    green = round(green / len(list_rgb_colors))
    blue = round(blue / len(list_rgb_colors))
    return (red, green, blue)

def convert_rgb_to_int(color_rgb):
    """
    Конвертация из rgb в int
    :param: color_rgb - rgb цвет (r,g,b)
    """
    red, green, blue = color_rgb
    color_int = (red * 65536) + (green * 256) + blue  # , (when R is RED, G is GREEN and B is BLUE)
    return color_int
