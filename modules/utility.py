import pandas as pd
import dvc.api

def get_csv_data(data_path):
    print('Reading data from dvc source....')
    data_url = dvc.api.get_url(data_path)
    df = pd.read_csv(data_url)
    print('Reading completed, data saved as {}'.format(data_path))
    return df

def save_csv(df, path):
    df.to_csv(path)
    print('Data saved as {}'.format(path))