#These are python scripts that use the streamflow prediction tool api to get specific values. The reach ids for the rivers going into the
#reservoirs are hardcoded. We will need to create a python dictionary with pairs for reservoirs and their reaches.

import requests
import datetime as dt


def getforecastflows():


    #These are the comids for the rivers that go into the reservoirs. See Streamflow Prediction Tool
    comids = ['21838', '21834', '21835']
    allvalues = {}

    for x in comids:
        #the information for where to look for the comids. We may need to think of a different way to do this because not all the rivers we
        #need are in this watershed/subbasin combination.
        watershed = 'Dominican Republic'
        subbasin = 'Yaque del Sur'
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

        for e in data:
            parser = e.split('"  methodCode="1"  sourceCode="1"  qualityControlLevelCode="1" >')
            dateraw = parser[0]
            dates = dt.datetime.strptime(dateraw, "%Y-%m-%dT%H:%M:%S")
            if str(dates).endswith("00:00:00"):
                value = float(parser[1].split('<')[0])
                values.append(value)
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

    return allformvalues

def getforecastdates():
    # These are the comids for the rivers that go into the reservoirs. See Streamflow Prediction Tool
    # the information for where to look for the comids. We may need to think of a different way to do this because not all the rivers we
    # need are in this watershed/subbasin combination.
    watershed = 'Dominican Republic'
    subbasin = 'Yaque del Sur'
    comid = '21838'
    startdate = 'most_recent'


    res = requests.get('https://tethys.byu.edu/apps/streamflow-prediction-tool/api/GetWaterML/?watershed_name=' +
                       watershed + '&subbasin_name=' + subbasin + '&reach_id=' + comid + '&start_folder=' +
                       startdate + '&stat_type=mean',
                       headers={'Authorization': 'Token 72b145121add58bcc5843044d9f1006d9140b84b'})

    # The following code takes the results from the streamflow prediction tool and then sorts through it to get the dates
    content = res.content

    data = content.split('dateTimeUTC="')
    data.pop(0)

    timestep = []

    series = []
    for e in data:
        parser = e.split('"  methodCode="1"  sourceCode="1"  qualityControlLevelCode="1" >')
        dateraw = parser[0]
        dates = dt.datetime.strptime(dateraw, "%Y-%m-%dT%H:%M:%S")
        if str(dates).endswith("00:00:00"):
            timestep.append(str(dates)[5:-9])

    return timestep


