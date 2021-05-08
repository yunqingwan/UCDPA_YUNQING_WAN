import kaggle

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

api.dataset_download_file('gpreda/covid-world-vaccination-progress',
                          file_name='country_vaccinations_by_manufacturer.csv')

api.dataset_download_file('gpreda/covid-world-vaccination-progress',
                          file_name='country_vaccinations.csv')

import zipfile
with zipfile.ZipFile('country_vaccinations.csv.zip', 'r') as zipref:
    zipref.extractall()

import pandas as pd

country_vac = pd.read_csv("country_vaccinations.csv")
country_vac_mfr = pd.read_csv('country_vaccinations_by_manufacturer.csv')

print(country_vac.head())
print(country_vac_mfr.head())

