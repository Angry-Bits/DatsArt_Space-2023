import requests
from PIL import Image
from io import BytesIO

def create_rgb_from_int(color_int):
    """
    Конвертация из 24bit int в rgb
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