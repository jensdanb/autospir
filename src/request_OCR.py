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

def upload(encoded_image: str): 
    uploaded_file = client.files.upload(
        file={
            "file_name": encoded_image.stem,
            "content": encoded_image.read_bytes(),
        },
        purpose="ocr",
    )

    # Get URL for the uploaded file
    signed_url = client.files.get_signed_url(file_id=uploaded_file.id, expiry=1)


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

'''

class StructuredOCR(BaseModel):
    file_name: str
    topics: list[str]
    languages: str
    ocr_contents: dict

def structured_ocr(image_file: Path, ocr_markdown: str) -> StructuredOCR:

    base64_data_url = encode_image(image_file)

    print("Awaiting formatting to table")
    try: 
        chat_response = client.chat.parse(
            model="pixtral-12b-latest",
            messages=[
                {
                    "role": "user",
                    "content": [
                        ImageURLChunk(image_url=base64_data_url),
                        TextChunk(text=(
                            f"This is the image's OCR in markdown:\n{ocr_markdown}\n.\n"
                            "Convert this into a structured JSON response "
                            "with the OCR contents in a sensible dictionnary."
                            )
                        )
                    ]
                }
            ],
            response_format=StructuredOCR,
            temperature=0
        )
    except: 
        print("---- \n Failed to get response from API \n Likely missing internet connection \n ----")
        return

    return chat_response.choices[0].message.parsed
'''
