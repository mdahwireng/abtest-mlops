from sklearn.preprocessing import LabelEncoder

class PrepareData():
    def __init__(self, df) -> None:
        self.data = df.copy()

    def encode_cat(self, cols, output=True):
        data = self.data.copy()
        print('Encoding categorical columns...')
        for col in cols:
            le = LabelEncoder()
            data[col] = le.fit(data[col])
        print('Encoding categorical columns completed')
        self.data = data
        if output:
            return data

    def drop_id_col(self, id_col):
        print('Dropping id_column...')
        data = self.data.copy()
        data.drop(columns=id_col, inplace=True)
        return data