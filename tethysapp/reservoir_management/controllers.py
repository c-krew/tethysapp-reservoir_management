#This is the main python script where your html content is created. search for tethys gizmos online for more information on gizmos
#Each page has its own function and code that is run for that specific page. Each html page needs its own function

from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import MapView, Button, TextInput, DatePicker, SelectInput, DataTableView, MVDraw, MVView, MVLayer, LinePlot, TableView, TimeSeries
from datetime import datetime
from model import getforecastflows, getforecastdates


@login_required()
def home(request):
    """
    Controller for the app home page.
    """



    context = {

    }

    return render(request, 'reservoir_management/home.html', context)


@login_required()
def sabana_yegua(request):
    """
    Controller for the Add Dam page.
    """


    #TimeSeries plot. The series is hardcoded but we need to program it to look into a csv file and get the needed timeseries.
    #you would need to create a python script outside of this and then refer to it just like the getforecastflows() and getforecastdates()
    #for the table as seen below.
    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Sabana Yequa',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': [
                [datetime(2001, 4, 10), 352.87],
                [datetime(2001, 4, 11), 352.41],
                [datetime(2001, 4, 12), 351.58],
                [datetime(2001, 10, 2), 364.65],
                [datetime(2001, 10, 3), 364.61],
                [datetime(2001, 10, 5), 364.84],
                [datetime(2001, 10, 8), 364.9],
                [datetime(2001, 10, 9), 364.87],
                [datetime(2001, 10, 10), 365],
                [datetime(2001, 10, 11), 365.19],
                [datetime(2001, 10, 12), 365.44],
                [datetime(2001, 10, 15), 366.45],
                [datetime(2001, 10, 16), 366.7],
                [datetime(2001, 10, 17), 366.88],
                [datetime(2001, 10, 18), 367.02],
                [datetime(2001, 10, 19), 367.13],
                [datetime(2001, 10, 22), 367.68],
                [datetime(2001, 10, 23), 367.46],
                [datetime(2001, 10, 24), 367.51],
                [datetime(2001, 10, 25), 367.55],
                [datetime(2001, 10, 26), 367.57],
                [datetime(2001, 10, 29), 367.68],
                [datetime(2002, 1, 29), 364.81],
                [datetime(2002, 1, 31), 364.52],
                [datetime(2002, 3, 4), 358.9],
                [datetime(2002, 3, 11), 357.92],
                [datetime(2002, 3, 18), 357.54],
                [datetime(2002, 3, 22), 356.93],
                [datetime(2002, 3, 26), 356.44],
                [datetime(2002, 4, 5), 355.12],
                [datetime(2002, 6, 3), 360.88],
                [datetime(2002, 6, 4), 362.12],
                [datetime(2002, 6, 5), 363.63],
                [datetime(2002, 6, 6), 365.23],
                [datetime(2002, 6, 7), 366.65],
                [datetime(2002, 6, 10), 368.89],
                [datetime(2002, 6, 11), 369.27],
                [datetime(2002, 6, 12), 369.6],
                [datetime(2002, 6, 13), 369.8],
                [datetime(2002, 6, 14), 370.1],
                [datetime(2002, 6, 18), 370.85],
                [datetime(2002, 6, 19), 370.97],
                [datetime(2002, 6, 20), 371.09],
                [datetime(2002, 6, 21), 371.17],
                [datetime(2002, 6, 24), 371.36],
                [datetime(2002, 6, 25), 371.36],
                [datetime(2002, 6, 26), 371.38],
                [datetime(2002, 6, 27), 371.42],
                [datetime(2002, 6, 28), 371.4],
                [datetime(2002, 8, 1), 370.26],
                [datetime(2002, 8, 2), 370.21],
                [datetime(2002, 8, 5), 370.03],
                [datetime(2002, 8, 6), 369.98],
                [datetime(2002, 8, 7), 369.9],
                [datetime(2002, 8, 8), 369.8],
                [datetime(2002, 8, 9), 369.77],
                [datetime(2002, 8, 12), 369.69],
                [datetime(2002, 8, 13), 369.68],
                [datetime(2002, 8, 14), 369.7],
                [datetime(2002, 8, 15), 369.65],
                [datetime(2002, 8, 19), 369.59],
                [datetime(2002, 8, 20), 369.58],
                [datetime(2002, 8, 21), 369.54],
                [datetime(2002, 8, 22), 369.5],
                [datetime(2002, 8, 23), 369.49],
                [datetime(2002, 8, 26), 369.52],
                [datetime(2002, 8, 27), 369.54],
                [datetime(2002, 8, 28), 369.58],
                [datetime(2002, 8, 29), 369.79],
                [datetime(2002, 8, 30), 369.95],
                [datetime(2002, 10, 1), 374.09],
                [datetime(2002, 10, 2), 374.13],
                [datetime(2002, 10, 3), 374.2],
                [datetime(2002, 10, 4), 374.27],
                [datetime(2002, 10, 7), 374.46],
                [datetime(2002, 10, 8), 374.74],
                [datetime(2002, 10, 9), 374.67],
                [datetime(2002, 10, 10), 374.94],
                [datetime(2002, 10, 11), 375.17],
                [datetime(2002, 10, 14), 375.71],
                [datetime(2002, 10, 15), 375.76],
                [datetime(2002, 10, 16), 375.9],
                [datetime(2002, 10, 17), 376.02],
                [datetime(2002, 10, 21), 376.02],
                [datetime(2002, 10, 22), 376.34],
                [datetime(2002, 10, 23), 376.42],
                [datetime(2002, 10, 24), 376.45],
                [datetime(2002, 10, 25), 376.5],
                [datetime(2002, 10, 28), 376.58],
                [datetime(2002, 10, 29), 376.58],
                [datetime(2002, 10, 30), 376.59],
                [datetime(2002, 10, 31), 376.61],
                [datetime(2003, 1, 2), 371.76],
                [datetime(2003, 1, 3), 371.63],
                [datetime(2003, 1, 7), 371.22],
                [datetime(2003, 1, 8), 371.11],
                [datetime(2003, 1, 9), 370.98],
                [datetime(2003, 1, 10), 370.85],
                [datetime(2003, 1, 13), 370.46],
                [datetime(2003, 1, 14), 370.32],
                [datetime(2003, 1, 15), 370.17],
                [datetime(2003, 1, 16), 370.02],
                [datetime(2003, 1, 17), 369.26],
                [datetime(2003, 1, 20), 369.5],
                [datetime(2003, 1, 22), 369.27],
                [datetime(2003, 1, 23), 369.12],
                [datetime(2003, 1, 24), 368.97],
                [datetime(2003, 1, 27), 368.45],
                [datetime(2003, 1, 28), 368.3],
                [datetime(2003, 1, 29), 368.13],
                [datetime(2003, 1, 30), 367.97],
                [datetime(2003, 1, 31), 367.85],
                [datetime(2003, 3, 4), 354.05],
                [datetime(2003, 3, 7), 363.48],
                [datetime(2003, 3, 10), 362.94],
                [datetime(2003, 3, 11), 362.76],
                [datetime(2003, 3, 12), 362.57],
                [datetime(2003, 3, 13), 362.38],
                [datetime(2003, 3, 14), 362.16],
                [datetime(2003, 3, 18), 361.38],
                [datetime(2003, 3, 19), 361.16],
                [datetime(2003, 3, 20), 360.97],
                [datetime(2003, 3, 21), 360.78],
                [datetime(2003, 3, 25), 359.88],
                [datetime(2003, 3, 26), 359.63],
                [datetime(2003, 3, 27), 359.4],
                [datetime(2003, 3, 28), 359.23],
                [datetime(2003, 3, 31), 358.72],
                [datetime(2003, 4, 1), 358.47],
                [datetime(2003, 4, 3), 358.24],
                [datetime(2003, 4, 4), 358.29],
                [datetime(2003, 4, 7), 358.49],
                [datetime(2003, 4, 9), 358.72],
                [datetime(2003, 4, 10), 358.77],
                [datetime(2003, 4, 11), 358.79],
                [datetime(2003, 4, 14), 358.92],
                [datetime(2003, 4, 15), 359.14],
                [datetime(2003, 4, 16), 359.42],
                [datetime(2003, 4, 17), 359.65],
                [datetime(2003, 4, 21), 359.98],
                [datetime(2003, 4, 22), 360.15],
                [datetime(2003, 4, 23), 360.58],
                [datetime(2003, 4, 24), 360.85],
                [datetime(2003, 4, 25), 361.05],
                [datetime(2003, 4, 28), 361.25],
                [datetime(2003, 4, 29), 361.57],
                [datetime(2003, 6, 2), 367.47],
                [datetime(2003, 6, 3), 367.44],
                [datetime(2003, 6, 4), 367.43],
                [datetime(2003, 6, 5), 367.45],
                [datetime(2003, 6, 6), 367.45],
                [datetime(2003, 6, 9), 367.52],
                [datetime(2003, 6, 10), 367.67],
                [datetime(2003, 6, 11), 367.82],
                [datetime(2003, 6, 12), 367.94],
                [datetime(2003, 6, 13), 368.16],
                [datetime(2003, 6, 16), 369.17],
                [datetime(2003, 6, 17), 369.43],
                [datetime(2003, 6, 18), 369.63],
                [datetime(2003, 6, 20), 370.4],
                [datetime(2003, 6, 23), 371.22],
                [datetime(2003, 6, 24), 371.33],
                [datetime(2003, 6, 25), 371.41],
                [datetime(2003, 6, 26), 371.75],
                [datetime(2003, 6, 27), 371.49],
                [datetime(2003, 6, 30), 371.53],
                [datetime(2003, 8, 1), 369.66],
                [datetime(2003, 8, 4), 369.48],
                [datetime(2003, 8, 5), 369.41],
                [datetime(2003, 8, 6), 369.36],
                [datetime(2003, 8, 7), 369.25],
                [datetime(2003, 8, 8), 369.15],
                [datetime(2003, 8, 11), 368.96],
                [datetime(2003, 8, 12), 368.86],
                [datetime(2003, 8, 13), 368.77],
                [datetime(2003, 8, 14), 368.71],
                [datetime(2003, 8, 15), 368.59],
                [datetime(2003, 8, 21), 391.64],
                [datetime(2003, 8, 25), 368.53],
                [datetime(2003, 8, 28), 369.17],
                [datetime(2003, 8, 29), 369.28],
                [datetime(2003, 10, 1), 376.06],
                [datetime(2003, 10, 2), 376.16],
                [datetime(2003, 10, 3), 376.27],
                [datetime(2003, 10, 6), 376.73],
                [datetime(2003, 10, 7), 376.86],
                [datetime(2003, 10, 8), 377.04],
                [datetime(2003, 10, 9), 377.88],
                [datetime(2003, 10, 10), 378.35],
                [datetime(2003, 10, 13), 379.32],
                [datetime(2003, 10, 20), 381.88],
                [datetime(2003, 10, 21), 382.22],
                [datetime(2003, 10, 22), 382.55],
                [datetime(2003, 10, 23), 383.08],
                [datetime(2003, 10, 24), 383.47],
                [datetime(2003, 10, 27), 385.3],
                [datetime(2003, 10, 28), 385.54],
                [datetime(2003, 10, 29), 386.39],
                [datetime(2003, 10, 30), 386.92],
                [datetime(2003, 10, 31), 387.39],
                [datetime(2004, 1, 2), 393.68],
                [datetime(2004, 1, 4), 385.2],
                [datetime(2004, 1, 6), 393.6],
                [datetime(2004, 1, 7), 393.59],
                [datetime(2004, 1, 8), 393.63],
                [datetime(2004, 1, 9), 393.64],
                [datetime(2004, 1, 12), 393.61],
                [datetime(2004, 1, 13), 393.6],
                [datetime(2004, 1, 14), 393.6],
                [datetime(2004, 1, 15), 393.59],
                [datetime(2004, 1, 16), 393.56],
                [datetime(2004, 1, 19), 393.47],
                [datetime(2004, 1, 20), 393.45],
                [datetime(2004, 1, 22), 393.38],
                [datetime(2004, 1, 23), 393.36],
                [datetime(2004, 1, 27), 392.25],
                [datetime(2004, 1, 28), 393.21],
                [datetime(2004, 1, 29), 393.18],
                [datetime(2004, 1, 30), 393.14],
                [datetime(2004, 3, 1), 391.09],
                [datetime(2004, 3, 2), 391],
                [datetime(2004, 3, 3), 390.96],
                [datetime(2004, 3, 4), 390.87],
                [datetime(2004, 3, 5), 390.81],
                [datetime(2004, 3, 7), 380.35],
                [datetime(2004, 3, 8), 390.63],
                [datetime(2004, 3, 9), 390.51],
                [datetime(2004, 3, 10), 390.41],
                [datetime(2004, 3, 14), 379.42],
                [datetime(2004, 3, 15), 389.89],
                [datetime(2004, 3, 16), 389.82],
                [datetime(2004, 3, 17), 389.73],
                [datetime(2004, 3, 18), 389.66],
                [datetime(2004, 3, 19), 389.51],
                [datetime(2004, 3, 22), 389.19],
                [datetime(2004, 3, 23), 389.09],
                [datetime(2004, 3, 24), 388.99],
                [datetime(2004, 3, 25), 388.93],
                [datetime(2004, 3, 26), 388.83],
                [datetime(2004, 3, 29), 388.52],
                [datetime(2004, 3, 30), 388.46],
                [datetime(2004, 3, 31), 388.41],
                [datetime(2004, 4, 1), 388.33],
                [datetime(2004, 4, 2), 388.24],
                [datetime(2004, 4, 5), 388.01],
                [datetime(2004, 4, 6), 387.92],
                [datetime(2004, 4, 7), 387.84],
                [datetime(2004, 4, 13), 387.49],
                [datetime(2004, 4, 14), 387.3],
                [datetime(2004, 4, 15), 387.23],
                [datetime(2004, 4, 16), 387.16],
                [datetime(2004, 4, 19), 386.91],
                [datetime(2004, 4, 20), 386.84],
                [datetime(2004, 4, 21), 386.76],
                [datetime(2004, 4, 22), 386.71],
                [datetime(2004, 4, 23), 386.63],
                [datetime(2004, 4, 26), 386.43],
                [datetime(2004, 4, 28), 386.27],
                [datetime(2004, 4, 29), 386.22],
                [datetime(2004, 5, 20), 385.98],
                [datetime(2004, 5, 21), 385.99],
                [datetime(2004, 5, 24), 386.71],
                [datetime(2004, 5, 25), 390.03],
                [datetime(2004, 5, 26), 390.61],
                [datetime(2004, 5, 27), 391.14],
                [datetime(2004, 5, 28), 391.61],
                [datetime(2004, 5, 31), 392.4],
                [datetime(2004, 6, 1), 392.52],
                [datetime(2004, 6, 2), 392.63],
                [datetime(2004, 6, 3), 392.69],
                [datetime(2004, 6, 4), 392.74],
                [datetime(2004, 6, 7), 392.9],
                [datetime(2004, 6, 8), 392.92],
                [datetime(2004, 6, 9), 392.99],
                [datetime(2004, 6, 11), 393.17],
                [datetime(2004, 6, 14), 393.35],
                [datetime(2004, 6, 15), 393.41],
                [datetime(2004, 6, 16), 393.46],
                [datetime(2004, 6, 22), 393.57],
                [datetime(2004, 6, 23), 393.54],
                [datetime(2004, 8, 2), 387.13],
                [datetime(2004, 8, 3), 386.72],
                [datetime(2004, 8, 4), 386.46],
                [datetime(2004, 8, 5), 386.24],
                [datetime(2004, 8, 9), 385.93],
                [datetime(2004, 8, 10), 385.87],
                [datetime(2004, 8, 11), 385.84],
                [datetime(2004, 8, 12), 385.75],
                [datetime(2004, 8, 13), 385.7],
                [datetime(2004, 8, 17), 385.45],
                [datetime(2004, 8, 18), 385.4],
                [datetime(2004, 8, 19), 385.31],
                [datetime(2004, 8, 20), 385.27],
                [datetime(2004, 8, 23), 380.32],
                [datetime(2004, 8, 24), 385.37],
                [datetime(2004, 8, 25), 385.35],
                [datetime(2004, 8, 26), 385.31],
                [datetime(2004, 8, 27), 385.25],
                [datetime(2004, 8, 30), 385.16],
                [datetime(2004, 8, 31), 385.16],
                [datetime(2004, 10, 1), 388.98],
                [datetime(2004, 10, 4), 388.75],
                [datetime(2004, 10, 5), 388.64],
                [datetime(2004, 10, 6), 388.51],
                [datetime(2004, 10, 7), 388.44],
                [datetime(2004, 10, 8), 388.33],
                [datetime(2004, 10, 11), 388.05],
                [datetime(2004, 10, 12), 387.96],
                [datetime(2004, 10, 13), 387.9],
                [datetime(2004, 10, 14), 388.07],
                [datetime(2004, 10, 15), 388.7],
                [datetime(2004, 10, 18), 388.4],
                [datetime(2004, 10, 19), 328.41],
                [datetime(2004, 10, 20), 388.42],
                [datetime(2004, 10, 21), 388.41],
                [datetime(2004, 10, 22), 388.45],
                [datetime(2004, 10, 25), 388.58],
                [datetime(2004, 10, 26), 388.56],
                [datetime(2004, 10, 27), 388.34],
                [datetime(2004, 10, 28), 388.51],
                [datetime(2004, 10, 29), 388.47],
                [datetime(2005, 1, 4), 385.2],
                [datetime(2005, 1, 5), 385.18],
                [datetime(2005, 1, 6), 385.16],
                [datetime(2005, 1, 7), 384.91],
                [datetime(2005, 1, 8), 385.11],
                [datetime(2005, 1, 11), 384.91],
                [datetime(2005, 1, 12), 384.94],
                [datetime(2005, 1, 13), 384.92],
                [datetime(2005, 1, 14), 384.89],
                [datetime(2005, 1, 17), 385.02],
                [datetime(2005, 1, 19), 384.95],
                [datetime(2005, 1, 20), 384.12],
                [datetime(2005, 1, 25), 384.71],
                [datetime(2005, 1, 27), 384.61],
                [datetime(2005, 1, 28), 384.52],
                [datetime(2005, 3, 1), 380.98],
                [datetime(2005, 3, 2), 380.86],
                [datetime(2005, 3, 3), 380.75],
                [datetime(2005, 3, 4), 380.62],
                [datetime(2005, 3, 7), 380.35],
                [datetime(2005, 3, 8), 380.25],
                [datetime(2005, 3, 9), 380.13],
                [datetime(2005, 3, 10), 379.9],
                [datetime(2005, 3, 11), 379.86],
                [datetime(2005, 3, 14), 379.42],
                [datetime(2005, 3, 15), 379.28],
                [datetime(2005, 3, 16), 379.13],
                [datetime(2005, 3, 17), 378.98],
                [datetime(2005, 3, 19), 374.86],
                [datetime(2005, 3, 21), 378.63],
                [datetime(2005, 3, 22), 378.16],
                [datetime(2005, 3, 23), 377.98],
                [datetime(2005, 3, 28), 377.24],
                [datetime(2005, 3, 29), 377.11],
                [datetime(2005, 3, 30), 376.98],
                [datetime(2005, 3, 31), 376.85],
                [datetime(2005, 4, 1), 376.71],
                [datetime(2005, 4, 4), 376.3],
                [datetime(2005, 4, 5), 376.26],
                [datetime(2005, 4, 6), 376.2],
                [datetime(2005, 4, 7), 376.15],
                [datetime(2005, 4, 8), 376.08],
                [datetime(2005, 4, 11), 375.71],
                [datetime(2005, 4, 12), 375.54],
                [datetime(2005, 4, 13), 375.49],
                [datetime(2005, 4, 14), 375.45],
                [datetime(2005, 4, 15), 375.37],
                [datetime(2005, 4, 18), 374.99],
                [datetime(2005, 4, 19), 374.86],
                [datetime(2005, 4, 20), 374.82],
                [datetime(2005, 4, 21), 374.83],
                [datetime(2005, 4, 22), 374.12],
                [datetime(2005, 4, 25), 375.15],
                [datetime(2005, 4, 26), 375.09],
                [datetime(2005, 4, 27), 375.01],
                [datetime(2005, 4, 28), 374.89],
                [datetime(2005, 4, 29), 374.9],
                [datetime(2005, 6, 1), 379.42],
                [datetime(2005, 6, 2), 379.5],
                [datetime(2005, 6, 3), 379.62],
                [datetime(2005, 6, 6), 380.42],
                [datetime(2005, 6, 7), 380.44],
                [datetime(2005, 6, 8), 380.54],
                [datetime(2005, 6, 9), 380.63],
                [datetime(2005, 6, 10), 380.76],
                [datetime(2005, 6, 13), 382.11],
                [datetime(2005, 6, 14), 382.32],
                [datetime(2005, 6, 15), 382.85],
                [datetime(2005, 6, 16), 383.27],
                [datetime(2005, 6, 17), 383.59],
                [datetime(2005, 6, 20), 384.41],
                [datetime(2005, 6, 21), 384.56],
                [datetime(2005, 6, 22), 384.66],
                [datetime(2005, 6, 23), 384.75],
                [datetime(2005, 6, 24), 384.87],
                [datetime(2005, 6, 27), 385.29],
                [datetime(2005, 6, 28), 385.42],
                [datetime(2005, 6, 29), 385.5],
                [datetime(2005, 6, 30), 385.58],
                [datetime(2006, 6, 22), 371.71],
                [datetime(2006, 6, 23), 391.73],
            ]
        }]
    )

    #this refers to python code in model.py. It uses the stremaflow prediction tool api to get this information.
    inflows = getforecastflows()
    forecastdates = getforecastdates()


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastdates[0], forecastdates[1], forecastdates[2], forecastdates[3], forecastdates[4], forecastdates[5], forecastdates[6]),
                           rows=[('Caudal de Entrada',inflows[0], inflows[1], inflows[2],inflows[3],inflows[4],inflows[5],inflows[6]),
                                 ('Caudal de Salida','10', '10', '13','12','12.4','11','13'),
                                 ('Niveles','368', '370', '369', '374','373','371','372')],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)


    context = {
        'timeseries_plot': timeseries_plot,
        'table_view': table_view,
 #       'historic_plot': historic_plot,
    }

    return render(request, 'reservoir_management/sabana_yegua.html', context)

@login_required()
def reportar(request):
    """
    Controller for the app home page.
    """

    #these are the different inputs on the reportar page of the app
    dam_input = SelectInput(display_text='Seleccionar una presa',
                               name='dam',
                               multiple=False,
                               original=True,
                               options=[('Sabana Yegua', 'Sabana Yegua'), ('Sabaneta', 'Sabaneta'), ('Hatillo', 'Hatillo')],
                               initial=[''])

    level_input = TextInput(display_text='Nivel de Agua',
                           name='levelinput',
                           placeholder='i.e. 375',
                           )

    time_input = TextInput(display_text='Tiempo en lo que fue medido',
                           name='timeinput',
                           placeholder='i.e. 14:12',
                           )


    context = {
        'dam_input': dam_input,
        'level_input':level_input,
        'time_input': time_input,
    }

    return render(request, 'reservoir_management/reportar.html', context)

@login_required()
def hatillo(request):
    """
    Controller for the Add Dam page.
    """


    #TimeSeries plot. The series is hardcoded but we need to program it to look into a csv file and get the needed timeseries.
    #you would need to create a python script outside of this and then refer to it just like the getforecastflows() and getforecastdates()
    #for the table as seen below.
    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Hatillo',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': [
                [datetime(2001, 4, 10), 352.87],
                [datetime(2001, 4, 11), 352.41],
                [datetime(2001, 4, 12), 351.58],
                [datetime(2001, 10, 2), 364.65],
                [datetime(2001, 10, 3), 364.61],
                [datetime(2001, 10, 5), 364.84],
                [datetime(2001, 10, 8), 364.9],
                [datetime(2001, 10, 9), 364.87],
                [datetime(2001, 10, 10), 365],
                [datetime(2001, 10, 11), 365.19],
                [datetime(2001, 10, 12), 365.44],
                [datetime(2001, 10, 15), 366.45],
                [datetime(2001, 10, 16), 366.7],
                [datetime(2001, 10, 17), 366.88],
                [datetime(2001, 10, 18), 367.02],
                [datetime(2001, 10, 19), 367.13],
                [datetime(2001, 10, 22), 367.68],
                [datetime(2001, 10, 23), 367.46],
                [datetime(2001, 10, 24), 367.51],
                [datetime(2001, 10, 25), 367.55],
                [datetime(2001, 10, 26), 367.57],
                [datetime(2001, 10, 29), 367.68],
                [datetime(2002, 1, 29), 364.81],
                [datetime(2002, 1, 31), 364.52],
                [datetime(2002, 3, 4), 358.9],
                [datetime(2002, 3, 11), 357.92],
                [datetime(2002, 3, 18), 357.54],
                [datetime(2002, 3, 22), 356.93],
                [datetime(2002, 3, 26), 356.44],
                [datetime(2002, 4, 5), 355.12],
                [datetime(2002, 6, 3), 360.88],
                [datetime(2002, 6, 4), 362.12],
                [datetime(2002, 6, 5), 363.63],
                [datetime(2002, 6, 6), 365.23],
                [datetime(2002, 6, 7), 366.65],
                [datetime(2002, 6, 10), 368.89],
                [datetime(2002, 6, 11), 369.27],
                [datetime(2002, 6, 12), 369.6],
                [datetime(2002, 6, 13), 369.8],
                [datetime(2002, 6, 14), 370.1],
                [datetime(2002, 6, 18), 370.85],
                [datetime(2002, 6, 19), 370.97],
                [datetime(2002, 6, 20), 371.09],
                [datetime(2002, 6, 21), 371.17],
                [datetime(2002, 6, 24), 371.36],
                [datetime(2002, 6, 25), 371.36],
                [datetime(2002, 6, 26), 371.38],
                [datetime(2002, 6, 27), 371.42],
                [datetime(2002, 6, 28), 371.4],
                [datetime(2002, 8, 1), 370.26],
                [datetime(2002, 8, 2), 370.21],
                [datetime(2002, 8, 5), 370.03],
                [datetime(2002, 8, 6), 369.98],
                [datetime(2002, 8, 7), 369.9],
                [datetime(2002, 8, 8), 369.8],
                [datetime(2002, 8, 9), 369.77],
                [datetime(2002, 8, 12), 369.69],
                [datetime(2002, 8, 13), 369.68],
                [datetime(2002, 8, 14), 369.7],
                [datetime(2002, 8, 15), 369.65],
                [datetime(2002, 8, 19), 369.59],
                [datetime(2002, 8, 20), 369.58],
                [datetime(2002, 8, 21), 369.54],
                [datetime(2002, 8, 22), 369.5],
                [datetime(2002, 8, 23), 369.49],
                [datetime(2002, 8, 26), 369.52],
                [datetime(2002, 8, 27), 369.54],
                [datetime(2002, 8, 28), 369.58],
                [datetime(2002, 8, 29), 369.79],
                [datetime(2002, 8, 30), 369.95],
                [datetime(2002, 10, 1), 374.09],
                [datetime(2002, 10, 2), 374.13],
                [datetime(2002, 10, 3), 374.2],
                [datetime(2002, 10, 4), 374.27],
                [datetime(2002, 10, 7), 374.46],
                [datetime(2002, 10, 8), 374.74],
                [datetime(2002, 10, 9), 374.67],
                [datetime(2002, 10, 10), 374.94],
                [datetime(2002, 10, 11), 375.17],
                [datetime(2002, 10, 14), 375.71],
                [datetime(2002, 10, 15), 375.76],
                [datetime(2002, 10, 16), 375.9],
                [datetime(2002, 10, 17), 376.02],
                [datetime(2002, 10, 21), 376.02],
                [datetime(2002, 10, 22), 376.34],
                [datetime(2002, 10, 23), 376.42],
                [datetime(2002, 10, 24), 376.45],
                [datetime(2002, 10, 25), 376.5],
                [datetime(2002, 10, 28), 376.58],
                [datetime(2002, 10, 29), 376.58],
                [datetime(2002, 10, 30), 376.59],
                [datetime(2002, 10, 31), 376.61],
                [datetime(2003, 1, 2), 371.76],
                [datetime(2003, 1, 3), 371.63],
                [datetime(2003, 1, 7), 371.22],
                [datetime(2003, 1, 8), 371.11],
                [datetime(2003, 1, 9), 370.98],
                [datetime(2003, 1, 10), 370.85],
                [datetime(2003, 1, 13), 370.46],
                [datetime(2003, 1, 14), 370.32],
                [datetime(2003, 1, 15), 370.17],
                [datetime(2003, 1, 16), 370.02],
                [datetime(2003, 1, 17), 369.26],
                [datetime(2003, 1, 20), 369.5],
                [datetime(2003, 1, 22), 369.27],
                [datetime(2003, 1, 23), 369.12],
                [datetime(2003, 1, 24), 368.97],
                [datetime(2003, 1, 27), 368.45],
                [datetime(2003, 1, 28), 368.3],
                [datetime(2003, 1, 29), 368.13],
                [datetime(2003, 1, 30), 367.97],
                [datetime(2003, 1, 31), 367.85],
                [datetime(2003, 3, 4), 354.05],
                [datetime(2003, 3, 7), 363.48],
                [datetime(2003, 3, 10), 362.94],
                [datetime(2003, 3, 11), 362.76],
                [datetime(2003, 3, 12), 362.57],
                [datetime(2003, 3, 13), 362.38],
                [datetime(2003, 3, 14), 362.16],
                [datetime(2003, 3, 18), 361.38],
                [datetime(2003, 3, 19), 361.16],
                [datetime(2003, 3, 20), 360.97],
                [datetime(2003, 3, 21), 360.78],
                [datetime(2003, 3, 25), 359.88],
                [datetime(2003, 3, 26), 359.63],
                [datetime(2003, 3, 27), 359.4],
                [datetime(2003, 3, 28), 359.23],
                [datetime(2003, 3, 31), 358.72],
                [datetime(2003, 4, 1), 358.47],
                [datetime(2003, 4, 3), 358.24],
                [datetime(2003, 4, 4), 358.29],
                [datetime(2003, 4, 7), 358.49],
                [datetime(2003, 4, 9), 358.72],
                [datetime(2003, 4, 10), 358.77],
                [datetime(2003, 4, 11), 358.79],
                [datetime(2003, 4, 14), 358.92],
                [datetime(2003, 4, 15), 359.14],
                [datetime(2003, 4, 16), 359.42],
                [datetime(2003, 4, 17), 359.65],
                [datetime(2003, 4, 21), 359.98],
                [datetime(2003, 4, 22), 360.15],
                [datetime(2003, 4, 23), 360.58],
                [datetime(2003, 4, 24), 360.85],
                [datetime(2003, 4, 25), 361.05],
                [datetime(2003, 4, 28), 361.25],
                [datetime(2003, 4, 29), 361.57],
                [datetime(2003, 6, 2), 367.47],
                [datetime(2003, 6, 3), 367.44],
                [datetime(2003, 6, 4), 367.43],
                [datetime(2003, 6, 5), 367.45],
                [datetime(2003, 6, 6), 367.45],
                [datetime(2003, 6, 9), 367.52],
                [datetime(2003, 6, 10), 367.67],
                [datetime(2003, 6, 11), 367.82],
                [datetime(2003, 6, 12), 367.94],
                [datetime(2003, 6, 13), 368.16],
                [datetime(2003, 6, 16), 369.17],
                [datetime(2003, 6, 17), 369.43],
                [datetime(2003, 6, 18), 369.63],
                [datetime(2003, 6, 20), 370.4],
                [datetime(2003, 6, 23), 371.22],
                [datetime(2003, 6, 24), 371.33],
                [datetime(2003, 6, 25), 371.41],
                [datetime(2003, 6, 26), 371.75],
                [datetime(2003, 6, 27), 371.49],
                [datetime(2003, 6, 30), 371.53],
                [datetime(2003, 8, 1), 369.66],
                [datetime(2003, 8, 4), 369.48],
                [datetime(2003, 8, 5), 369.41],
                [datetime(2003, 8, 6), 369.36],
                [datetime(2003, 8, 7), 369.25],
                [datetime(2003, 8, 8), 369.15],
                [datetime(2003, 8, 11), 368.96],
                [datetime(2003, 8, 12), 368.86],
                [datetime(2003, 8, 13), 368.77],
                [datetime(2003, 8, 14), 368.71],
                [datetime(2003, 8, 15), 368.59],
                [datetime(2003, 8, 21), 391.64],
                [datetime(2003, 8, 25), 368.53],
                [datetime(2003, 8, 28), 369.17],
                [datetime(2003, 8, 29), 369.28],
                [datetime(2003, 10, 1), 376.06],
                [datetime(2003, 10, 2), 376.16],
                [datetime(2003, 10, 3), 376.27],
                [datetime(2003, 10, 6), 376.73],
                [datetime(2003, 10, 7), 376.86],
                [datetime(2003, 10, 8), 377.04],
                [datetime(2003, 10, 9), 377.88],
                [datetime(2003, 10, 10), 378.35],
                [datetime(2003, 10, 13), 379.32],
                [datetime(2003, 10, 20), 381.88],
                [datetime(2003, 10, 21), 382.22],
                [datetime(2003, 10, 22), 382.55],
                [datetime(2003, 10, 23), 383.08],
                [datetime(2003, 10, 24), 383.47],
                [datetime(2003, 10, 27), 385.3],
                [datetime(2003, 10, 28), 385.54],
                [datetime(2003, 10, 29), 386.39],
                [datetime(2003, 10, 30), 386.92],
                [datetime(2003, 10, 31), 387.39],
                [datetime(2004, 1, 2), 393.68],
                [datetime(2004, 1, 4), 385.2],
                [datetime(2004, 1, 6), 393.6],
                [datetime(2004, 1, 7), 393.59],
                [datetime(2004, 1, 8), 393.63],
                [datetime(2004, 1, 9), 393.64],
                [datetime(2004, 1, 12), 393.61],
                [datetime(2004, 1, 13), 393.6],
                [datetime(2004, 1, 14), 393.6],
                [datetime(2004, 1, 15), 393.59],
                [datetime(2004, 1, 16), 393.56],
                [datetime(2004, 1, 19), 393.47],
                [datetime(2004, 1, 20), 393.45],
                [datetime(2004, 1, 22), 393.38],
                [datetime(2004, 1, 23), 393.36],
                [datetime(2004, 1, 27), 392.25],
                [datetime(2004, 1, 28), 393.21],
                [datetime(2004, 1, 29), 393.18],
                [datetime(2004, 1, 30), 393.14],
                [datetime(2004, 3, 1), 391.09],
                [datetime(2004, 3, 2), 391],
                [datetime(2004, 3, 3), 390.96],
                [datetime(2004, 3, 4), 390.87],
                [datetime(2004, 3, 5), 390.81],
                [datetime(2004, 3, 7), 380.35],
                [datetime(2004, 3, 8), 390.63],
                [datetime(2004, 3, 9), 390.51],
                [datetime(2004, 3, 10), 390.41],
                [datetime(2004, 3, 14), 379.42],
                [datetime(2004, 3, 15), 389.89],
                [datetime(2004, 3, 16), 389.82],
                [datetime(2004, 3, 17), 389.73],
                [datetime(2004, 3, 18), 389.66],
                [datetime(2004, 3, 19), 389.51],
                [datetime(2004, 3, 22), 389.19],
                [datetime(2004, 3, 23), 389.09],
                [datetime(2004, 3, 24), 388.99],
                [datetime(2004, 3, 25), 388.93],
                [datetime(2004, 3, 26), 388.83],
                [datetime(2004, 3, 29), 388.52],
                [datetime(2004, 3, 30), 388.46],
                [datetime(2004, 3, 31), 388.41],
                [datetime(2004, 4, 1), 388.33],
                [datetime(2004, 4, 2), 388.24],
                [datetime(2004, 4, 5), 388.01],
                [datetime(2004, 4, 6), 387.92],
                [datetime(2004, 4, 7), 387.84],
                [datetime(2004, 4, 13), 387.49],
                [datetime(2004, 4, 14), 387.3],
                [datetime(2004, 4, 15), 387.23],
                [datetime(2004, 4, 16), 387.16],
                [datetime(2004, 4, 19), 386.91],
                [datetime(2004, 4, 20), 386.84],
                [datetime(2004, 4, 21), 386.76],
                [datetime(2004, 4, 22), 386.71],
                [datetime(2004, 4, 23), 386.63],
                [datetime(2004, 4, 26), 386.43],
                [datetime(2004, 4, 28), 386.27],
                [datetime(2004, 4, 29), 386.22],
                [datetime(2004, 5, 20), 385.98],
                [datetime(2004, 5, 21), 385.99],
                [datetime(2004, 5, 24), 386.71],
                [datetime(2004, 5, 25), 390.03],
                [datetime(2004, 5, 26), 390.61],
                [datetime(2004, 5, 27), 391.14],
                [datetime(2004, 5, 28), 391.61],
                [datetime(2004, 5, 31), 392.4],
                [datetime(2004, 6, 1), 392.52],
                [datetime(2004, 6, 2), 392.63],
                [datetime(2004, 6, 3), 392.69],
                [datetime(2004, 6, 4), 392.74],
                [datetime(2004, 6, 7), 392.9],
                [datetime(2004, 6, 8), 392.92],
                [datetime(2004, 6, 9), 392.99],
                [datetime(2004, 6, 11), 393.17],
                [datetime(2004, 6, 14), 393.35],
                [datetime(2004, 6, 15), 393.41],
                [datetime(2004, 6, 16), 393.46],
                [datetime(2004, 6, 22), 393.57],
                [datetime(2004, 6, 23), 393.54],
                [datetime(2004, 8, 2), 387.13],
                [datetime(2004, 8, 3), 386.72],
                [datetime(2004, 8, 4), 386.46],
                [datetime(2004, 8, 5), 386.24],
                [datetime(2004, 8, 9), 385.93],
                [datetime(2004, 8, 10), 385.87],
                [datetime(2004, 8, 11), 385.84],
                [datetime(2004, 8, 12), 385.75],
                [datetime(2004, 8, 13), 385.7],
                [datetime(2004, 8, 17), 385.45],
                [datetime(2004, 8, 18), 385.4],
                [datetime(2004, 8, 19), 385.31],
                [datetime(2004, 8, 20), 385.27],
                [datetime(2004, 8, 23), 380.32],
                [datetime(2004, 8, 24), 385.37],
                [datetime(2004, 8, 25), 385.35],
                [datetime(2004, 8, 26), 385.31],
                [datetime(2004, 8, 27), 385.25],
                [datetime(2004, 8, 30), 385.16],
                [datetime(2004, 8, 31), 385.16],
                [datetime(2004, 10, 1), 388.98],
                [datetime(2004, 10, 4), 388.75],
                [datetime(2004, 10, 5), 388.64],
                [datetime(2004, 10, 6), 388.51],
                [datetime(2004, 10, 7), 388.44],
                [datetime(2004, 10, 8), 388.33],
                [datetime(2004, 10, 11), 388.05],
                [datetime(2004, 10, 12), 387.96],
                [datetime(2004, 10, 13), 387.9],
                [datetime(2004, 10, 14), 388.07],
                [datetime(2004, 10, 15), 388.7],
                [datetime(2004, 10, 18), 388.4],
                [datetime(2004, 10, 19), 328.41],
                [datetime(2004, 10, 20), 388.42],
                [datetime(2004, 10, 21), 388.41],
                [datetime(2004, 10, 22), 388.45],
                [datetime(2004, 10, 25), 388.58],
                [datetime(2004, 10, 26), 388.56],
                [datetime(2004, 10, 27), 388.34],
                [datetime(2004, 10, 28), 388.51],
                [datetime(2004, 10, 29), 388.47],
                [datetime(2005, 1, 4), 385.2],
                [datetime(2005, 1, 5), 385.18],
                [datetime(2005, 1, 6), 385.16],
                [datetime(2005, 1, 7), 384.91],
                [datetime(2005, 1, 8), 385.11],
                [datetime(2005, 1, 11), 384.91],
                [datetime(2005, 1, 12), 384.94],
                [datetime(2005, 1, 13), 384.92],
                [datetime(2005, 1, 14), 384.89],
                [datetime(2005, 1, 17), 385.02],
                [datetime(2005, 1, 19), 384.95],
                [datetime(2005, 1, 20), 384.12],
                [datetime(2005, 1, 25), 384.71],
                [datetime(2005, 1, 27), 384.61],
                [datetime(2005, 1, 28), 384.52],
                [datetime(2005, 3, 1), 380.98],
                [datetime(2005, 3, 2), 380.86],
                [datetime(2005, 3, 3), 380.75],
                [datetime(2005, 3, 4), 380.62],
                [datetime(2005, 3, 7), 380.35],
                [datetime(2005, 3, 8), 380.25],
                [datetime(2005, 3, 9), 380.13],
                [datetime(2005, 3, 10), 379.9],
                [datetime(2005, 3, 11), 379.86],
                [datetime(2005, 3, 14), 379.42],
                [datetime(2005, 3, 15), 379.28],
                [datetime(2005, 3, 16), 379.13],
                [datetime(2005, 3, 17), 378.98],
                [datetime(2005, 3, 19), 374.86],
                [datetime(2005, 3, 21), 378.63],
                [datetime(2005, 3, 22), 378.16],
                [datetime(2005, 3, 23), 377.98],
                [datetime(2005, 3, 28), 377.24],
                [datetime(2005, 3, 29), 377.11],
                [datetime(2005, 3, 30), 376.98],
                [datetime(2005, 3, 31), 376.85],
                [datetime(2005, 4, 1), 376.71],
                [datetime(2005, 4, 4), 376.3],
                [datetime(2005, 4, 5), 376.26],
                [datetime(2005, 4, 6), 376.2],
                [datetime(2005, 4, 7), 376.15],
                [datetime(2005, 4, 8), 376.08],
                [datetime(2005, 4, 11), 375.71],
                [datetime(2005, 4, 12), 375.54],
                [datetime(2005, 4, 13), 375.49],
                [datetime(2005, 4, 14), 375.45],
                [datetime(2005, 4, 15), 375.37],
                [datetime(2005, 4, 18), 374.99],
                [datetime(2005, 4, 19), 374.86],
                [datetime(2005, 4, 20), 374.82],
                [datetime(2005, 4, 21), 374.83],
                [datetime(2005, 4, 22), 374.12],
                [datetime(2005, 4, 25), 375.15],
                [datetime(2005, 4, 26), 375.09],
                [datetime(2005, 4, 27), 375.01],
                [datetime(2005, 4, 28), 374.89],
                [datetime(2005, 4, 29), 374.9],
                [datetime(2005, 6, 1), 379.42],
                [datetime(2005, 6, 2), 379.5],
                [datetime(2005, 6, 3), 379.62],
                [datetime(2005, 6, 6), 380.42],
                [datetime(2005, 6, 7), 380.44],
                [datetime(2005, 6, 8), 380.54],
                [datetime(2005, 6, 9), 380.63],
                [datetime(2005, 6, 10), 380.76],
                [datetime(2005, 6, 13), 382.11],
                [datetime(2005, 6, 14), 382.32],
                [datetime(2005, 6, 15), 382.85],
                [datetime(2005, 6, 16), 383.27],
                [datetime(2005, 6, 17), 383.59],
                [datetime(2005, 6, 20), 384.41],
                [datetime(2005, 6, 21), 384.56],
                [datetime(2005, 6, 22), 384.66],
                [datetime(2005, 6, 23), 384.75],
                [datetime(2005, 6, 24), 384.87],
                [datetime(2005, 6, 27), 385.29],
                [datetime(2005, 6, 28), 385.42],
                [datetime(2005, 6, 29), 385.5],
                [datetime(2005, 6, 30), 385.58],
                [datetime(2006, 6, 22), 371.71],
                [datetime(2006, 6, 23), 391.73],
            ]
        }]
    )

    #this refers to python code in model.py. It uses the stremaflow prediction tool api to get this information.
    inflows = getforecastflows()
    forecastdates = getforecastdates()


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastdates[0], forecastdates[1], forecastdates[2], forecastdates[3], forecastdates[4], forecastdates[5], forecastdates[6]),
                           rows=[('Caudal de Entrada',inflows[0], inflows[1], inflows[2],inflows[3],inflows[4],inflows[5],inflows[6]),
                                 ('Caudal de Salida','10', '10', '13','12','12.4','11','13'),
                                 ('Niveles','368', '370', '369', '374','373','371','372')],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)


    context = {
        'timeseries_plot': timeseries_plot,
        'table_view': table_view,
 #       'historic_plot': historic_plot,
    }

    return render(request, 'reservoir_management/hatillo.html', context)

@login_required()
def maguaca(request):
    """
    Controller for the Add Dam page.
    """


    #TimeSeries plot. The series is hardcoded but we need to program it to look into a csv file and get the needed timeseries.
    #you would need to create a python script outside of this and then refer to it just like the getforecastflows() and getforecastdates()
    #for the table as seen below.
    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Maguaca',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': [
                [datetime(2001, 4, 10), 352.87],
                [datetime(2001, 4, 11), 352.41],
                [datetime(2001, 4, 12), 351.58],
                [datetime(2001, 10, 2), 364.65],
                [datetime(2001, 10, 3), 364.61],
                [datetime(2001, 10, 5), 364.84],
                [datetime(2001, 10, 8), 364.9],
                [datetime(2001, 10, 9), 364.87],
                [datetime(2001, 10, 10), 365],
                [datetime(2001, 10, 11), 365.19],
                [datetime(2001, 10, 12), 365.44],
                [datetime(2001, 10, 15), 366.45],
                [datetime(2001, 10, 16), 366.7],
                [datetime(2001, 10, 17), 366.88],
                [datetime(2001, 10, 18), 367.02],
                [datetime(2001, 10, 19), 367.13],
                [datetime(2001, 10, 22), 367.68],
                [datetime(2001, 10, 23), 367.46],
                [datetime(2001, 10, 24), 367.51],
                [datetime(2001, 10, 25), 367.55],
                [datetime(2001, 10, 26), 367.57],
                [datetime(2001, 10, 29), 367.68],
            ]
        }]
    )

    #this refers to python code in model.py. It uses the stremaflow prediction tool api to get this information.
    inflows = getforecastflows()
    forecastdates = getforecastdates()


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastdates[0], forecastdates[1], forecastdates[2], forecastdates[3], forecastdates[4], forecastdates[5], forecastdates[6]),
                           rows=[('Caudal de Entrada',inflows[0], inflows[1], inflows[2],inflows[3],inflows[4],inflows[5],inflows[6]),
                                 ('Caudal de Salida','10', '10', '13','12','12.4','11','13'),
                                 ('Niveles','368', '370', '369', '374','373','371','372')],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)


    context = {
        'timeseries_plot': timeseries_plot,
        'table_view': table_view,
 #       'historic_plot': historic_plot,
    }

    return render(request, 'reservoir_management/maguaca.html', context)

@login_required()
def chacuey(request):
    """
    Controller for the Add Dam page.
    """


    #TimeSeries plot. The series is hardcoded but we need to program it to look into a csv file and get the needed timeseries.
    #you would need to create a python script outside of this and then refer to it just like the getforecastflows() and getforecastdates()
    #for the table as seen below.
    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Chacuey',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': [
                [datetime(2001, 4, 10), 352.87],
                [datetime(2001, 4, 11), 352.41],
                [datetime(2001, 4, 12), 351.58],
                [datetime(2001, 10, 2), 364.65],
                [datetime(2001, 10, 3), 364.61],
                [datetime(2001, 10, 5), 364.84],
                [datetime(2001, 10, 8), 364.9],
                [datetime(2001, 10, 9), 364.87],
                [datetime(2001, 10, 10), 365],
                [datetime(2001, 10, 11), 365.19],
                [datetime(2001, 10, 12), 365.44],
                [datetime(2001, 10, 15), 366.45],
                [datetime(2001, 10, 16), 366.7],
                [datetime(2001, 10, 17), 366.88],
                [datetime(2001, 10, 18), 367.02],
                [datetime(2001, 10, 19), 367.13],
                [datetime(2001, 10, 22), 367.68],
                [datetime(2001, 10, 23), 367.46],
                [datetime(2001, 10, 24), 367.51],
                [datetime(2001, 10, 25), 367.55],
                [datetime(2001, 10, 26), 367.57],
                [datetime(2001, 10, 29), 367.68],
            ]
        }]
    )

    #this refers to python code in model.py. It uses the stremaflow prediction tool api to get this information.
    inflows = getforecastflows()
    forecastdates = getforecastdates()


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastdates[0], forecastdates[1], forecastdates[2], forecastdates[3], forecastdates[4], forecastdates[5], forecastdates[6]),
                           rows=[('Caudal de Entrada',inflows[0], inflows[1], inflows[2],inflows[3],inflows[4],inflows[5],inflows[6]),
                                 ('Caudal de Salida','10', '10', '13','12','12.4','11','13'),
                                 ('Niveles','368', '370', '369', '374','373','371','372')],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)


    context = {
        'timeseries_plot': timeseries_plot,
        'table_view': table_view,
 #       'historic_plot': historic_plot,
    }

    return render(request, 'reservoir_management/chacuey.html', context)

@login_required()
def jiguey(request):
    """
    Controller for the Add Dam page.
    """


    #TimeSeries plot. The series is hardcoded but we need to program it to look into a csv file and get the needed timeseries.
    #you would need to create a python script outside of this and then refer to it just like the getforecastflows() and getforecastdates()
    #for the table as seen below.
    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Jiguey',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': [
                [datetime(2001, 4, 10), 352.87],
                [datetime(2001, 4, 11), 352.41],
                [datetime(2001, 4, 12), 351.58],
                [datetime(2001, 10, 2), 364.65],
                [datetime(2001, 10, 3), 364.61],
                [datetime(2001, 10, 5), 364.84],
                [datetime(2001, 10, 8), 364.9],
                [datetime(2001, 10, 9), 364.87],
                [datetime(2001, 10, 10), 365],
                [datetime(2001, 10, 11), 365.19],
                [datetime(2001, 10, 12), 365.44],
                [datetime(2001, 10, 15), 366.45],
                [datetime(2001, 10, 16), 366.7],
                [datetime(2001, 10, 17), 366.88],
                [datetime(2001, 10, 18), 367.02],
                [datetime(2001, 10, 19), 367.13],
                [datetime(2001, 10, 22), 367.68],
                [datetime(2001, 10, 23), 367.46],
                [datetime(2001, 10, 24), 367.51],
                [datetime(2001, 10, 25), 367.55],
                [datetime(2001, 10, 26), 367.57],
                [datetime(2001, 10, 29), 367.68],
            ]
        }]
    )

    #this refers to python code in model.py. It uses the stremaflow prediction tool api to get this information.
    inflows = getforecastflows()
    forecastdates = getforecastdates()


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastdates[0], forecastdates[1], forecastdates[2], forecastdates[3], forecastdates[4], forecastdates[5], forecastdates[6]),
                           rows=[('Caudal de Entrada',inflows[0], inflows[1], inflows[2],inflows[3],inflows[4],inflows[5],inflows[6]),
                                 ('Caudal de Salida','10', '10', '13','12','12.4','11','13'),
                                 ('Niveles','368', '370', '369', '374','373','371','372')],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)


    context = {
        'timeseries_plot': timeseries_plot,
        'table_view': table_view,
 #       'historic_plot': historic_plot,
    }

    return render(request, 'reservoir_management/jiguey.html', context)

@login_required()
def moncion(request):
    """
    Controller for the Add Dam page.
    """


    #TimeSeries plot. The series is hardcoded but we need to program it to look into a csv file and get the needed timeseries.
    #you would need to create a python script outside of this and then refer to it just like the getforecastflows() and getforecastdates()
    #for the table as seen below.
    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Moncion',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': [
                [datetime(2001, 4, 10), 352.87],
                [datetime(2001, 4, 11), 352.41],
                [datetime(2001, 4, 12), 351.58],
                [datetime(2001, 10, 2), 364.65],
                [datetime(2001, 10, 3), 364.61],
                [datetime(2001, 10, 5), 364.84],
                [datetime(2001, 10, 8), 364.9],
                [datetime(2001, 10, 9), 364.87],
                [datetime(2001, 10, 10), 365],
                [datetime(2001, 10, 11), 365.19],
                [datetime(2001, 10, 12), 365.44],
                [datetime(2001, 10, 15), 366.45],
                [datetime(2001, 10, 16), 366.7],
                [datetime(2001, 10, 17), 366.88],
                [datetime(2001, 10, 18), 367.02],
                [datetime(2001, 10, 19), 367.13],
                [datetime(2001, 10, 22), 367.68],
                [datetime(2001, 10, 23), 367.46],
                [datetime(2001, 10, 24), 367.51],
                [datetime(2001, 10, 25), 367.55],
                [datetime(2001, 10, 26), 367.57],
                [datetime(2001, 10, 29), 367.68],
            ]
        }]
    )

    #this refers to python code in model.py. It uses the stremaflow prediction tool api to get this information.
    inflows = getforecastflows()
    forecastdates = getforecastdates()


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastdates[0], forecastdates[1], forecastdates[2], forecastdates[3], forecastdates[4], forecastdates[5], forecastdates[6]),
                           rows=[('Caudal de Entrada',inflows[0], inflows[1], inflows[2],inflows[3],inflows[4],inflows[5],inflows[6]),
                                 ('Caudal de Salida','10', '10', '13','12','12.4','11','13'),
                                 ('Niveles','368', '370', '369', '374','373','371','372')],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)


    context = {
        'timeseries_plot': timeseries_plot,
        'table_view': table_view,
 #       'historic_plot': historic_plot,
    }

    return render(request, 'reservoir_management/moncion.html', context)

@login_required()
def pinalito(request):
    """
    Controller for the Add Dam page.
    """


    #TimeSeries plot. The series is hardcoded but we need to program it to look into a csv file and get the needed timeseries.
    #you would need to create a python script outside of this and then refer to it just like the getforecastflows() and getforecastdates()
    #for the table as seen below.
    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Pinalito',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': [
                [datetime(2001, 4, 10), 352.87],
                [datetime(2001, 4, 11), 352.41],
                [datetime(2001, 4, 12), 351.58],
                [datetime(2001, 10, 2), 364.65],
                [datetime(2001, 10, 3), 364.61],
                [datetime(2001, 10, 5), 364.84],
                [datetime(2001, 10, 8), 364.9],
                [datetime(2001, 10, 9), 364.87],
                [datetime(2001, 10, 10), 365],
                [datetime(2001, 10, 11), 365.19],
                [datetime(2001, 10, 12), 365.44],
                [datetime(2001, 10, 15), 366.45],
                [datetime(2001, 10, 16), 366.7],
                [datetime(2001, 10, 17), 366.88],
                [datetime(2001, 10, 18), 367.02],
                [datetime(2001, 10, 19), 367.13],
                [datetime(2001, 10, 22), 367.68],
                [datetime(2001, 10, 23), 367.46],
                [datetime(2001, 10, 24), 367.51],
                [datetime(2001, 10, 25), 367.55],
                [datetime(2001, 10, 26), 367.57],
                [datetime(2001, 10, 29), 367.68],
            ]
        }]
    )

    #this refers to python code in model.py. It uses the stremaflow prediction tool api to get this information.
    inflows = getforecastflows()
    forecastdates = getforecastdates()


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastdates[0], forecastdates[1], forecastdates[2], forecastdates[3], forecastdates[4], forecastdates[5], forecastdates[6]),
                           rows=[('Caudal de Entrada',inflows[0], inflows[1], inflows[2],inflows[3],inflows[4],inflows[5],inflows[6]),
                                 ('Caudal de Salida','10', '10', '13','12','12.4','11','13'),
                                 ('Niveles','368', '370', '369', '374','373','371','372')],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)


    context = {
        'timeseries_plot': timeseries_plot,
        'table_view': table_view,
 #       'historic_plot': historic_plot,
    }

    return render(request, 'reservoir_management/pinalito.html', context)

@login_required()
def rincon(request):
    """
    Controller for the Add Dam page.
    """


    #TimeSeries plot. The series is hardcoded but we need to program it to look into a csv file and get the needed timeseries.
    #you would need to create a python script outside of this and then refer to it just like the getforecastflows() and getforecastdates()
    #for the table as seen below.
    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Rincon',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': [
                [datetime(2001, 4, 10), 352.87],
                [datetime(2001, 4, 11), 352.41],
                [datetime(2001, 4, 12), 351.58],
                [datetime(2001, 10, 2), 364.65],
                [datetime(2001, 10, 3), 364.61],
                [datetime(2001, 10, 5), 364.84],
                [datetime(2001, 10, 8), 364.9],
                [datetime(2001, 10, 9), 364.87],
                [datetime(2001, 10, 10), 365],
                [datetime(2001, 10, 11), 365.19],
                [datetime(2001, 10, 12), 365.44],
                [datetime(2001, 10, 15), 366.45],
                [datetime(2001, 10, 16), 366.7],
                [datetime(2001, 10, 17), 366.88],
                [datetime(2001, 10, 18), 367.02],
                [datetime(2001, 10, 19), 367.13],
                [datetime(2001, 10, 22), 367.68],
                [datetime(2001, 10, 23), 367.46],
                [datetime(2001, 10, 24), 367.51],
                [datetime(2001, 10, 25), 367.55],
                [datetime(2001, 10, 26), 367.57],
                [datetime(2001, 10, 29), 367.68],
            ]
        }]
    )

    #this refers to python code in model.py. It uses the stremaflow prediction tool api to get this information.
    inflows = getforecastflows()
    forecastdates = getforecastdates()


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastdates[0], forecastdates[1], forecastdates[2], forecastdates[3], forecastdates[4], forecastdates[5], forecastdates[6]),
                           rows=[('Caudal de Entrada',inflows[0], inflows[1], inflows[2],inflows[3],inflows[4],inflows[5],inflows[6]),
                                 ('Caudal de Salida','10', '10', '13','12','12.4','11','13'),
                                 ('Niveles','368', '370', '369', '374','373','371','372')],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)


    context = {
        'timeseries_plot': timeseries_plot,
        'table_view': table_view,
 #       'historic_plot': historic_plot,
    }

    return render(request, 'reservoir_management/rincon.html', context)

@login_required()
def sabaneta(request):
    """
    Controller for the Add Dam page.
    """


    #TimeSeries plot. The series is hardcoded but we need to program it to look into a csv file and get the needed timeseries.
    #you would need to create a python script outside of this and then refer to it just like the getforecastflows() and getforecastdates()
    #for the table as seen below.
    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Sabaneta',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': [
                [datetime(2001, 4, 10), 352.87],
                [datetime(2001, 4, 11), 352.41],
                [datetime(2001, 4, 12), 351.58],
                [datetime(2001, 10, 2), 364.65],
                [datetime(2001, 10, 3), 364.61],
                [datetime(2001, 10, 5), 364.84],
                [datetime(2001, 10, 8), 364.9],
                [datetime(2001, 10, 9), 364.87],
                [datetime(2001, 10, 10), 365],
                [datetime(2001, 10, 11), 365.19],
                [datetime(2001, 10, 12), 365.44],
                [datetime(2001, 10, 15), 366.45],
                [datetime(2001, 10, 16), 366.7],
                [datetime(2001, 10, 17), 366.88],
                [datetime(2001, 10, 18), 367.02],
                [datetime(2001, 10, 19), 367.13],
                [datetime(2001, 10, 22), 367.68],
                [datetime(2001, 10, 23), 367.46],
                [datetime(2001, 10, 24), 367.51],
                [datetime(2001, 10, 25), 367.55],
                [datetime(2001, 10, 26), 367.57],
                [datetime(2001, 10, 29), 367.68],
            ]
        }]
    )

    #this refers to python code in model.py. It uses the stremaflow prediction tool api to get this information.
    inflows = getforecastflows()
    forecastdates = getforecastdates()


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastdates[0], forecastdates[1], forecastdates[2], forecastdates[3], forecastdates[4], forecastdates[5], forecastdates[6]),
                           rows=[('Caudal de Entrada',inflows[0], inflows[1], inflows[2],inflows[3],inflows[4],inflows[5],inflows[6]),
                                 ('Caudal de Salida','10', '10', '13','12','12.4','11','13'),
                                 ('Niveles','368', '370', '369', '374','373','371','372')],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)


    context = {
        'timeseries_plot': timeseries_plot,
        'table_view': table_view,
 #       'historic_plot': historic_plot,
    }

    return render(request, 'reservoir_management/sabaneta.html', context)

@login_required()
def tavera_bao(request):
    """
    Controller for the Add Dam page.
    """


    #TimeSeries plot. The series is hardcoded but we need to program it to look into a csv file and get the needed timeseries.
    #you would need to create a python script outside of this and then refer to it just like the getforecastflows() and getforecastdates()
    #for the table as seen below.
    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Tavera-Bao',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': [
                [datetime(2001, 4, 10), 352.87],
                [datetime(2001, 4, 11), 352.41],
                [datetime(2001, 4, 12), 351.58],
                [datetime(2001, 10, 2), 364.65],
                [datetime(2001, 10, 3), 364.61],
                [datetime(2001, 10, 5), 364.84],
                [datetime(2001, 10, 8), 364.9],
                [datetime(2001, 10, 9), 364.87],
                [datetime(2001, 10, 10), 365],
                [datetime(2001, 10, 11), 365.19],
                [datetime(2001, 10, 12), 365.44],
                [datetime(2001, 10, 15), 366.45],
                [datetime(2001, 10, 16), 366.7],
                [datetime(2001, 10, 17), 366.88],
                [datetime(2001, 10, 18), 367.02],
                [datetime(2001, 10, 19), 367.13],
                [datetime(2001, 10, 22), 367.68],
                [datetime(2001, 10, 23), 367.46],
                [datetime(2001, 10, 24), 367.51],
                [datetime(2001, 10, 25), 367.55],
                [datetime(2001, 10, 26), 367.57],
                [datetime(2001, 10, 29), 367.68],
            ]
        }]
    )

    #this refers to python code in model.py. It uses the stremaflow prediction tool api to get this information.
    inflows = getforecastflows()
    forecastdates = getforecastdates()


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastdates[0], forecastdates[1], forecastdates[2], forecastdates[3], forecastdates[4], forecastdates[5], forecastdates[6]),
                           rows=[('Caudal de Entrada',inflows[0], inflows[1], inflows[2],inflows[3],inflows[4],inflows[5],inflows[6]),
                                 ('Caudal de Salida','10', '10', '13','12','12.4','11','13'),
                                 ('Niveles','368', '370', '369', '374','373','371','372')],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)


    context = {
        'timeseries_plot': timeseries_plot,
        'table_view': table_view,
 #       'historic_plot': historic_plot,
    }

    return render(request, 'reservoir_management/tavera_bao.html', context)

@login_required()
def valdesia(request):
    """
    Controller for the Add Dam page.
    """


    #TimeSeries plot. The series is hardcoded but we need to program it to look into a csv file and get the needed timeseries.
    #you would need to create a python script outside of this and then refer to it just like the getforecastflows() and getforecastdates()
    #for the table as seen below.
    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Valdesia',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': [
                [datetime(2001, 4, 10), 352.87],
                [datetime(2001, 4, 11), 352.41],
                [datetime(2001, 4, 12), 351.58],
                [datetime(2001, 10, 2), 364.65],
                [datetime(2001, 10, 3), 364.61],
                [datetime(2001, 10, 5), 364.84],
                [datetime(2001, 10, 8), 364.9],
                [datetime(2001, 10, 9), 364.87],
                [datetime(2001, 10, 10), 365],
                [datetime(2001, 10, 11), 365.19],
                [datetime(2001, 10, 12), 365.44],
                [datetime(2001, 10, 15), 366.45],
                [datetime(2001, 10, 16), 366.7],
                [datetime(2001, 10, 17), 366.88],
                [datetime(2001, 10, 18), 367.02],
                [datetime(2001, 10, 19), 367.13],
                [datetime(2001, 10, 22), 367.68],
                [datetime(2001, 10, 23), 367.46],
                [datetime(2001, 10, 24), 367.51],
                [datetime(2001, 10, 25), 367.55],
                [datetime(2001, 10, 26), 367.57],
                [datetime(2001, 10, 29), 367.68],
            ]
        }]
    )

    #this refers to python code in model.py. It uses the stremaflow prediction tool api to get this information.
    inflows = getforecastflows()
    forecastdates = getforecastdates()


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastdates[0], forecastdates[1], forecastdates[2], forecastdates[3], forecastdates[4], forecastdates[5], forecastdates[6]),
                           rows=[('Caudal de Entrada',inflows[0], inflows[1], inflows[2],inflows[3],inflows[4],inflows[5],inflows[6]),
                                 ('Caudal de Salida','10', '10', '13','12','12.4','11','13'),
                                 ('Niveles','368', '370', '369', '374','373','371','372')],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)


    context = {
        'timeseries_plot': timeseries_plot,
        'table_view': table_view,
 #       'historic_plot': historic_plot,
    }

    return render(request, 'reservoir_management/valdesia.html', context)
