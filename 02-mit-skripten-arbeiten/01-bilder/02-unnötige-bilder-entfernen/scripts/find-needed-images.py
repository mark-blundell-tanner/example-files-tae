import os
import glob
import re

def find_referenced_images():
    # specify the directory path
    md_directory_path = '../'

    # find all .md files in the directory and its subdirectories
    md_files = glob.glob(os.path.join(md_directory_path, '**/*.md'), recursive=True)

    # list to store all referenced images
    referenced_images = []

    # iterate over all .md files
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

            # find all image references in the .md file
            image_refs = re.findall(r'\!\[.*?\]\((.*?)\)', content, re.IGNORECASE)

            # add the referenced image files to the list
            for image_ref in image_refs:
                # get the directory of the current markdown file
                md_file_dir = os.path.dirname(md_file)

                # get the absolute path to the image file
                image_file_path = os.path.abspath(os.path.join(md_file_dir, image_ref))

                # add the image file to the list of referenced images
                referenced_images.append(image_file_path)

    # write the image files that are referenced in the .md files to a file
    with open('needed-images.txt', 'w', encoding='utf-8') as f:
        for image_file in referenced_images:
            f.write(f"{image_file}\n")

def find_all_images():
    # specify the directory path
    image_directory_path = '../bilder/'

    # find all image files in the directory and its subdirectories
    image_files = glob.glob(os.path.join(image_directory_path, '**/*.*'), recursive=True)

    # filter out non-image files
    image_files = [f for f in image_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # write the image files to a file
    with open('all-images.txt', 'w', encoding='utf-8') as f:
        for image_file in image_files:
            # get the absolute path to the image file
            image_file_path = os.path.abspath(image_file)

            f.write(f"{image_file_path}\n")

if __name__ == "__main__":
    find_referenced_images()
    find_all_images()