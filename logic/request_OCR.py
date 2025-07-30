import base64
from pathlib import Path
from os import environ
from mistralai import Mistral, ImageURLChunk


api_key = environ['MISTRAL_API_KEY']
client = Mistral(api_key=api_key)
ocr_model_name="mistral-ocr-latest"

def encode_image(image_file: Path):
    encoded_image = base64.b64encode(image_file.read_bytes()).decode()
    base64_data_url = f"data:image/jpeg;base64,{encoded_image}"
    return base64_data_url


def image_to_markdown(image_file: Path) -> str:
    
    base64_data_url = encode_image(image_file)

    # Process the image using OCR
    print("Awaiting text extraction")
    try: 
        image_response = client.ocr.process(
            document=ImageURLChunk(image_url=base64_data_url),
            model="mistral-ocr-latest"
        )
    except: 
        print("Failed to get response from API")
        print(f"Check that you have internet connection and a valid API key for {ocr_model_name}")
        exit()
    image_ocr_markdown = image_response.pages[0].markdown

    return image_ocr_markdown

