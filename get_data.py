import requests
import pandas as pd
from pandas.io.json import json_normalize
from pandas_profiling import ProfileReport

""" Ins this file: How to get data from European resource"""
url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/json/'
r = requests.get(url)
j = json_normalize(r.json()['records'])
df = pd.DataFrame.from_dict(j)
profile = ProfileReport(df)
profile.to_file(output_file="output.html")
