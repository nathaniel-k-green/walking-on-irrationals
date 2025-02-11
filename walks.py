# Nadalee Thao, Nathaniel Green
# UW - La Crosse

from PIL import Image
import json, time

# image dimensions
width = 5000
height = 5000

CENTER = (width // 2, height // 2)

# colors 
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
ORANGE  = (255, 128, 0)
MAGENTA = (255, 0, 255)

EXISTING_IMAGE = False


def createFileName(prefix):
    curr = time.ctime(time.time())
    return prefix + curr.replace(" ", "-").replace(":", "-") + ".png"

def wavelength_to_rgb(wavelength):
    """
    Converts a wavelength (in nanometers) to an approximate RGB color tuple.

    Args:
        wavelength: The wavelength of light in nanometers (between 380 and 750 nm).

    Returns:
        A tuple of (red, green, blue) values, each in the range 0-255.
        If the wavelength is outside the visible spectrum, returns (0, 0, 0).
    """
    if 380 <= wavelength <= 750:
        if 380 <= wavelength <= 439:
            red = -(wavelength - 440) / (440 - 380)
            green = 0.0
            blue = 1.0
        elif 440 <= wavelength <= 489:
            red = 0.0
            green = (wavelength - 440) / (490 - 440)
            blue = 1.0
        elif 490 <= wavelength <= 509:
            red = 0.0
            green = 1.0
            blue = -(wavelength - 510) / (510 - 490)
        elif 510 <= wavelength <= 579:
            red = (wavelength - 510) / (580 - 510)
            green = 1.0
            blue = 0.0
        elif 580 <= wavelength <= 644:
            red = 1.0
            green = -(wavelength - 645) / (645 - 580)
            blue = 0.0
        elif 645 <= wavelength <= 750:
            red = 1.0
            green = 0.0
            blue = 0.0

        # Adjust intensity to prevent dim colors outside the central range of wavelengths
        if 380 <= wavelength <= 419 or 691 <= wavelength <= 750:
            factor = 0.3 + 0.7 * (
                1
                - abs(wavelength - (420 if wavelength < 500 else 690))
                / (750 - (420 if wavelength < 500 else 690))
            )
        else:
            factor = 1.0
            
        red = int(red * factor * 255)
        green = int(green * factor * 255)
        blue = int(blue * factor * 255)

        return red, green, blue
    else:
        return 0, 0, 0


def position_to_wavelength(pos, num_digits):
    fx = int(380 + ((750 - 380) / (num_digits)) * pos)
    return fx


def main():
    e_str = ''
    with open('numbers.json', 'r') as file:
        data = json.load(file)
        e_str = data["e"]["more_digits"].replace(".", "")
        print(len(e_str))


    if EXISTING_IMAGE:
        # Open an existing image:
        image = Image.open("your_image.jpg")
    else:
        # Create a new image:
        image = Image.new("RGB", (width, height), "white") # (mode, size, color)

    # Get pixel access object:
    pixels = image.load()

    cur_x = CENTER[0]
    cur_y = CENTER[1]
    for pos, digit in enumerate(e_str):
        for _ in range(8):
            pixels[cur_x, cur_y] = wavelength_to_rgb(position_to_wavelength(pos, len(e_str)))
            pixels[cur_x - 1, cur_y - 1] = wavelength_to_rgb(position_to_wavelength(pos, len(e_str)))
            if digit == '0':
                cur_x += 1
            elif digit == '1':
                cur_y -= 1
            elif digit == '2':
                cur_x -= 1
            elif digit == '3': 
                cur_y += 1 

    print("digits walked")

    image.save(createFileName("pics/my-file-"))

    



if __name__ == "__main__":
    main()
