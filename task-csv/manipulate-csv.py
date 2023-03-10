import pandas as pd

path = r'C:\Users\7000031725\Desktop\fileio\task-csv\reco_raw_Sample.csv'

df = pd.read_csv(path)
# print(df.to_string())
# print('-------------------------------')
print(df.columns.str.lower())

df2 = df.rename(columns={'country_name': 'country',
                'region_name': 'region'}, inplace=False)

# print(df2.to_string())
