from starlette.responses import FileResponse 
from fastapi import FastAPI, UploadFile
from pathlib import Path

from logic.image_to_dataframe import process_files

UPLOAD_DIR = Path() / "uploads"

app = FastAPI()


@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.post("/uploadfile/")
async def create_upload_file(file_upload: UploadFile):
    data = await file_upload.read()
    save_to = UPLOAD_DIR / file_upload.filename
    with open(save_to, 'wb') as f:
        f.write(data)
    return {"filename": file_upload.filename}


if __name__ == "__main__": 
    # process_files()
    exit()