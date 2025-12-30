from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


days ={
    'saturday': 'this is saturday in dictionary',
    'sunday': 'this is sunday in dictionary',
    'monday': 'this is monday in dictionary',
    'tuesday': 'this is tuesday in dictionary',
    'wednesday': 'this is wednesday in dictionary',
    'friday': 'this is friday in dictionary',
}







def saturday(request):
    return HttpResponse("this is saturday")

def sunday(request):
    return HttpResponse("this is sunday")

def monday(request):
    return HttpResponse("this is monday")

def dynamic_days(request, day):
    day_data = days.get(day)
    if day_data is not None:
        return HttpResponse(f'day is : {day} and data is : {day_data}')
    return HttpResponseNotFound('day does not exists')