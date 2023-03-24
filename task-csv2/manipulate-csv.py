import pandas as pd

path = r'C:\Users\7000031725\Desktop\New folder\reco_raw_Sample.csv'

df = pd.read_csv(path, delimiter='|',quotechar=',')
# print(df.to_string())
# print('-------------------------------')
# print(df.columns.str.lower())

# renaming the columns
df.rename(columns={'country_name': 'country',
                   'region_name': 'region'}, inplace=True)
# print(df.columns)

# # removing the columns
df.drop(['device_model_category', 'os_name',
        'app_code', 'error_id', 'is_child'],axis=1,inplace=True)
# print(df.columns)

# changing the value of EPISODE
df['classification1'] = df['classification'].replace('EPISODE','sony episode')
print(df.to_string())
df['new_monitory_value'] = df['monitory_value'].replace({'SVOD':'service VOD','AVOD':'advertisement VOD'})
print(df.to_string())
# print(df['classification'].to_string())

#converting the csv file into a df 
df.to_csv(r'C:\Users\7000031725\Desktop\New folder\edited_reco_raw_Sample.csv')
