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
print("The number of countries that are affected by Covid 19:")
print(country_vac["country"].nunique())
print(country_vac.country.unique())

#indexing and grouping data for Ireland
print(country_vac.columns)
ireland_vac = country_vac[country_vac['country'] == 'Ireland']
print(ireland_vac)

uk_vac = country_vac[country_vac['country'] == 'United Kingdom']
print(uk_vac)

#repalce missing values
ireland_missing_values_count = ireland_vac.isnull().sum()
print(ireland_missing_values_count)

cleaned_ireland_vac = ireland_vac.fillna(method='ffill', axis=0).fillna(0)
print(cleaned_ireland_vac.isnull().sum())

uk_missing_values_count = uk_vac.isnull().sum()
print(uk_missing_values_count)

cleaned_uk_vac = uk_vac.fillna(method='ffill', axis=0).fillna(0)
print(cleaned_uk_vac.isnull().sum())

#iterate through each row and select 'date' and 'people_vaccinated' column respectively
print(cleaned_ireland_vac.columns)
print("People vaccinated per hundred in Ireland from vaccination starts:")
for i in range(len(cleaned_ireland_vac)):
    print(cleaned_ireland_vac.iloc[i, 2], cleaned_ireland_vac.iloc[i, 9])

print("People vaccinated per hundred in UK from vaccination starts:")
print(cleaned_uk_vac.columns)
for i in range(len(cleaned_uk_vac)):
    print(cleaned_uk_vac.iloc[i, 2], cleaned_uk_vac.iloc[i, 9])

#merge dataframes for data from Ireland and UK
ireland_uk_vac = pd.merge(cleaned_ireland_vac, cleaned_uk_vac, on='date', how='outer')
print(cleaned_ireland_vac)
print(ireland_uk_vac)
print(ireland_uk_vac.columns)

print("The vaccines are used in Ireland are :")
print(ireland_uk_vac.iloc[:, 12].value_counts(normalize=True))

print("The vaccines are used in UK are: ")
print(ireland_uk_vac.iloc[:, 26].value_counts(normalize=True))

print("Obtain data of vaccinated people per hundred in Ireland and UK")
vac_per_hundred_irl_uk = ireland_uk_vac[['date', 'country_x', 'people_vaccinated_per_hundred_x',
                                        'country_y','people_vaccinated_per_hundred_y']]
print(vac_per_hundred_irl_uk)

#to return a column of a pandas DataFrame as a list
ireland_vac_per_hundred_list = ireland_uk_vac['people_vaccinated_per_hundred_x'].tolist()
print(ireland_vac_per_hundred_list)

#to remove nan value in the list to return max number in the list:
import math
ireland_vac_per_hundred_list_noNaN = [x for x in ireland_vac_per_hundred_list if math.isnan(x) == False]
print(ireland_vac_per_hundred_list_noNaN)
print("The maximum daily rate of people vaccinated per hundred in Ireland from 2020-12-31 to 2021-05-05 is: ")
print(max(ireland_vac_per_hundred_list_noNaN))

uk_vac_per_hundred_list = ireland_uk_vac['people_vaccinated_per_hundred_y'].tolist()
print(uk_vac_per_hundred_list)

uk_vac_per_hundred_list_noNaN = [x for x in uk_vac_per_hundred_list if math.isnan(x) == False]
print(uk_vac_per_hundred_list_noNaN)

print("The maximum daily rate of people vaccinated per hundred in UK from 2020-12-31 to 2021-05-05 is: ")
print(max(uk_vac_per_hundred_list_noNaN))

#Numpy
import numpy as np
print(type(ireland_uk_vac['people_vaccinated_per_hundred_x']))
#covert columns in pandas DataFrame to Numpy array
vac_per_hundred_irl_number_only = ireland_uk_vac['people_vaccinated_per_hundred_x']
vac_per_hundred_uk_number_only = ireland_uk_vac['people_vaccinated_per_hundred_y']
x = vac_per_hundred_irl_number_only.to_numpy()
y = vac_per_hundred_uk_number_only.to_numpy()
print(x)
print(y)

print("The ratio of people vaccinated per hundred between Ireland and UK on daily basis is:")
print(x/y)

#define a function to find if the people vaccinated per hundred in Ireland and UK great than 50
x_list = x.tolist()
y_list = y.tolist()

def check(list, val):
    return(any(x > val for x in list))

list = x_list
val = 50
if(check(list,50)):
    print("The people vaccinated per hundred per day in Ireland has over 50")
else:
    print("The people vaccinated per hundred per day in Ireland hasn't over 50")

list =y_list
val = 50
if(check(list, val)):
    print("The people vaccinated per hundred per day in UK has over 50")
else:
    print("The people vaccinated per hundred per day in UK hasn't over 50")

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import datetime as dt

fix, ax = plt.subplots()
cleaned_ireland_vac["date"] = pd.to_datetime((cleaned_ireland_vac["date"]))
cleaned_uk_vac["date"] = pd.to_datetime((cleaned_uk_vac["date"]))
ax.plot(cleaned_ireland_vac["date"], cleaned_ireland_vac['people_fully_vaccinated_per_hundred'], color="g", label="Ireland")
ax.plot(cleaned_uk_vac["date"], cleaned_uk_vac['people_fully_vaccinated_per_hundred'], color="r", label="UK")
ax.set(xlabel="Time (Dates)",
       ylabel="People fully vaccinated per hundred",
       title="People fully vaccinated per hundred in Ireland and UK\n January 2021 - May 2021")

date_form = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(date_form)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
plt.xticks(rotation=45)
ax.legend()
plt.show()


cleaned_ireland_vac["date"] = pd.to_datetime((cleaned_ireland_vac["date"]))
plt.bar(cleaned_ireland_vac["date"], cleaned_ireland_vac["people_vaccinated"], color="green")
plt.xlabel("Time (Dates)")
plt.ylabel("People vaccinated")
plt.title("People vaccinated in Ireland\n January 2021 - May 2021")
plt.xticks(rotation=45)
plt.show()

cleaned_uk_vac["date"] = pd.to_datetime((cleaned_uk_vac["date"]))
plt.bar(cleaned_uk_vac["date"], cleaned_uk_vac["people_vaccinated"], color="red")
plt.xlabel("Time (Dates)")
plt.ylabel("People vaccinated")
plt.title("People vaccinated in UK\n January 2021 - May 2021")
plt.xticks(rotation=45)
plt.show()