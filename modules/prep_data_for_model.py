import numpy as np
class PrepareForModel():
    def __init__(self, df) -> None:
        self.data = df.copy()

    def split(self, train, test, validation):
        data = self.data.copy()
        second = train + test
        train_df, test_df, val_df = np.split(data.sample(frac=1, random_state=42),
                                        [int(train*len(data)), int(second*len(data))])
        self.train_df = train_df
        self.test_df = test_df
        self.val_df = val_df
        return train_df, test_df, val_df

def get_target(df, target_col='answer'):
    data = df.copy()
    target = data[target_col]
    data.drop(columns=[target_col], inplace=True)
    return data, target