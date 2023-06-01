import os
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pandas import read_csv

@csrf_exempt
@login_required
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file.name.endswith('.csv'):
            filename = file.name
            with open(filename, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return JsonResponse({'message': 'Файл загружен успешно!'})
        else:
            return JsonResponse({'error': 'Неверный формат файла!'})

def get_files(request):
    files = [f for f in os.listdir('.') if f.endswith('.csv')]
    return JsonResponse({'files': files})

def get_data(request, filename):
    if not os.path.exists(filename):
        return JsonResponse({'error': 'Файл не найден!'})
    df = read_csv(filename)
    filters = request.GET.get('filters')
    if filters:
        filters = filters.split(',')
        for f in filters:
            column, value = f.split(':')
            df = df[df[column] == value]
    sort_by = request.GET.get('sort_by')
    if sort_by:
        sort_by = sort_by.split(',')
        df = df.sort_values(by=sort_by)
    return JsonResponse(df.to_dict(orient='records'), safe=False)

@login_required
def delete_file(request, filename):
    if os.path.exists(filename):
        os.remove(filename)
        return JsonResponse({'message': 'Файл удален успешно!'})
    else:
        return JsonResponse({'error': 'Файл не найден!'})
    