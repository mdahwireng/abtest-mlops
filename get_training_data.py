from modules.utility import get_csv_data, save_csv
from modules.prep_data_for_model import PrepareForModel, get_target

cleaned_df = get_csv_data(path='./data/AdsmartABdata.csv', version='v2.0')

browser_df = get_csv_data(path='./data/bowser_df.csv', version='bv1')
brower_df_prep = PrepareForModel(browser_df)
browser_train, browser_test, browser_val = brower_df_prep.split(0.7,0.2,0.1)

browser_trainX, browser_trainY = get_target(browser_train)
save_csv(browser_trainX, './data/browser_trainX.csv')
save_csv(browser_trainY, './data/browser_trainY.csv')

browser_testX, browser_testY = get_target(browser_test)
save_csv(browser_testX, './data/browser_testX.csv')
save_csv(browser_testY, './data/browser_testY.csv')

browser_valX, browser_valY = get_target(browser_val)
save_csv(browser_valX, './data/browser_valX.csv')
save_csv(browser_valY, './data/browser_valY.csv')

platform_df = get_csv_data(path='./data/platform_df.csv', version='pv1')
platform_df_prep = PrepareForModel(platform_df)
platform_train, platform_test, platform_val = platform_df_prep.split(0.7,0.2,0.1)

platform_trainX, platform_trainY = get_target(platform_train)
save_csv(platform_trainX, './data/platform_trainX.csv')
save_csv(platform_trainY, './data/platform_trainY.csv')

platform_testX, platform_testY = get_target(platform_test)
save_csv(platform_testX, './data/platform_testX.csv')
save_csv(platform_testY, './data/platform_testY.csv')

platform_valX, platform_valY = get_target(browser_val)
save_csv(platform_valX, './data/platform_valY.csv')
save_csv(platform_valY, './data/platform_valY.csv')