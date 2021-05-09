import kaggle

from kaggle.api.kaggle_api_extended import KaggleApi

#import data from Kaggle API
api = KaggleApi()
api.authenticate()

api.dataset_download_file('gpreda/covid-world-vaccination-progress',
                          file_name='country_vaccinations_by_manufacturer.csv')

api.dataset_download_file('gpreda/covid-world-vaccination-progress',
                          file_name='country_vaccinations.csv')

import zipfile
with zipfile.ZipFile('country_vaccinations.csv.zip', 'r') as zipref:
    zipref.extractall()

#Import a CSV File into a Pandas DataFrame
import pandas as pd
import numpy as np

country_vac = pd.read_csv("country_vaccinations.csv")
country_vac_mfr = pd.read_csv('country_vaccinations_by_manufacturer.csv')

print(country_vac.head())
print(country_vac_mfr.head())
print(country_vac.shape)
print(country_vac_mfr.shape)
print(country_vac.country.unique())

#Sorting ascending
print(country_vac.sort_values('date').head())

#indexing and grouping
print(country_vac.columns)
ireland_vac = country_vac[country_vac['country'] == 'Ireland']
print(ireland_vac)

#repalce missing values
missing_values_count = ireland_vac.isnull().sum()
print(missing_values_count)

cleaned_ireland_vac = ireland_vac.fillna(method='bfill', axis=0).fillna(0)
print(cleaned_ireland_vac.isnull().sum())








