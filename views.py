from django.shortcuts import render
from .models import user_appointments
from django.http import HttpResponse
from django.core import serializers
import datetime
import json

def home(request):
    return render(request, 'index.html', {})

def get_appointments(request):
    res = {'a':1,'b':2}
    return HttpResponse(json.dumps(res))

def save_appointments(request):
    description = request.POST['description']
    date = request.POST['date']
    time = request.POST['time']
    date = datetime.datetime.strptime(date,'%Y-%m-%d')
    save_appointments = user_appointments(date = date, time = str(time), description = str(description))
    save_appointments.save()
    return HttpResponse("<h1>submitted</h1>")

def search_appointments(request):
    search_text = request.GET['search_text']
    if search_text == "":
        data = serializers.serialize("json", user_appointments.objects.all())
    else:
        print("else")
        data = serializers.serialize("json", user_appointments.objects.filter(description__contains = search_text).all())
    return HttpResponse(data)
    