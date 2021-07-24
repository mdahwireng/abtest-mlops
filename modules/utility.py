import pandas as pd
import dvc.api

def get_csv_data(data_path):
    data_url = dvc.api.get_url(data_path)
    df = pd.read_csv(data_url)
    return df

def save_csv(df, path):
    df.to_csv(path)