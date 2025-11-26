import os
import glob

def main():
    # read the image paths from "all-images.md"
    with open('all-images.txt', 'r', encoding='utf-8') as f:
        all_images = set(line.strip() for line in f)

    # read the image paths from "needed-images.md"
    with open('needed-images.txt', 'r', encoding='utf-8') as f:
        needed_images = set(line.strip() for line in f)

    # find the image files that are not in both lists
    to_delete = all_images - needed_images

    # delete the image files
    for image_file in to_delete:
        try:
            os.remove(image_file)
            print(f"Deleted: {image_file}")
        except OSError as e:
            print(f"Error: {e.strerror}")

if __name__ == "__main__":
    main()