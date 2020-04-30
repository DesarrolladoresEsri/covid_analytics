import pandas as pd


def _cleanname(name):
    if name[-1] == '-':
        name = name[:-1]
    return name


def pulldataDict():
    dfo = pd.read_csv(
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    df = dfo
    df['Province/State'].fillna(value='', inplace=True)
    df['site'] = df['Country/Region']+'-'+df['Province/State']
    df['site'] = df['site'].apply(lambda x: _cleanname(x))
    sites = list(df['site'].unique())
    df0 = df.groupby(['Country/Region', 'Province/State',
                      'site', 'Lat', 'Long']).sum().stack().reset_index()
    df0.rename(columns={'level_5': 'date', 0: 'accumulated'}, inplace=True)
    df0['date'] = df0['date'].apply(lambda x: pd.to_datetime(x))
    return {"sites": sites, "Dataframe": df0}
