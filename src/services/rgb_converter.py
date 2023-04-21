


def create_rgb_from_int(color_int):
    """
    Конвертация из 24bit int в rgb
    """
    blue = 0x0000ff & color_int
    green = 0x0000ff & (color_int >> 8)
    red = 0x0000ff & (color_int >> 16)
    alpha = 0x0000ff & (color_int >> 24)

    return (red, green, blue)