from django.http import JsonResponse, Http404, HttpResponse
from .app import ReservoirManagement as app
import datetime as dt
import pandas as pd
import os

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
        writer = pd.ExcelWriter(filenew, engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer, index=False, sheet_name='Sheet1')

        # Get the xlsxwriter workbook and worksheet objects.
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

    return JsonResponse(return_obj)
