from io import StringIO
import pandas as pd

def to_dataframe(md: str) -> pd.DataFrame:
    df = pd.read_table(StringIO(md), sep="|", header=None, skipinitialspace=True)

    header_index = index_header(df)
    df.rename(columns=df.iloc[header_index], inplace = True)
    df.drop(df.index[header_index], inplace = True)

    return df.dropna(axis=1, how='all').iloc[1:]


def index_header(df: pd.DataFrame) -> int:
    def is_red_flag(value) -> bool:
        s = str(value)
        if s == 'nan' or not any(c.isalpha() for c in s):
            return True
        else: 
            return False
    minefield = df.map(is_red_flag)

    df['red_flags'] = minefield.sum(axis=1)
    return df['red_flags'].idxmin()

