from pathlib import Path
from glob import iglob

from src.image_to_dataframe import make_excel



# single_filename = "input/table_1.png"
input_file_names = iglob('*input/*[.png, .jpg]')


for filename in input_file_names:
    path = Path(filename)
    if path.is_file():
        make_excel(filename)