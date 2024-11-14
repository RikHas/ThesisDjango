from django.shortcuts import render, redirect
from .models import Record


# Create your views here.
def record_list(request):
    records = Record.objects.all()
    return render(request, 'records/record_list.html', {'records': records})


def add_record(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Record.objects.create(title=title, description=description)
        return redirect('record_list')
    return render(request, 'records/add_record.html')


def delete_record(request, record_id):
    record = Record.objects.get(id=record_id)
    record.delete()
    return redirect('record_list')
