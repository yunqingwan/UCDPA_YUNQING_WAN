import kaggle

from kaggle.api.kaggle_api_extended import KaggleApi

#import data from Kaggle API
api = KaggleApi()
api.authenticate()

api.dataset_download_file('gpreda/covid-world-vaccination-progress',
                          file_name='country_vaccinations.csv')

import zipfile
with zipfile.ZipFile('country_vaccinations.csv.zip', 'r') as zipref:
    zipref.extractall()

#Import a CSV File into a Pandas DataFrame
import pandas as pd
import numpy as np

country_vac = pd.read_csv("country_vaccinations.csv")

print(country_vac.head())
print(country_vac.shape)
print(country_vac.country.unique())

#Sorting ascending
print(country_vac.sort_values('date').head())

#indexing and grouping data for Ireland
print(country_vac.columns)
ireland_vac = country_vac[country_vac['country'] == 'Ireland']
print(ireland_vac)

#repalce missing values
missing_values_count = ireland_vac.isnull().sum()
print(missing_values_count)

cleaned_ireland_vac = ireland_vac.fillna(method='bfill', axis=0).fillna(0)
print(cleaned_ireland_vac.isnull().sum())

#iterate through each row and select
#'date' and 'people_vaccinated' column respectively
print("People vaccinated in Ireland according to date:\n")
for i in range(len(cleaned_ireland_vac)):
    print(cleaned_ireland_vac.iloc[i, 2], cleaned_ireland_vac.iloc[i, 9])

uk_vac = country_vac[country_vac['country'] == 'United Kingdom']
print(uk_vac)
print(uk_vac.columns)
cleaned_uk_vac = uk_vac.fillna(method='bfill', axis=0).fillna(0)
print(cleaned_uk_vac.isnull().sum())

print("People vaccinated in UK according to data:\n")
for i in range(len(cleaned_uk_vac)):
    print(cleaned_uk_vac.iloc[i, 2], cleaned_uk_vac.iloc[i, 9])

#merge dataframes for data from Ireland and UK
ireland_uk_vac = pd.merge(cleaned_ireland_vac, cleaned_uk_vac, on='date', how ='outer')
print(cleaned_ireland_vac)
print(ireland_uk_vac)
print(ireland_uk_vac.columns)

print("Obtain data of vaccinated people per hundred in Ireland and UK")
vac_per_hundred_irl_uk = ireland_uk_vac[['country_x', 'people_vaccinated_per_hundred_x',
                                        'country_y','people_vaccinated_per_hundred_y']]
print(vac_per_hundred_irl_uk)









