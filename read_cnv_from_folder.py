#!/usr/bin/env python3
'''
    File name: read_cnv_from_folder.py
    Author: Sigurd Sandvoll Sundberg
    Date created: 4/10/2021
    Date last modified: 4/10/2021
    Python Version: 3.8.10
'''
# Reading the file can be done in the following way also:
#     >> import numpy as np
#     >> np.loadtxt(filename, comments=["#" ,"*"], usecols=[0,1,2])
# This creates a output array on the following format:
#     >> [[<depth meter> , <Temperature Celsius>, <Salinity ___>],[...],...]
# Another method would be through the use of seabird:

# locale.setlocale(locale.LC_TIME, ("nb_NO", "UTF-8"))

# -- Imports --
from seabird.cnv import fCNV
import pandas as pd
import os
import locale
from typing import Dict, List, Union, Tuple

# -- Custom Imports --
from map_keys import map_keys, update_dict_keys


def read_cnv_file(file: str) -> pd.DataFrame:
    profile: fCNV = fCNV(file)
    keys: List = profile.keys()
    df: pd.DataFrame = pd.DataFrame()
    for key in keys:
        df[key] = profile[key]
    return df


def read_directory(directory: str, tail: str) -> List[str]:
    output: List[str] = []
    folder: os.DirEntry = os.scandir(directory)
    for file in folder:
        if file.name[-4:] == tail:
            output.append(file.name)
    folder.close()
    return output


def _filename(file: str) -> str:
    return file.split("_", 1)[0]


def read_cnv_from_folder(folder: str, m: str) -> Tuple[Dict[str, Union[pd.DataFrame]], List[str]]:
    tail: str = ".cnv"
    filepath: List[str] = read_directory(folder, tail)
    df_dict: Dict[str, pd.DataFrame] = {}
    keys: List[str] = []
    # -------------------------
    # Set locale to the same as in the files
    locale.setlocale(locale.LC_TIME, ("en_US", "UTF-8"))
    for file in filepath:
        df_dict[_filename(file)] = read_cnv_file(folder + file)
        keys.append(_filename(file))
    locale.setlocale(locale.LC_TIME, "")
    mapped_keys: List[str] = map_keys(keys, m)
    df_dict = update_dict_keys(df_dict, m)
    return (df_dict, mapped_keys)


if __name__ == '__main__':
    print("This program is not supposed to be ran as main, use the function 'read_cnv_from_folder'.")
