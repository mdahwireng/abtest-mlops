from sklearn.preprocessing import LabelEncoder
import pandas as pd

class PrepareData():
    def __init__(self, df) -> None:
        data = df.copy()
        data.rename(columns={'yes':'answer'}, inplace=True)
        self.data = data


    def encode_cat(self, cols, output=False):
        data = self.data.copy()
        print('Encoding categorical columns...')
        for col in cols:
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col])
        print('Encoding categorical columns completed')
        self.data = data
        if output:
            return data


    def drop_id_col(self, id_col, output=False):
        print('Dropping id_column...')
        data = self.data.copy()
        data.drop(columns=id_col, inplace=True)
        print('Dropping id_column completed')
        self.data = data
        if output:
            return data

    def get_day(self):
        data = self.data.copy()
        data['date'] = pd.to_datetime(data['date'])
        print('Retrieving day of the week from date...')
        data['day'] = data['date'].apply(lambda x:x.weekday())
        print('Retrieval of day from date completed')
        self.data = data

    def subset(self):
        data = self.data.copy()
        browser_cols = ['experiment', 'day', 'hour', 'device_make', 'browser', 'answer']
        platform_cols = ['experiment', 'day', 'hour', 'device_make', 'platform_os', 'answer']
        print('Subsetting for browser df...')
        browser_df = data[browser_cols]
        print('Subsetting for platform_os df...')
        platform_df = data[platform_cols]
        print('Subsetting completed and data returned in this order:\nbrowser_df, platform_df')
        return browser_df, platform_df