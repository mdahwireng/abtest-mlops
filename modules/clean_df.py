import dvc.api
import pandas as pd

class CleanData:
    def __init__(self, df):
        self.data = df.copy()

    def convert_to_date(self, cols):
        data = self.data.copy()
        for col in cols:
            data[col] = pd.to_datetime(data[col])
        self.data = data
    
    def remove_unanswered(self):
        data = self.data.copy()
        answered_index = ((data['yes'] == 1) | (data['no'] ==1))
        cleaned_df = data[answered_index]
        cleaned_df.reset_index(drop=True, inplace=True)
        self.data = cleaned_df
        return cleaned_df  