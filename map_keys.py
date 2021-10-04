#!/usr/bin/env python3
'''
    File name: map_keys.py
    Author: Sigurd Sandvoll Sundberg
    Date created: 4/10/2021
    Date last modified: 4/10/2021
    Python Version: 3.8.10
'''
import json
from typing import Dict, List
import pandas as pd


def _map_keys(file: str) -> Dict[str, str]:
    output: Dict
    with open(file, 'r') as f:
        output = json.load(f)
    return output


def map_keys(ip: List[str], m: str) -> List[str]:
    mapping: Dict[str, str] = _map_keys(m)
    for i, value in enumerate(ip):
        ip[i] = mapping[value]
    return ip


def update_dict_keys(d: Dict[str, str], m: str) -> Dict[str, str]:
    mapping: Dict[str, str] = _map_keys(m)
    for old, new in mapping.items():
        d[new] = d.pop(old)
    return d


def main() -> int:
    import os
    p = os.scandir("./data/braarud/")
    # Setup data
    l1: List[str] = []
    l2: List[str] = ["910-BN1",
                     "926-R2",
                     "1000-CP2",
                     "1045-BN1",
                     "1120-BN1",
                     "1139-R2",
                     "1156-CP2",
                     "1235-R2",
                     "1250-BN1",
                     "1350-BN1",
                     "1405-R2",
                     "1425-CP2",
                     "1511-R2",
                     "1523-BN1"
                     ]
    sorted_l2: List[List[str, str]] = []
    # Sorting the maps such that the two arrays appear the same
    for ele in l2:
        sorted_l2.append(ele.split("-")[::-1])
    sorted_l2.sort(key=lambda x: x[0])
    for f in p:
        if f.name[-4:] == ".cnv":
            l1.append(f.name[:-13])
    l1.sort()
    # Adding the mapping to a dict and dumping to json
    output: Dict[str, str] = {}
    for key, value in zip(l1, sorted_l2):
        output[key] = "-".join(value[::-1])
    with open("./data/braarud/map.json", "w") as o:
        json.dump(output, o)
    return 0


if __name__ == '__main__':
    main()
    # keys: Dict[str, str] = _map_keys()
