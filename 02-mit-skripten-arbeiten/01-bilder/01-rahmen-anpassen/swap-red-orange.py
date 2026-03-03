from PIL import Image
import os

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

for root, _, files in os.walk("02-mit-skripten-arbeiten/01-bilder/01-rahmen-anpassen/bilder"):
    for file in files:
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
                replace_red_with_orange(os.path.join(root, file))
