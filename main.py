# main.py
from Goom.ocr import perform_ocr

def main():
    image_path = "path/to/image_B.jpg"
    result = perform_ocr(image_path)
    print(f"OCR Result for Project B: {result}")

if __name__ == "__main__":
    main()