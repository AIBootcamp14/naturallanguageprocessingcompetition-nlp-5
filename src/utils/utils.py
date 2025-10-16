import os
import random

import json
import yaml

import pandas as pd


def show_example(df:pd.DataFrame, num:int = 0, idx:int = 'none'):
    length = len(df)
    if idx == 'none':
        idx = random.randint(0,length-1)
    for i in range(idx, idx + 1 + num):
        print('='*10, f'idx = {i}' ,'='*10)
        print('='*10, 'dialogue', '='*10)
        print(df['dialogue'][i])
        print('='*10, 'summary', '='*10)
        print(df['summary'][i])
        print()


def get_project_path():
    return os.path.dirname(
        os.path.dirname( #/pj/src/
            os.path.dirname( #/pj/src/utils/
                os.path.abspath(__file__)))) # /pj/src/utils/utils.py

def get_data_path():
    return os.path.join(
        os.path.dirname( # /pj/src/utils/
            os.path.abspath(__file__)),"..","..","data" # /pj/src/utils/utils.py
    )

def loaded_cfg(config_path):
    with open(config_path, "r") as file:
        loaded_config = yaml.safe_load(file)
    return loaded_config