from sklearn.preprocessing import LabelEncoder

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
            data[col] = le.fit(data[col])
        print('Encoding categorical columns completed')
        self.data = data
        if output:
            return data


    def drop_id_col(self, id_col, output=False):
        print('Dropping id_column...')
        data = self.data.copy()
        data.drop(columns=id_col, inplace=True)
        self.data = data
        if output:
            return data

    def get_day(self):
        data = self.data.copy()
        data['day'] = data['date'].apply(lambda x:x.weekday())
        self.data = data

    def subset(self):
        data = self.data.copy()
        browser_cols = ['experiment', 'date', 'day', 'hour', 'device_make', 'browser', 'answer']
        platform_cols = ['experiment', 'date', 'day', 'hour', 'device_make', 'platform_os', 'answer']
        browser_df = data[browser_cols]
        platform_df = data[platform_cols]
        return browser_df, platform_df