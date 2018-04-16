#This is the main python script where your html content is created. search for tethys gizmos online for more information on gizmos
#Each page has its own function and code that is run for that specific page. Each html page needs its own function

from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import *
import datetime
from model import getforecastflows, gethistoricaldata, getrecentdata, forecastdata, forecastlevels


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

    forecasteddata = forecastdata(comids, 'Sabana_Yegua', 3)
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

    table_view = TableView(column_names=('Caudales/Niveles',forecasteddata['dates'][0], forecasteddata['dates'][1],
                                         forecasteddata['dates'][2], forecasteddata['dates'][3], forecasteddata['dates'][4],
                                         forecasteddata['dates'][5], forecasteddata['dates'][6]),
                           rows=[('Caudal de Entrada (Total)',forecasteddata['total'][0], forecasteddata['total'][1],
                                  forecasteddata['total'][2],forecasteddata['total'][3],forecasteddata['total'][4],
                                  forecasteddata['total'][5],forecasteddata['total'][6]),
                                 ('Caudal de Entrada (593)', forecasteddata['593'][0], forecasteddata['593'][1],
                                  forecasteddata['593'][2], forecasteddata['593'][3], forecasteddata['593'][4],
                                  forecasteddata['593'][5], forecasteddata['593'][6]),
                                 ('Caudal de Entrada (600)', forecasteddata['600'][0], forecasteddata['600'][1],
                                  forecasteddata['600'][2], forecasteddata['600'][3],forecasteddata['600'][4],
                                  forecasteddata['600'][5], forecasteddata['600'][6]),
                                 ('Caudal de Entrada (599)', forecasteddata['599'][0], forecasteddata['599'][1],
                                  forecasteddata['599'][2], forecasteddata['599'][3], forecasteddata['599'][4],
                                  forecasteddata['599'][5], forecasteddata['599'][6]),
                                 ('Niveles Prognosticos',forecasteddata['levels'][0], forecasteddata['levels'][1],
                                  forecasteddata['levels'][2], forecasteddata['levels'][3],forecasteddata['levels'][4],
                                  forecasteddata['levels'][5],forecasteddata['levels'][6])],
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
    #       'historic_plot': historic_plot,

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

    forecasteddata = forecastdata(comids, 'Hatillo', .3)
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
        y_min = 35
    )


    #This creates the table
    table_view = TableView(column_names=('Caudales/Niveles',forecasteddata['dates'][0], forecasteddata['dates'][1],
                                         forecasteddata['dates'][2], forecasteddata['dates'][3], forecasteddata['dates'][4],
                                         forecasteddata['dates'][5], forecasteddata['dates'][6]),
                           rows=[('Caudal de Entrada (Total)',forecasteddata['total'][0], forecasteddata['total'][1],
                                  forecasteddata['total'][2],forecasteddata['total'][3],forecasteddata['total'][4],
                                  forecasteddata['total'][5],forecasteddata['total'][6]),
                                 ('Caudal de Entrada (834)', forecasteddata['834'][0], forecasteddata['834'][1],
                                  forecasteddata['834'][2], forecasteddata['834'][3], forecasteddata['834'][4],
                                  forecasteddata['834'][5], forecasteddata['834'][6]),
                                 ('Caudal de Entrada (813)', forecasteddata['813'][0], forecasteddata['813'][1],
                                  forecasteddata['813'][2], forecasteddata['813'][3],forecasteddata['813'][4],
                                  forecasteddata['813'][5], forecasteddata['813'][6]),
                                 ('Caudal de Entrada (849)', forecasteddata['849'][0], forecasteddata['849'][1],
                                  forecasteddata['849'][2], forecasteddata['849'][3], forecasteddata['849'][4],
                                  forecasteddata['849'][5], forecasteddata['849'][6]),
                                 ('Caudal de Entrada (857)', forecasteddata['857'][0], forecasteddata['857'][1],
                                  forecasteddata['857'][2], forecasteddata['857'][3], forecasteddata['857'][4],
                                  forecasteddata['857'][5], forecasteddata['857'][6]),
                                 ('Niveles Prognosticos',forecasteddata['levels'][0], forecasteddata['levels'][1],
                                  forecasteddata['levels'][2], forecasteddata['levels'][3],forecasteddata['levels'][4],
                                  forecasteddata['levels'][5],forecasteddata['levels'][6])],
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
    #       'historic_plot': historic_plot,

    return render(request, 'reservoir_management/hatillo.html', context)

@login_required()
def maguaca(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['1399']

    forecasteddata = forecastdata(comids, 'Maguaca', .1)
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
    table_view = TableView(column_names=('Caudales/Niveles',forecasteddata['dates'][0], forecasteddata['dates'][1],
                                         forecasteddata['dates'][2], forecasteddata['dates'][3], forecasteddata['dates'][4],
                                         forecasteddata['dates'][5], forecasteddata['dates'][6]),
                           rows=[('Caudal de Entrada (Total)',forecasteddata['total'][0], forecasteddata['total'][1],
                                  forecasteddata['total'][2],forecasteddata['total'][3],forecasteddata['total'][4],
                                  forecasteddata['total'][5],forecasteddata['total'][6]),
                                 ('Caudal de Entrada (1399)', forecasteddata['1399'][0], forecasteddata['1399'][1],
                                  forecasteddata['1399'][2], forecasteddata['1399'][3], forecasteddata['1399'][4],
                                  forecasteddata['1399'][5], forecasteddata['1399'][6]),
                                 ('Niveles Prognosticos',forecasteddata['levels'][0], forecasteddata['levels'][1],
                                  forecasteddata['levels'][2], forecasteddata['levels'][3],forecasteddata['levels'][4],
                                  forecasteddata['levels'][5],forecasteddata['levels'][6])],
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
    #       'historic_plot': historic_plot,

    return render(request, 'reservoir_management/maguaca.html', context)

@login_required()
def chacuey(request):
    """
    Controller for the Add Dam page.
    """

    comids = ['1396']

    forecasteddata = forecastdata(comids, 'Chacuey', .1)
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
    table_view = TableView(column_names=('Caudales/Niveles',forecasteddata['dates'][0], forecasteddata['dates'][1],
                                         forecasteddata['dates'][2], forecasteddata['dates'][3], forecasteddata['dates'][4],
                                         forecasteddata['dates'][5], forecasteddata['dates'][6]),
                           rows=[('Caudal de Entrada (Total)',forecasteddata['total'][0], forecasteddata['total'][1],
                                  forecasteddata['total'][2],forecasteddata['total'][3],forecasteddata['total'][4],
                                  forecasteddata['total'][5],forecasteddata['total'][6]),
                                 ('Caudal de Entrada (1396)', forecasteddata['1396'][0], forecasteddata['1396'][1],
                                  forecasteddata['1396'][2], forecasteddata['1396'][3], forecasteddata['1396'][4],
                                  forecasteddata['1396'][5], forecasteddata['1396'][6]),
                                 ('Niveles Prognosticos',forecasteddata['levels'][0], forecasteddata['levels'][1],
                                  forecasteddata['levels'][2], forecasteddata['levels'][3],forecasteddata['levels'][4],
                                  forecasteddata['levels'][5],forecasteddata['levels'][6])],
                           hover=True,
                           striped=True,
                           bordered=True,
                           condensed=False)

    outflow_edit = TableView(column_names=('Dia', 'Caudal de Salida (cms)', 'Tiempo de salida (horas)'),
                             rows=[(forecasteddata['dates'][0], '0','0'),
                                   (forecasteddata['dates'][1], '0','0'),
                                   (forecasteddata['dates'][2], '0','0'),
                                   (forecasteddata['dates'][3], '0','0'),
                                   (forecasteddata['dates'][4], '0','0'),
                                   (forecasteddata['dates'][5], '0', '0'),
                                   (forecasteddata['dates'][6], '0', '0'),
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
        'table_view': table_view,
        'outflow_button':outflow_button,
        'calculate': calculate,
        'outflow_edit': outflow_edit,
    }
 #       'historic_plot': historic_plot,


    return render(request, 'reservoir_management/chacuey.html', context)

@login_required()
def jiguey(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['475', '496']

    forecasteddata = forecastdata(comids, 'Jiguey', 3)
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
    table_view = TableView(column_names=('Caudales/Niveles',forecasteddata['dates'][0], forecasteddata['dates'][1],
                                         forecasteddata['dates'][2], forecasteddata['dates'][3], forecasteddata['dates'][4],
                                         forecasteddata['dates'][5], forecasteddata['dates'][6]),
                           rows=[('Caudal de Entrada (Total)',forecasteddata['total'][0], forecasteddata['total'][1],
                                  forecasteddata['total'][2],forecasteddata['total'][3],forecasteddata['total'][4],
                                  forecasteddata['total'][5],forecasteddata['total'][6]),
                                 ('Caudal de Entrada (475)', forecasteddata['475'][0], forecasteddata['475'][1],
                                  forecasteddata['475'][2], forecasteddata['475'][3], forecasteddata['475'][4],
                                  forecasteddata['475'][5], forecasteddata['475'][6]),
                                 ('Caudal de Entrada (496)', forecasteddata['496'][0], forecasteddata['496'][1],
                                  forecasteddata['496'][2], forecasteddata['496'][3],forecasteddata['496'][4],
                                  forecasteddata['496'][5], forecasteddata['496'][6]),
                                 ('Niveles Prognosticos',forecasteddata['levels'][0], forecasteddata['levels'][1],
                                  forecasteddata['levels'][2], forecasteddata['levels'][3],forecasteddata['levels'][4],
                                  forecasteddata['levels'][5],forecasteddata['levels'][6])],
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
    #       'historic_plot': historic_plot,

    return render(request, 'reservoir_management/jiguey.html', context)

@login_required()
def moncion(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['1148', '1182']

    observeddata = gethistoricaldata('Moncion')
    forecasteddata = forecastdata(comids,'Moncion', 1)

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Moncion',
        y_axis_title='Niveles de agua',
        y_axis_units='m',
        series=[{
            'name': 'Historico',
            'data': observeddata
        }],
        y_min = 100
    )


    table_view = TableView(column_names=('Caudales/Niveles',forecasteddata['dates'][0], forecasteddata['dates'][1],
                                         forecasteddata['dates'][2], forecasteddata['dates'][3], forecasteddata['dates'][4],
                                         forecasteddata['dates'][5], forecasteddata['dates'][6]),
                           rows=[('Caudal de Entrada (Total)',forecasteddata['total'][0], forecasteddata['total'][1],
                                  forecasteddata['total'][2],forecasteddata['total'][3],forecasteddata['total'][4],
                                  forecasteddata['total'][5],forecasteddata['total'][6]),
                                 ('Caudal de Entrada (1148)', forecasteddata['1148'][0], forecasteddata['1148'][1],
                                  forecasteddata['1148'][2], forecasteddata['1148'][3], forecasteddata['1148'][4],
                                  forecasteddata['1148'][5], forecasteddata['1148'][6]),
                                 ('Caudal de Entrada (1182)', forecasteddata['1182'][0], forecasteddata['1182'][1],
                                  forecasteddata['1182'][2], forecasteddata['1182'][3],forecasteddata['1182'][4],
                                  forecasteddata['1182'][5], forecasteddata['1182'][6]),
                                 ('Niveles Prognosticos',forecasteddata['levels'][0], forecasteddata['levels'][1],
                                  forecasteddata['levels'][2], forecasteddata['levels'][3],forecasteddata['levels'][4],
                                  forecasteddata['levels'][5],forecasteddata['levels'][6])],
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
    #       'historic_plot': historic_plot,

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
    #       'historic_plot': historic_plot,

    return render(request, 'reservoir_management/pinalito.html', context)

@login_required()
def rincon(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['853', '922']

    forecasteddata = forecastdata(comids, 'Rincon', 1)
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
    table_view = TableView(column_names=('Caudales/Niveles',forecasteddata['dates'][0], forecasteddata['dates'][1],
                                         forecasteddata['dates'][2], forecasteddata['dates'][3], forecasteddata['dates'][4],
                                         forecasteddata['dates'][5], forecasteddata['dates'][6]),
                           rows=[('Caudal de Entrada (Total)',forecasteddata['total'][0], forecasteddata['total'][1],
                                  forecasteddata['total'][2],forecasteddata['total'][3],forecasteddata['total'][4],
                                  forecasteddata['total'][5],forecasteddata['total'][6]),
                                 ('Caudal de Entrada (853)', forecasteddata['853'][0], forecasteddata['853'][1],
                                  forecasteddata['853'][2], forecasteddata['853'][3], forecasteddata['853'][4],
                                  forecasteddata['853'][5], forecasteddata['853'][6]),
                                 ('Caudal de Entrada (922)', forecasteddata['922'][0], forecasteddata['922'][1],
                                  forecasteddata['922'][2], forecasteddata['922'][3],forecasteddata['922'][4],
                                  forecasteddata['922'][5], forecasteddata['922'][6]),
                                 ('Niveles Prognosticos',forecasteddata['levels'][0], forecasteddata['levels'][1],
                                  forecasteddata['levels'][2], forecasteddata['levels'][3],forecasteddata['levels'][4],
                                  forecasteddata['levels'][5],forecasteddata['levels'][6])],
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
    #       'historic_plot': historic_plot,

    return render(request, 'reservoir_management/rincon.html', context)

@login_required()
def sabaneta(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['863', '862']

    forecasteddata = forecastdata(comids, 'Sabaneta', 5)
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
    table_view = TableView(column_names=('Caudales/Niveles',forecasteddata['dates'][0], forecasteddata['dates'][1],
                                         forecasteddata['dates'][2], forecasteddata['dates'][3], forecasteddata['dates'][4],
                                         forecasteddata['dates'][5], forecasteddata['dates'][6]),
                           rows=[('Caudal de Entrada (Total)',forecasteddata['total'][0], forecasteddata['total'][1],
                                  forecasteddata['total'][2],forecasteddata['total'][3],forecasteddata['total'][4],
                                  forecasteddata['total'][5],forecasteddata['total'][6]),
                                 ('Caudal de Entrada (863)', forecasteddata['863'][0], forecasteddata['863'][1],
                                  forecasteddata['863'][2], forecasteddata['863'][3], forecasteddata['863'][4],
                                  forecasteddata['863'][5], forecasteddata['863'][6]),
                                 ('Caudal de Entrada (862)', forecasteddata['862'][0], forecasteddata['862'][1],
                                  forecasteddata['862'][2], forecasteddata['862'][3],forecasteddata['862'][4],
                                  forecasteddata['862'][5], forecasteddata['862'][6]),
                                 ('Niveles Prognosticos',forecasteddata['levels'][0], forecasteddata['levels'][1],
                                  forecasteddata['levels'][2], forecasteddata['levels'][3],forecasteddata['levels'][4],
                                  forecasteddata['levels'][5],forecasteddata['levels'][6])],
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
    #       'historic_plot': historic_plot,

    return render(request, 'reservoir_management/sabaneta.html', context)

@login_required()
def tavera_bao(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['1024', '1140', '1142', '1153']

    forecasteddata = forecastdata(comids, 'Tavera', 3)
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
    table_view = TableView(column_names=('Caudales/Niveles',forecasteddata['dates'][0], forecasteddata['dates'][1],
                                         forecasteddata['dates'][2], forecasteddata['dates'][3], forecasteddata['dates'][4],
                                         forecasteddata['dates'][5], forecasteddata['dates'][6]),
                           rows=[('Caudal de Entrada (Total)',forecasteddata['total'][0], forecasteddata['total'][1],
                                  forecasteddata['total'][2],forecasteddata['total'][3],forecasteddata['total'][4],
                                  forecasteddata['total'][5],forecasteddata['total'][6]),
                                 ('Caudal de Entrada (1024)', forecasteddata['1024'][0], forecasteddata['1024'][1],
                                  forecasteddata['1024'][2], forecasteddata['1024'][3], forecasteddata['1024'][4],
                                  forecasteddata['1024'][5], forecasteddata['1024'][6]),
                                 ('Caudal de Entrada (1140)', forecasteddata['1140'][0], forecasteddata['1140'][1],
                                  forecasteddata['1140'][2], forecasteddata['1140'][3],forecasteddata['1140'][4],
                                  forecasteddata['1140'][5], forecasteddata['1140'][6]),
                                 ('Caudal de Entrada (1142)', forecasteddata['1142'][0], forecasteddata['1142'][1],
                                  forecasteddata['1142'][2], forecasteddata['1142'][3], forecasteddata['1142'][4],
                                  forecasteddata['1142'][5], forecasteddata['1142'][6]),
                                 ('Caudal de Entrada (1153)', forecasteddata['1153'][0], forecasteddata['1153'][1],
                                  forecasteddata['1153'][2], forecasteddata['1153'][3], forecasteddata['1153'][4],
                                  forecasteddata['1153'][5], forecasteddata['1153'][6]),
                                 ('Niveles Prognosticos',forecasteddata['levels'][0], forecasteddata['levels'][1],
                                  forecasteddata['levels'][2], forecasteddata['levels'][3],forecasteddata['levels'][4],
                                  forecasteddata['levels'][5],forecasteddata['levels'][6])],
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
    #       'historic_plot': historic_plot,

    return render(request, 'reservoir_management/tavera_bao.html', context)

@login_required()
def valdesia(request):
    """
    Controller for the Add Dam page.
    """
    comids = ['159']

    forecasteddata = forecastdata(comids, 'Valdesia', 1)
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
    table_view = TableView(column_names=('Caudales/Niveles',forecasteddata['dates'][0], forecasteddata['dates'][1],
                                         forecasteddata['dates'][2], forecasteddata['dates'][3], forecasteddata['dates'][4],
                                         forecasteddata['dates'][5], forecasteddata['dates'][6]),
                           rows=[('Caudal de Entrada (Total)',forecasteddata['total'][0], forecasteddata['total'][1],
                                  forecasteddata['total'][2],forecasteddata['total'][3],forecasteddata['total'][4],
                                  forecasteddata['total'][5],forecasteddata['total'][6]),
                                 ('Caudal de Entrada (159)', forecasteddata['159'][0], forecasteddata['159'][1],
                                  forecasteddata['159'][2], forecasteddata['159'][3], forecasteddata['159'][4],
                                  forecasteddata['159'][5], forecasteddata['159'][6]),
                                 ('Niveles Prognosticos',forecasteddata['levels'][0], forecasteddata['levels'][1],
                                  forecasteddata['levels'][2], forecasteddata['levels'][3],forecasteddata['levels'][4],
                                  forecasteddata['levels'][5],forecasteddata['levels'][6])],
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
    #       'historic_plot': historic_plot,

    return render(request, 'reservoir_management/valdesia.html', context)
