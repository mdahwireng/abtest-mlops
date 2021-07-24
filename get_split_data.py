from modules.utility import get_csv_data, save_csv
from modules.prepare_data import PrepareData

cleaned_df = get_csv_data(path='./data/AdsmartABdata.csv', version='v2.0')

prep_data = PrepareData(cleaned_df)
prep_data.encode_cat(cols=['experiment', 'date', 'hour', 'device_make', 'browser'])
prep_data.drop_id_col(id_col=['auction_id'])
prep_data.get_day()
brwser_df, platform_df = prep_data.subset()

save_csv(brwser_df, './data/bowser_df.csv')
save_csv(platform_df, './data/platform_df.csv')