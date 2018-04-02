#This is the main python script where your html content is created. search for tethys gizmos online for more information on gizmos
#Each page has its own function and code that is run for that specific page. Each html page needs its own function

from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import *
import datetime
from model import getforecastflows, gethistoricaldata, getrecentdata


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

    forecastinfo = getforecastflows(comids)
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
                                 ('Caudal de Entrada (593)', forecastinfo['593'][0], forecastinfo['593'][1], forecastinfo['593'][2], forecastinfo['593'][3],
                                  forecastinfo['593'][4], forecastinfo['593'][5], forecastinfo['593'][6]),
                                 ('Caudal de Entrada (600)', forecastinfo['600'][0], forecastinfo['600'][1], forecastinfo['600'][2], forecastinfo['600'][3],
                                  forecastinfo['600'][4], forecastinfo['600'][5], forecastinfo['600'][6]),
                                 ('Caudal de Entrada (599)', forecastinfo['599'][0], forecastinfo['599'][1], forecastinfo['599'][2], forecastinfo['599'][3],
                                  forecastinfo['599'][4], forecastinfo['599'][5], forecastinfo['599'][6]),
                                 ('Caudal de Salida','10', '10', '13','12','12.4','11','13'),
                                 ('Niveles','393', '393.8', '394', '394.1','394','394.4','394.8')],
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
                                        ('Chacuey', 'Chacuey'),
                                        ],
                               initial=[''])

    level_input = TextInput(display_text='Nivel de Agua',
                           name='levelinput',
                           placeholder='i.e. 375',
                           )


    today = datetime.datetime.now()
    year = str(today.year)
    month = str(today.strftime("%B"))
    day = str(today.day)
    date = month + ' ' + day + ', ' + year

    date_input = DatePicker(name='dateinput',
                             display_text='Date',
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


    context = {
        'dam_input': dam_input,
        'level_input':level_input,
        'date_input': date_input,
        'table_view': table_view,
        'message_box': message_box,
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

    comids = ['834', '813', '849', '857']

    forecastinfo = getforecastflows(comids)
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
                                 ('Caudal de Entrada (834)', forecastinfo['834'][0], forecastinfo['834'][1], forecastinfo['834'][2], forecastinfo['834'][3],
                                  forecastinfo['834'][4], forecastinfo['834'][5], forecastinfo['834'][6]),
                                 ('Caudal de Entrada (813)', forecastinfo['813'][0], forecastinfo['813'][1], forecastinfo['813'][2], forecastinfo['813'][3],
                                  forecastinfo['813'][4], forecastinfo['813'][5], forecastinfo['813'][6]),
                                 ('Caudal de Entrada (849)', forecastinfo['849'][0], forecastinfo['849'][1], forecastinfo['849'][2], forecastinfo['849'][3],
                                  forecastinfo['849'][4], forecastinfo['849'][5], forecastinfo['849'][6]),
                                 ('Caudal de Entrada (857)', forecastinfo['857'][0], forecastinfo['857'][1], forecastinfo['857'][2], forecastinfo['857'][3],
                                  forecastinfo['857'][4], forecastinfo['857'][5], forecastinfo['857'][6]),
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
    comids = ['1399']

    forecastinfo = getforecastflows(comids)
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
                                 ('Caudal de Entrada (1399)', forecastinfo['1399'][0], forecastinfo['1399'][1], forecastinfo['1399'][2], forecastinfo['1399'][3],
                                  forecastinfo['1399'][4], forecastinfo['1399'][5], forecastinfo['1399'][6]),
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
    comids = ['1396']

    forecastinfo = getforecastflows(comids)
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
                                 ('Caudal de Entrada (1396)', forecastinfo['1396'][0], forecastinfo['1396'][1], forecastinfo['1396'][2], forecastinfo['1396'][3],
                                  forecastinfo['1396'][4], forecastinfo['1396'][5], forecastinfo['1396'][6]),
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
    comids = ['475', '496']

    forecastinfo = getforecastflows(comids)
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
                                 ('Caudal de Entrada (475)', forecastinfo['475'][0], forecastinfo['475'][1], forecastinfo['475'][2], forecastinfo['475'][3],
                                  forecastinfo['475'][4], forecastinfo['475'][5], forecastinfo['475'][6]),
                                 ('Caudal de Entrada (496)', forecastinfo['496'][0], forecastinfo['496'][1], forecastinfo['496'][2], forecastinfo['496'][3],
                                  forecastinfo['496'][4], forecastinfo['496'][5], forecastinfo['496'][6]),
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
    comids = ['1148', '1182']

    forecastinfo = getforecastflows(comids)
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
                                 ('Caudal de Entrada (1148)', forecastinfo['1148'][0], forecastinfo['1148'][1], forecastinfo['1148'][2], forecastinfo['1148'][3],
                                  forecastinfo['1148'][4], forecastinfo['1148'][5], forecastinfo['1148'][6]),
                                 ('Caudal de Entrada (1182)', forecastinfo['1182'][0], forecastinfo['1182'][1], forecastinfo['1182'][2], forecastinfo['1182'][3],
                                  forecastinfo['1182'][4], forecastinfo['1182'][5], forecastinfo['1182'][6]),
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
    comids = ['853', '922']

    forecastinfo = getforecastflows(comids)
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
                                 ('Caudal de Entrada (853)', forecastinfo['853'][0], forecastinfo['853'][1], forecastinfo['853'][2], forecastinfo['853'][3],
                                  forecastinfo['853'][4], forecastinfo['853'][5], forecastinfo['853'][6]),
                                 ('Caudal de Entrada (922)', forecastinfo['922'][0], forecastinfo['922'][1], forecastinfo['922'][2], forecastinfo['922'][3],
                                  forecastinfo['922'][4], forecastinfo['922'][5], forecastinfo['922'][6]),
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
    comids = ['863', '862']

    forecastinfo = getforecastflows(comids)
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
                                 ('Caudal de Entrada (863)', forecastinfo['863'][0], forecastinfo['863'][1], forecastinfo['863'][2], forecastinfo['863'][3],
                                  forecastinfo['863'][4], forecastinfo['863'][5], forecastinfo['863'][6]),
                                 ('Caudal de Entrada (862)', forecastinfo['862'][0], forecastinfo['862'][1], forecastinfo['862'][2], forecastinfo['862'][3],
                                  forecastinfo['862'][4], forecastinfo['862'][5], forecastinfo['862'][6]),
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
    comids = ['1024', '1140', '1142', '1153']

    forecastinfo = getforecastflows(comids)
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
                                 ('Caudal de Entrada (1024)', forecastinfo['1024'][0], forecastinfo['1024'][1], forecastinfo['1024'][2], forecastinfo['1024'][3],
                                  forecastinfo['1024'][4], forecastinfo['1024'][5], forecastinfo['1024'][6]),
                                 ('Caudal de Entrada (1140)', forecastinfo['1140'][0], forecastinfo['1140'][1], forecastinfo['1140'][2], forecastinfo['1140'][3],
                                  forecastinfo['1140'][4], forecastinfo['1140'][5], forecastinfo['1140'][6]),
                                 ('Caudal de Entrada (1142)', forecastinfo['1142'][0], forecastinfo['1142'][1], forecastinfo['1142'][2], forecastinfo['1142'][3],
                                  forecastinfo['1142'][4], forecastinfo['1142'][5], forecastinfo['1142'][6]),
                                 ('Caudal de Entrada (1153)', forecastinfo['1153'][0], forecastinfo['1153'][1], forecastinfo['1153'][2], forecastinfo['1153'][3],
                                  forecastinfo['1153'][4], forecastinfo['1153'][5], forecastinfo['1153'][6]),
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
    comids = ['159']

    forecastinfo = getforecastflows(comids)
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
                                 ('Caudal de Entrada (159)', forecastinfo['159'][0], forecastinfo['159'][1], forecastinfo['159'][2], forecastinfo['159'][3],
                                  forecastinfo['159'][4], forecastinfo['159'][5], forecastinfo['159'][6]),
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
