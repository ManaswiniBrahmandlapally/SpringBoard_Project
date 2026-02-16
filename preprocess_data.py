import numpy as np
import pandas as pd

def preprocess_data():
    df = pd.read_csv("clean_data (1).csv")

    df['ProdID'] = df['ProdID'].replace('-2147483648', np.nan)
    df["User's ID"] = df["User's ID"].replace('-2147483648', np.nan)

    df = df.dropna(subset=["User's ID"])
    df["User's ID"] = df["User's ID"].astype('int64')

    df = df.dropna(subset=['ProdID'])
    df['ProdID'] = df['ProdID'].astype('int64')

    df['Review Count'] = df['Review Count'].astype('int64')

    df['Category'] = df['Category'].fillna('')
    df['Brand'] = df['Brand'].fillna('')
    df['Description'] = df['Description'].fillna('')
    df['Tags'] = df['Tags'].fillna('')

    df['ImageURL'] = df['ImageURL'].astype(str).str.replace('|','',regex=False)

    df.reset_index(drop=True, inplace=True)

    return df   


if __name__ == "__main__":
    cleaned = preprocess_data()
    print(cleaned.head())
