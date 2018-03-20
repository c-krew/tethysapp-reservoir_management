from django.http import JsonResponse, Http404, HttpResponse


def append_res_info(request):
    return_obj = {
        'success': True
    }

    # Check if its an ajax post request
    if request.is_ajax() and request.method == 'GET':
        dam = request.GET.get('dam')
        level = request.GET.get('level')
        date = request.GET.get('date')

        print(date)



    return JsonResponse(return_obj)