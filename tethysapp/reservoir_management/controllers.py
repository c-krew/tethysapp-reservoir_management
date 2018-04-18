#This is the main python script where your html content is created. search for tethys gizmos online for more information on gizmos
#Each page has its own function and code that is run for that specific page. Each html page needs its own function

from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import *
import datetime
from model import getforecastflows, gethistoricaldata, getrecentdata, forecastdata, forecastlevels, gettabledates


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

    comids = ['834', '813', '849', '857']

    forecasteddata = gettabledates(comids)
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

    observeddata = gethistoricaldata('Moncion')
    forecasteddata = gettabledates(comids)

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
