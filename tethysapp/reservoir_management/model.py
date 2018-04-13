#These are python scripts that use the streamflow prediction tool api to get specific values. The reach ids for the rivers going into the
#reservoirs are hardcoded. We will need to create a python dictionary with pairs for reservoirs and their reaches.

import requests
import datetime as dt
import pandas as pd
from .app import ReservoirManagement as app
import os


def getforecastflows(comids):


    #These are the comids for the rivers that go into the reservoirs. See Streamflow Prediction Tool
    allvalues = {}

    for x in comids:
        #the information for where to look for the comids. We may need to think of a different way to do this because not all the rivers we
        #need are in this watershed/subbasin combination.
        comid = x
        startdate = 'most_recent'

        request_params = dict(watershed_name='Dominican Republic', subbasin_name='National', reach_id=x,
                              forecast_folder='most_recent', stat_type='mean')
        request_headers = dict(Authorization='Token fa7fa9f7d35eddb64011913ef8a27129c9740f3c')
        res = requests.get('http://tethys-staging.byu.edu/apps/streamflow-prediction-tool/api/GetForecast/',
                           params=request_params, headers=request_headers)

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
    damsheet = os.path.join(app_workspace.path, 'DamLevel_DR_BYU 2018.xlsx')

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



def forecastlevels(comids,res):

    outflow = 3.0
    outtime = 24.0
    elevval = 185.1

    outvol = outflow * outtime * 3600.0

    totalflow = []
    tsvol = []
    tselev = []

    elev = res + '_Elev'
    vol = res + '_Vol'

    app_workspace = app.get_app_workspace()
    elevcurves = os.path.join(app_workspace.path, 'BATIMETRIA PRESAS RD.xlsx')

    df = pd.read_excel(elevcurves)

    volres = df.loc[df[elev] == elevval, vol].iloc[0]
    volin = volres * 1000000

    for comid in comids:
        request_params = dict(watershed_name='Dominican Republic', subbasin_name='National', reach_id=comid,
                              forecast_folder='most_recent', stat_type='mean', return_format='csv')
        request_headers = dict(Authorization='Token fa7fa9f7d35eddb64011913ef8a27129c9740f3c')
        res = requests.get('https://tethys-staging.byu.edu/apps/streamflow-prediction-tool/api/GetForecast/',
                           params=request_params, headers=request_headers)

        data = res.content.splitlines()

        ts = []
        comidflows = []

        for i in data:
            ts.append(i.split(','))

        ts.pop(0)

        for r in ts:
            comidflows.append(float(r[1]))

        totalflow.append(comidflows)

    totalflow = [sum(x) for x in zip(*totalflow)]

    entries = len(ts)

    for x in range(0, entries):
        if x == 0:
            inflow1 = float(totalflow[x])
            time1 = dt.datetime.strptime(ts[x][0], "%Y-%m-%d %H:%M:%S")
        else:
            inflow2 = float(totalflow[x])
            time2 = dt.datetime.strptime(ts[x][0], "%Y-%m-%d %H:%M:%S")
            timedif = (time2 - time1).total_seconds()
            vol2 = (inflow2 + inflow1) / 2 * timedif
            volin = volin + vol2
            inflow1 = inflow2
            time1 = time2
            if ts[x][0].endswith('12:00:00'):
                if not tsvol:
                    tsvol.append([str(ts[x][0])[:10], volin - (outvol / 2.0)])
                    volin = volin - (outvol / 2.0)
                else:
                    tsvol.append([str(ts[x][0])[:10], volin - outvol])
                    volin = volin - (outvol)

    for q in tsvol:
        volval = q[1]
        volval = volval / 1000000.0
        evolval = (df.loc[df[vol] > volval, elev].iloc[0])
        tselev.append([q[0], evolval])

    return(tselev)

def forecastdata(comids,res,outflow):
    outtime = 24.0

    if res == 'Sabana_Yegua':
        res = 'S. Yegua'
    app_workspace = app.get_app_workspace()
    damsheet = os.path.join(app_workspace.path, 'DamLevel_DR_BYU 2018.xlsx')

    dfnan = pd.read_excel(damsheet)
    df1 = dfnan[['Nivel', res]]
    df = df1.dropna()[::-1]
    reslevel = df[:1]
    lastdate = reslevel['Nivel']
    lastlevel = reslevel[res]

    lastobsdate = str(lastdate.iloc[0])[:10]
    elevval = lastlevel.iloc[0]

    outvol = outflow * outtime * 3600.0

    totalflow = []
    tsvol = []
    tselev = []
    data = {}
    dataformatted = {}

    if res == 'S. Yegua':
        res = 'Sabana_Yegua'

    elev = res + '_Elev'
    vol = res + '_Vol'

    elevcurve = os.path.join(app_workspace.path, 'BATIMETRIA PRESAS RD.xlsx')

    df = pd.read_excel(elevcurve)

    volres = df.loc[df[elev] == elevval, vol].iloc[0]
    volin = volres * 1000000

    for comid in comids:
        request_params = dict(watershed_name='Dominican Republic', subbasin_name='National', reach_id=comid,
                              forecast_folder='most_recent', stat_type='mean', return_format='csv')
        request_headers = dict(Authorization='Token fa7fa9f7d35eddb64011913ef8a27129c9740f3c')
        res = requests.get('https://tethys-staging.byu.edu/apps/streamflow-prediction-tool/api/GetForecast/',
                           params=request_params, headers=request_headers)

        content = res.content.splitlines()

        ts = []
        comidflows = []
        allcomidflows = []

        for i in content:
            ts.append(i.split(','))

        ts.pop(0)

        for r in ts:
            allcomidflows.append(float(r[1]))
            if r[0].endswith('12:00:00'):
                comidflows.append(float(r[1]))

        totalflow.append(allcomidflows)
        data[comid] = comidflows

    newseries = []
    for x in data:
        newseries.append(data[x])

    total = [sum(x) for x in zip(*newseries)]
    alltotal = [sum(x) for x in zip(*totalflow)]
    data['total'] = total

    for x in data:
        formattedtotal = ["%.2f" % elem for elem in data[x]]
        dataformatted[x] = formattedtotal

    entries = len(ts)

    dates = []

    for x in range(0, entries):
        if x == 0:
            inflow1 = float(alltotal[x])
            time1 = dt.datetime.strptime(ts[x][0], "%Y-%m-%d %H:%M:%S")
        else:
            inflow2 = float(alltotal[x])
            time2 = dt.datetime.strptime(ts[x][0], "%Y-%m-%d %H:%M:%S")
            timedif = (time2 - time1).total_seconds()
            vol2 = (inflow2 + inflow1) / 2 * timedif
            volin = volin + vol2
            inflow1 = inflow2
            time1 = time2
            if ts[x][0].endswith('12:00:00'):
                if not tsvol:
                    tsvol.append([str(ts[x][0])[:10], volin - (outvol / 2.0)])
                    dates.append(str(ts[x][0])[5:-9])
                    volin = volin - (outvol / 2.0)
                else:
                    tsvol.append([str(ts[x][0])[:10], volin - outvol])
                    dates.append(str(ts[x][0])[5:-9])
                    volin = volin - (outvol)

    for q in tsvol:
        volval = q[1]
        volval = volval / 1000000.0
        evolval = (df.loc[df[vol] > volval, elev].iloc[0])
        tselev.append(evolval)

    dataformatted['levels'] = tselev
    dataformatted['dates'] = dates

    return(dataformatted)





