# cps-extras
Some one off scripts to pull CPS dtata

CPS has a number of public APIs that are documented at [api.cps.edu](api.cps.edu).

Contained in this repo are a number of scripts for calling them and processing the COVID health specific APIs. However, many of the functions here can be easily modified for use in other APIs.


The scripts are meant to value readability over performance as to allow easier modification for whatever your personal use-case may be. 

## Requirements and Dependencies ##

- Python
  - I am using `3.9` but im sure you will be okay with something earlier or later.
- Pip

## Virtual Environments ##

Using a virtual environment is highly suggested. 

In the root directory of this repo, create and activate a virtual environment with the following commands:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

And install additional requirements:
```sh
pip install -r requirements.txt
```

---


## Contents of scripts ##

### Full API Export - `full_export.py` ###
This script will export the response of an api (or multiple APIs) as a .csv file. You can then open it in excel or another spreadsheet program if that is more to your liking.

There is a list of API endpoints that are mostly commented out. The APIs that are NOT commented out will be called. Each API response will be saved with a file name formatted as `api_name`-`date-time`.csv.