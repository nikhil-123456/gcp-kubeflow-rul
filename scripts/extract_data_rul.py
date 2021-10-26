# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:44:40 2021

@author: Nikhil
"""

import json
import pandas as pd
import argparse
from pathlib import Path
import requests, zipfile, io

def _download_data(args):

    # Extract NASA dataset from online
    r = requests.get('https://ti.arc.nasa.gov/c/6/')
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extract('train_FD001.txt')
    data = pd.read_table('train_FD001.txt',sep='\s+', header=None)
    data = data.to_numpy()
    
    # Creates a json object based on `data`
    data={'data':data.tolist()}
    data_json = json.dumps(data)

    # Saves the json object into a file
    with open(args.data, 'w') as out_file:
        json.dump(data_json, out_file)

if __name__ == '__main__':
    
    # This component does not receive any input
    # it only outputs one artifact which is `data`.
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str)
    
    args = parser.parse_args()
    
    # Creating the directory where the output file will be created 
    # (the directory may or may not exist).
    Path(args.data).parent.mkdir(parents=True, exist_ok=True)

    _download_data(args)

