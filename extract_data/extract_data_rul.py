# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:44:40 2021

@author: Nikhil
"""


import json
import pandas as pd
import argparse
from pathlib import Path

#from sklearn.model_selection import train_test_split

def _download_data(args):
    data = pd.read_table(args.input_path,sep='\s+', header=None)
    data = data.to_numpy()
    data={'data':data.tolist()}

    # Creates a json object based on `data`
    data_json = json.dumps(data)

    # Saves the json object into a file
    with open(args.output_data, 'w') as out_file:
        json.dump(data_json, out_file)

if __name__ == '__main__':
    
    # This component does not receive any input
    # it only outpus one artifact which is `data`.
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str)
    parser.add_argument('--output_data',type=str)
    args = parser.parse_args()
    
    # Creating the directory where the output file will be created 
    # (the directory may or may not exist).
    Path(args.output_data).parent.mkdir(parents=True, exist_ok=True)

    _download_data(args)
    
