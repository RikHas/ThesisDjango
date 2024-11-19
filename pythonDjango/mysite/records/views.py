from django.shortcuts import render, redirect
from .models import Record


# Create your views here.
def record_list(request):
    """
    Функция для отображения списка записей.

    Аргументы:
        request (HttpRequest): Объект запроса от клиента.

    Возвращает:
        HTML-страница с отображением всех записей.
    """
    records = Record.objects.all()
    return render(request, 'records/record_list.html', {'records': records})


def add_record(request):
    """
    Функция для добавления новой записи.

    Аргументы:
        request (HttpRequest): Объект запроса от клиента.

    Возвращает:
        HttpResponse:
            - Если метод POST, перенаправляет на список записей.
            - Если метод GET, возвращает HTML-страницу с формой для добавления записи.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Record.objects.create(title=title, description=description)
        return redirect('record_list')
    return render(request, 'records/add_record.html')


def delete_record(request, record_id):
    """
    Фуекция для удаления записи.

    Аргументы:
        request (HttpRequest): Объект запроса от клиента.
        record_id (int): Идентификатор записи для удаления.

    Возвращает:
        HttpResponse: Перенаправление на список записей после удаления.
    """
    record = Record.objects.get(id=record_id)
    record.delete()
    return redirect('record_list')
