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

    # Gets and split dataset
    #x, y = load_breast_cancer(return_X_y=True)
    #data = pd.read_table('C:/Users/Nikhil/kubeflow/RUL_Prediction/train_FD001.txt', sep='\s+', header=None)
    data = pd.read_table('gs://bucket_kubeflow/train_FD001.txt',sep='\s+', header=None)
    #columns = ['unit_number','time_in_cycles','setting_1','setting_2','TRA','T2','T24','T30','T50','P2','P15','P30','Nf','Nc','epr','Ps30','phi','NRf','NRc','BPR','farB','htBleed','Nf_dmd','PCNfR_dmd','W31','W32']
    #data.columns = columns
    #univ_stat = train.describe()
    #data.drop(columns=['Nf_dmd','PCNfR_dmd','P2','P15','T2','TRA','farB','epr'],inplace=True)
    data = data.to_numpy()
   
    #x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # Creates `data` structure to save and 
    # share train and test datasets.
    #data = {'x_train' : x_train.tolist(),
    #        'y_train' : y_train.tolist(),
    #        'x_test' : x_test.tolist(),
    #        'y_test' : y_test.tolist()}
    data={'data':data.tolist()}

    # Creates a json object based on `data`
    data_json = json.dumps(data)

    # Saves the json object into a file
    with open(args.data, 'w') as out_file:
        json.dump(data_json, out_file)

if __name__ == '__main__':
    
    # This component does not receive any input
    # it only outpus one artifact which is `data`.
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str)
    
    args = parser.parse_args()
    
    # Creating the directory where the output file will be created 
    # (the directory may or may not exist).
    Path(args.data).parent.mkdir(parents=True, exist_ok=True)

    _download_data(args)
    