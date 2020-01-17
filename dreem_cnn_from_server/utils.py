import os
import h5py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

def select_columns(df, select=[], drop=[], dummy_vars=True):
    if len(select) == 0:
        cols = [c for c in df.columns if not _contains_one_of_sub_str(drop, c)]
    else:
        cols = [c for c in df.columns
        if _contains_one_of_sub_str(select, c)
        and not _contains_one_of_sub_str(drop, c)]

    if not dummy_vars:
        cols = [c for c in cols if 'curr_sleep_stage' not in c]

    return cols

def _contains_one_of_sub_str(str_arr, col_name):
    for s in str_arr:
        if s in col_name: return True
    return False

if __name__ == "__main__":
    str_arr = ['fft', 'wawelet']

    df_train_path = os.path.join(os.path.dirname(__file__), '..', 'df_train_final.h5')
    df_train = pd.read_hdf(df_train_path)

    df = df_train[select_columns(df_train, drop=str_arr, dummy_vars=False)]

    print(list(df.columns))
