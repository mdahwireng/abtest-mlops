from modules.utility import get_csv_data, save_csv
from modules.prepare_data import PrepareData

cleaned_df = get_csv_data(path='./data/AdsmartABdata.csv', version="v2")