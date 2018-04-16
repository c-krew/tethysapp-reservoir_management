from django.http import JsonResponse, Http404, HttpResponse
from .app import ReservoirManagement as app
import datetime as dt
import pandas as pd
import os
import requests

def append_res_info(request):
    return_obj = {
        'success': True
    }

    # Check if its an ajax post request
    if request.is_ajax() and request.method == 'GET':
        dam = request.GET.get('dam')
        level = request.GET.get('level')
        date = request.GET.get('date')

        app_workspace = app.get_app_workspace()
        file = os.path.join(app_workspace.path, 'DamLevel_DR_BYU 2018.xlsx')
        filenew = os.path.join(app_workspace.path, 'NEWDamLevel_DR_BYU 2018.xlsx')

        reservoir = dam
        level = level
        date = date

        dams = {'Tavera-Bao': "1", 'Moncion': "3", 'Rincon': "4", 'Hatillo': "5", 'Jiguey': "6",
                'Valdesia': "7", 'Sabana Yegua': "8", 'Sabaneta': "9", 'Pinalito': "10", 'Chacuey': "11",
                'Maguaca': "12"}

        damnames = {'Tavera-Bao': "Tavera", 'Moncion': "Moncion", 'Rincon': "Rincon", 'Hatillo': "Hatillo",
                    'Jiguey': "Jiguey",
                    'Valdesia': "Valdesia", 'Sabana Yegua': "S. Yegua", 'Sabaneta': "Sabaneta",
                    'Pinalito': "Pinalito",
                    'Chacuey': "Chacuey", 'Maguaca': "Maguaca"}

        df = pd.read_excel(file)

        from datetime import datetime
        time = str(datetime.strptime(date, '%B %d, %Y'))[0:10]

        df.loc[df.Nivel == time, damnames[reservoir]] = level

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(file, engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, index=False, sheet_name='Sheet1')

        # Get the xlsxwriter workbook and worksheet objects.
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

    return JsonResponse(return_obj)

def forecastdata(request):

    dataformatted = {
        'success': True
    }

    comids = request.GET.get('comid')
    res = request.GET.get('res')
    outflow = request.GET.get('outflows')
    outflow = outflow.split(",")
    comids = comids.split(",")

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


    totalflow = []
    tsvol = []
    tselev = []
    data = {}

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

        tsnum = 0

        for r in ts:
            allcomidflows.append(float(r[1]))
            if r[0].endswith('12:00:00'):
                if tsnum == 7:
                    break
                else:
                    comidflows.append(float(r[1]))
                    tsnum = tsnum + 1

        totalflow.append(allcomidflows)
        data[comid] = comidflows

    newseries = []
    for x in data:
        newseries.append(data[x])

    total = [sum(x) for x in zip(*newseries)]
    alltotal = [sum(x) for x in zip(*totalflow)]
    data['total'] = total

    formattedtotal = ["%.2f" % elem for elem in data['total']]
    dataformatted['Entrada'] = formattedtotal

    # for x in data:
    #     formattedtotal = ["%.2f" % elem for elem in data[x]]
    #     dataformatted[x] = formattedtotal



    entries = len(ts)

    dates = []
    days = 0

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
                    tsvol.append([str(ts[x][0])[:10], volin - (float(outflow[days]) / 2.0)])
                    dates.append(str(ts[x][0])[5:-9])
                    volin = volin - (float(outflow[days]) / 2.0)
                    days = days + 1
                else:
                    tsvol.append([str(ts[x][0])[:10], volin - float(outflow[days])])
                    dates.append(str(ts[x][0])[5:-9])
                    volin = volin - (float(outflow[days]))
                    days = days + 1
                if days == 7:
                    break


    for q in tsvol:
        volval = q[1]
        volval = volval / 1000000.0
        evolval = (df.loc[df[vol] > volval, elev].iloc[0])
        tselev.append(evolval)

    dataformatted['Nivel'] = tselev
    dataformatted['Dia'] = dates

    return JsonResponse(dataformatted)