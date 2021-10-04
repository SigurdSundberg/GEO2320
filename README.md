# GEO2320
Repository for the UiO subject GEO2320 - Oceanography

## Folders
This repo contains folders [data](data) which containts the two subfolders:
* [braarud](data/braarud) - Here the data from the .zip with the data from the onboard CDT on Trygve Braarud should be. In addition it contains a key map for the `scripts` included. 
* [castaway](data/castaway) - Here the data from the manual Castaway CDT should be located. It also containts a map used by the `scripts`.  

## Files 
The files found are as follows:
1. [map_key.py](map_keys.py) - This file is used by the other two programs to create mappings of `dictionary` keys and uses the two `.json` files found in [braarud](data/braarud) and [castaway](data/castaway).
2. [read_cnv_from_folder.py](read_cnv_from_folder.py) - Script for reading the `.cnv` files found in [braarud](data/braarud). Returns a `dict[str, pd.DataFrame]`.
3. [read_csv_from_folder.py](read_csv_from_folder.py) - Script for reading the `.cnv` files found in [castaway](data/castaway). Returns a `dict[str, pd.DataFrame]`.

## Usage of the files:
The following imports are used: 

``` 
# -- Imports --
import pandas as pd
from typing import Dict, List

# -- Custom Imports --
from read_cnv_from_folder import read_cnv_from_folder as r_cnv
from read_csv_from_folder import read_csv_from_folder as r_csv
```

After that you can run this code to read the files:

```
# -- Variables -- 
folder_braarud = "./data/braarud/"
folder_castaway = "./data/castaway/"
braarud_map = "./data/braarud/map.json"
castaway_map = "./data/castaway/map_castaway.json"

# -- List of keys --
seabird_keys: List[str]

# -- Reading files --
onboard_seabird: Dict[str, pd.DataFrame]
castaway_seabird: Dict[str, pd.DataFrame]
weather_light: Dict[str, pd.DataFrame]

# Reading the .cnv files
onboard_seabird, seabird_keys = r_cnv(folder_braarud, braarud_map)
castaway_seabird, _ = r_csv(folder_castaway, castaway_map)

# Sorting the keys in temporal order
seabird_keys.sort(key=lambda x: int(x.split("-")[0]))
```

This gives you two `dict` in `onboard_seabird` containing the onboard CDT measurements and `castaway_seabird` containing the manual CDT measurements.
In addition there is a `list[str]` that contain the keys similar to the `.xlsx` file found with the data. 

