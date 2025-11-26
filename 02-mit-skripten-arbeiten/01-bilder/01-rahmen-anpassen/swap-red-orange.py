from PIL import Image
import os
import argparse

parser = argparse.ArgumentParser(description="Replace red with orange or vice versa in images.")
parser.add_argument("-r", "--red-to-orange", action="store_true", help="Replace red with orange")
parser.add_argument("-o", "--orange-to-red", action="store_true", help="Replace orange with red")
mode = parser.parse_args()

# Check if an argument has been defined
if not (mode.red_to_orange or mode.orange_to_red):
    print("\033[31mError: Argument required. Please specify either:\033[0m\n  -r, --red-to-orange - Replace red with orange\n  -o, --orange-to-red - Replace orange with red")
    exit(1)

if (mode.red_to_orange and mode.orange_to_red):
    print("\033[31mError: Please specify only one mode at a time.\033[0m")
    exit(1)

def replace_red_with_orange(img_path):
    img = Image.open(img_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    changed = False

    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if (r, g, b) == (255, 0, 0):
                pixels[x, y] = (255, 144, 0, a)
                changed = True

    if changed:
        img.save(img_path)
        print(f"Updated: {img_path}")

def replace_orange_with_red(img_path):
    img = Image.open(img_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    changed = False

    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if (r, g, b) == (255, 144, 0):
                pixels[x, y] = (255, 0, 0, a)
                changed = True

    if changed:
        img.save(img_path)
        print(f"Updated: {img_path}")

for root, _, files in os.walk("bilder"):
    for file in files:
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            if mode.red_to_orange:
                replace_red_with_orange(os.path.join(root, file))
            elif mode.orange_to_red:
                replace_orange_with_red(os.path.join(root, file))
