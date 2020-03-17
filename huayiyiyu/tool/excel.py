import pandas as pd

import os
import sys

def import_data():
    df = pd.read_excel(io='exc.xlsx')
    data={}
    for i in range(0,len(df)):
        clothes = df.loc[i]['Unnamed: 0']
        if not pd.isnull(clothes):
            key=clothes
            data[key]=[]
        data[key].append(df.loc[i]['詞目/譯語'])
    return data



