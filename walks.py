# Nadalee Thao, Nathaniel Green
# UW - La Crosse

from PIL import Image
import json

# image dimensions
width = 250
height = 250

# colors 
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
ORANGE  = (255, 128, 0)
MAGENTA = (255, 0, 255)


def main():
    with open('numbers.json', 'r') as file:
        data = json.load(file)
        print(data["e"]["value"])
    print(RED)

    # Open an existing image:
    image = Image.open("your_image.jpg")

    # Create a new image:
    image = Image.new("RGB", (width, height), "white") # (mode, size, color)

    # Get pixel access object:
    pixels = image.load()

    # Set the color of a pixel at (x, y):
    pixels[x, y] = (R, G, B)  # RGB color values (0-255)


    # Draw a horizontal line:
    for x in range(start_x, end_x + 1):
        pixels[x, y] = (0, 0, 255) # Blue color

    # Draw a rectangle:
    for x in range(x1, x2 + 1):
        pixels[x, y1] = (255, 0, 0) # Red
        pixels[x, y2] = (255, 0, 0)
    for y in range(y1, y2 + 1):
        pixels[x1, y] = (255, 0, 0)
        pixels[x2, y] = (255, 0, 0)

    image.save("modified_image.png")

    



if __name__ == "__main__":
    main()
