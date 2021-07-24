from modules.utility import get_csv_data, save_csv
from modules.clean_df import CleanData

raw_data = get_csv_data('./data/AdsmartABdaa.csv')

clean = CleanData(raw_data)

clean.convert_to_date('date')

cleaned_data = clean.remove_unanswered()

save_csv(cleaned_data, './data/cleaned.csv')