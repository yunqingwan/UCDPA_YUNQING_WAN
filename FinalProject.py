import pandas as pd

country_vac = pd.read_csv("country_vaccinations.csv")
country_vac_mfr = pd.read_csv("country_vaccinations_by_manufacturer.csv")

print(country_vac.head())
print(country_vac_mfr.head())