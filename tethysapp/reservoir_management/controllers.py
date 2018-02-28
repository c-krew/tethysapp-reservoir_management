#This is the main python script where your html content is created. search for tethys gizmos online for more information on gizmos
#Each page has its own function and code that is run for that specific page. Each html page needs its own function

from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import MapView, Button, TextInput, DatePicker, SelectInput, DataTableView, MVDraw, MVView, MVLayer, LinePlot, TableView, TimeSeries
from datetime import datetime
from model import getforecastflows, gethistoricaldata


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
    watershed = 'Dominican Republic'
    subbasin = 'Yaque del Sur'
    comids = ['21838', '21834', '21835']

    forecastinfo = getforecastflows(watershed,subbasin,comids)
    data = gethistoricaldata('S. Yegua')

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Sabana Yequa',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': data
        }],
        y_min = 300
    )

    table_view = TableView(column_names=('Caudales/Niveles',forecastinfo['timestep'][0], forecastinfo['timestep'][1], forecastinfo['timestep'][2], forecastinfo['timestep'][3], forecastinfo['timestep'][4], forecastinfo['timestep'][5], forecastinfo['timestep'][6]),
                           rows=[('Caudal de Entrada (Total)',forecastinfo['total'][0], forecastinfo['total'][1], forecastinfo['total'][2],forecastinfo['total'][3],forecastinfo['total'][4],forecastinfo['total'][5],forecastinfo['total'][6]),
                                 ('Caudal de Entrada (21838)', forecastinfo['21838'][0], forecastinfo['21838'][1], forecastinfo['21838'][2], forecastinfo['21838'][3],
                                  forecastinfo['21838'][4], forecastinfo['21838'][5], forecastinfo['21838'][6]),
                                 ('Caudal de Entrada (21835)', forecastinfo['21835'][0], forecastinfo['21835'][1], forecastinfo['21835'][2], forecastinfo['21835'][3],
                                  forecastinfo['21835'][4], forecastinfo['21835'][5], forecastinfo['21835'][6]),
                                 ('Caudal de Entrada (21834)', forecastinfo['21834'][0], forecastinfo['21834'][1], forecastinfo['21834'][2], forecastinfo['21834'][3],
                                  forecastinfo['21834'][4], forecastinfo['21834'][5], forecastinfo['21834'][6]),
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
    #you would need to create a python script outside of this and then refer to it just like the getforecastflows() and getforecastinfo[timestep]()
    #for the table as seen below.

    watershed = 'Dominican Republic'
    subbasin = 'Yaque del Sur'
    comids = ['21838', '21834', '21835']

    forecastinfo = getforecastflows(watershed,subbasin,comids)
    data = gethistoricaldata('Hatillo')

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Hatillo',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': data
        }],
        y_min = 40
    )


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastinfo['timestep'][0], forecastinfo['timestep'][1], forecastinfo['timestep'][2], forecastinfo['timestep'][3], forecastinfo['timestep'][4], forecastinfo['timestep'][5], forecastinfo['timestep'][6]),
                           rows=[('Caudal de Entrada (Total)',forecastinfo['total'][0], forecastinfo['total'][1], forecastinfo['total'][2],forecastinfo['total'][3],forecastinfo['total'][4],forecastinfo['total'][5],forecastinfo['total'][6]),
                                 ('Caudal de Entrada (21838)', forecastinfo['21838'][0], forecastinfo['21838'][1], forecastinfo['21838'][2], forecastinfo['21838'][3],
                                  forecastinfo['21838'][4], forecastinfo['21838'][5], forecastinfo['21838'][6]),
                                 ('Caudal de Entrada (21835)', forecastinfo['21835'][0], forecastinfo['21835'][1], forecastinfo['21835'][2], forecastinfo['21835'][3],
                                  forecastinfo['21835'][4], forecastinfo['21835'][5], forecastinfo['21835'][6]),
                                 ('Caudal de Entrada (21834)', forecastinfo['21834'][0], forecastinfo['21834'][1], forecastinfo['21834'][2], forecastinfo['21834'][3],
                                  forecastinfo['21834'][4], forecastinfo['21834'][5], forecastinfo['21834'][6]),
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

    watershed = 'Dominican Republic'
    subbasin = 'Yaque del Sur'
    comids = ['21838', '21834', '21835']

    forecastinfo = getforecastflows(watershed,subbasin,comids)
    data = gethistoricaldata('Maguaca')

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Maguaca',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': data
        }],
        y_min = 0
    )

    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastinfo['timestep'][0], forecastinfo['timestep'][1], forecastinfo['timestep'][2], forecastinfo['timestep'][3], forecastinfo['timestep'][4], forecastinfo['timestep'][5], forecastinfo['timestep'][6]),
                           rows=[('Caudal de Entrada (Total)',forecastinfo['total'][0], forecastinfo['total'][1], forecastinfo['total'][2],forecastinfo['total'][3],forecastinfo['total'][4],forecastinfo['total'][5],forecastinfo['total'][6]),
                                 ('Caudal de Entrada (21838)', forecastinfo['21838'][0], forecastinfo['21838'][1], forecastinfo['21838'][2], forecastinfo['21838'][3],
                                  forecastinfo['21838'][4], forecastinfo['21838'][5], forecastinfo['21838'][6]),
                                 ('Caudal de Entrada (21835)', forecastinfo['21835'][0], forecastinfo['21835'][1], forecastinfo['21835'][2], forecastinfo['21835'][3],
                                  forecastinfo['21835'][4], forecastinfo['21835'][5], forecastinfo['21835'][6]),
                                 ('Caudal de Entrada (21834)', forecastinfo['21834'][0], forecastinfo['21834'][1], forecastinfo['21834'][2], forecastinfo['21834'][3],
                                  forecastinfo['21834'][4], forecastinfo['21834'][5], forecastinfo['21834'][6]),
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

    watershed = 'Dominican Republic'
    subbasin = 'Yaque del Sur'
    comids = ['21838', '21834', '21835']

    forecastinfo = getforecastflows(watershed,subbasin,comids)
    data = gethistoricaldata('Chacuey')

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Chacuey',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': data
        }],
        y_min = 0
    )

    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastinfo['timestep'][0], forecastinfo['timestep'][1], forecastinfo['timestep'][2], forecastinfo['timestep'][3], forecastinfo['timestep'][4], forecastinfo['timestep'][5], forecastinfo['timestep'][6]),
                           rows=[('Caudal de Entrada (Total)',forecastinfo['total'][0], forecastinfo['total'][1], forecastinfo['total'][2],forecastinfo['total'][3],forecastinfo['total'][4],forecastinfo['total'][5],forecastinfo['total'][6]),
                                 ('Caudal de Entrada (21838)', forecastinfo['21838'][0], forecastinfo['21838'][1], forecastinfo['21838'][2], forecastinfo['21838'][3],
                                  forecastinfo['21838'][4], forecastinfo['21838'][5], forecastinfo['21838'][6]),
                                 ('Caudal de Entrada (21835)', forecastinfo['21835'][0], forecastinfo['21835'][1], forecastinfo['21835'][2], forecastinfo['21835'][3],
                                  forecastinfo['21835'][4], forecastinfo['21835'][5], forecastinfo['21835'][6]),
                                 ('Caudal de Entrada (21834)', forecastinfo['21834'][0], forecastinfo['21834'][1], forecastinfo['21834'][2], forecastinfo['21834'][3],
                                  forecastinfo['21834'][4], forecastinfo['21834'][5], forecastinfo['21834'][6]),
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

    watershed = 'Dominican Republic'
    subbasin = 'Yaque del Sur'
    comids = ['21838', '21834', '21835']

    forecastinfo = getforecastflows(watershed,subbasin,comids)
    data = gethistoricaldata('Jiguey')

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Jiguey',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': data
        }],
        y_min = 300
    )

    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastinfo['timestep'][0], forecastinfo['timestep'][1], forecastinfo['timestep'][2], forecastinfo['timestep'][3], forecastinfo['timestep'][4], forecastinfo['timestep'][5], forecastinfo['timestep'][6]),
                           rows=[('Caudal de Entrada (Total)',forecastinfo['total'][0], forecastinfo['total'][1], forecastinfo['total'][2],forecastinfo['total'][3],forecastinfo['total'][4],forecastinfo['total'][5],forecastinfo['total'][6]),
                                 ('Caudal de Entrada (21838)', forecastinfo['21838'][0], forecastinfo['21838'][1], forecastinfo['21838'][2], forecastinfo['21838'][3],
                                  forecastinfo['21838'][4], forecastinfo['21838'][5], forecastinfo['21838'][6]),
                                 ('Caudal de Entrada (21835)', forecastinfo['21835'][0], forecastinfo['21835'][1], forecastinfo['21835'][2], forecastinfo['21835'][3],
                                  forecastinfo['21835'][4], forecastinfo['21835'][5], forecastinfo['21835'][6]),
                                 ('Caudal de Entrada (21834)', forecastinfo['21834'][0], forecastinfo['21834'][1], forecastinfo['21834'][2], forecastinfo['21834'][3],
                                  forecastinfo['21834'][4], forecastinfo['21834'][5], forecastinfo['21834'][6]),
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

    watershed = 'Dominican Republic'
    subbasin = 'Yaque del Sur'
    comids = ['21838', '21834', '21835']

    forecastinfo = getforecastflows(watershed,subbasin,comids)
    data = gethistoricaldata('Moncion')

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Moncion',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': data
        }],
        y_min = 100
    )

    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastinfo['timestep'][0], forecastinfo['timestep'][1], forecastinfo['timestep'][2], forecastinfo['timestep'][3], forecastinfo['timestep'][4], forecastinfo['timestep'][5], forecastinfo['timestep'][6]),
                           rows=[('Caudal de Entrada (Total)',forecastinfo['total'][0], forecastinfo['total'][1], forecastinfo['total'][2],forecastinfo['total'][3],forecastinfo['total'][4],forecastinfo['total'][5],forecastinfo['total'][6]),
                                 ('Caudal de Entrada (21838)', forecastinfo['21838'][0], forecastinfo['21838'][1], forecastinfo['21838'][2], forecastinfo['21838'][3],
                                  forecastinfo['21838'][4], forecastinfo['21838'][5], forecastinfo['21838'][6]),
                                 ('Caudal de Entrada (21835)', forecastinfo['21835'][0], forecastinfo['21835'][1], forecastinfo['21835'][2], forecastinfo['21835'][3],
                                  forecastinfo['21835'][4], forecastinfo['21835'][5], forecastinfo['21835'][6]),
                                 ('Caudal de Entrada (21834)', forecastinfo['21834'][0], forecastinfo['21834'][1], forecastinfo['21834'][2], forecastinfo['21834'][3],
                                  forecastinfo['21834'][4], forecastinfo['21834'][5], forecastinfo['21834'][6]),
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

    watershed = 'Dominican Republic'
    subbasin = 'Yaque del Sur'
    comids = ['21838', '21834', '21835']

    forecastinfo = getforecastflows(watershed,subbasin,comids)
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
                                 ('Caudal de Entrada (21838)', forecastinfo['21838'][0], forecastinfo['21838'][1], forecastinfo['21838'][2], forecastinfo['21838'][3],
                                  forecastinfo['21838'][4], forecastinfo['21838'][5], forecastinfo['21838'][6]),
                                 ('Caudal de Entrada (21835)', forecastinfo['21835'][0], forecastinfo['21835'][1], forecastinfo['21835'][2], forecastinfo['21835'][3],
                                  forecastinfo['21835'][4], forecastinfo['21835'][5], forecastinfo['21835'][6]),
                                 ('Caudal de Entrada (21834)', forecastinfo['21834'][0], forecastinfo['21834'][1], forecastinfo['21834'][2], forecastinfo['21834'][3],
                                  forecastinfo['21834'][4], forecastinfo['21834'][5], forecastinfo['21834'][6]),
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

    watershed = 'Dominican Republic'
    subbasin = 'Yaque del Sur'
    comids = ['21838', '21834', '21835']

    forecastinfo = getforecastflows(watershed,subbasin,comids)
    data = gethistoricaldata('Rincon')

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Rincon',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': data
        }],
        y_min = 100
    )

    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastinfo['timestep'][0], forecastinfo['timestep'][1], forecastinfo['timestep'][2], forecastinfo['timestep'][3], forecastinfo['timestep'][4], forecastinfo['timestep'][5], forecastinfo['timestep'][6]),
                           rows=[('Caudal de Entrada (Total)',forecastinfo['total'][0], forecastinfo['total'][1], forecastinfo['total'][2],forecastinfo['total'][3],forecastinfo['total'][4],forecastinfo['total'][5],forecastinfo['total'][6]),
                                 ('Caudal de Entrada (21838)', forecastinfo['21838'][0], forecastinfo['21838'][1], forecastinfo['21838'][2], forecastinfo['21838'][3],
                                  forecastinfo['21838'][4], forecastinfo['21838'][5], forecastinfo['21838'][6]),
                                 ('Caudal de Entrada (21835)', forecastinfo['21835'][0], forecastinfo['21835'][1], forecastinfo['21835'][2], forecastinfo['21835'][3],
                                  forecastinfo['21835'][4], forecastinfo['21835'][5], forecastinfo['21835'][6]),
                                 ('Caudal de Entrada (21834)', forecastinfo['21834'][0], forecastinfo['21834'][1], forecastinfo['21834'][2], forecastinfo['21834'][3],
                                  forecastinfo['21834'][4], forecastinfo['21834'][5], forecastinfo['21834'][6]),
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

    watershed = 'Dominican Republic'
    subbasin = 'Yaque del Sur'
    comids = ['21838', '21834', '21835']

    forecastinfo = getforecastflows(watershed,subbasin,comids)
    data = gethistoricaldata('Sabaneta')

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Sabaneta',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': data
        }],
        y_min = 300
    )

    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastinfo['timestep'][0], forecastinfo['timestep'][1], forecastinfo['timestep'][2], forecastinfo['timestep'][3], forecastinfo['timestep'][4], forecastinfo['timestep'][5], forecastinfo['timestep'][6]),
                           rows=[('Caudal de Entrada (Total)',forecastinfo['total'][0], forecastinfo['total'][1], forecastinfo['total'][2],forecastinfo['total'][3],forecastinfo['total'][4],forecastinfo['total'][5],forecastinfo['total'][6]),
                                 ('Caudal de Entrada (21838)', forecastinfo['21838'][0], forecastinfo['21838'][1], forecastinfo['21838'][2], forecastinfo['21838'][3],
                                  forecastinfo['21838'][4], forecastinfo['21838'][5], forecastinfo['21838'][6]),
                                 ('Caudal de Entrada (21835)', forecastinfo['21835'][0], forecastinfo['21835'][1], forecastinfo['21835'][2], forecastinfo['21835'][3],
                                  forecastinfo['21835'][4], forecastinfo['21835'][5], forecastinfo['21835'][6]),
                                 ('Caudal de Entrada (21834)', forecastinfo['21834'][0], forecastinfo['21834'][1], forecastinfo['21834'][2], forecastinfo['21834'][3],
                                  forecastinfo['21834'][4], forecastinfo['21834'][5], forecastinfo['21834'][6]),
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

    watershed = 'Dominican Republic'
    subbasin = 'Yaque del Sur'
    comids = ['21838', '21834', '21835']

    forecastinfo = getforecastflows(watershed,subbasin,comids)
    data = gethistoricaldata('Bao')

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Tavera-Bao',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': data
        }],
        y_min = 300
    )

    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastinfo['timestep'][0], forecastinfo['timestep'][1], forecastinfo['timestep'][2], forecastinfo['timestep'][3], forecastinfo['timestep'][4], forecastinfo['timestep'][5], forecastinfo['timestep'][6]),
                           rows=[('Caudal de Entrada (Total)',forecastinfo['total'][0], forecastinfo['total'][1], forecastinfo['total'][2],forecastinfo['total'][3],forecastinfo['total'][4],forecastinfo['total'][5],forecastinfo['total'][6]),
                                 ('Caudal de Entrada (21838)', forecastinfo['21838'][0], forecastinfo['21838'][1], forecastinfo['21838'][2], forecastinfo['21838'][3],
                                  forecastinfo['21838'][4], forecastinfo['21838'][5], forecastinfo['21838'][6]),
                                 ('Caudal de Entrada (21835)', forecastinfo['21835'][0], forecastinfo['21835'][1], forecastinfo['21835'][2], forecastinfo['21835'][3],
                                  forecastinfo['21835'][4], forecastinfo['21835'][5], forecastinfo['21835'][6]),
                                 ('Caudal de Entrada (21834)', forecastinfo['21834'][0], forecastinfo['21834'][1], forecastinfo['21834'][2], forecastinfo['21834'][3],
                                  forecastinfo['21834'][4], forecastinfo['21834'][5], forecastinfo['21834'][6]),
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

    watershed = 'Dominican Republic'
    subbasin = 'Yaque del Sur'
    comids = ['21838', '21834', '21835']

    forecastinfo = getforecastflows(watershed,subbasin,comids)
    data = gethistoricaldata('Valdesia')

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Valdesia',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': data
        }],
        y_min = 120
    )

    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecastinfo['timestep'][0], forecastinfo['timestep'][1], forecastinfo['timestep'][2], forecastinfo['timestep'][3], forecastinfo['timestep'][4], forecastinfo['timestep'][5], forecastinfo['timestep'][6]),
                           rows=[('Caudal de Entrada (Total)',forecastinfo['total'][0], forecastinfo['total'][1], forecastinfo['total'][2],forecastinfo['total'][3],forecastinfo['total'][4],forecastinfo['total'][5],forecastinfo['total'][6]),
                                 ('Caudal de Entrada (21838)', forecastinfo['21838'][0], forecastinfo['21838'][1], forecastinfo['21838'][2], forecastinfo['21838'][3],
                                  forecastinfo['21838'][4], forecastinfo['21838'][5], forecastinfo['21838'][6]),
                                 ('Caudal de Entrada (21835)', forecastinfo['21835'][0], forecastinfo['21835'][1], forecastinfo['21835'][2], forecastinfo['21835'][3],
                                  forecastinfo['21835'][4], forecastinfo['21835'][5], forecastinfo['21835'][6]),
                                 ('Caudal de Entrada (21834)', forecastinfo['21834'][0], forecastinfo['21834'][1], forecastinfo['21834'][2], forecastinfo['21834'][3],
                                  forecastinfo['21834'][4], forecastinfo['21834'][5], forecastinfo['21834'][6]),
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
