import pandas as pd

class CleanData:
    def __init__(self, df):
        self.data = df.copy()

    def convert_to_date(self, cols):
        print('Converting colums to datetime initialized...')
        data = self.data.copy()
        for col in cols:
            print('\nConverting colums {} to datetime'.format(col))
            data[col] = pd.to_datetime(data[col])
        print('Converting colums to datetime completed')
        self.data = data
    
    def remove_unanswered(self):
        print('\nRemoval of anwsered surveys initialized...')
        data = self.data.copy()
        answered_index = ((data['yes'] == 1) | (data['no'] ==1))
        cleaned_df = data[answered_index]
        cleaned_df.reset_index(drop=True, inplace=True)
        print('\nRemoval of anwsered surveys completed')
        self.data = cleaned_df
        return cleaned_df  