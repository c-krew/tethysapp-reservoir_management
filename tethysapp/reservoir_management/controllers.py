#This is the main python script where your html content is created. search for tethys gizmos online for more information on gizmos
#Each page has its own function and code that is run for that specific page. Each html page needs its own function

from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404, HttpResponse
from tethys_sdk.gizmos import *
import datetime
import plotly.graph_objs as go
import os
import pandas as pd
from model import getforecastflows, gethistoricaldata, getrecentdata, forecastdata, forecastlevels, gettabledates
from .app import ReservoirManagement as app


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

    #this refers to python code in model.py. It uses the stremaflow prediction tool api to get this information.
    comids = ['593', '600', '599']

    forecasteddata = gettabledates(comids)
    data = gethistoricaldata('S. Yegua')

    min_level = [[data[0][0], 358.00], [data[-1][0], 358.00]]
    max_level = [[data[0][0], 396.40], [data[-1][0], 396.4]]

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Sabana Yequa',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[
            {'name': 'Historico','data': data},
            {'name': 'Nivel Minimo de Operacion', 'data': min_level, 'type': 'line', 'color': '#660066'},
            {'name': 'Nivel Maximo de Operacion', 'data': max_level, 'type': 'line', 'color': '#FF0000'}
            ],
        y_min = 350
    )


    outflow_edit = TableView(column_names=('Dia', 'Caudal de Salida (cms)', 'Tiempo de salida (horas)'),
                             rows=[(forecasteddata[0], '0', '0'),
                                   (forecasteddata[1], '0', '0'),
                                   (forecasteddata[2], '0', '0'),
                                   (forecasteddata[3], '0', '0'),
                                   (forecasteddata[4], '0', '0'),
                                   (forecasteddata[5], '0', '0'),
                                   (forecasteddata[6], '0', '0'),
                                   ],
                             hover=True,
                             striped=True,
                             bordered=True,
                             condensed=True,
                             editable_columns=(False, 'Outflow', 'Time'),
                             row_ids=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'],
                             classes="outflowtable"
                             )

    calculate = Button(display_text='Calcular Niveles del Embalse',
                       name='calculate',
                       style='',
                       icon='',
                       href='',
                       submit=False,
                       disabled=False,
                       attributes={"onclick": "calculatelevels()"},
                       classes='calcbut'
                       )

    outflow_button = Button(display_text='Ingresar caudales de salida',
                            name='dimensions',
                            style='',
                            icon='',
                            href='',
                            submit=False,
                            disabled=False,
                            attributes={"onclick": "outflowmodal()"},
                            classes='outflow_button'
                            )
    context = {
        'timeseries_plot': timeseries_plot,
        'outflow_button': outflow_button,
        'calculate': calculate,
        'outflow_edit': outflow_edit,
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
                               options=[('Sabana Yegua', 'Sabana Yegua'),
                                        ('Sabaneta', 'Sabaneta'),
                                        ('Hatillo', 'Hatillo'),
                                        ('Tavera-Bao', 'Tavera-Bao'),
                                        ('Moncion', 'Moncion'),
                                        ('Rincon', 'Rincon'),
                                        ('Jiguey', 'Jiguey'),
                                        ('Valdesia', 'Valdesia'),
                                        ('Rio Blanco', 'Rio Blanco'),
                                        ('Pinalito', 'Pinalito'),
                                        ('Maguaca', 'Maguaca'),
                                        ('Chacuey', 'Chacuey')
                                        ],
                               attributes={"onchange": "get_min_max_operating_levels()"},
                            )

    level_input = TextInput(display_text='Nivel de Agua',
                           name='levelinput',
                           placeholder='Niveles de Operacion: Min-358 Max-396.4',
                           )


    today = datetime.datetime.now()
    year = str(today.year)
    month = str(today.strftime("%B"))
    day = str(today.day)
    date = month + ' ' + day + ', ' + year

    date_input = DatePicker(name='dateinput',
                             display_text='Dia',
                             autoclose=True,
                             format='MM d, yyyy',
                             start_date='2/15/2014',
                             start_view='month',
                             today_button=True,
                             initial= date)

    data = getrecentdata()
    table_view = TableView(column_names=('Tiempo','Tavera-Bao','Moncion','Rincon','Hatillo',
                                         'Jiguey','Valdesia','S. Yegua','Sabaneta','Rio Blanco',
                                         'Pinalito','Maguaca','Chacuey'),
                           rows=data,
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=True)

    message_box = MessageBox(name='sampleModal',
                             title='Resumen de Entradas',
                             message='',
                             dismiss_button='Regresar',
                             affirmative_button='Proceder',
                             width=400,
                             affirmative_attributes='onclick=append();',
                             )

    download_button = Button(display_text='Descargar Datos',
                            name='download',
                            style='',
                            icon='',
                            href='file:///C:/Users/student/tethysdev/tethysapp-reservoir_management/tethysapp/reservoir_management/workspaces/app_workspace/DamLevel_DR_BYU 2018.xlsx',
                            submit=False,
                            disabled=False,
                            attributes={"onclick": "outflowmodal()"},
                            classes='outflow_button'
                            )


    context = {
        'dam_input': dam_input,
        'level_input':level_input,
        'date_input': date_input,
        'table_view': table_view,
        'message_box': message_box,
        'download_button': download_button,
    }

    return render(request, 'reservoir_management/reportar.html', context)

@login_required()
def hatillo(request):
    """
    Controller for the Add Dam page.
    """

    comids = ['834', '813', '849', '857']

    forecasteddata = gettabledates(comids)
    data = gethistoricaldata('Hatillo')

    min_level = [[data[0][0], 70.00], [data[-1][0], 70.00]]
    max_level = [[data[0][0], 86.50], [data[-1][0], 86.50]]

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Hatillo',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[
            {'name': 'Historico','data': data},
            {'name': 'Nivel Minimo', 'data': min_level, 'type': 'line', 'color': '#660066'},
            {'name': 'Nivel Maximo', 'data': max_level, 'type': 'line', 'color': '#FF0000'}
            ],
        y_min = 55
    )

    outflow_edit = TableView(column_names=('Dia', 'Caudal de Salida (cms)', 'Tiempo de salida (horas)'),
                             rows=[(forecasteddata[0], '0', '0'),
                                   (forecasteddata[1], '0', '0'),
                                   (forecasteddata[2], '0', '0'),
                                   (forecasteddata[3], '0', '0'),
                                   (forecasteddata[4], '0', '0'),
                                   (forecasteddata[5], '0', '0'),
                                   (forecasteddata[6], '0', '0'),
                                   ],
                             hover=True,
                             striped=True,
                             bordered=True,
                             condensed=True,
                             editable_columns=(False, 'Outflow', 'Time'),
                             row_ids=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'],
                             classes="outflowtable"
                             )

    calculate = Button(display_text='Calcular Niveles del Embalse',
                       name='calculate',
                       style='',
                       icon='',
                       href='',
                       submit=False,
                       disabled=False,
                       attributes={"onclick": "calculatelevels()"},
                       classes='calcbut'
                       )

    outflow_button = Button(display_text='Ingresar caudales de salida',
                            name='dimensions',
                            style='',
                            icon='',
                            href='',
                            submit=False,
                            disabled=False,
                            attributes={"onclick": "outflowmodal()"},
                            classes='outflow_button'
                            )
    context = {
        'timeseries_plot': timeseries_plot,
        'outflow_button': outflow_button,
        'calculate': calculate,
        'outflow_edit': outflow_edit,
    }

    return render(request, 'reservoir_management/hatillo.html', context)

@login_required()
def maguaca(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['1399']

    forecasteddata = gettabledates(comids)
    data = gethistoricaldata('Maguaca')

    min_level = [[data[0][0], 46.70], [data[-1][0], 46.70]]
    max_level = [[data[0][0], 57.00], [data[-1][0], 57.00]]

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Maguaca',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[
            {'name': 'Historico','data': data},
            {'name': 'Nivel Minimo', 'data': min_level, 'type': 'line', 'color': '#660066'},
            {'name': 'Nivel Maximo', 'data': max_level, 'type': 'line', 'color': '#FF0000'}
            ],
        y_min = 30
    )


    outflow_edit = TableView(column_names=('Dia', 'Caudal de Salida (cms)', 'Tiempo de salida (horas)'),
                             rows=[(forecasteddata[0], '0', '0'),
                                   (forecasteddata[1], '0', '0'),
                                   (forecasteddata[2], '0', '0'),
                                   (forecasteddata[3], '0', '0'),
                                   (forecasteddata[4], '0', '0'),
                                   (forecasteddata[5], '0', '0'),
                                   (forecasteddata[6], '0', '0'),
                                   ],
                             hover=True,
                             striped=True,
                             bordered=True,
                             condensed=True,
                             editable_columns=(False, 'Outflow', 'Time'),
                             row_ids=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'],
                             classes="outflowtable"
                             )

    calculate = Button(display_text='Calcular Niveles del Embalse',
                       name='calculate',
                       style='',
                       icon='',
                       href='',
                       submit=False,
                       disabled=False,
                       attributes={"onclick": "calculatelevels()"},
                       classes='calcbut'
                       )

    outflow_button = Button(display_text='Ingresar caudales de salida',
                            name='dimensions',
                            style='',
                            icon='',
                            href='',
                            submit=False,
                            disabled=False,
                            attributes={"onclick": "outflowmodal()"},
                            classes='outflow_button'
                            )
    context = {
        'timeseries_plot': timeseries_plot,
        'outflow_button': outflow_button,
        'calculate': calculate,
        'outflow_edit': outflow_edit,
    }


    return render(request, 'reservoir_management/maguaca.html', context)

@login_required()
def chacuey(request):
    """
    Controller for the Add Dam page.
    """

    comids = ['1396']

    forecasteddata = gettabledates(comids)
    data = gethistoricaldata('Chacuey')

    min_level = [[data[0][0], 47.00], [data[-1][0], 47.00]]
    max_level = [[data[0][0], 54.63], [data[-1][0], 54.63]]

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Chacuey',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[
            {'name': 'Historico','data': data},
            {'name': 'Nivel Minimo', 'data': min_level, 'type': 'line', 'color': '#660066'},
            {'name': 'Nivel Maximo', 'data': max_level, 'type': 'line', 'color': '#FF0000'}
            ],
        y_min = 30
    )


    outflow_edit = TableView(column_names=('Dia', 'Caudal de Salida (cms)', 'Tiempo de salida (horas)'),
                             rows=[(forecasteddata[0], '0', '0'),
                                   (forecasteddata[1], '0', '0'),
                                   (forecasteddata[2], '0', '0'),
                                   (forecasteddata[3], '0', '0'),
                                   (forecasteddata[4], '0', '0'),
                                   (forecasteddata[5], '0', '0'),
                                   (forecasteddata[6], '0', '0'),
                                   ],
                             hover=True,
                             striped=True,
                             bordered=True,
                             condensed=True,
                             editable_columns=(False, 'Outflow', 'Time'),
                             row_ids = ['day1', 'day2', 'day3', 'day4', 'day5', 'day6','day7'],
                             classes = "outflowtable"
                             )

    calculate = Button(display_text='Calcular Niveles del Embalse',
                       name='calculate',
                       style='',
                       icon='',
                       href='',
                       submit=False,
                       disabled=False,
                       attributes={"onclick": "calculatelevels()"},
                       classes='calcbut'
                       )

    outflow_button = Button(display_text='Ingresar caudales de salida',
                            name='dimensions',
                            style='',
                            icon='',
                            href='',
                            submit=False,
                            disabled=False,
                            attributes={"onclick": "outflowmodal()"},
                            classes='outflow_button'
                            )
    context = {
        'timeseries_plot': timeseries_plot,
        'outflow_button':outflow_button,
        'calculate': calculate,
        'outflow_edit': outflow_edit,
    }



    return render(request, 'reservoir_management/chacuey.html', context)

@login_required()
def jiguey(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['475', '496']

    forecasteddata = gettabledates(comids)
    data = gethistoricaldata('Jiguey')

    min_level = [[data[0][0], 500.00], [data[-1][0], 500.00]]
    max_level = [[data[0][0], 541.50], [data[-1][0], 541.50]]

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Jiguey',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[
            {'name': 'Historico','data': data},
            {'name': 'Nivel Minimo', 'data': min_level, 'type': 'line', 'color': '#660066'},
            {'name': 'Nivel Maximo', 'data': max_level, 'type': 'line', 'color': '#FF0000'}
            ],
        y_min = 450
    )


    outflow_edit = TableView(column_names=('Dia', 'Caudal de Salida (cms)', 'Tiempo de salida (horas)'),
                             rows=[(forecasteddata[0], '0', '0'),
                                   (forecasteddata[1], '0', '0'),
                                   (forecasteddata[2], '0', '0'),
                                   (forecasteddata[3], '0', '0'),
                                   (forecasteddata[4], '0', '0'),
                                   (forecasteddata[5], '0', '0'),
                                   (forecasteddata[6], '0', '0'),
                                   ],
                             hover=True,
                             striped=True,
                             bordered=True,
                             condensed=True,
                             editable_columns=(False, 'Outflow', 'Time'),
                             row_ids=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'],
                             classes="outflowtable"
                             )

    calculate = Button(display_text='Calcular Niveles del Embalse',
                       name='calculate',
                       style='',
                       icon='',
                       href='',
                       submit=False,
                       disabled=False,
                       attributes={"onclick": "calculatelevels()"},
                       classes='calcbut'
                       )

    outflow_button = Button(display_text='Ingresar caudales de salida',
                            name='dimensions',
                            style='',
                            icon='',
                            href='',
                            submit=False,
                            disabled=False,
                            attributes={"onclick": "outflowmodal()"},
                            classes='outflow_button'
                            )
    context = {
        'timeseries_plot': timeseries_plot,
        'outflow_button': outflow_button,
        'calculate': calculate,
        'outflow_edit': outflow_edit,
    }


    return render(request, 'reservoir_management/jiguey.html', context)

@login_required()
def moncion(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['1148', '1182']

    data = gethistoricaldata('Moncion')
    forecasteddata = gettabledates(comids)

    min_level = [[data[0][0], 223.00], [data[-1][0], 223.00]]
    max_level = [[data[0][0], 280.00], [data[-1][0], 280.00]]

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Moncion',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[
            {'name': 'Historico','data': data},
            {'name': 'Nivel Minimo', 'data': min_level, 'type': 'line', 'color': '#660066'},
            {'name': 'Nivel Maximo', 'data': max_level, 'type': 'line', 'color': '#FF0000'}
            ],
        y_min = 180
    )


    outflow_edit = TableView(column_names=('Dia', 'Caudal de Salida (cms)', 'Tiempo de salida (horas)'),
                             rows=[(forecasteddata[0], '0', '0'),
                                   (forecasteddata[1], '0', '0'),
                                   (forecasteddata[2], '0', '0'),
                                   (forecasteddata[3], '0', '0'),
                                   (forecasteddata[4], '0', '0'),
                                   (forecasteddata[5], '0', '0'),
                                   (forecasteddata[6], '0', '0'),
                                   ],
                             hover=True,
                             striped=True,
                             bordered=True,
                             condensed=True,
                             editable_columns=(False, 'Outflow', 'Time'),
                             row_ids=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'],
                             classes="outflowtable"
                             )

    calculate = Button(display_text='Calcular Niveles del Embalse',
                       name='calculate',
                       style='',
                       icon='',
                       href='',
                       submit=False,
                       disabled=False,
                       attributes={"onclick": "calculatelevels()"},
                       classes='calcbut'
                       )

    outflow_button = Button(display_text='Ingresar caudales de salida',
                            name='dimensions',
                            style='',
                            icon='',
                            href='',
                            submit=False,
                            disabled=False,
                            attributes={"onclick": "outflowmodal()"},
                            classes='outflow_button'
                            )
    context = {
        'timeseries_plot': timeseries_plot,
        'outflow_button': outflow_button,
        'calculate': calculate,
        'outflow_edit': outflow_edit,
    }

    return render(request, 'reservoir_management/moncion.html', context)

@login_required()
def pinalito(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['790']

    forecastinfo = getforecastflows(comids)
    data = gethistoricaldata('Pinalito')

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Pinalito',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': data
        }],
        y_min = 1160
    )

    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastinfo['timestep'][0], forecastinfo['timestep'][1], forecastinfo['timestep'][2], forecastinfo['timestep'][3], forecastinfo['timestep'][4], forecastinfo['timestep'][5], forecastinfo['timestep'][6]),
                           rows=[('Caudal de Entrada (Total)',forecastinfo['total'][0], forecastinfo['total'][1], forecastinfo['total'][2],forecastinfo['total'][3],forecastinfo['total'][4],forecastinfo['total'][5],forecastinfo['total'][6]),
                                 ('Caudal de Entrada (790)', forecastinfo['790'][0], forecastinfo['790'][1], forecastinfo['790'][2], forecastinfo['790'][3],
                                  forecastinfo['790'][4], forecastinfo['790'][5], forecastinfo['790'][6]),
                                 ('Niveles','368', '370', '369', '374','373','371','372')],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)

    outflow_edit = TableView(column_names=('Dia', 'Caudal de Salida (cms)', 'Tiempo de salida (horas)'),
                             rows=[(forecasteddata['dates'][0], '0', '0'),
                                   (forecasteddata['dates'][1], '0', '0'),
                                   (forecasteddata['dates'][2], '0', '0'),
                                   (forecasteddata['dates'][3], '0', '0'),
                                   (forecasteddata['dates'][4], '0', '0'),
                                   (forecasteddata['dates'][5], '0', '0'),
                                   (forecasteddata['dates'][6], '0', '0'),
                                   ],
                             hover=True,
                             striped=True,
                             bordered=True,
                             condensed=True,
                             editable_columns=(False, 'Outflow', 'Time'),
                             row_ids=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'],
                             classes="outflowtable"
                             )

    calculate = Button(display_text='Calcular Niveles del Embalse',
                       name='calculate',
                       style='',
                       icon='',
                       href='',
                       submit=False,
                       disabled=False,
                       attributes={"onclick": "calculatelevels()"},
                       classes='calcbut'
                       )

    outflow_button = Button(display_text='Ingresar caudales de salida',
                            name='dimensions',
                            style='',
                            icon='',
                            href='',
                            submit=False,
                            disabled=False,
                            attributes={"onclick": "outflowmodal()"},
                            classes='outflow_button'
                            )
    context = {
        'timeseries_plot': timeseries_plot,
        'table_view': table_view,
        'outflow_button': outflow_button,
        'calculate': calculate,
        'outflow_edit': outflow_edit,
    }


    return render(request, 'reservoir_management/pinalito.html', context)

@login_required()
def rincon(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['853', '922']

    forecasteddata = gettabledates(comids)
    data = gethistoricaldata('Rincon')

    min_level = [[data[0][0], 108.50], [data[-1][0], 108.50]]
    max_level = [[data[0][0], 122.00], [data[-1][0], 122.00]]

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Rincon',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[
            {'name': 'Historico','data': data},
            {'name': 'Nivel Minimo', 'data': min_level, 'type': 'line', 'color': '#660066'},
            {'name': 'Nivel Maximo', 'data': max_level, 'type': 'line', 'color': '#FF0000'}
            ],
        y_min = 95
    )


    outflow_edit = TableView(column_names=('Dia', 'Caudal de Salida (cms)', 'Tiempo de salida (horas)'),
                             rows=[(forecasteddata[0], '0', '0'),
                                   (forecasteddata[1], '0', '0'),
                                   (forecasteddata[2], '0', '0'),
                                   (forecasteddata[3], '0', '0'),
                                   (forecasteddata[4], '0', '0'),
                                   (forecasteddata[5], '0', '0'),
                                   (forecasteddata[6], '0', '0'),
                                   ],
                             hover=True,
                             striped=True,
                             bordered=True,
                             condensed=True,
                             editable_columns=(False, 'Outflow', 'Time'),
                             row_ids=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'],
                             classes="outflowtable"
                             )

    calculate = Button(display_text='Calcular Niveles del Embalse',
                       name='calculate',
                       style='',
                       icon='',
                       href='',
                       submit=False,
                       disabled=False,
                       attributes={"onclick": "calculatelevels()"},
                       classes='calcbut'
                       )

    outflow_button = Button(display_text='Ingresar caudales de salida',
                            name='dimensions',
                            style='',
                            icon='',
                            href='',
                            submit=False,
                            disabled=False,
                            attributes={"onclick": "outflowmodal()"},
                            classes='outflow_button'
                            )
    context = {
        'timeseries_plot': timeseries_plot,
        'outflow_button': outflow_button,
        'calculate': calculate,
        'outflow_edit': outflow_edit,
    }


    return render(request, 'reservoir_management/rincon.html', context)

@login_required()
def sabaneta(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['863', '862']

    forecasteddata = gettabledates(comids)
    data = gethistoricaldata('Sabaneta')

    min_level = [[data[0][0], 612.00], [data[-1][0], 612.00]]
    max_level = [[data[0][0], 644.00], [data[-1][0], 644.00]]

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Sabaneta',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[
            {'name': 'Historico','data': data},
            {'name': 'Nivel Minimo', 'data': min_level, 'type': 'line', 'color': '#660066'},
            {'name': 'Nivel Maximo', 'data': max_level, 'type': 'line', 'color': '#FF0000'}
            ],
        y_min = 580
    )

    outflow_edit = TableView(column_names=('Dia', 'Caudal de Salida (cms)', 'Tiempo de salida (horas)'),
                             rows=[(forecasteddata[0], '0', '0'),
                                   (forecasteddata[1], '0', '0'),
                                   (forecasteddata[2], '0', '0'),
                                   (forecasteddata[3], '0', '0'),
                                   (forecasteddata[4], '0', '0'),
                                   (forecasteddata[5], '0', '0'),
                                   (forecasteddata[6], '0', '0'),
                                   ],
                             hover=True,
                             striped=True,
                             bordered=True,
                             condensed=True,
                             editable_columns=(False, 'Outflow', 'Time'),
                             row_ids=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'],
                             classes="outflowtable"
                             )

    calculate = Button(display_text='Calcular Niveles del Embalse',
                       name='calculate',
                       style='',
                       icon='',
                       href='',
                       submit=False,
                       disabled=False,
                       attributes={"onclick": "calculatelevels()"},
                       classes='calcbut'
                       )

    outflow_button = Button(display_text='Ingresar caudales de salida',
                            name='dimensions',
                            style='',
                            icon='',
                            href='',
                            submit=False,
                            disabled=False,
                            attributes={"onclick": "outflowmodal()"},
                            classes='outflow_button'
                            )
    context = {
        'timeseries_plot': timeseries_plot,
        'outflow_button': outflow_button,
        'calculate': calculate,
        'outflow_edit': outflow_edit,
    }

    return render(request, 'reservoir_management/sabaneta.html', context)

@login_required()
def tavera_bao(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['1024', '1140', '1142', '1153']

    forecasteddata = gettabledates(comids)
    data = gethistoricaldata('Tavera')

    min_level = [[data[0][0], 300.00], [data[-1][0], 300.00]]
    max_level = [[data[0][0], 327.50], [data[-1][0], 327.50]]

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Tavera-Bao',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[
            {'name': 'Historico','data': data},
            {'name': 'Nivel Minimo', 'data': min_level, 'type': 'line', 'color': '#660066'},
            {'name': 'Nivel Maximo', 'data': max_level, 'type': 'line', 'color': '#FF0000'}
            ],
        y_min = 270
    )



    outflow_edit = TableView(column_names=('Dia', 'Caudal de Salida (cms)', 'Tiempo de salida (horas)'),
                             rows=[(forecasteddata[0], '0', '0'),
                                   (forecasteddata[1], '0', '0'),
                                   (forecasteddata[2], '0', '0'),
                                   (forecasteddata[3], '0', '0'),
                                   (forecasteddata[4], '0', '0'),
                                   (forecasteddata[5], '0', '0'),
                                   (forecasteddata[6], '0', '0'),
                                   ],
                             hover=True,
                             striped=True,
                             bordered=True,
                             condensed=True,
                             editable_columns=(False, 'Outflow', 'Time'),
                             row_ids=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'],
                             classes="outflowtable"
                             )

    calculate = Button(display_text='Calcular Niveles del Embalse',
                       name='calculate',
                       style='',
                       icon='',
                       href='',
                       submit=False,
                       disabled=False,
                       attributes={"onclick": "calculatelevels()"},
                       classes='calcbut'
                       )

    outflow_button = Button(display_text='Ingresar caudales de salida',
                            name='dimensions',
                            style='',
                            icon='',
                            href='',
                            submit=False,
                            disabled=False,
                            attributes={"onclick": "outflowmodal()"},
                            classes='outflow_button'
                            )
    context = {
        'timeseries_plot': timeseries_plot,
        'outflow_button': outflow_button,
        'calculate': calculate,
        'outflow_edit': outflow_edit,
    }

    return render(request, 'reservoir_management/tavera_bao.html', context)

@login_required()
def valdesia(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['159']

    forecasteddata = gettabledates(comids)
    data = gethistoricaldata('Valdesia')

    min_level = [[data[0][0], 130.75], [data[-1][0], 130.75]]
    max_level = [[data[0][0], 150.00], [data[-1][0], 150.00]]

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Valdesia',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[
            {'name': 'Historico','data': data},
            {'name': 'Nivel Minimo', 'data': min_level, 'type': 'line', 'color': '#660066'},
            {'name': 'Nivel Maximo', 'data': max_level, 'type': 'line', 'color': '#FF0000'}
            ],
        y_min = 110
    )


    outflow_edit = TableView(column_names=('Dia', 'Caudal de Salida (cms)', 'Tiempo de salida (horas)'),
                             rows=[(forecasteddata[0], '0', '0'),
                                   (forecasteddata[1], '0', '0'),
                                   (forecasteddata[2], '0', '0'),
                                   (forecasteddata[3], '0', '0'),
                                   (forecasteddata[4], '0', '0'),
                                   (forecasteddata[5], '0', '0'),
                                   (forecasteddata[6], '0', '0'),
                                   ],
                             hover=True,
                             striped=True,
                             bordered=True,
                             condensed=True,
                             editable_columns=(False, 'Outflow', 'Time'),
                             row_ids=['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7'],
                             classes="outflowtable"
                             )

    calculate = Button(display_text='Calcular Niveles del Embalse',
                       name='calculate',
                       style='',
                       icon='',
                       href='',
                       submit=False,
                       disabled=False,
                       attributes={"onclick": "calculatelevels()"},
                       classes='calcbut'
                       )

    outflow_button = Button(display_text='Ingresar caudales de salida',
                            name='dimensions',
                            style='',
                            icon='',
                            href='',
                            submit=False,
                            disabled=False,
                            attributes={"onclick": "outflowmodal()"},
                            classes='outflow_button'
                            )
    context = {
        'timeseries_plot': timeseries_plot,
        'outflow_button': outflow_button,
        'calculate': calculate,
        'outflow_edit': outflow_edit,
    }

    return render(request, 'reservoir_management/valdesia.html', context)

def get_forecast_curve(request):
    get_data = request.GET

    try:
        levels = get_data['forecastlevels'].split(",")
        forecastdates = get_data['forecastdates'].split(",")
        res = get_data['res']

        datetimedates = []
        forecastlevel = []
        observeddates = []
        observedlevels = []

        for x in range(0,len(forecastdates)):
            datetimedates.append(datetime.datetime.strptime(forecastdates[x], "%Y-%m-%d"))
            forecastlevel.append(float(levels[x]))

        if res == 'Sabana_Yegua':
            res = 'S. Yegua'
        app_workspace = app.get_app_workspace()
        damsheet = os.path.join(app_workspace.path, 'DamLevel_DR_BYU 2018.xlsx')

        dfnan = pd.read_excel(damsheet)
        df1 = dfnan[['Nivel', res]]
        df = df1.dropna()[::-1]
        reslevels = (df[:15])

        for index, row in reslevels.iterrows():
            observeddates.append(datetime.datetime.strptime(str(row['Nivel'])[:10], "%Y-%m-%d"))
            observedlevels.append(row[res])

        forecast = go.Scatter(
            x=datetimedates,
            y=forecastlevel,
            fill='tozeroy',
            name='pronosticos'
        )

        observed = go.Scatter(
            x=observeddates,
            y=observedlevels,
            fill='tozeroy',
            name='observados'
        )

        layout = go.Layout(title="Niveles Observados y Pronosticados",
                           xaxis=dict(
                               title='Dia',
                               type='datetime'),
                           yaxis=dict(
                               title='Nivel del Emblase',
                               range=[float(min(min(forecastlevel),min(observedlevels)))-2.0, float(max(max(forecastlevel),max(observedlevels))) + 2.0]),
                           showlegend=True)

        chart_obj = PlotlyView(
            go.Figure(data=[forecast,observed],
                      layout=layout)
        )

        context = {
            'gizmo_object': chart_obj,
        }

        return render(request,'reservoir_management/gizmo_ajax.html', context)

    except Exception as e:
        print str(e)
        return JsonResponse({'error':'Unknown Error'})
