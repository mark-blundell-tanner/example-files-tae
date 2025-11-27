# Bilder aus einer PDF extrahieren

```python
import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    
    image_count = 0
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        
        # Get list of images on the page
        image_list = page.get_images()
        
        # Extract each image
        for img_index, img in enumerate(image_list):
            # Get image data
            xref = img[0]
            pix = fitz.Pixmap(pdf_document, xref)
            
            # Skip if image has transparency (CMYK)
            if pix.n - pix.alpha < 4:
                # Save as PNG
                img_filename = f"image_page{page_num + 1}_{img_index + 1}.png"
                img_path = os.path.join(output_folder, img_filename)
                pix.save(img_path)
                image_count += 1
                print(f"Saved: {img_filename}")
            else:
                # Convert CMYK to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                img_filename = f"image_page{page_num + 1}_{img_index + 1}.png"
                img_path = os.path.join(output_folder, img_filename)
                pix1.save(img_path)
                image_count += 1
                print(f"Saved: {img_filename}")
                pix1 = None
            
            pix = None
    
    pdf_document.close()
    print(f"Total images extracted: {image_count}")

# Usage
extract_images_from_pdf("SIMOVE_ANS_EngineeringManual.pdf", "extracted_images")
```
