from pathlib import Path
from glob import iglob
from pandas import DataFrame

from .image_to_text import image_to_markdown
from .text_to_dataframe import to_dataframe


def make_dataframe(filename: str) -> DataFrame:
    print(filename) 
    print("--------")
    image_file = Path(filename)
    if image_file.is_dir(): 
        print("Found dir")
    assert image_file.is_file(), "The provided image path does not exist."

    markdown = image_to_markdown(image_file)
    ### Use the above line for new images, the below for already formatted markdown
    #with open("input/md_sample1.md", "r") as md_file: 
    #    markdown = md_file.readlines()
    #    markdown = "".join(markdown)
    print("Markdown result: ")
    print(markdown)

    df = to_dataframe(markdown)
    print("Dataframe result:")
    print(df)
    return df