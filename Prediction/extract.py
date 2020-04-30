import pandas as pd
def cleanname(name):
        if name[-1]=='-':
            name=name[:-1]
        else:
            name=name
        return name
def pulldataDict():
    dfo=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    df=dfo
    df['Province/State'].fillna(value='',inplace=True)
    df['site']=df['Country/Region']+'-'+df['Province/State']
    #clean the countries with little data 
#     df=df[df[list(df)[-4]]>0]
#     df=df[df[list(df)[-3]]>0]
    #clean site name to do the filters
    df['site']=df['site'].apply(lambda x: cleanname(x))
    sites=list(df['site'].unique())
    df0=df.groupby(['Country/Region','Province/State','site','Lat','Long']).sum().stack().reset_index()
    df0.rename(columns={'level_5':'date',0:'accumulated'}, inplace=True)
    df0['date']=df0['date'].apply(lambda x:pd.to_datetime(x))
    return {"sites":sites,"Dataframe":df0}
