from pathlib import Path
from glob import iglob

from src.image_to_dataframe import make_dataframe


def make_excel(filename):
    
    df = make_dataframe(filename)

    target_path = "out" + filename[2:-3] + "xlsx"
    df.to_excel(target_path)

    print("--------")
    print("Finished " + filename)
    print("--------")


# single_filename = "input/table_1.png"
input_file_names = iglob('*input/*[.png, .jpg]')


for filename in input_file_names:
    path = Path(filename)
    if path.is_file():
        make_excel(filename)