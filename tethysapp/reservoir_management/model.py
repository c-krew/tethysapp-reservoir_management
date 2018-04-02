#These are python scripts that use the streamflow prediction tool api to get specific values. The reach ids for the rivers going into the
#reservoirs are hardcoded. We will need to create a python dictionary with pairs for reservoirs and their reaches.

import requests
import datetime as dt
import pandas as pd
from .app import ReservoirManagement as app
import os


def getforecastflows(watershed,subbasin,comids):


    #These are the comids for the rivers that go into the reservoirs. See Streamflow Prediction Tool
    allvalues = {}

    for x in comids:
        #the information for where to look for the comids. We may need to think of a different way to do this because not all the rivers we
        #need are in this watershed/subbasin combination.
        comid = x
        startdate = 'most_recent'


        res = requests.get('https://tethys.byu.edu/apps/streamflow-prediction-tool/api/GetWaterML/?watershed_name=' +
                           watershed + '&subbasin_name=' + subbasin + '&reach_id=' + comid + '&start_folder=' +
                           startdate + '&stat_type=mean',
                           headers={'Authorization': 'Token 72b145121add58bcc5843044d9f1006d9140b84b'})


        #The following code takes the results from the streamflow prediction tool and then sorts through it to get the flows
        content = res.content

        data = content.split('dateTimeUTC="')
        data.pop(0)

        values = []
        timestep = []

        for e in data:
            parser = e.split('"  methodCode="1"  sourceCode="1"  qualityControlLevelCode="1" >')
            dateraw = parser[0]
            dates = dt.datetime.strptime(dateraw, "%Y-%m-%dT%H:%M:%S")
            if str(dates).endswith("00:00:00"):
                value = float(parser[1].split('<')[0])
                values.append(value)
                timestep.append(str(dates)[5:-9])
        allvalues[comid] = values

    newseries = []
    allformvalues = {}
    for x in allvalues:
        newseries.append(allvalues[x])

    total = [sum(x) for x in zip(*newseries)]
    allvalues['total'] = total

    for x in allvalues:
        formattedtotal = ["%.2f" % elem for elem in allvalues[x]]
        allformvalues[x] = formattedtotal

    allformvalues['timestep'] = timestep

    return allformvalues


def gethistoricaldata(res):

    app_workspace = app.get_app_workspace()
    damsheet = os.path.join(app_workspace.path, 'DamLevel_DR_BYU 2018.xlsx')

    dfnan = pd.read_excel(damsheet)
    df1 = dfnan[['Nivel', res]]
    df = df1.dropna()

    data = []

    for index, row in df.iterrows():
        timestep = row["Nivel"].to_pydatetime()
        value = row[res]
        data.append([timestep, value])

    if res == 'Bao':
        del data[0]
        del data[0]
    elif res == 'Moncion':
        del data[0]

    return data

def getrecentdata():

    app_workspace = app.get_app_workspace()
    damsheet = os.path.join(app_workspace.path, 'NEWDamLevel_DR_BYU 2018.xlsx')

    dfnan = pd.read_excel(damsheet)

    today = dt.datetime.now()
    year = str(today.year)
    month = str(today.strftime("%B"))
    day = str(today.day)
    date = month + ' ' + day + ', ' + year

    time = str(dt.datetime.strptime(date, '%B %d, %Y'))[0:10]

    dfdateindex = dfnan.set_index("Nivel")

    dfdateindex = dfdateindex.loc[:time]

    dftable = (dfdateindex[::-1])
    dftable = (dftable[:10])

    data = []
    for row in dftable.itertuples():
        Time = str(row[0])[:10]
        #    Level = str(row[1:15])
        Tavera = row[1]
        #Bao = row[2]
        Moncion = row[3]
        Rincon = row[4]
        Hatillo = row[5]
        Jiguey = row[6]
        Valdesia = row[7]
        Yegua = row[8]
        Sabaneta = row[9]
        Blanco = row[10]
        Pinalito = row[11]
        Maguaca = row[12]
        Chacuey = row[13]
        #    Lopez = row[14]

        data.append((Time, Tavera, Moncion, Rincon, Hatillo, Jiguey, Valdesia, Yegua, Sabaneta, Blanco, Pinalito,
                     Maguaca, Chacuey))

    return data





