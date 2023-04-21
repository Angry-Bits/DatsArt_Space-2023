


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
