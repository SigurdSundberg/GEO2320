#!/usr/bin/env python3
'''
    File name: read_csv_from_folder.py
    Author: Sigurd Sandvoll Sundberg
    Date created: 4/10/2021
    Date last modified: 4/10/2021
    Python Version: 3.8.10
'''


# -- Imports --
import pandas as pd
import os
from typing import Dict, List, Union, Tuple
import numpy as np

# -- Custom Import --
from map_keys import map_keys, update_dict_keys


def _get_index(c: List[bool]) -> int:
    for i, l in enumerate(c):
        if l:
            return i


def read_csv_file(file: str) -> Union[pd.DataFrame, None]:
    df: pd.DataFrame = pd.read_csv(
        file,
        comment="%",
        header=0,
        index_col=0
    )
    if df.empty:
        print(f"The following file is empty: {file}.")
        print("Handling by adding 'None' to the dictionary")
        return None

    # Look at the deepest point in the cast and return only downcast
    max_depth: np.float64 = df.iloc[:, 0].idxmax()
    masked_bool_array: np.ndarray[bool] = df.index.get_loc(max_depth)
    bottom_index: int = _get_index(masked_bool_array) + 1
    df = df.iloc[:bottom_index]
    return df  # Return only downcast part


def read_directory(directory: str, tail: str) -> List[str]:
    output: List[str] = []
    folder: os.DirEntry = os.scandir(directory)
    for file in folder:
        if file.name[-4:] == tail:
            output.append(file.name)
    folder.close()
    return output


def _filename(file: str) -> str:
    return file.rstrip("_downup.csv")


def read_csv_from_folder(folder: str, m: str) -> Tuple[Dict[str, Union[pd.DataFrame]], List[str]]:
    tail: str = ".csv"
    filepath: List[str] = read_directory(folder, tail)
    df_dict: Dict[str, Union[pd.DataFrame, None]] = {}
    keys: List[str] = []

    # -------------------------
    # Set locale to the same as in the files
    for file in filepath:
        df_dict[_filename(file)] = read_csv_file(folder + file)
        keys.append((_filename(file)))
    mapped_keys = map_keys(keys, m)
    df_dict = update_dict_keys(df_dict, m)
    return (df_dict, mapped_keys)


if __name__ == '__main__':
    print("This program is not supposed to be ran as main, use the function 'read_cnv_from_folder'.")
